# Подтверждение LAND: сайт (44 атома math.json) против 45 (dict45: те же 44 + обученный LAND, learn.py); кодер SZ с одной
# выраженностью у всех корней, якоря WordNet — старые + якоря LAND. Пул — ../adopt без слов ../adopt и ../adopt2.
#   python make.py SCRATCH  → items.json, lists.json, spec_old.md, spec_land.md, SCRATCH/rN/{spec,codes}.md
import json, os, random, re, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [f"{D}/../reader", f"{D}/../newroots"]
import lib, sz
from nltk.corpus import wordnet as wn
m = sz.m; test = {o["w"] for o in json.load(open(f"{D}/../measure/items.json"))}
used = {o["w"] for p in ("adopt", "adopt2") for o in json.load(open(f"{D}/../{p}/items.json"))}
sp47 = open(f"{D}/../adopt/spec_new.md").read()
spl = "".join(l for l in sp47.splitlines(True) if not (l.startswith("- SACRED:") or l.startswith("- CONTAINER:"))).replace("## Roots (47)", "## Roots (45)")
open(f"{D}/spec_land.md", "w").write(spl); open(f"{D}/spec_old.md", "w").write(open(f"{D}/../adopt/spec_old.md").read())
spw = set(re.findall(r"[a-z]+", sp47[sp47.index("## Roots"):sp47.index("## Form")]))
def ok(w):
    s = wn.synsets(w, "n")
    return w.isalpha() and w.islower() and len(w) > 2 and s and not s[0].instance_hypernyms() and w not in test and w not in spw and wn.morphy(w, "n") not in spw
pool = [w for w in m["words"][:6000] if ok(w)]
V = lib.vecs(set(pool)); pool = [w for w in pool if w in V]
sexok = {w for w in pool if wn.synsets(w, "n")[0].lexname() == "noun.person"}
site = {"names": np.array(m["names"]), "C": np.array(m["dict"]["C"]), "A": np.array(m["dict"]["A"])}; d45 = dict(np.load(f"{D}/dict45.npz"))
anch = [a for a in sz.NEW_ANCH if a[1] == "LAND"] + [a for a in sz.ANCH0 if a[0] != "body_of_water.n.01"]
o1 = sz.build(False, pool, V, sexok, {"dict": site}); o2 = sz.build(False, pool, V, sexok, {"dict": d45, "anch": anch})
roots = lambda c: [t.split("(")[0] for t in c.split("|")[0].split()]
chg = [w for w in pool if o1[w] != o2[w]]; land = [w for w in chg if "LAND" in roots(o2[w])]; side = [w for w in chg if "LAND" not in roots(o2[w])]
print(f"пул {len(pool)}: изменилось {len(chg)} ({len(chg) / len(pool):.0%}), с LAND {len(land)}, без LAND {len(side)}")
random.seed(20261016); fl = [w for w in land if w not in used]; fs = [w for w in side if w not in used]; print("свежих", len(fl), len(fs))
its = [{"w": w, "grp": "LAND", "sz": o1[w], "sz2": o2[w]} for w in random.sample(fl, min(72, len(fl)))]
its += [{"w": w, "grp": "-", "sz": o1[w], "sz2": o2[w]} for w in random.sample(fs, min(24, len(fs)))]
json.dump(its, open(f"{D}/items.json", "w"), indent=1)
S = sys.argv[1]; lists = []; k = 0
for var, key, spec in (("old", "sz", "spec_old.md"), ("new", "sz2", "spec_land.md")):
    ws = list(its); random.shuffle(ws)
    for j in range(2):
        ch = ws[j::2]
        for rep in (1, 2):
            k += 1; d = f"{S}/r{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/{spec}").read()); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[key]}\n" for i, o in enumerate(ch)))
            lists.append({"r": k, "var": var, "words": [o["w"] for o in ch]})
json.dump(lists, open(f"{D}/lists.json", "w"), indent=1); print("читателей", k, "слов", len(its))
