"""Чистая математика: кодер (≤3 и ≤4 корня) → декодер (сумма и смесь), 10000 слов сайта, худшие слова."""
import json, sys, time, multiprocessing as mp
sys.path.insert(0, 'scripts')
import numpy as np
from lib_code import Coder, root_specs
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json'))
W = m['words']
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(float)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names = m['names']; has = np.array(m['has_axis']); HW, S = m['head_w'], m['s']
C, A = (np.array(m['dicts']['learned'][k]) for k in 'CA')
co = Coder(C, A, head_w=HW)
co6 = Coder(C, A, head_w=HW, topr=6)  # 4 корня: опоры из 6 лучших (8 — ~2 ч на 10000)
u = lambda y: y / np.linalg.norm(y)
def enc(args):
    i, k = args
    R, v, y = co(V[i], 3)
    if k == 4:
        R4, v4, y4 = co6(V[i], 4)
        if u(y4) @ V[i] > u(y) @ V[i]: R, v = R4, v4
    return [int(r) for r in R], [int(x) for x in v]
if __name__ == '__main__':
    poles = set(w for _, p, n, c in root_specs() for w in (p + ' ' + (n or '') + ' ' + (c or '')).split())
    idx = [i for i, w in enumerate(W) if w not in poles]
    rng = np.random.default_rng(0); idx = sorted(rng.choice(idx, min(int(sys.argv[1]), len(idx)), replace=False).tolist())
    out = {'idx': idx}
    for k in (3, 4):
        t0 = time.time()
        with mp.Pool(8) as p: out[k] = p.map(enc, [(i, k) for i in idx], chunksize=20)
        print(k, f"{time.time()-t0:.0f} с", flush=True)
    json.dump(out, open(SP + f'r4_codes_{len(idx)}.json', 'w'))
