"""Подгонка словаря под коды моделей (идея 4, шаг 2): векторы корней (c_r, a_r) — решение гребневой регрессии
    min Σ_коды α_k ‖y(код) − x_слово‖² + λ ‖Θ − Θ_якорь‖²,  y = Σ_j w_j (c_r + s·v_j·a_r)  (как в site/math.js Coder.parts),
по главному слову кода (связки и второе слово не берутся). Коды: модели — слепые тесты links / pi_for (calib.json) и рецепты;
свои — коды нынешнего кодера для 1000 случайных слов (own_codes.json из mathread/rand1000.json), с весом ALPHA, чтобы не потерять ①.
Якорь — словарь spec (dicts.py). Проверка на отложенных кодах моделей — 5 частей, cos y с x (на сайте меряет eval.js).
    .venv/bin/python data/eval/runs/anchor/fit.py   → dict_fit_<λ>_<α>.json"""
import json, re, sys
from pathlib import Path
import numpy as np
REPO = Path(__file__).resolve().parents[4]; OUT = Path(__file__).parent; MR = OUT.parent / "mathread"
sys.path.insert(0, str(REPO / "scripts")); sys.path.insert(0, str(REPO / "scripts" / "site"))
from build_math import hubness  # noqa: E402
unit = lambda v: v / (np.linalg.norm(v, axis=-1, keepdims=True) + 1e-9)  # noqa: E731
m = json.loads((REPO / "site/data/math.json").read_text()); names = m["names"]; R = len(names); S, HW = m["s"], m["head_w"]
has = np.array(m["has_axis"]); idx = {w: i for i, w in enumerate(m["words"])}
X = unit(np.frombuffer((REPO / "site/data/vocab.bin").read_bytes(), np.int8).reshape(-1, m["dim"]).astype(float))
def parse(code):
    head = re.split(r"\b(?:FROM|FOR|LIKE|PI)\b", code)[0].split("|")[0]; out = []
    for n, v in re.findall(r"\b([A-Z][A-Z]+)\b(?:\(=\s*([+-]?\d+)\s*\))?", re.sub(r'"[^"]*"', " ", head)):
        if n in names: r = names.index(n); out.append((r, int(v) if v and has[r] else 0))
    return out
def row(code):
    z = np.zeros(2 * R)
    for j, (r, v) in enumerate(parse(code)): w = 1.0 if j == 0 else HW; z[r] += w; z[R + r] += w * S * v
    return z
llm = [(c["w"], c["code"]) for c in json.load(open(MR / "calib.json")) if not c["src"].startswith("math")]
llm += [(e["en"], e["code"]) for e in json.load(open(REPO / "site/data/recipes.json")) if re.fullmatch(r"[a-z]+", e["en"])]
llm = [(w, c) for w, c in llm if w in idx and parse(c)]
dev = {w for w, _ in json.load(open(MR / "words.json"))["dev"]} | {w for w, _ in json.load(open(MR / "words.json"))["test"]}
llm = [(w, c) for w, c in llm if w not in dev]
spec = json.load(open(OUT / "dict_spec.json")); T0 = np.concatenate([np.array(spec["C"]), np.array(spec["A"])])
own = [tuple(p) for p in json.load(open(OUT / "own_codes.json")) if p[0] in idx]   # [[слово, код]] — коды нынешнего кодера для 1000 случайных слов (mathread/rand1000.json)
def fit(pairs, wts, lam):
    M = np.stack([row(c) for _, c in pairs]) * np.sqrt(wts)[:, None]; T = X[[idx[w] for w, _ in pairs]] * np.sqrt(wts)[:, None]
    Th = np.linalg.solve(M.T @ M + lam * np.eye(2 * R), M.T @ T + lam * T0)
    C, A = unit(Th[:R]), Th[R:]; A = np.where(has[:, None], unit(A), 0); return C, A
def score(C, A, pairs):
    Th = np.concatenate([C, A]); Y = unit(np.stack([row(c) for _, c in pairs]) @ Th); return float(np.mean(np.sum(Y * X[[idx[w] for w, _ in pairs]], 1)))
rng = np.random.default_rng(0); perm = rng.permutation(len(llm)); folds = np.array_split(perm, 5)
print(f"кодов моделей {len(llm)}, своих {len(own)}")
print(f"якорь spec: cos y·x на кодах моделей {score(T0[:R], T0[R:], llm):.3f}, на своих {score(T0[:R], T0[R:], own[:2000]):.3f}")
best = []
for lam in (3, 10, 30, 100):
    for alpha in (0, 0.05, 0.2):
        cv = []
        for f in folds:
            tr = [llm[i] for i in perm if i not in set(f)]; te = [llm[i] for i in f]
            pairs = tr + own; wts = np.array([1.0] * len(tr) + [alpha] * len(own))
            if alpha == 0: pairs, wts = tr, np.ones(len(tr))
            C, A = fit(pairs, wts, lam); cv.append(score(C, A, te))
        pairs = llm + own if alpha else llm; wts = np.array([1.0] * len(llm) + ([alpha] * len(own) if alpha else []))
        C, A = fit(pairs, wts, lam)
        print(f"λ {lam} α {alpha}: отложенные коды моделей cos {np.mean(cv):.3f}; свои коды {score(C, A, own[:2000]):.3f}; уход центра от якоря {np.mean(np.sum(C * T0[:R], 1)):.2f}")
        json.dump({"C": np.round(C, 5).tolist(), "A": np.round(A, 5).tolist(), "hub": np.round(hubness(X, C, A, has), 4).tolist()}, open(OUT / f"dict_fit_{lam}_{alpha}.json", "w"))

# честная проверка чтения: 5 частей, словарь без кодов своей части → cv_<λ>_<α>_<k>.json (+ отложенные коды); читает eval_cv.js
for lam, alpha in ((3, 0.2), (3, 0), (1, 0.2), (3, 0.5)):
    for k, f in enumerate(folds):
        fs_ = set(f); tr = [llm[i] for i in perm if i not in fs_]; te = [llm[i] for i in f]
        pairs = tr + own if alpha else tr; wts = np.array([1.0] * len(tr) + ([alpha] * len(own) if alpha else []))
        C, A = fit(pairs, wts, lam)
        json.dump({"C": np.round(C, 5).tolist(), "A": np.round(A, 5).tolist(), "hub": np.round(hubness(X, C, A, has), 4).tolist(), "test": te}, open(OUT / f"cv_{lam}_{alpha}_{k}.json", "w"))
