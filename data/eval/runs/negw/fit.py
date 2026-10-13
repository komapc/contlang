# Веса negVec по корням (README). Вход dump_r1.json (dump.js, коды rand1000).
#  learned: гребневая регрессия t − x ≈ Σ_{r ∉ код} w_r·C_r (t — единичная сумма корней кода, x — слово);
#  mean: w_r ∝ cos(среднее слово, C_r), масштаб — та же регрессия с одним множителем.
#   .venv/bin/python data/eval/runs/negw/fit.py
import json, os, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{D}/dump_r1.json"))
C = np.array(J["C"]); R = len(C); rows = J["rows"]
T = np.array([r["t"] for r in rows]); X = np.array([r["x"] for r in rows])
mask = np.ones((len(rows), R)); [mask[i].__setitem__(r["S"], 0) for i, r in enumerate(rows)]
# система: для каждого слова (t − x) = Σ_r mask_r w_r C_r  →  признаки F[i, :, r] = mask_r·C_r
Y = (T - X).ravel(); F = (mask[:, None, :] * C.T[None, :, :]).reshape(-1, R)
out = {}
for lam in (1.0, 10.0, 100.0):
    w = np.linalg.solve(F.T @ F + lam * np.eye(R), F.T @ Y); out[f"learned_{lam:g}"] = w.tolist()
mu = X.mean(0); mu /= np.linalg.norm(mu); b = C @ mu / np.linalg.norm(C, axis=1)
g = F @ b; k = float(g @ Y / (g @ g)); out["mean"] = (k * b).tolist()
json.dump(out, open(f"{D}/weights.json", "w"))
w = np.array(out["learned_10"]); o = np.argsort(-w)
print("learned λ=10, крупнейшие:", ", ".join(f"{J['names'][r]} {w[r]:+.3f}" for r in o[:8]))
print("learned λ=10, меньшие:", ", ".join(f"{J['names'][r]} {w[r]:+.3f}" for r in o[-6:]))
print("mean: масштаб", round(k, 3), "| крупнейшие:", ", ".join(f"{J['names'][r]} {k*b[r]:+.3f}" for r in np.argsort(-b)[:6]))
print("corr(learned, mean) =", round(float(np.corrcoef(w, b)[0, 1]), 2))
