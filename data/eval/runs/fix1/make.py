# Слова и роли (dec.md) → items.json.  python make.py
import json, os, random
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); its = json.load(open(f"{D}/../big1000/items.json"))
T = {"device.n.01", "instrument.n.01", "tool.n.01", "implement.n.01", "machine.n.01", "weapon.n.01", "utensil.n.01"}
def role(w, pos):
    ss = wn.synsets(w, "n") if pos == "noun" else []
    if not ss: return None
    s = ss[0]
    if s.lexname() == "noun.person": return "agent"
    if s.lexname() == "noun.attribute": return "quality"
    if s.lexname() == "noun.artifact" and T & {h.name() for p in s.hypernym_paths() for h in p}: return "tool"
R = [dict(o, role=role(o["w"], o["pos"])) for o in its]; random.seed(20261023)
out = [o for o in R if o["role"]] + random.sample([o for o in R if not o["role"]], 70); random.shuffle(out)
json.dump(out, open(f"{D}/items.json", "w"), indent=0); print(len(out))
