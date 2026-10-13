# На каком месте корни модели (H, без рода) по разным сигналам выбора корня — доля корней H в первых k
import json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D); sys.path.insert(0, f"{D}/../reader"); import lib, values, coder
m = json.load(open(f"{lib.REPO}/site/data/math.json")); C = np.array(m["dict"]["C"]); A = np.array(m["dict"]["A"]); NI = {n: i for i, n in enumerate(m["names"])}
items = json.load(open(f"{D}/../taxonomy/items.json")); V = coder.V()
W = np.stack([V[w] for w in m["words"][::5] if w in V]); dC = W @ C.T; muC, sdC = dC.mean(0), dC.std(0); dA = W @ A.T; muA, sdA = dA.mean(0), dA.std(0)
P = {r: lib.interp(V, r, None) for r in lib.SPEC}; P = {r: x / np.linalg.norm(x) for r, x in P.items()}
G = np.stack([P[r] for r in m["names"]]); dG = W @ G.T; muG, sdG = dG.mean(0), dG.std(0)
def sig(w):
    x = V[w]; zc = (x @ C.T - muC) / sdC; za = np.abs((x @ A.T - muA) / sdA); zg = (x @ G.T - muG) / sdG
    _, tr = coder.encode(w, trace=True); fs = {r: s for r, (s, _) in tr.items()}
    sc = {"центр z": zc, "ось |z|": za, "max(центр, ось)": np.maximum(zc, za), "подпись z": zg, "подпись+ось": np.maximum(zg, za)}
    out = {k: [m["names"][i] for i in np.argsort(-v)] for k, v in sc.items()}
    out["факты"] = sorted(fs, key=lambda r: -fs[r]) + [r for r in out["центр z"] if r not in fs]
    return out
K = (1, 3, 5, 10); rec = {}
for it in items:
    hs = [r for r, _ in lib.parse(it["H"])[0]][1:] or [r for r, _ in lib.parse(it["H"])[0]]
    for k, rk in sig(it["w"]).items():
        for kk in K: rec.setdefault(k, {}).setdefault(kk, []).extend([r in rk[:kk] for r in hs])
for k, d in rec.items(): print(f"{k}: " + ", ".join(f"@{kk} {np.mean(v):.0%}" for kk, v in d.items()))
