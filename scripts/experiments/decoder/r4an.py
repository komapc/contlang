"""Анализ: ранги слова после кода (≤3 / ≤4 корня) и декодера (сумма / смесь)."""
import json, sys, collections
sys.path.insert(0, 'scripts')
import numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(float)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names = m['names']; has = np.array(m['has_axis']); HW, S = m['head_w'], m['s']
C, A = (np.array(m['dict'][k]) for k in 'CA')
unit = lambda x: x / (np.linalg.norm(x, axis=-1, keepdims=True) + 1e-9)
zc = lambda s: (s - s.mean(0)) / s.std(0)
freq = {l.split('\t')[0]: l.rstrip('\n').split('\t')[1] for l in list(open('data/wordlist_en_x5.tsv'))[1:]}
d = json.load(open(SP + sys.argv[1])); idx = d['idx']
comp = lambda R, v: [(1.0 if j == 0 else HW) * (C[r] + S * x * A[r]) for j, (r, x) in enumerate(zip(R, v))]
rng = np.random.default_rng(0); Y = []
for _ in range(3000):
    k = rng.integers(1, 5); R = list(rng.choice(len(names), k, replace=False))
    Y.append(unit(sum(comp(R, [int(rng.integers(-5, 6)) if has[r] else 0 for r in R]))))
HUB = np.sort(V @ np.stack(Y).T, 1)[:, -10:].mean(1)
fmt = lambda R, v: " ".join(names[r] + (f"(={x:+d})" if has[r] else "") for r, x in zip(R, v))
res = {}
for k in ('3', '4'):
    codes = d[k]; rs, rm, cosx, tops, topm = [], [], [], [], []
    for a in range(0, len(idx), 400):
        ch = list(zip(idx[a:a+400], codes[a:a+400]))
        Ys = np.stack([unit(sum(comp(R, v))) for _, (R, v) in ch])
        Ss = V @ Ys.T                                   # 10721 × n
        Ps = [unit(np.stack(comp(R, v))) for _, (R, v) in ch]
        Z = zc(V @ np.concatenate(Ps).T)               # z по словарю для каждого корня
        off = np.cumsum([0] + [len(p) for p in Ps])
        soft = np.stack([-np.log(np.exp(-2 * Z[:, off[j]:off[j+1]]).sum(1)) / 2 for j in range(len(ch))], 1)
        mix = 0.5 * zc(2 * Ss - HUB[:, None]) + 0.5 * soft
        for j, (i, _) in enumerate(ch):
            rs.append(int((Ss[:, j] > Ss[i, j]).sum()) + 1); rm.append(int((mix[:, j] > mix[i, j]).sum()) + 1)
            cosx.append(float(Ys[j] @ V[i]))
            tops.append([W[t] for t in np.argsort(-Ss[:, j])[:3]]); topm.append([W[t] for t in np.argsort(-mix[:, j])[:3]])
    res[k] = dict(sum=rs, mix=rm, cos=cosx, tops=tops, topm=topm)
json.dump(res, open(SP + 'r4_res.json', 'w'))
st = lambda r: (lambda r: f"top1 {np.mean(r==1):5.1%}  top3 {np.mean(r<=3):5.1%}  top10 {np.mean(r<=10):5.1%}  top100 {np.mean(r<=100):5.1%}  медиана {int(np.median(r))}")(np.array(r))
isf = np.array([W[i] in freq for i in idx])
for k in ('3', '4'):
    print(f"\n### ≤{k} корней   cos(код, слово) средний {np.mean(res[k]['cos']):.3f}")
    for h in ('sum', 'mix'):
        r = np.array(res[k][h]); print(f"{h:4s} все   {st(r)}\n{h:4s} частые {st(r[isf])}   ({isf.sum()})\n{h:4s} редкие {st(r[~isf])}")
n4 = [len(R) for R, v in d['4']]; print("\nдлина кодов ≤4:", collections.Counter(n4), " ≤3:", collections.Counter(len(R) for R, v in d['3']))
r3, r4 = np.array(res['3']['mix']), np.array(res['4']['mix'])
print(f"4-й корень (смесь): лучше {np.mean(r4<r3):.1%}, хуже {np.mean(r4>r3):.1%}")
order = np.argsort(-r4)
print("\n## Худшие 40 (≤4, смесь)\n| слово | частое | код | cos | место сумма/смесь | смесь читает |")
for j in order[:40]:
    i = idx[j]; print(f"| {W[i]} | {'да' if isf[j] else ''} | `{fmt(*d['4'][j])}` | {res['4']['cos'][j]:.2f} | {res['4']['sum'][j]}/{r4[j]} | {', '.join(res['4']['topm'][j])} |")
print("\n## Худшие частые 30\n| слово | код | cos | место сумма/смесь | смесь читает |")
for j in [j for j in order if isf[j]][:30]:
    i = idx[j]; print(f"| {W[i]} | `{fmt(*d['4'][j])}` | {res['4']['cos'][j]:.2f} | {res['4']['sum'][j]}/{r4[j]} | {', '.join(res['4']['topm'][j])} |")
# что общего у худших: корни, части речи, cos
bad = r4 > 100
rc = collections.Counter(names[R[0]] for (R, v), b in zip(d['4'], bad) if b); ra = collections.Counter(names[R[0]] for R, v in d['4'])
print(f"\nхудших (место >100): {bad.sum()} ({bad.mean():.1%}); cos у них {np.mean(np.array(res['4']['cos'])[bad]):.3f} против {np.mean(np.array(res['4']['cos'])[~bad]):.3f}")
print("главный корень у худших (доля среди кодов с этим главным):", ", ".join(f"{n} {c}/{ra[n]}" for n, c in sorted(rc.items(), key=lambda x: -x[1]/ra[x[0]])[:12]))
pc = collections.Counter(freq[W[i]] for i, b in zip(idx, bad) if b and W[i] in freq); pa = collections.Counter(freq[W[i]] for i in idx if W[i] in freq)
print("части речи у худших частых:", ", ".join(f"{p} {pc[p]}/{pa[p]}" for p in pa))
