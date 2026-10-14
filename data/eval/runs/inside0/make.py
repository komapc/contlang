# INSIDE(=0) — «на границе»: подпись середины оси INSIDE (spec_new) против нынешней (spec_old, 44 корня, без LAND).
# 100 слов поля «граница, край, поверхность» (words.json). Шаг 1: Haiku пишет коды по spec_old (w1..w4); шаг 2: другая Haiku со
# spec_new переписывает только те, где новая подпись помогает (v1..v4); шаг 3: изменённые читают по 4 слепых читателя.
#   python make.py write SCRATCH | revise SCRATCH | read SCRATCH
import json, os, re, random, sys
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); step, S = sys.argv[1], sys.argv[2]; W = json.load(open(f"{D}/words.json"))
T1 = open(f"{D}/../adopt4/model/make.py").read().split('T1 = """')[1].split('"""')[0]
T2 = """# Task: improve min-co codes with a clarified scale

spec.md explains how min-co words are written. The root INSIDE now has a labelled middle: INSIDE(=0) means on the border, at the edge, the surface.
list.md gives numbered English nouns (with their main sense after the dash) and the current code for each, after "→".

For each noun: if INSIDE(=0) would let a reader who knows only spec.md guess the noun clearly more surely, write a new code
(`ROOTS | o`, with form marks if they help; at most 3 roots; only roots from spec.md). Otherwise copy the current code exactly as it is.

Write answers.md in ONE single write with exactly one line per noun, same numbering:
N. code
Check that answers.md has as many lines as list.md, then reply "done".
"""
gl = lambda w: wn.synsets(w)[0].definition()
rd = lambda f: [re.match(r"\s*\d+\.\s*(.*)", l)[1].strip() for l in open(f) if l.strip()]
if step == "write":
    for k in range(4):
        d = f"{S}/w{k + 1}"; os.makedirs(d, exist_ok=True); ch = W[k * 25:(k + 1) * 25]
        open(f"{d}/spec.md", "w").write(open(f"{D}/spec_old.md").read()); open(f"{d}/task.md", "w").write(T1)
        open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {w} — {gl(w)}\n" for i, w in enumerate(ch)))
if step == "revise":
    its = []
    for k in range(4):
        a = rd(f"{S}/w{k + 1}/answers.md"); ch = W[k * 25:(k + 1) * 25]; assert len(a) == 25, (k, len(a))
        its += [{"w": w, "old": c} for w, c in zip(ch, a)]
        d = f"{S}/v{k + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/spec.md", "w").write(open(f"{D}/spec_new.md").read()); open(f"{d}/task.md", "w").write(T2)
        open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {w} — {gl(w)} → {c}\n" for i, (w, c) in enumerate(zip(ch, a))))
    json.dump(its, open(f"{D}/items.json", "w"), indent=1)
if step == "read":
    its = json.load(open(f"{D}/items.json"))
    for k in range(4):
        a = rd(f"{S}/v{k + 1}/answers.md"); assert len(a) == 25
        for o, c in zip(its[k * 25:(k + 1) * 25], a): o["new"] = c
    json.dump(its, open(f"{D}/items.json", "w"), indent=1)
    ch = [o for o in its if o["new"] != o["old"]]; print("изменено", len(ch)); [print(" ", o["w"], "|", o["old"], "->", o["new"]) for o in ch]
    random.seed(20261020); lists = []; k = 0
    for var, spec in (("old", "spec_old.md"), ("new", "spec_new.md")):
        for rep in range(4):
            random.shuffle(ch); k += 1; d = f"{S}/r{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/{spec}").read()); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[var]}\n" for i, o in enumerate(ch)))
            lists.append({"r": k, "var": var, "words": [o["w"] for o in ch]})
    json.dump(lists, open(f"{D}/lists.json", "w"), indent=1)
