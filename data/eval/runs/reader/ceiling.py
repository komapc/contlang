# Потолок корреляции внутри слова: насколько читатель 1 предсказывает читателя 2 того же кода (по вариантам одного слова)
import json, os, numpy as np
from scipy.stats import spearmanr
D = os.path.dirname(os.path.abspath(__file__)); R = json.load(open(f"{D}/readings.json")); LAB = json.load(open(f"{D}/labels.json"))
L = {(o["w"], o["v"], o["r"]): LAB[f"{o['w']}\t{o['ans'][0] if o['ans'] else '—'}"] for o in R}
rho = []
for w in {o["w"] for o in R}:
    vs = sorted({o["v"] for o in R if o["w"] == w}); a = [L[(w, v, 1)] for v in vs]; b = [L[(w, v, 2)] for v in vs]
    r = spearmanr(a, b)[0]
    if r == r: rho.append(r)
r1 = np.mean(rho); print(f"читатель 1 ↔ читатель 2: {r1:.3f} по {len(rho)} словам; потолок для среднего двух (Спирмен–Браун) ≈ {np.sqrt(2 * r1 / (1 + r1)):.3f}")
