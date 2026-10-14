# Модель читателя v2 (признаки proxy.py + голова × корень, λ 2) на всех прочтениях; выбор кода из кандидатов cand.json
# по cos(предсказанный ответ, слово).   python choose.py cand.json → chosen.json
import json, re, sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../three2"))
from proxy import feats, vec, X, ix, ri, NR, LINK
D = os.path.dirname(os.path.abspath(__file__))
toks = lambda c: [r for r, _ in re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", c.split("|")[0]) if r in ri]
def f2(c):
    f = np.zeros(NR * NR); t = toks(c)
    for r in t[1:]: f[ri[t[0]] * NR + ri[r]] = 1
    return np.concatenate([feats(c), f])
def train(rd, lam=2.0):
    F = np.stack([f2(o["code"]) for o in rd]); Y = np.stack([vec(o["ans"]) for o in rd])
    return np.linalg.solve(F.T @ F + lam * np.eye(F.shape[1]), F.T @ Y)
def readings(): return [o for o in json.load(open(f"{D}/../three2/readings.json")) if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] in ix]
if __name__ == "__main__":
    B = train(readings()); C = json.load(open(sys.argv[1])); out = {}
    for w, o in C.items():
        t = X[ix[w]]; P = np.stack([f2(c) for c in o["cands"]]) @ B; P /= np.linalg.norm(P, axis=1, keepdims=True); s = P @ t
        k = int(np.argmax(s)); out[w] = {"site": o["site"], "proxy": o["cands"][k], "s_site": round(float(s[0]), 3), "s_proxy": round(float(s[k]), 3), "k": k}
    json.dump(out, open(f"{D}/chosen.json", "w"), indent=0)
    v = list(out.values()); print("код сменился у", sum(o["site"] != o["proxy"] for o in v), "из", len(v), "; оценка модели site / proxy:",
          round(np.mean([o["s_site"] for o in v]), 3), round(np.mean([o["s_proxy"] for o in v]), 3), "; место у кодера: медиана", int(np.median([o["k"] for o in v])))
    for w in list(out)[:25]: print(f"{w:14s} {out[w]['site']:44s} → {out[w]['proxy']}")
