"""Проверка декодеров сайта на собственных кодах математики (data/decoder_experiments.md, раздел «Сайт»).

Берёт данные сайта (site/data/math.json, vocab.bin, хабовость из build_math.py), кодирует N случайных слов
словаря тем же кодером (до 3 корней), раскодирует «суммой» и «смесью» и печатает место слова и cos первой догадки
со словом. Слова-полюса и имена собственные исключены (слово должно быть в /usr/share/dict/words строчными
или в data/wordlist_en_x5.tsv). Рецепты как мерило не используются.
    .venv/bin/python scripts/experiments/decoder/site_eval.py [N=2000]
"""
import json
import multiprocessing as mp
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "scripts"))
from lib_code import Coder, root_specs, wordlist  # noqa: E402

m = json.loads((REPO / "site/data/math.json").read_text())
W = m["words"]
V = np.frombuffer((REPO / "site/data/vocab.bin").read_bytes(), np.int8).reshape(len(W), m["dim"]).astype(np.float64)
V /= np.linalg.norm(V, axis=1, keepdims=True)
zc = lambda a: (a - a.mean(0)) / a.std(0)  # noqa: E731


def parts(C, A, S, v):
    return np.stack([(1.0 if j == 0 else m["head_w"]) * (C[r] + m["s"] * x * A[r]) for j, (r, x) in enumerate(zip(S, v))])


def scores(P, hub):
    """Как site/math.js Vocab.scores: сумма и смесь (CSLS + мягкое «И»)."""
    y = P.sum(0)
    s = V @ (y / np.linalg.norm(y))
    Z = zc(V @ (P / np.linalg.norm(P, axis=1, keepdims=True)).T)
    k = m["mix"]["soft"]
    soft = -np.log(np.exp(-k * Z).sum(1)) / k
    return s, m["mix"]["w"] * zc(2 * s - hub) + (1 - m["mix"]["w"]) * soft


C, A = (np.array(m["dict"][k]) for k in "CA")
HUB = np.array(m["mix"]["hub"])


def enc(i):
    S, v, _ = Coder(C, A, head_w=m["head_w"]).__call__(V[i], 3)
    return [int(r) for r in S], [int(x) for x in v]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    poles = {w for _, p, q, c in root_specs() for s in (p, q, c) for w in (s or "").split()}
    low = {l.strip() for l in open("/usr/share/dict/words") if l.strip().islower()}
    ok = set(wordlist()[0]) | low
    pool = [i for i, w in enumerate(W) if w in ok and w not in poles]
    idx = np.random.default_rng(1).choice(pool, n, replace=False)
    print(f"слов {n} из {len(pool)} (без полюсов и имён)")
    for d in ("learned",):
        hub = HUB
        with mp.Pool(4) as p:
            codes = p.map(enc, [int(i) for i in idx], chunksize=20)
        res = {"sum": [], "mix": []}
        for i, (S, v) in zip(idx, codes):
            for name, sc in zip(("sum", "mix"), scores(parts(C, A, S, v), hub)):
                g = int(np.argmax(sc))
                res[name].append((int((np.delete(sc, i) > sc[i]).sum()) + 1, float(V[g] @ V[i])))
        for name, r in res.items():
            rk, cg = np.array([x[0] for x in r]), np.array([x[1] for x in r])
            print(f"{d:8s} {name}: top1 {np.mean(rk == 1):.1%} top3 {np.mean(rk <= 3):.1%} top10 {np.mean(rk <= 10):.1%} "
                  f"медиана места {np.median(rk):.0f} | cos первой догадки со словом: медиана {np.median(cg):.2f}, <0,3 у {np.mean(cg < 0.3):.1%}")
        if d == "learned":
            json.dump({"idx": idx.tolist(), "codes": codes}, open(REPO / "scripts/experiments/decoder/site_eval_codes.json", "w"))


if __name__ == "__main__":
    main()
