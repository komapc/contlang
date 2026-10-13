# Проверка новых корней и удаления старых на свежих словах (не из ../measure): частые существительные сайта (ранг < 6000, не имена,
# не слова из подписей спецификации). NR — слова, чей код SZ → SZ2 изменился, по 40 на новый корень (первый новый корень в коде SZ2).
# AB — слова, чей код SZ2 содержит SIDE, CARE или MOOD, по 30 на корень; вариант drop — SZ2 без этих трёх корней (спецификация 44).
#   python make.py SCRATCH  → items.json, spec_*.md, SCRATCH/rN/{spec,codes}.md, lists.json
import json, os, random, re, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [f"{D}/../reader", f"{D}/../newroots"]
import lib, sz
from nltk.corpus import wordnet as wn
NEW, DROP = ("LAND", "SACRED", "CONTAINER"), ("SIDE", "CARE", "MOOD")
m = sz.m; test = {o["w"] for o in json.load(open(f"{D}/../measure/items.json"))}
sp47 = open(f"{D}/../newroots/spec.md").read(); sp44 = open(f"{D}/../reader/spec.md").read()
spd = "".join(l for l in sp47.splitlines(True) if not any(l.startswith(f"- {r}:") for r in DROP)).replace("## Roots (47)", "## Roots (44)")
for n, t in (("spec_old.md", sp44), ("spec_new.md", sp47), ("spec_drop.md", spd)): open(f"{D}/{n}", "w").write(t)
spw = set(re.findall(r"[a-z]+", sp47[sp47.index("## Roots"):sp47.index("## Form")]))
def ok(w):
    s = wn.synsets(w, "n")
    return w.isalpha() and w.islower() and len(w) > 2 and s and not s[0].instance_hypernyms() and w not in test and w not in spw and wn.morphy(w, "n") not in spw
pool = [w for w in m["words"][:6000] if ok(w)]
SP2 = lib.spec_from(f"{D}/spec_new.md")
V = lib.vecs(set(pool) | {w for r in SP2.values() for _, ws in r["pts"] for w in ws} | {w for r in SP2.values() for w in r["plain"]})
pool = [w for w in pool if w in V]
sexok = {w for w in pool if wn.synsets(w, "n")[0].lexname() == "noun.person"}
o1, o2 = sz.build(False, pool, V, sexok), sz.build(True, pool, V, sexok); o3 = sz.build(True, pool, V, sexok, {"drop": DROP})
roots = lambda c: [t.split("(")[0] for t in c.split("|")[0].split()]
random.seed(20261014); its = []
for r in NEW:
    ws = [w for w in pool if o1[w] != o2[w] and next((x for x in roots(o2[w]) if x in NEW), None) == r]
    print(r, "изменённых", len(ws)); its += [{"w": w, "set": "NR", "root": r, "sz": o1[w], "sz2": o2[w]} for w in random.sample(ws, 40)]
used = {o["w"] for o in its}
for r in DROP:
    ws = [w for w in pool if r in roots(o2[w]) and w not in used and o3[w] != o2[w]]
    print(r, "в SZ2", len(ws)); s = random.sample(ws, 30); used |= set(s); its += [{"w": w, "set": "AB", "root": r, "sz2": o2[w], "drop": o3[w]} for w in s]
ch = sum(o1[w] != o2[w] for w in pool); print(f"пул {len(pool)}, SZ → SZ2 изменилось {ch} ({ch / len(pool):.0%}); с {'/'.join(DROP)}: {sum(any(r in roots(o2[w]) for r in DROP) for w in pool)}")
json.dump(its, open(f"{D}/items.json", "w"), indent=1)
# варианты: old (sz, spec_old), new (sz2, spec_new), drop (spec_drop); список ≤ 70 строк, по 2 читателя
S = sys.argv[1]; lists = []; k = 0
for var, key, spec in (("old", "sz", "spec_old.md"), ("new", "sz2", "spec_new.md"), ("drop", "drop", "spec_drop.md")):
    ws = [o for o in its if key in o]; random.shuffle(ws); n = -(-len(ws) // 70); per = -(-len(ws) // n)
    for j in range(n):
        ch = ws[j * per:(j + 1) * per]
        for rep in (1, 2):
            k += 1; d = f"{S}/r{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/{spec}").read()); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[key]}\n" for i, o in enumerate(ch)))
            lists.append({"r": k, "var": var, "words": [o["w"] for o in ch]})
json.dump(lists, open(f"{D}/lists.json", "w"), indent=1); print("читателей", k, [len(l["words"]) for l in lists])
