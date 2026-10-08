"""Двойная ось: вес корня {1, .6, .3} свободно (B) против веса по позиции 1/.6/.6 (A). ≤3 корня, точный перебор по 8 опорам."""
import itertools, json, sys, time, multiprocessing as mp
import numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names = m['names']; has = np.array(m['has_axis']); HW, S = m['head_w'], m['s']
C, A = (np.array(m['dicts']['learned'][k], dtype=np.float32) for k in 'CA'); R_ = len(C)
M = np.concatenate([C, A]); G = M @ M.T; s = S
LV = list(range(-5, 6)); WS = [1.0, 0.6, 0.3]
grids = {}
def grid(flags):
    if flags not in grids: grids[flags] = np.array(list(itertools.product(*[LV if f else [0] for f in flags])), dtype=np.float32)
    return grids[flags]
def wsets(k, free):
    if not free: return [np.array([1.0] + [HW] * (k - 1))]
    return [np.array(w) for w in itertools.product(WS, repeat=k) if max(w) == 1.0]
def encode(x, free):
    cx, ax = C @ x, A @ x; cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:8]); best = (-2,)
    for k in (1, 2, 3):
        for Sx in itertools.combinations(cand, k):
            orders = [list(Sx)] if free else [[Sx[h]] + [r for i, r in enumerate(Sx) if i != h] for h in range(k)] if k > 1 else [list(Sx)]
            for S2 in orders:
                Gr = grid(tuple(has[S2])); idx = S2 + [R_ + r for r in S2]; GG = G[np.ix_(idx, idx)]; b = np.concatenate([cx[S2], ax[S2]])
                for w in wsets(k, free):
                    U = np.concatenate([np.broadcast_to(w, Gr.shape), w * s * Gr], 1)
                    cos = (U @ b) / np.sqrt(np.maximum(((U @ GG) * U).sum(1), 1e-9)); i = int(np.argmax(cos))
                    if cos[i] > best[0]: best = (float(cos[i]), [int(r) for r in S2], [int(t) for t in Gr[i]], [float(t) for t in w])
    return best
comp = lambda R, v, w: [wj * (C[r] + s * x * A[r]) for r, x, wj in zip(R, v, w)]
unit = lambda x: x / (np.linalg.norm(x, axis=-1, keepdims=True) + 1e-9)
zc = lambda a: (a - a.mean(0)) / a.std(0)
g = np.random.default_rng(0); Y = []
for _ in range(3000):
    k = g.integers(1, 4); R = list(g.choice(R_, k, replace=False)); Y.append(unit(sum(comp(R, [int(g.integers(-5, 6)) if has[r] else 0 for r in R], g.choice(WS, k)))))
HUB = np.sort(V @ np.stack(Y).T, 1)[:, -10:].mean(1)
def ranks(i, R, v, w):
    y = unit(sum(comp(R, v, w))); Sv = V @ y
    Z = zc(V @ unit(np.stack(comp(R, v, w))).T)
    soft = -np.log((np.array(w) * np.exp(-2 * Z)).sum(1)) / 2         # слабый корень меньше штрафует
    soft0 = -np.log(np.exp(-2 * Z).sum(1)) / 2
    mix = 0.5 * zc(2 * Sv - HUB) + 0.5 * soft; mix0 = 0.5 * zc(2 * Sv - HUB) + 0.5 * soft0
    rk = lambda a: int((a > a[i]).sum()) + 1
    return rk(Sv), rk(mix), rk(mix0)
def work(a):
    i, free = a; c, R, v, w = encode(V[i], free); return dict(cos=c, R=R, v=v, w=w, r=ranks(i, R, v, w))
if __name__ == '__main__':
    d = json.load(open(SP + 'r5_8421.json')); idx = d['idx'][:int(sys.argv[1])]
    out = {'idx': idx}
    for free in (False, True):
        t0 = time.time()
        with mp.Pool(8) as p: out[str(free)] = p.map(work, [(i, free) for i in idx], chunksize=5)
        print(free, f"{time.time()-t0:.0f} с", flush=True)
    json.dump(out, open(SP + f'r6_{len(idx)}.json', 'w'))
