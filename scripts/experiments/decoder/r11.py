"""r11 = r10 с чисткой: главное — гипероним только первого (главного) значения цели (до 3 уровней вверх), в варианте near ещё и среди 300 ближайших к цели, уточнение — любое хорошее слово
из 300 ближайших, но не синоним, не гипероним и не из ветки главного (не «брат» цели: pepper для garlic запрещён)."""
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
exec(open(SP + 'r9.py').read().split('def pair')[0])
VAR = sys.argv[2] if len(sys.argv) > 2 else 'first'; NEARH = VAR.startswith('near')   # B: главное слово — среди 300 ближайших к цели
from nltk.corpus import wordnet as wn
gset = {int(g): j for j, g in enumerate(good)}; wi = {w: i for i, w in enumerate(W)}
import functools
@functools.lru_cache(None)
def up(s, d): return frozenset(s.closure(lambda x: x.hypernyms() + x.instance_hypernyms(), depth=d))
@functools.lru_cache(None)
def syns(w): return tuple(wn.synsets(w)[:3])

def heads(t):
    ss = wn.synsets(W[t])[:3]; out = {}
    for s in ss[:3 if VAR == 'near3' else 1]:
        for h in up(s, 3):
            for l in h.lemma_names():
                i = wi.get(l.lower())
                if i is not None and i in gset and i != t: out.setdefault(i, h)
    return out, ss

def pos(w):
    s = wn.synsets(w); return s[0].pos().replace('s', 'a') if s else '?'

def pair(t):
    hs, ss = heads(t)
    near300 = set(int(good[j]) for j in np.argsort(-SG[t])[:300])
    if NEARH: hs = {h: v for h, v in hs.items() if h in near300}
    if not hs: return None
    syn = {l.lower() for s in ss for l in s.lemma_names()}
    near = [int(good[j]) for j in np.argsort(-SG[t])[:300]]
    best = None
    for h, hsyn in hs.items():
        ms = []
        for m_ in near:
            w = W[m_]
            if m_ == h or w in syn or same(w, W[t]) or same(w, W[h]): continue
            if any(hsyn in up(s, 8) or s == hsyn for s in syns(w)): continue   # из ветки главного
            ms.append(m_)
        if not ms: continue
        a = ZG[:, gset[h]][:, None]; Zm = ZG[:, [gset[x] for x in ms]]
        S = (SG[:, gset[h]][:, None] + HW * SG[:, [gset[x] for x in ms]]) / np.sqrt(1 + HW**2 + 2 * HW * (V[ms] @ V[h]))
        soft = -np.log(np.exp(-2 * a) + np.exp(-2 * HW * Zm)) / 2; cs = 2 * S - HUB[:, None]
        mix = 0.5 * (cs - cs.mean(0)) / cs.std(0) + 0.5 * (soft - soft.mean(0)) / soft.std(0)
        mix[h] = -np.inf; mix[ms, np.arange(len(ms))] = -np.inf
        rk = (mix > mix[t]).sum(0) + 1; j = int(np.lexsort((-S[t], rk))[0])
        c = (int(rk[j]), W[h], W[ms[j]], pos(W[ms[j]]))
        if best is None or c[0] < best[0]: best = c
    return best

import multiprocessing as mp
t0 = time.time()
ps = []
with mp.Pool(8) as P:
    for n, p in enumerate(P.imap(pair, [i for i, r in bad], chunksize=5)):
        ps.append(p)
        if n % 100 == 0: print(n, f"{time.time()-t0:.0f} с", flush=True)
out = [(W[i], r['mix'], *p) for (i, r), p in zip(bad, ps) if p is not None]; skip = len(bad) - len(out)
print(f"{time.time()-t0:.0f} с", flush=True)
json.dump(out, open(SP + f'r11_{VAR}.json', 'w'))
pr = np.array([o[2] for o in out]); sr = np.array([o[1] for o in out])
print(f"плохих {len(bad)}, без гиперонима в словаре {skip}, проверено {len(out)}")
print(f"пара: top1 {np.mean(pr==1):.1%} top3 {np.mean(pr<=3):.1%} top10 {np.mean(pr<=10):.1%} медиана {np.median(pr):.0f} | "
      f"тот же код: top1 0% top3 {np.mean(sr<=3):.1%} медиана {np.median(sr):.0f} | пара лучше {np.mean(pr<sr):.1%} хуже {np.mean(pr>sr):.1%}")
import collections; print('уточнение:', collections.Counter(o[5] for o in out))
