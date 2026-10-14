# Как читатель складывает несколько слов: предсказание «A LIKE B (LIKE C)» = n(p(A)) + β·n(p(B)) + β·n(p(C)), p — модель читателя (proxy.py),
# обученная БЕЗ прочтений 188 слов теста. β подбирается по прочтениям W2 и W3 из ../three (cos предсказания с ответом).  python combine.py
import json, re, os, numpy as np
from proxy import feats, vec, fit, LINK, X, ix, D
T3 = set(json.load(open(f"{D}/../three/codes.json")))
rd = json.load(open(f"{D}/readings.json"))
tr = [o for o in rd if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] not in T3]
B = fit(np.stack([feats(o["code"]) for o in tr]), np.stack([vec(o["ans"]) for o in tr])); np.save(f"{D}/proxy_B_heldout.npy", B)
n = lambda v: v / (np.linalg.norm(v) + 1e-9); p = lambda c: n(feats(c) @ B)
mw = [o for o in rd if o["run"] in ("three_W2", "three_W3") and vec(o["ans"]) is not None]
for beta in (0, 0.25, 0.5, 0.75, 1.0, 1.5):
    cs = [float(n(sum([p(LINK.split(o["code"])[0])] + [beta * p(x) for x in LINK.split(o["code"])[2::2]])) @ vec(o["ans"])) for o in mw]
    print(f"β {beta:4}: cos(предсказание, ответ) {np.mean(cs):.3f}  (n {len(mw)})")
print("обучение без 188 слов:", len(tr), "прочтений")
