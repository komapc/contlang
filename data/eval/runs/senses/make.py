# Слова и смыслы → items.json (см. dec.md). python make.py
import json, os, random, re
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); B = f"{D}/../big1000"; its = json.load(open(f"{B}/items.json")); P = {"noun": "n", "verb": "v"}
cnt = lambda s: sum(l.count() for l in s.lemmas())
def anchors(w, s):
    a = [l.name() for l in s.lemmas()] + [l.name() for h in s.hypernyms() for l in h.lemmas()] + re.findall(r"[a-z]+", s.definition().lower())
    return [x.lower() for x in a if "_" not in x and x.lower() != w and len(x) > 2]
out = []
for o in its:
    if o["pos"] not in P: continue
    ss = [s for s in wn.synsets(o["w"], P[o["pos"]]) if cnt(s) >= 3]
    if len(ss) < 2: continue
    far = [s for s in ss[1:] if (ss[0].wup_similarity(s) or 0) < 0.3 and s.lexname() != ss[0].lexname()]
    if not far: continue
    out.append({"w": o["w"], "pos": o["pos"], "senses": [{"gloss": s.definition(), "anchors": anchors(o["w"], s)} for s in (ss[0], far[0])]})
random.seed(20261022); out = random.sample(out, 100); json.dump(out, open(f"{D}/items.json", "w"), indent=0); print(len(out))
