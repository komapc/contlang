# Знак значения по прямым связям ConceptNet: слово ↔ слова полюсов оси (spec.md, ±5) — покрытие и совпадение со знаком модели (H, |v| ≥ 3).
import csv, gzip, json, os, sys, collections, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lib
items = json.load(open(f"{lib.D}/../taxonomy/items.json")); T = {it["w"] for it in items}
E = collections.defaultdict(list); f = f"{lib.D}/cn_test.json"
if not os.path.exists(f):
    with gzip.open(f"{lib.REPO}/data/raw/conceptnet/conceptnet-assertions-5.7.0.csv.gz", "rt") as fh:
        for l in fh:
            p = l.split("\t")
            if not (p[2].startswith("/c/en/") and p[3].startswith("/c/en/")): continue
            a, b = p[2].split("/")[3], p[3].split("/")[3]
            if a in T or b in T: E[a].append((p[1].split("/")[2], b, json.loads(p[4])["weight"])); E[b].append(("~" + p[1].split("/")[2], a, json.loads(p[4])["weight"]))
    json.dump(E, open(f, "w"))
E = json.load(open(f))
from nltk.corpus import wordnet as wn
STOP = {"in", "out", "take", "give", "one", "all", "some", "full", "far", "long", "still", "stand", "just", "now"}
def grow(ws):
    out = set(ws)
    for w in ws:
        if w in STOP: continue
        for s in wn.synsets(w)[:3]:
            out |= {l.name().lower() for l in s.lemmas() if "_" not in l.name()}
            for t in s.similar_tos(): out |= {l.name().lower() for l in t.lemmas() if "_" not in l.name()}
    return out - STOP
GROW = os.environ.get("GROW") == "1"
def poles(r):
    pts = lib.SPEC[r]["pts"]; P = {x for vv, ws in pts if vv > 0 for x in ws}; N = {x for vv, ws in pts if vv < 0 for x in ws}
    if GROW: P, N = grow(P), grow(N); P, N = P - N, N - P
    return P, N
n = cov = ok = 0; ex = []
for it in items:
    w = it["w"]; nb = E.get(w, [])
    for r, v in lib.parse(it["H"] or "")[0]:
        if v is None or abs(v) < 3 or not lib.SPEC[r]["axis"]: continue
        P, N = poles(r)
        sp = sum(wt for rel, b, wt in nb if b in P and "Antonym" not in rel) - sum(wt for rel, b, wt in nb if b in P and "Antonym" in rel)
        sn = sum(wt for rel, b, wt in nb if b in N and "Antonym" not in rel) - sum(wt for rel, b, wt in nb if b in N and "Antonym" in rel)
        n += 1
        if sp != sn: cov += 1; ok += np.sign(sp - sn) == np.sign(v); ex.append(f"{w} {r}{v:+d}: {sp:.1f}/{sn:.1f}")
print(f"покрытие {cov}/{n} = {cov / n:.0%}, совпадение {ok}/{max(cov, 1)}"); print("; ".join(ex[:30]))
