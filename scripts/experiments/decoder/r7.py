"""Порядок корней в математике: веса центра wc и оси wa по позициям; декодер-смесь с позиционными весами в «И».
Метрика порядка: место слова, если поменять местами первые два корня."""
import itertools, json, sys, time, multiprocessing as mp
import numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names = m['names']; has = np.array(m['has_axis']); s = m['s']
C, A = (np.array(m['dicts']['learned'][k], dtype=np.float32) for k in 'CA'); R_ = len(C)
M = np.concatenate([C, A]); G = M @ M.T
LV = list(range(-5, 6))
VARS = {  # имя: (веса центра по позициям, веса оси по позициям)
    "A сейчас 1/.6/.6": ([1, .6, .6], [1, .6, .6]),
    "G убывающие 1/.6/.36": ([1, .6, .36], [1, .6, .36]),
    "M центр модиф. ×.5": ([1, .3, .3], [1, .6, .6]),
    "M центр модиф. ×.25": ([1, .15, .15], [1, .6, .6]),
    "M+G": ([1, .3, .18], [1, .6, .36]),
}
grids = {}
def grid(flags):
    if flags not in grids: grids[flags] = np.array(list(itertools.product(*[LV if f else [0] for f in flags])), dtype=np.float32)
    return grids[flags]
def wvec(S2, wc, wa):
    k = len(S2); c = np.array(wc[:k], dtype=np.float32); a = np.array(wa[:k], dtype=np.float32)
    c = np.where(has[S2], c, np.maximum(c, a))      # у корня без оси центр — всё, что он даёт
    return c, a
def encode(x, wc, wa):
    cx, ax = C @ x, A @ x; cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:8]); best = (-2,)
    sym = wc[1] == wc[2] and wa[1] == wa[2]
    for k in (1, 2, 3):
        for Sx in itertools.combinations(cand, k):
            orders = ([[Sx[h]] + [r for i, r in enumerate(Sx) if i != h] for h in range(k)] if sym else [list(p) for p in itertools.permutations(Sx)])
            for S2 in orders:
                c, a = wvec(S2, wc, wa); Gr = grid(tuple(has[S2])); idx = S2 + [R_ + r for r in S2]
                U = np.concatenate([np.broadcast_to(c, Gr.shape), a * s * Gr], 1)
                cos = (U @ np.concatenate([cx[S2], ax[S2]])) / np.sqrt(np.maximum(((U @ G[np.ix_(idx, idx)]) * U).sum(1), 1e-9))
                i = int(np.argmax(cos))
                if cos[i] > best[0]: best = (float(cos[i]), [int(r) for r in S2], [int(t) for t in Gr[i]])
    return best
unit = lambda x: x / (np.linalg.norm(x, axis=-1, keepdims=True) + 1e-9)
zc = lambda q: (q - q.mean(0)) / q.std(0)
def parts(R, v, wc, wa):
    c, a = wvec(list(R), wc, wa); return [cj * C[r] + aj * s * x * A[r] for r, x, cj, aj in zip(R, v, c, a)]
HUBS = {}
def hub(key):
    if key not in HUBS:
        wc, wa = VARS[key]; g = np.random.default_rng(0); Y = []
        for _ in range(3000):
            k = g.integers(1, 4); R = list(g.choice(R_, k, replace=False)); Y.append(unit(sum(parts(R, [int(g.integers(-5, 6)) if has[r] else 0 for r in R], wc, wa))))
        HUBS[key] = np.sort(V @ np.stack(Y).T, 1)[:, -10:].mean(1)
    return HUBS[key]
def rank(i, R, v, key, posw):
    wc, wa = VARS[key]; P = parts(R, v, wc, wa); Sv = V @ unit(sum(P))
    Z = zc(V @ unit(np.stack(P)).T)
    pw = np.array(wc[:len(R)]) + np.array(wa[:len(R)]) if posw else np.ones(len(R))
    soft = -np.log((np.exp(-2 * Z) * pw / pw.max()).sum(1)) / 2
    mix = 0.5 * zc(2 * Sv - hub(key)) + 0.5 * soft
    return int((mix > mix[i]).sum()) + 1, [W[t] for t in np.argsort(-mix)[:3]]
def work(a):
    i, key = a; wc, wa = VARS[key]; c, R, v = encode(V[i], wc, wa)
    r0, top = rank(i, R, v, key, False); r1, _ = rank(i, R, v, key, True)
    rs = rank(i, [R[1], R[0]] + R[2:], [v[1], v[0]] + v[2:], key, True)[0] if len(R) > 1 else None
    return dict(cos=c, R=R, v=v, r=r0, rp=r1, swap=rs, top=top)
if __name__ == '__main__':
    d = json.load(open(SP + 'r5_8421.json')); idx = d['idx'][:int(sys.argv[1])]; out = {'idx': idx}
    for key in VARS:
        t0 = time.time(); hub(key)
        with mp.Pool(8) as p: out[key] = p.map(work, [(i, key) for i in idx], chunksize=5)
        x = out[key]; r = np.array([e['r'] for e in x]); rp = np.array([e['rp'] for e in x]); sw = np.array([e['swap'] for e in x if e['swap']]); rr = np.array([e['rp'] for e in x if e['swap']])
        print(f"{key:22s} cos {np.mean([e['cos'] for e in x]):.3f} | смесь top1 {np.mean(r==1):5.1%} | с позиц. «И» top1 {np.mean(rp==1):5.1%} top10 {np.mean(rp<=10):5.1%}"
              f" | перестановка 1↔2: слово теряет 1-е место {np.mean((sw>1)&(rr==1))/max(np.mean(rr==1),1e-9):5.1%}, медиана места {np.median(sw):.0f}  ({time.time()-t0:.0f} с)", flush=True)
    json.dump(out, open(SP + f'r7_{len(idx)}.json', 'w'))
