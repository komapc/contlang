# Проверка без читателей: умеет ли модель читателя (../three2/proxy.py) выбрать из двух кодов одного слова тот, что Haiku прочитал лучше?
# Пары — коды одного слова с разными оценками судьи (readings.json). Модель обучается без слова (5 групп по словам).
# Сравнение: cos вектора кода математики (центры и оси корней, веса позиций) с целью.   python pairs_check.py
import json, re, sys, os, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../three2"))
from proxy import feats, vec, fit, X, ix, m, ri, LINK
D = os.path.dirname(os.path.abspath(__file__))
rd = [o for o in json.load(open(f"{D}/../three2/readings.json")) if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] in ix and o["score"] is not None]
C, A = np.array(m["dict"]["C"]), np.array(m["dict"]["A"]); S, HW = m["s"], m["head_w"]
def mvec(code):
    toks = re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", code.split("|")[0]); y = np.zeros(300)
    for k, (r, v) in enumerate([t for t in toks if t[0] in ri]): y += (1 if k == 0 else HW) * (C[ri[r]] + S * (int(v) if v else 0) * A[ri[r]])
    return y / (np.linalg.norm(y) + 1e-9)
words = sorted({o["w"] for o in rd}); g = {w: i % 5 for i, w in enumerate(np.random.default_rng(0).permutation(words))}
F = np.stack([feats(o["code"]) for o in rd]); Y = np.stack([vec(o["ans"]) for o in rd]); G = np.array([g[o["w"]] for o in rd]); P = np.zeros_like(Y)
for k in range(5):
    tr = G != k; P[~tr] = F[~tr] @ fit(F[tr], Y[tr])
P /= np.linalg.norm(P, axis=1, keepdims=True) + 1e-9
T = np.stack([X[ix[o["w"]]] for o in rd]); sp = (P * T).sum(1); sm = np.array([mvec(o["code"]) @ X[ix[o["w"]]] for o in rd])
by = {}
for i, o in enumerate(rd): by.setdefault(o["w"], []).append(i)
res = {"proxy": [], "math": [], "both": []}; kinds = {}
for w, ii in by.items():
    for a, b in itertools.combinations(ii, 2):
        if rd[a]["code"] == rd[b]["code"] or rd[a]["score"] == rd[b]["score"]: continue
        hi, lo = (a, b) if rd[a]["score"] > rd[b]["score"] else (b, a)
        res["proxy"].append(sp[hi] > sp[lo]); res["math"].append(sm[hi] > sm[lo]); res["both"].append(sp[hi] + sm[hi] > sp[lo] + sm[lo])
        kinds.setdefault(tuple(sorted((rd[hi]["run"], rd[lo]["run"]))), []).append(sp[hi] > sp[lo])
n = len(res["proxy"]); print(f"пар {n} (слов {len(by)}); доля, где выбран лучше прочитанный код:")
for k, v in res.items():
    v = np.array(v, float); rng = np.random.default_rng(0); lo, hi = np.percentile([rng.choice(v, n).mean() for _ in range(2000)], [2.5, 97.5])
    print(f"  {k:6s} {v.mean():.1%} [{lo:.1%} … {hi:.1%}]")
for k, v in sorted(kinds.items(), key=lambda t: -len(t[1]))[:8]: print("   ", k, len(v), f"{np.mean(v):.0%}")
