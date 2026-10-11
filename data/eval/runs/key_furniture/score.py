"""Подсчёт: для каждого варианта key / furniture — сколько декодеров назвали слово первым и в тройке; что читали вместо него; наполнители — контроль."""
import json, re, glob, collections
from nltk.corpus import wordnet as wn
k = json.load(open("key.json"))
OK = {"key": {"key", "keys"}, "furniture": {"furniture", "furnishings", "furnishing"}}
def lem(w):
    w = w.strip().lower().strip('.*`"'); return {w} | {x for p in 'nvar' for x in [wn.morphy(w.replace(' ', '_'), p)] if x}
res = collections.defaultdict(list); fill = [0, 0]
for f in sorted(glob.glob('dec_*.md')):
    s = str(int(f[4:6])); ans = {}
    for l in open(f):
        m = re.match(r'\s*(\d+)\.\s*(.*)', l)
        if m: ans[int(m[1])] = [x.strip() for x in re.split(r'[|,]', m[2]) if x.strip()]
    for i, (w, c, n) in enumerate(k["sheets"][s], 1):
        a = ans.get(i, []); t = OK.get(w, {w})
        hit = lambda x: bool(lem(x) & t)
        top1 = bool(a) and hit(a[0]); top3 = any(hit(x) for x in a[:3])
        if n: res[w, n].append((top1, top3, a[0] if a else '—'))
        else: fill[0] += top1; fill[1] += 1
for w, L in (("key", k["K"]), ("furniture", k["F"])):
    print(f"\n### {w}\n\n| # | код | слов | первым | в тройке | прочитано первым |\n|--:|---|:-:|--:|--:|---|")
    rows = sorted(((sum(a for a, _, _ in res[w, n]), sum(b for _, b, _ in res[w, n]), n, c) for n, c in enumerate(L, 1)), key=lambda r: (-r[0], -r[1]))
    for t1, t3, n, c in rows:
        r = res[w, n]; print(f"| {n} | `{c}` | {1 + (' PI ' in c)} | {t1}/{len(r)} | {t3}/{len(r)} | {', '.join(x for _, _, x in r)} |")
print(f"\nНаполнители (проверенные рецепты, контроль): первым {fill[0]} из {fill[1]}")
