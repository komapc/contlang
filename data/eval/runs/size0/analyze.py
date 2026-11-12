"""size0: lexicon size vs accuracy from data already collected (no new agents).

Metric: "share of text understood" U(L) = share of Brown content-word tokens (noun, verb, adj, adv; function words from
lexn1 FUNC excluded) a blind reader reads as close (judge 2 of 0–2), given L units to learn. L = base (min-co v1: 76 by the
retell1 rule; v2b: 82; Toki Pona: 120) + N lexicon entries (the first N Brown lemmas). A lexicon word is read right with
probability a_lex (ceiling 1.0; variant 0.9); the rest are composed, with accuracy a(frequency band) from big1000
(1000 random words from the first 10 000, Haiku encoder "llm", first answer, Haiku judge).
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size0/analyze.py
"""
import collections, json, re
from pathlib import Path
from nltk.corpus import brown, wordnet as wn

D = Path(__file__).resolve().parent
B = D.parent / "big1000"
FUNC = set((D.parent / "lexn1/run.py").read_text().split('FUNC = set("""')[1].split('"""')[0].split())
P = {"NN": "n", "VB": "v", "JJ": "a", "RB": "r"}
cnt = collections.Counter()
for w, t in brown.tagged_words():
    p, w = P.get(t[:2]), w.lower()
    if p and w.isalpha():
        cnt[wn.morphy(w, p) or w] += 1
for f in FUNC:
    cnt.pop(f, None)
rank = {w: k + 1 for k, (w, _) in enumerate(cnt.most_common())}
tot = sum(cnt.values())

L = json.load(open(D.parent / "reader/labels.json"))
items = {o["w"]: o for o in json.load(open(B / "items.json"))}
lab = {}
for l in json.load(open(B / "lists.json")):
    a = {int(m[1]): m[2].split("|")[0].strip().lower() for x in open(B / f"answers/r{l['r']}_{l['var']}.md")
         if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    for i, w in enumerate(l["words"]):
        k = f"{w}\t{a.get(i + 1, '—')}"
        if k in L:
            lab[(l["var"], w)] = L[k]
PP = {"noun": "n", "verb": "v", "adjective": "a", "adverb": "r"}
def lemma_rank(w):
    p = PP.get(items[w]["pos"])
    lm = (wn.morphy(w, p) if p else None) or w
    return rank.get(lm, 10 ** 6)

BANDS = [(1, 300), (301, 1000), (1001, 3000), (3001, 10000), (10001, 10 ** 7)]
out = ["# size0 — result", "", "## Composition accuracy by frequency (big1000, first answer, close)", ""]
acc = {}
for v in ("llm", "math"):
    for lo, hi in BANDS:
        x = [lab[(v, w)] == 2 for w in items if (v, w) in lab and lo <= lemma_rank(w) <= hi]
        acc[(v, lo)] = sum(x) / len(x) if x else None
        out.append(f"  {v:4s} rank {lo}–{hi if hi < 10 ** 6 else '…'}: n {len(x):4d}, close {acc[(v, lo)]:.0%}" if x else f"  {v} {lo}: empty")
def band(r):
    return next(lo for lo, hi in BANDS if lo <= r <= hi)
def U(N, v="llm", a_lex=1.0):
    s = 0
    for w, c in cnt.items():
        r = rank[w]
        s += c * (a_lex if r <= N else acc[(v, band(r))])
    return s / tot
out += ["", "## Share of text understood U(N) (Brown content words; base min-co v1 = 76, used by big1000)", "",
        "| N entries | L = 76 + N | text coverage | U, a_lex 1.0 | U, a_lex 0.9 |", "|---|---|---|---|---|"]
curve = []
for N in (0, 10, 20, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000, 20000):
    cov = sum(c for w, c in cnt.items() if rank[w] <= N) / tot
    u1, u9 = U(N), U(N, a_lex=0.9)
    curve.append({"N": N, "L": 76 + N, "cov": cov, "U": u1, "U09": u9})
    out.append(f"| {N} | {76 + N} | {cov:.0%} | {u1:.0%} | {u9:.0%} |")
json.dump(curve, open(D / "curve.json", "w"), indent=1)
(D / "result.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
