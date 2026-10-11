"""Подгонка, шаг 3: как fit.py, но свои коды — все ≈4760 оставшихся слов словаря сайта (own8k.json, gen_own.js; отложенные 1000 из eval.js в них не входят),
якорь — обученный словарь сайта (learned) или spec. fit.py брал свои коды rand1000 и переучивался на них (① на других 1000 словах 396 → 345).
Пишет dict_g_<якорь>_<λ>_<α>.json и для честного теста 1 — cv_g_<якорь>_<λ>_<α>_<k>.json (eval_cv.js g_<якорь>_<λ>_<α>).
    .venv/bin/python data/eval/runs/anchor/fit2.py"""
import json, sys
from pathlib import Path
import numpy as np
sys.argv = sys.argv[:1]
exec(open(Path(__file__).parent / "fit.py").read().split("best = []")[0])   # общие определения: X, row, fit, score, llm, folds, perm
own = [tuple(p) for p in json.load(open(OUT / "own8k.json")) if p[0] in idx]
anchors = {n: np.concatenate([np.array(d["C"]), np.array(d["A"])]) for n, d in ((n, json.load(open(OUT / f"dict_{n}.json"))) for n in ("learned", "spec"))}
def run(T, pairs, wts, lam):
    global T0; T0 = T; return fit(pairs, wts, lam)
for an, lam, alpha in (("learned", 3, 0.05), ("learned", 3, 0.2), ("learned", 30, 0.05), ("spec", 3, 0.05), ("spec", 3, 0.2)):
    T = anchors[an]; wts = lambda n: np.array([1.0] * n + [alpha] * len(own)); tag = f"g_{an}_{lam}_{alpha}"; cv = []
    for k, f in enumerate(folds):
        fs_ = set(f); tr = [llm[i] for i in perm if i not in fs_]; te = [llm[i] for i in f]
        C, A = run(T, tr + own, wts(len(tr)), lam); cv.append(score(C, A, te))
        json.dump({"C": np.round(C, 5).tolist(), "A": np.round(A, 5).tolist(), "hub": np.round(hubness(X, C, A, has), 4).tolist(), "test": te}, open(OUT / f"cv_{tag}_{k}.json", "w"))
    C, A = run(T, llm + own, wts(len(llm)), lam)
    print(f"{tag}: отложенные коды моделей cos y·x {np.mean(cv):.3f}; свои {score(C, A, own[:2000]):.3f}; центр ↔ learned {np.mean(np.sum(C * anchors['learned'][:R], 1)):.2f}", flush=True)
    json.dump({"C": np.round(C, 5).tolist(), "A": np.round(A, 5).tolist(), "hub": np.round(hubness(X, C, A, has), 4).tolist()}, open(OUT / f"dict_{tag}.json", "w"))
