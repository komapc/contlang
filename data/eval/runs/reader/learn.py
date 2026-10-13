# Обученная модель читателя: признаки кода → вектор первого ответа (гребневая регрессия, остаток над читателем по спецификации).
# Проверка по словам (5 групп): AUC «близко» и корреляция внутри слова.  python learn.py [λ...]
import json, os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lib
from scipy.stats import spearmanr, rankdata
D = lib.D; R = json.load(open(f"{D}/readings.json")); LAB = json.load(open(f"{D}/labels.json")); V = lib.vecs({o["w"] for o in R})
gloss = lambda c: lib.gloss(V, c)
N = lib.NAMES; NI = {n: i for i, n in enumerate(N)}; ROLES = ["agent", "tool", "result", "quality"]
def feat(code):
    rs, pos, ro = lib.parse(code); f = np.zeros(len(N) * 8 + 8)
    for k, (r, v) in enumerate(rs[:3]):
        b = NI[r] * 8 + (0 if k == 0 else 4)
        if v is None: f[b] += 1
        elif v == 0: f[b + 3] += 1
        else: f[b + 1] += max(v, 0) / 5; f[b + 2] += max(-v, 0) / 5
    if ro: f[len(N) * 8 + ROLES.index(ro)] = 1
    f[len(N) * 8 + 4 + "oiae".index(pos) if pos in "oiae" else len(N) * 8 + 4] = 1
    return f
ok = [k for k, o in enumerate(R) if o["ans"] and lib.pv(V, o["ans"][0]) is not None]
F = np.stack([feat(o["code"]) for o in R]); G0 = np.stack([gloss(o["code"]) for o in R])
Y = np.stack([lib.pv(V, o["ans"][0]) if k in set(ok) else np.zeros(300) for k, o in enumerate(R)])
X = np.stack([V[o["w"]] for o in R]); lab = np.array([LAB[f"{o['w']}\t{o['ans'][0] if o['ans'] else '—'}"] for o in R])
words = sorted({o["w"] for o in R}); grp = {w: i % 5 for i, w in enumerate(np.random.default_rng(0).permutation(words))}
okm = np.zeros(len(R), bool); okm[ok] = True
def fit(tr, lam, beta):
    T = Y[tr] - beta * G0[tr]; A = F[tr]; return np.linalg.solve(A.T @ A + lam * np.eye(A.shape[1]), A.T @ T)
def score(s, name):
    y = (lab == 2).astype(float); auc = (rankdata(s)[y == 1].sum() - y.sum() * (y.sum() + 1) / 2) / (y.sum() * (len(y) - y.sum()))
    ws = {}
    for o, si, li in zip(R, s, lab): ws.setdefault(o["w"], {}).setdefault(o["v"], []).append((si, li))
    rho = [spearmanr([np.mean([a for a, _ in x]) for x in d.values()], [np.mean([b for _, b in x]) for x in d.values()])[0] for d in ws.values()]
    rho = [r for r in rho if r == r]; print(f"{name}: AUC {auc:.3f}, внутри слова {np.mean(rho):.3f}"); return np.mean(rho)
best = None
for lam in [float(x) for x in sys.argv[1:]] or [3, 10, 30]:
    for beta in [0, 1]:
        P = np.zeros_like(Y)
        for g in range(5):
            te = np.array([grp[o["w"]] == g for o in R]); tr = ~te & okm; W = fit(tr, lam, beta); P[te] = F[te] @ W + beta * G0[te]
        P /= np.linalg.norm(P, axis=1, keepdims=True) + 1e-9; s = (P * X).sum(1)
        r = score(s, f"λ {lam} β {beta}")
        if best is None or r > best[0]: best = (r, lam, beta)
print("лучшее", best)
# Сито для кодеров: средняя предсказанная близость по варианту против настоящей доли «близко» (по 15 вариантам)
lam, beta = best[1], best[2]; P = np.zeros_like(Y)
for g in range(5):
    te = np.array([grp[o["w"]] == g for o in R]); tr = ~te & okm; W = fit(tr, lam, beta); P[te] = F[te] @ W + beta * G0[te]
P /= np.linalg.norm(P, axis=1, keepdims=True) + 1e-9; s = (P * X).sum(1); sg = (G0 * X).sum(1)
vs = sorted({o["v"] for o in R}); act = [np.mean([l == 2 for o, l in zip(R, lab) if o["v"] == v]) for v in vs]
for nm, ss in (("обученный", s), ("по спецификации", sg)):
    pr = [np.mean([x for o, x in zip(R, ss) if o["v"] == v]) for v in vs]
    print(f"сито ({nm}): Спирмен по вариантам {spearmanr(pr, act)[0]:.2f}; " + ", ".join(f"{v} {p:.3f}/{a:.0%}" for v, p, a in sorted(zip(vs, pr, act), key=lambda t: -t[2])))
