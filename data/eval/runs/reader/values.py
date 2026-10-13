# Значение корня без модели: (1) прямые связи ConceptNet с полюсами (spec.md) → ±5; (2) иначе проекция на ось math.json при |z| ≥ Z → ±5;
# (3) иначе связи с расширенными (WordNet) полюсами → ±5; иначе голый корень (None). Проверка на знаках модели H: python values.py
import json, os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lib
from nltk.corpus import wordnet as wn
m = json.load(open(f"{lib.REPO}/site/data/math.json")); AX = np.array(m["dict"]["A"]); NI = {n: i for i, n in enumerate(m["names"])}
E = json.load(open(f"{lib.D}/cn_test.json"))
STOP = {"in", "out", "take", "give", "one", "all", "some", "full", "far", "long", "still", "stand", "just", "now"}
def grow(ws):
    out = set(ws)
    for w in ws:
        if w in STOP: continue
        for s in wn.synsets(w)[:3]:
            out |= {l.name().lower() for l in s.lemmas() if "_" not in l.name()}
            for t in s.similar_tos(): out |= {l.name().lower() for l in t.lemmas() if "_" not in l.name()}
    return out - STOP
POL = {}
for r, sp in lib.SPEC.items():
    if not sp["axis"]: continue
    P = {x for vv, ws in sp["pts"] if vv > 0 for x in ws}; N = {x for vv, ws in sp["pts"] if vv < 0 for x in ws}; GP, GN = grow(P), grow(N)
    POL[r] = (P, N, GP - GN, GN - GP)
_st = {}
def zax(V, x, r):
    if r not in _st:
        W = np.stack([V[w] for w in m["words"][::5] if w in V]); d = W @ AX[NI[r]]; _st[r] = (d.mean(), d.std())
    return (x @ AX[NI[r]] - _st[r][0]) / _st[r][1]
def cn(w, P, N):
    nb = E.get(w, []); f = lambda S: sum((-wt if "Antonym" in rel else wt) for rel, b, wt in nb if b in S); return f(P) - f(N)
def value(V, w, r, Z=2.0, use=("cn", "z", "cn+"), CN=0.0):
    """→ (v, источник) или (None, None)"""
    if not lib.SPEC[r]["axis"]: return None, None
    P, N, GP, GN = POL[r]
    if "cn" in use and abs(d := cn(w, P, N)) > CN: return int(np.sign(d) * 5), "cn"
    if "z" in use and abs(z := zax(V, V[w], r)) >= Z: return int(np.sign(z) * 5), "z"
    if "cn+" in use and abs(d := cn(w, GP, GN)) > CN: return int(np.sign(d) * 5), "cn+"
    return None, None
if __name__ == "__main__":
    items = json.load(open(f"{lib.D}/../taxonomy/items.json")); V = lib.vecs({it["w"] for it in items})
    for Z, CN in ((1.5, 0), (1.5, .3), (1.5, .5), (1.5, 1), (2.0, .5)):
        n = c = ok = 0; src = {}
        for it in items:
            for r, v in lib.parse(it["H"] or "")[0]:
                if v is None or abs(v) < 3 or not lib.SPEC[r]["axis"]: continue
                b, s = value(V, it["w"], r, Z, CN=CN); n += 1
                if b is not None: c += 1; ok += np.sign(b) == np.sign(v); src.setdefault(s, [0, 0]); src[s][0] += np.sign(b) == np.sign(v); src[s][1] += 1
        print(f"Z {Z} CN > {CN}: покрытие {c}/{n} = {c / n:.0%}, совпадение {ok / c:.0%}; " + ", ".join(f"{k} {a}/{b}" for k, (a, b) in src.items()))
