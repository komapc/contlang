"""Словарь корней, согласованный с проверенными рецептами (docs/math.md, раздел 6).

Как scripts/18_sparse_learn.py, но в гребневую регрессию добавлены пары
«рецепт → слово» из data/site/tips_short.md и docs/encoding.md (коды, проверенные
слепыми тестами) с весом BETA: код рецепта должен декодироваться в своё слово.
Оценка: общая точность на отложенных словах (как в разделе 5) и место слова
рецепта среди ближайших к его коду — на рецептах, не участвовавших в обучении
(5 частей), и на всех (так словарь работает на сайте).

    .venv/bin/python scripts/21_recipe_dict.py [β ...] [--cv]   → data/recipe_dict.md, data/sparse_dict_recipes.npz
    (по умолчанию β = 30 без перекрёстной проверки: один прогон обучения; --cv добавляет 5 частей, в 6 раз дольше;
    в .npz сохраняется последний β из списка)
"""
import re
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from lib_code import HEAD, SEP, Coder, Data, encode_all, metrics, root_specs, row, unit  # noqa: E402

LAM, TAU, ITERS, HW = 30.0, 0.85, 3, 0.6
OUT = ROOT / "data" / "recipe_dict.md"
NPZ = ROOT / "data" / "sparse_dict_recipes.npz"
TOK = re.compile(r"^([A-Z]+)(?:\(=([+-]?\d+)\))?$")


def recipes():
    """Пары (английское слово, код) из подсказок сайта и encoding.md."""
    pairs = {}
    tips = (ROOT / "data" / "site" / "tips_short.md").read_text(encoding="utf8")
    for w, c in re.findall(r"([a-z]+)(?:/[a-z]+)? `([A-Z][^`]*?\|[^`]*)`", tips):
        pairs.setdefault(w, c)
    enc = (ROOT / "docs" / "encoding.md").read_text(encoding="utf8")
    for w, c in re.findall(r"\*([a-z]+)\* = `([A-Z][^`]*?\|[^`]*)`", enc):
        pairs.setdefault(w, c)
    return pairs


def parse(code, ix):
    out = []
    for t in code.split("|")[0].split():
        m = TOK.match(t)
        if not m or m[1] not in ix:
            return None
        out.append((ix[m[1]], int(m[2] or 0)))
    return out or None


def design(codes, R, s, hw):
    M = np.zeros((len(codes), 2 * R))
    for i, code in enumerate(codes):
        for j, (r, v) in enumerate(code):
            w = 1.0 if j == 0 else hw
            M[i, r] += w
            M[i, R + r] += w * s * v
    return M


def learn(d, C0, A0, Mr, Xr, beta):
    """18_sparse_learn.learn + строки рецептов с весом beta."""
    from importlib import import_module
    clamp = import_module("18_sparse_learn").clamp
    R, has = len(C0), A0.any(1)
    Th0 = np.concatenate([C0, A0])
    C, A = C0.copy(), A0.copy()
    Xtr = d.V[d.train]
    for _ in range(ITERS):
        co = Coder(C, A, head_w=HW)
        M = co.design(encode_all(co, Xtr))
        Th_cur = np.concatenate([C, A])
        T = np.linalg.norm(M @ Th_cur, axis=1)[:, None] * Xtr
        Tr = np.linalg.norm(Mr @ Th_cur, axis=1)[:, None] * Xr
        G = M.T @ M + beta * Mr.T @ Mr + LAM * np.eye(2 * R)
        B = M.T @ T + beta * Mr.T @ Tr + LAM * Th0
        Th = unit(np.linalg.solve(G, B))
        for i in range(2 * R):
            Th[i] = 0 if (i >= R and not has[i - R]) else clamp(Th[i], Th0[i], TAU)
        C, A = Th[:R], Th[R:]
    return C, A


def ranks(C, A, Mr, tgt, V):
    Y = unit(Mr @ np.concatenate([C, A]))
    s = Y @ V.T
    return (s > s[np.arange(len(tgt)), tgt][:, None]).sum(1) + 1


def main():
    specs = root_specs()
    d = Data([specs])
    names, C0, A0 = d.dictionary(specs)
    ix = {n: i for i, n in enumerate(names)}
    vi = {w: i for i, w in enumerate(d.vocab)}
    raw = recipes()
    P = [(w, parse(c, ix)) for w, c in raw.items() if w in vi and parse(c, ix)]
    tgt = np.array([vi[w] for w, _ in P])
    Mr = design([c for _, c in P], len(names), 0.4, HW)
    Xr = d.V[tgt]
    Xte = d.V[d.test]
    betas = [float(a) for a in sys.argv[1:] if not a.startswith("-")] or [30.0]
    cv = "--cv" in sys.argv
    folds = np.array_split(np.random.default_rng(0).permutation(len(P)), 5)
    L = ["# Словарь, согласованный с рецептами", "",
         f"Скрипт `scripts/21_recipe_dict.py`. Пары «рецепт → слово»: {len(raw)} из подсказок сайта и encoding.md, "
         f"{len(P)} со словом в словаре Numberbatch и разобранным кодом. Общая точность — на отложенных {len(d.test)} словах "
         "(как в docs/math.md, раздел 5); рецепты — место слова среди ближайших к коду рецепта (все слова словаря).", "",
         "| β (вес рецептов) | " + HEAD[2:] + " рецепты top10 (вне обучения) | рецепты top10 (все) | медиана места (вне обучения) |",
         "| --: " + SEP + " --: | --: | --: |"]
    print(f"рецептов {len(P)}, обучающих слов {len(d.train)}", flush=True)
    for beta in betas:
        t0 = time.time()
        rr = np.zeros(len(P), int)
        for k, te in enumerate(folds if cv and beta else []):  # при β=0 рецепты в обучение не входят, «вне обучения» = «все»
            tr = np.setdiff1d(np.arange(len(P)), te)
            C, A = learn(d, C0, A0, Mr[tr], Xr[tr], beta)
            rr[te] = ranks(C, A, Mr[te], tgt[te], d.V)
            print(f"  β={beta:g} часть {k + 1}/5, {time.time() - t0:.0f} с", flush=True)
        C, A = learn(d, C0, A0, Mr, Xr, beta)
        ra = ranks(C, A, Mr, tgt, d.V)
        if not beta:
            rr = ra
        m = metrics(d, d.test, np.stack([e[2] for e in encode_all(Coder(C, A, head_w=HW), Xte)]))
        cvs = f"{(rr <= 10).mean():.1%} | " if cv else "— | "
        L.append(f"| {beta:g} " + row(m) + f" {cvs}{(ra <= 10).mean():.1%} | " + (f"{int(np.median(rr))} |" if cv else "— |"))
        print(L[-1], f"({time.time() - t0:.0f} с)", flush=True)
    np.savez(NPZ, names=np.array(names), C=C, A=A, beta=beta)
    OUT.write_text("\n".join(L) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
