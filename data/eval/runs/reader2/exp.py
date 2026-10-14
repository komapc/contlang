# Варианты модели читателя: перекрёстная проверка по словам; меры — AUC близко/мимо по cos(предсказание, цель) и доля верных пар.
import json, re, sys, os, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../three2"))
from proxy import feats, vec, fit, X, ix, m, ri, NR, LINK
D = os.path.dirname(os.path.abspath(__file__))
rd = [o for o in json.load(open(f"{D}/../three2/readings.json")) if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] in ix and o["score"] is not None]
words = sorted({o["w"] for o in rd}); g = {w: i % 5 for i, w in enumerate(np.random.default_rng(0).permutation(words))}
Y = np.stack([vec(o["ans"]) for o in rd]); G = np.array([g[o["w"]] for o in rd]); T = np.stack([X[ix[o["w"]]] for o in rd]); sc = np.array([o["score"] for o in rd])
toks = lambda c: [(r, int(v) if v else None) for r, v in re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", c.split("|")[0]) if r in ri]
def f_inter(c):
    t = toks(c); f = np.zeros(NR * NR)
    if t:
        h = ri[t[0][0]]
        for r, _ in t[1:]: f[h * NR + ri[r]] = 1
    return f
def f_pos(c):  # корень на позиции k (0, 1, 2) × значение
    f = np.zeros(3 * NR * 2)
    for k, (r, v) in enumerate(toks(c)[:3]): j = ri[r]; f[(k * NR + j) * 2] = 1; f[(k * NR + j) * 2 + 1] = (v or 0) / 5
    return f
def f_bins(c):  # корень × знак значения (−, 0/нет, +) × сила
    f = np.zeros(NR * 5)
    for r, v in toks(c):
        b = 2 if v is None or v == 0 else (0 if v <= -3 else 1 if v < 0 else 3 if v < 3 else 4); f[ri[r] * 5 + b] = 1
    return f
by = {}
for i, o in enumerate(rd): by.setdefault(o["w"], []).append(i)
PAIRS = [(a, b) if rd[a]["score"] > rd[b]["score"] else (b, a) for ii in by.values() for a, b in itertools.combinations(ii, 2) if rd[a]["code"] != rd[b]["code"] and rd[a]["score"] != rd[b]["score"]]
def evaluate(F, lam, name):
    P = np.zeros_like(Y)
    for k in range(5):
        tr = G != k; P[~tr] = F[~tr] @ np.linalg.solve(F[tr].T @ F[tr] + lam * np.eye(F.shape[1]), F[tr].T @ Y[tr])
    P /= np.linalg.norm(P, axis=1, keepdims=True) + 1e-9; s = (P * T).sum(1)
    pos, neg = s[sc == 2], s[sc == 0]; auc = np.mean([(p > neg).mean() for p in pos])
    pr = np.mean([s[a] > s[b] for a, b in PAIRS]); print(f"{name:34s} λ {lam:5.1f}  AUC {auc:.3f}  пары {pr:.1%}  cos(пред, ответ) {(P * Y).sum(1).mean():.3f}"); return s
base = np.stack([feats(o["code"]) for o in rd])
for lam in (1, 3, 10, 30): evaluate(base, lam, "база")
FI = np.stack([f_inter(o["code"]) for o in rd]); FP = np.stack([f_pos(o["code"]) for o in rd]); FB = np.stack([f_bins(o["code"]) for o in rd])
for lam in (3, 10, 30): evaluate(np.hstack([base, FI]), lam, "+ голова×корень")
for lam in (3, 10, 30): evaluate(np.hstack([base, FP]), lam, "+ позиция×корень")
for lam in (3, 10, 30): evaluate(np.hstack([base, FB]), lam, "+ корень×знак")
for lam in (10, 30): evaluate(np.hstack([base, FB, FP, FI]), lam, "всё")
print("пар", len(PAIRS))
print("--- масштаб групп признаков (меньше масштаб = сильнее сжатие)")
for lam in (1, 2, 3):
    for a in (0.5, 1.0, 2.0):
        evaluate(np.hstack([base, a * FI]), lam, f"+ голова×корень ×{a}")
for a, b in ((1, 0.5), (1, 1), (2, 1)): evaluate(np.hstack([base, a * FI, b * FB]), 3, f"+ г×к ×{a}, к×знак ×{b}")
print("--- только пары кодов математики (без big1000_llm)")
F2 = np.hstack([base, FI]); s2 = evaluate(F2, 2, "база + г×к")
mp = [(a, b) for a, b in PAIRS if "llm" not in rd[a]["run"] and "llm" not in rd[b]["run"]]
print("пар", len(mp), "proxy", f"{np.mean([s2[a] > s2[b] for a, b in mp]):.1%}")
s0 = evaluate(base, 3, "база"); print("база на них", f"{np.mean([s0[a] > s0[b] for a, b in mp]):.1%}")
