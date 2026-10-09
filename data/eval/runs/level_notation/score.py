"""Подсчёт: точное попадание (лучшее) и в тройке (лучшее + 2 альт.), по вариантам и типам пунктов.
Совпадение — та же лемма (WordNet morphy) или то же слово."""
import json, re, glob, collections
from nltk.corpus import wordnet as wn
key = json.load(open('key.json'))
def lem(w):
    w = w.strip().lower().strip('.*`')
    return {w} | {x for p in 'nvar' for x in [wn.morphy(w, p)] if x}
c = collections.Counter()
for f in sorted(glob.glob('dec_*.md')):
    v = f[4]; ans = {}
    for l in open(f):
        m = re.match(r'\s*(\d+)\.\s*(.*)', l)
        if m: ans[int(m[1])] = [x for x in re.split(r'[|,]', m[2]) if x.strip()]
    for i, (w, h, d, mod) in enumerate(key, 1):
        typ = 'уровень + уточнение' if mod else 'только уровень'
        a = ans.get(i, []); t = lem(w)
        top1 = bool(a) and bool(lem(a[0]) & t); top3 = any(lem(x) & t for x in a[:3])
        for k in (typ, 'всего'):
            c[v, k, 'n'] += 1; c[v, k, '1'] += top1; c[v, k, '3'] += top3
print('| вариант | тип | пунктов | лучшее | в тройке |\n|---|---|--:|--:|--:|')
for v in 'ABC':
    for k in ('только уровень', 'уровень + уточнение', 'всего'):
        n = c[v, k, 'n']
        if n: print(f"| {v} | {k} | {n} | {c[v,k,'1']/n:.0%} | {c[v,k,'3']/n:.0%} |")
