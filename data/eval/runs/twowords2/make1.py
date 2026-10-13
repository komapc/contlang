# «Два слова» 2, шаг 1б: из nouns.txt (порядок случайный) первые 100 слов, у которых первый смысл-существительное в WordNet —
# само слово (не «gen → information») и толкование без informal / slang / abbreviation. → words.tsv (слово \t толкование), gen/words_K.md.
#   .venv/bin/python data/eval/runs/twowords2/make1.py
import os, re
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__))
out = []
for w in open(f"{D}/nouns.txt").read().split():
    ss = wn.synsets(w, "n")
    if not ss or wn.morphy(w, "n") != w or w not in [l.name() for l in ss[0].lemmas()]: continue
    if w.endswith("s") and wn.synsets(w[:-1], "n"): continue  # viewers, ways, findings: в WordNet своя лемма, но читается как множественное
    g = ss[0].definition()
    if re.search(r"informal|slang|abbreviation|offensive|obscene", g): continue
    out.append((w, g))
    if len(out) == 100: break
open(f"{D}/words.tsv", "w").write("".join(f"{w}\t{g}\n" for w, g in out))
for k in (1, 2):
    open(f"{D}/gen/words_{k}.md", "w").write("".join(f"{i + 1}. {w} — {g}\n" for i, (w, g) in enumerate(out[(k - 1) * 50:k * 50])))
print(len(out), ", ".join(w for w, _ in out))
