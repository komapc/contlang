import json, collections, numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']; names = m['names']; has = m['has_axis']
d = json.load(open(SP + 'r4_codes_10000.json')); res = json.load(open(SP + 'r4_res.json')); idx = d['idx']
low = {l.strip() for l in open('/usr/share/dict/words') if l.strip().islower()}
freq = {l.split('\t')[0] for l in list(open('data/wordlist_en_x5.tsv'))[1:]}
keep = np.array([W[i] in low or W[i] in freq for i in idx]); print("нарицательных:", keep.sum(), "из", len(idx), " частых среди них:", sum(W[i] in freq for i in idx))
fmt = lambda R, v: " ".join(names[r] + (f"(={x:+d})" if has[r] else "") for r, x in zip(R, v))
st = lambda r: f"top1 {np.mean(r==1):5.1%}  top3 {np.mean(r<=3):5.1%}  top10 {np.mean(r<=10):5.1%}  top100 {np.mean(r<=100):5.1%}  медиана {int(np.median(r))}"
for k in '34':
    for h in ('sum', 'mix'): print(f"≤{k} {h:4s} {st(np.array(res[k][h])[keep])}")
r3, r4 = np.array(res['3']['mix']), np.array(res['4']['mix'])
print(f"4-й корень на нарицательных (смесь): лучше {np.mean((r4<r3)[keep]):.1%}, хуже {np.mean((r4>r3)[keep]):.1%}")
J = [j for j in np.argsort(-r4) if keep[j]]
print("\n| слово | код (≤4) | cos | место сумма → смесь (≤3 смесь) | смесь читает |\n|---|---|--:|---|---|")
for j in J[:45]:
    print(f"| {W[idx[j]]} | `{fmt(*d['4'][j])}` | {res['4']['cos'][j]:.2f} | {res['4']['sum'][j]} → {r4[j]} ({r3[j]}) | {', '.join(res['4']['topm'][j])} |")
bad = keep & (r4 > 20); print("\nместо >20:", bad.sum(), f"({bad.sum()/keep.sum():.1%}); cos {np.mean(np.array(res['4']['cos'])[bad]):.3f} против {np.mean(np.array(res['4']['cos'])[keep & ~bad]):.3f}")
rc = collections.Counter(names[r] for (R, v), b in zip(d['4'], bad) if b for r in R); ra = collections.Counter(names[r] for (R, v), k in zip(d['4'], keep) if k for r in R)
print("корни у плохих (доля):", ", ".join(f"{n} {rc[n]}/{ra[n]}" for n in sorted(rc, key=lambda n: -rc[n]/ra[n])[:10]))
print("длина кода у плохих:", collections.Counter(len(d['4'][j][0]) for j in np.where(bad)[0]))
