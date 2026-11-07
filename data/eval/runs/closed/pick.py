# Выборка (dec.md): те же фильтры, что в ../pipe/pick.py, другой seed (20261108), без предложений pipe; по 6 из 10 жанров = 60.
#   NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/closed/pick.py
import json, os, random, sys
D = os.path.dirname(os.path.abspath(__file__))
from nltk.corpus import brown
src = open(f"{D}/../pipe/pick.py").read(); ns = {"__file__": f"{D}/../pipe/pick.py"}
exec(src[:src.index("rng = random.Random")], ns)  # CATS, det, ok
old = {x["s"] for v in json.load(open(f"{D}/../pipe/sents.json")).values() for x in v}
rng = random.Random(20261108); out = []
for c in ns["CATS"]:
    S = sorted({ns["det"](s) for s in brown.sents(categories=c) if ns["ok"](s)} - old); rng.shuffle(S)
    out += [{"id": f"c{len(out) + i + 1}", "cat": c, "s": x} for i, x in enumerate(S[:6])]
json.dump(out, open(f"{D}/sents.json", "w"), indent=1, ensure_ascii=False)
for x in out: print(x["id"], x["cat"], "|", x["s"])
