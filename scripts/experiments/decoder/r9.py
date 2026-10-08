"""Два слова вместо одного кода (смихут / прил.+сущ. / нареч.+глагол).
Для слов, которые кодер «через декодер» (≤3 корня) не ставит первыми: ищем пару (главное h, уточнение m)
из «хороших» слов (свой код раскодируется первым), читатель получает h и m и ищет слово,
близкое к обоим («И»: soft-min z-оценок + CSLS по сумме h + .6·m); h, m и их однокоренные исключены."""
import json, sys, time
import numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(np.float32)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
d = json.load(open(SP + 'r5_8421.json')); idx = d['idx']; res = d['3']
good = np.array([i for i, r in zip(idx, res) if r['mix'] == 1])
bad = [(i, r) for i, r in zip(idx, res) if r['mix'] > 1]
HW = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
K = 60
SG = V @ V[good].T                                  # cos всех слов с хорошими
MU, SD = SG.mean(0), SG.std(0); ZG = (SG - MU) / SD
rng = np.random.default_rng(0)
P = rng.choice(len(good), (3000, 2))
Y = SG[:, P[:, 0]] + HW * SG[:, P[:, 1]]
Y /= np.linalg.norm(V[good[P[:, 0]]] + HW * V[good[P[:, 1]]], axis=1)
HUB = np.sort(Y, 1)[:, -10:].mean(1); del Y
same = lambda a, b: len(a) >= 4 and len(b) >= 4 and a[:4] == b[:4]

def pair(t):
    c = [j for j in np.argsort(-SG[t]) if not same(W[good[j]], W[t]) and good[j] != t][:K]
    c = np.array(c); Sc, Zc = SG[:, c], ZG[:, c]
    H, M = np.meshgrid(np.arange(K), np.arange(K), indexing='ij'); ok = H != M; H, M = H[ok], M[ok]
    nrm = np.sqrt(1 + HW**2 + 2 * HW * (V[good[c]] @ V[good[c]].T)[H, M])
    S = (Sc[:, H] + HW * Sc[:, M]) / nrm
    soft = -np.log(np.exp(-2 * Zc[:, H]) + np.exp(-2 * HW * Zc[:, M])) / 2
    cs = 2 * S - HUB[:, None]
    mix = 0.5 * (cs - cs.mean(0)) / cs.std(0) + 0.5 * (soft - soft.mean(0)) / soft.std(0)
    gc = good[c]
    for k in range(K):                                # части и их однокоренные не считаются
        bl = [gc[k]]
        mix[gc[k], H == k] = -np.inf; mix[gc[k], M == k] = -np.inf
    rk = (mix > mix[t]).sum(0) + 1
    j = int(np.lexsort((-S[t], rk))[0])
    return int(rk[j]), W[gc[H[j]]], W[gc[M[j]]], float(S[t, j])

t0 = time.time(); out = []
for n, (i, r) in enumerate(bad):
    out.append((W[i], r['mix'], r['code'], *pair(i)))
    if n % 200 == 0: print(n, f"{time.time()-t0:.0f} с", flush=True)
json.dump(out, open(SP + f'r9_{HW}.json', 'w'))
pr = np.array([o[3] for o in out]); sr = np.array([o[1] for o in out])
print(f"плохих слов {len(out)} из {len(idx)} | пара: top1 {np.mean(pr==1):.1%} top3 {np.mean(pr<=3):.1%} top10 {np.mean(pr<=10):.1%} медиана {np.median(pr):.0f}"
      f" | один код: top3 {np.mean(sr<=3):.1%} top10 {np.mean(sr<=10):.1%} медиана {np.median(sr):.0f} | пара лучше {np.mean(pr<sr):.1%} хуже {np.mean(pr>sr):.1%}")
tot = (len(idx) - len(out) + (pr == 1).sum()) / len(idx)
print(f"итого «код или пара» top1 {tot:.1%} (было {(len(idx)-len(out))/len(idx):.1%})")
