"""size0: размер словаря ↔ точность по уже собранным данным (без новых агентов).

Метрика — «понятая доля текста» U(L): доля словоупотреблений знаменательных слов Brown (сущ., глаг., прил., нареч.;
служебные из lexn1 FUNC не считаются), которые слепой читатель прочитает «близко» (судья 2 из 0–2), при L заучиваемых
единицах. L = база (min-co v1: 76 по правилу retell1; v2b: 82; Toki Pona: 120) + N статей словаря (первые N лемм Brown).
Слово из словаря читается с точностью a_lex (потолок 1,0; вариант 0,9), остальное — сборкой, точность a(полоса частоты)
из big1000 (1000 случайных слов из первых 10 000, кодер Haiku «llm», первый ответ, судья Haiku).
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
out = ["# size0 — результат", "", "## Точность сборки по частоте (big1000, первый ответ, «близко»)", ""]
acc = {}
for v in ("llm", "math"):
    for lo, hi in BANDS:
        x = [lab[(v, w)] == 2 for w in items if (v, w) in lab and lo <= lemma_rank(w) <= hi]
        acc[(v, lo)] = sum(x) / len(x) if x else None
        out.append(f"  {v:4s} ранг {lo}–{hi if hi < 10 ** 6 else '…'}: n {len(x):4d}, близко {acc[(v, lo)]:.0%}" if x else f"  {v} {lo}: пусто")
def band(r):
    return next(lo for lo, hi in BANDS if lo <= r <= hi)
def U(N, v="llm", a_lex=1.0):
    s = 0
    for w, c in cnt.items():
        r = rank[w]
        s += c * (a_lex if r <= N else acc[(v, band(r))])
    return s / tot
out += ["", "## Понятая доля текста U(N) (Brown, знаменательные слова; база min-co v1 = 76, на ней писал big1000)", "",
        "| N статей | L = 76 + N | покрытие текста | U, a_lex 1,0 | U, a_lex 0,9 |", "|---|---|---|---|---|"]
curve = []
for N in (0, 100, 300, 1000, 2000, 3000, 5000, 10000, 20000):
    cov = sum(c for w, c in cnt.items() if rank[w] <= N) / tot
    u1, u9 = U(N), U(N, a_lex=0.9)
    curve.append({"N": N, "L": 76 + N, "cov": cov, "U": u1, "U09": u9})
    out.append(f"| {N} | {76 + N} | {cov:.0%} | {u1:.0%} | {u9:.0%} |")
json.dump(curve, open(D / "curve.json", "w"), indent=1)
(D / "result.txt").write_text("\n".join(out) + "\n")
print("\n".join(out))
