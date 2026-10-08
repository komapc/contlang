"""Кодер «через декодер»: кандидаты-коды (лучший уровень для каждой комбинации корней и главного), из 40 лучших по cos
выбирается тот, у которого декодер-смесь ставит слово выше всего (при равенстве — больший cos)."""
import itertools, json, sys, time, multiprocessing as mp
sys.path.insert(0, 'scripts')
import numpy as np
from lib_code import Coder
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names = m['names']; has = np.array(m['has_axis']); HW, S = m['head_w'], m['s']
C, A = (np.array(m['dicts']['learned'][k]) for k in 'CA')
unit = lambda x: x / (np.linalg.norm(x, axis=-1, keepdims=True) + 1e-9)
zc = lambda s: (s - s.mean(0)) / s.std(0)
comp = lambda R, v: [(1.0 if j == 0 else HW) * (C[r] + S * x * A[r]) for j, (r, x) in enumerate(zip(R, v))]
rng = np.random.default_rng(0); Y = []
for _ in range(3000):
    k = rng.integers(1, 5); R = list(rng.choice(len(names), k, replace=False))
    Y.append(unit(sum(comp(R, [int(rng.integers(-5, 6)) if has[r] else 0 for r in R]))))
HUB = np.sort(V @ np.stack(Y).T, 1)[:, -10:].mean(1)
co8, co6 = Coder(C, A, head_w=HW), Coder(C, A, head_w=HW, topr=6)

def cands(co, x, m):
    cx, ax = co.C @ x, co.A @ x
    cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:co.topr]); out = []
    for k in range(1, m + 1):
        for Sx in itertools.combinations(cand, k):
            for h in (range(k) if k > 1 else [0]):
                S2 = [Sx[h]] + [r for i, r in enumerate(Sx) if i != h]
                w = np.array([1.0] + [co.hw] * (k - 1)); G = co.grid(tuple(co.has[S2])); idx = S2 + [co.R + r for r in S2]
                U = np.concatenate([np.broadcast_to(w, G.shape), w * co.s * G], 1)
                cos = (U @ np.concatenate([cx[S2], ax[S2]])) / np.sqrt(np.maximum(((U @ co.G[np.ix_(idx, idx)]) * U).sum(1), 1e-9))
                i = int(np.argmax(cos)); out.append((float(cos[i]), [int(r) for r in S2], [int(t) for t in G[i]]))
    return out

def ranks(i, cs):
    Ys = np.stack([unit(sum(comp(R, v))) for _, R, v in cs]); Ss = V @ Ys.T
    Ps = [unit(np.stack(comp(R, v))) for _, R, v in cs]; Z = zc(V @ np.concatenate(Ps).T); off = np.cumsum([0] + [len(p) for p in Ps])
    soft = np.stack([-np.log(np.exp(-2 * Z[:, off[j]:off[j+1]]).sum(1)) / 2 for j in range(len(cs))], 1)
    mix = 0.5 * zc(2 * Ss - HUB[:, None]) + 0.5 * soft
    return (mix > mix[i]).sum(0) + 1, (Ss > Ss[i]).sum(0) + 1

def work(a):
    i, m_ = a; x = V[i]
    cs = cands(co8, x, 3)
    if m_ == 4: cs += [c for c in cands(co6, x, 4) if len(c[1]) == 4]
    cs = sorted(cs, key=lambda c: -c[0])[:40]
    rm, rs = ranks(i, cs); j = min(range(len(cs)), key=lambda j: (rm[j], -cs[j][0]))
    return dict(cos0=cs[0][0], code0=cs[0][1:], mix0=int(rm[0]), sum0=int(rs[0]), cos=cs[j][0], code=cs[j][1:], mix=int(rm[j]), sum=int(rs[j]), pos=j)

if __name__ == '__main__':
    d = json.load(open(SP + 'r4_codes_10000.json'))
    low = {l.strip() for l in open('/usr/share/dict/words') if l.strip().islower()}
    freq = {l.split('\t')[0] for l in list(open('data/wordlist_en_x5.tsv'))[1:]}
    idx = [i for i in d['idx'] if W[i] in low or W[i] in freq][:int(sys.argv[1])]
    out = {'idx': idx}
    for m_ in (3, 4):
        t0 = time.time()
        with mp.Pool(8) as p: out[m_] = p.map(work, [(i, m_) for i in idx], chunksize=10)
        print(m_, f"{time.time()-t0:.0f} с", flush=True)
    json.dump(out, open(SP + f'r5_{len(idx)}.json', 'w'))
