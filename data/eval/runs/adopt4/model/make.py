# Тест 2: модель пишет коды без LAND (spec_old, 44 корня), затем другая модель с spec_land (45) переписывает только те коды,
# где LAND делает слово яснее (как ../newroots H2). Слова: 60 из пула ../adopt с первым значением noun.location / noun.object
# (местность, вода, суша — там LAND может понадобиться) + 20 случайных; ни одного из ../adopt, ../adopt2, ../adopt3.
#   python model/make.py SCRATCH  → model/items.json, SCRATCH/wK/{spec.md,list.md,task.md}
import json, os, random, sys
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../.."; from nltk.corpus import wordnet as wn
pool = json.load(open(f"{D}/../pool.json")); used = {o["w"] for p in ("adopt", "adopt2", "adopt3") for o in json.load(open(f"{R}/{p}/items.json"))}
pool = [w for w in pool if w not in used]; random.seed(20261017)
geo = [w for w in pool if wn.synsets(w, "n")[0].lexname() in ("noun.location", "noun.object")]; print("geo", len(geo))
ws = random.sample(geo, 60); ws += random.sample([w for w in pool if w not in set(geo)], 20); random.shuffle(ws)
its = [{"w": w, "gloss": wn.synsets(w, "n")[0].definition(), "geo": w in set(geo)} for w in ws]
json.dump(its, open(f"{D}/items.json", "w"), indent=1)
S = sys.argv[1]
T1 = """# Task: write min-co codes

spec.md explains how min-co words are written. list.md gives numbered English nouns with their main sense after the dash.
For each noun write the code that lets a reader who knows only spec.md guess the noun (or a word of the same meaning) most surely:
`ROOTS | o`, at most 3 roots, only roots from spec.md, form marks after `|` if they help.

Write answers.md in ONE single write with exactly one line per noun, same numbering:
N. code
Check that answers.md has as many lines as list.md, then reply "done".
"""
for k in (1, 2):
    d = f"{S}/w{k}"; os.makedirs(d, exist_ok=True); ch = its[(k - 1) * 40:k * 40]
    open(f"{d}/spec.md", "w").write(open(f"{R}/adopt3/spec_old.md").read()); open(f"{d}/task.md", "w").write(T1)
    open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {o['w']} — {o['gloss']}\n" for i, o in enumerate(ch)))
