# Пул ../adopt (частые существительные сайта, не имена, не из ../measure, не из подписей спецификации) → pool.json
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); from nltk.corpus import wordnet as wn
m = json.load(open(f"{D}/../../../../site/data/math.json")); test = {o["w"] for o in json.load(open(f"{D}/../measure/items.json"))}
sp = open(f"{D}/../adopt/spec_new.md").read(); spw = set(re.findall(r"[a-z]+", sp[sp.index("## Roots"):sp.index("## Form")]))
def ok(w):
    s = wn.synsets(w, "n")
    return w.isalpha() and w.islower() and len(w) > 2 and s and not s[0].instance_hypernyms() and w not in test and w not in spw and wn.morphy(w, "n") not in spw
json.dump([w for w in m["words"][:6000] if ok(w)], open(f"{D}/pool.json", "w"))
