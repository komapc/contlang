# Честная проверка новых корней: SZ на обученном словаре 44 корней (dict44) против 47 (dict47, learn.py); у всех корней одна
# выраженность. Пул — как ../adopt (частые существительные сайта). 40 изменённых слов на новый корень и 40 изменённых без новых корней (побочный сдвиг словаря).
#   python make.py SCRATCH  → items.json, lists.json, SCRATCH/rN/{spec,codes}.md
import json, os, random, re, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [f"{D}/../reader", f"{D}/../newroots"]
import lib, sz
from nltk.corpus import wordnet as wn
NEW = ("LAND", "SACRED", "CONTAINER")
m = sz.m; test = {o["w"] for o in json.load(open(f"{D}/../measure/items.json"))}
sp47 = open(f"{D}/../adopt/spec_new.md").read(); spw = set(re.findall(r"[a-z]+", sp47[sp47.index("## Roots"):sp47.index("## Form")]))
def ok(w):
    s = wn.synsets(w, "n")
    return w.isalpha() and w.islower() and len(w) > 2 and s and not s[0].instance_hypernyms() and w not in test and w not in spw and wn.morphy(w, "n") not in spw
pool = [w for w in m["words"][:6000] if ok(w)]
SP2 = lib.spec_from(f"{D}/../adopt/spec_new.md")
V = lib.vecs(set(pool) | {w for r in SP2.values() for _, ws in r["pts"] for w in ws} | {w for r in SP2.values() for w in r["plain"]})
pool = [w for w in pool if w in V]
sexok = {w for w in pool if wn.synsets(w, "n")[0].lexname() == "noun.person"}
d44, d47 = (dict(np.load(f"{D}/dict{t}.npz")) for t in ("44", "47"))
o1 = sz.build(False, pool, V, sexok, {"dict": d44}); o2 = sz.build(True, pool, V, sexok, {"dict": d47})
roots = lambda c: [t.split("(")[0] for t in c.split("|")[0].split()]
random.seed(20261015); its = []
for r in NEW:
    ws = [w for w in pool if o1[w] != o2[w] and next((x for x in roots(o2[w]) if x in NEW), None) == r]
    print(r, "изменённых", len(ws), "в кодах всего", sum(r in roots(o2[w]) for w in pool)); its += [{"w": w, "root": r, "sz": o1[w], "sz2": o2[w]} for w in random.sample(ws, 40)]
side = [w for w in pool if o1[w] != o2[w] and not set(roots(o2[w])) & set(NEW)]; its += [{"w": w, "root": "-", "sz": o1[w], "sz2": o2[w]} for w in random.sample(side, 40)]
ch = sum(o1[w] != o2[w] for w in pool); print(f"пул {len(pool)}, изменилось {ch} ({ch / len(pool):.0%}), из них без новых корней {sum(o1[w] != o2[w] and not set(roots(o2[w])) & set(NEW) for w in pool)}")
json.dump(its, open(f"{D}/items.json", "w"), indent=1)
S = sys.argv[1]; lists = []; k = 0
for var, key, spec in (("old", "sz", "spec_old.md"), ("new", "sz2", "spec_new.md")):
    ws = list(its); random.shuffle(ws)
    for j in range(3):
        ch = ws[j::3]
        for rep in (1, 2):
            k += 1; d = f"{S}/r{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/../adopt/{spec}").read()); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[key]}\n" for i, o in enumerate(ch)))
            lists.append({"r": k, "var": var, "words": [o["w"] for o in ch]})
json.dump(lists, open(f"{D}/lists.json", "w"), indent=1); print("читателей", k)
