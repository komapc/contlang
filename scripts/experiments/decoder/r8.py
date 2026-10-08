"""Порядок корней: «главный — область, модификаторы — оттенок» (M), с исключением для ролевых корней (R),
словарь переобучается под каждую схему (как scripts/18_sparse_learn.py). Проверка — собственные коды математики
на словах сайта, не входивших в обучение; декодер-смесь с позиционным «И»."""
import itertools, json, sys, time, multiprocessing as mp
sys.path.insert(0, 'scripts')
import numpy as np
from lib_code import Data, root_specs, unit
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
LAM, TAU, ITERS, s = 30.0, 0.85, 3, 0.4
ROLE = {"SOMEONE", "THING", "PLACE", "DO"}
VARS = {"A сейчас": ([1, .6, .6], [1, .6, .6], False),
        "M ×.25": ([1, .15, .15], [1, .6, .6], False),
        "M ×.25 + роли": ([1, .15, .15], [1, .6, .6], True)}
LV = list(range(-5, 6)); grids = {}
def grid(flags):
    if flags not in grids: grids[flags] = np.array(list(itertools.product(*[LV if f else [0] for f in flags])), dtype=np.float32)
    return grids[flags]
class Enc:
    def __init__(self, C, A, names, var):
        self.C, self.A = C.astype(np.float32), A.astype(np.float32); self.has = A.any(1); self.R = len(C)
        Mx = np.concatenate([self.C, self.A]); self.G = Mx @ Mx.T
        self.wc, self.wa, self.role = var; self.isrole = np.array([n in ROLE for n in names])
    def weights(self, S2):
        k = len(S2); head = 0
        if self.role:  # главный — первый содержательный корень; ролевые — как модификаторы
            nr = [j for j, r in enumerate(S2) if not self.isrole[r]]; head = nr[0] if nr else 0
        c = np.full(k, self.wc[1], np.float32); a = np.full(k, self.wa[1], np.float32); c[head], a[head] = self.wc[0], self.wa[0]
        c = np.where(self.has[S2], c, np.maximum(c, a)); return c, a
    def __call__(self, x):
        cx, ax = self.C @ x, self.A @ x; cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:8]); best = (-2,)
        for k in (1, 2, 3):
            for Sx in itertools.combinations(cand, k):
                for h in range(k):
                    S2 = [Sx[h]] + [r for i, r in enumerate(Sx) if i != h]
                    if self.role and self.isrole[S2[0]] and not all(self.isrole[S2]): continue  # тот же вектор, что и при содержательном главном
                    c, a = self.weights(S2); Gr = grid(tuple(self.has[S2])); idx = S2 + [self.R + r for r in S2]
                    U = np.concatenate([np.broadcast_to(c, Gr.shape), a * s * Gr], 1)
                    cos = (U @ np.concatenate([cx[S2], ax[S2]])) / np.sqrt(np.maximum(((U @ self.G[np.ix_(idx, idx)]) * U).sum(1), 1e-9))
                    i = int(np.argmax(cos))
                    if cos[i] > best[0]: best = (float(cos[i]), [int(r) for r in S2], [int(t) for t in Gr[i]])
        return best
    def parts(self, R, v):
        c, a = self.weights(list(R)); return [cj * self.C[r] + aj * s * x * self.A[r] for r, x, cj, aj in zip(R, v, c, a)]
def clamp(new, old, tau):
    c = new @ old
    return new if c >= tau else tau * old + np.sqrt(1 - tau ** 2) * unit(new - c * old)
E = None
def _enc(x): return E(x)
def learn(d, C0, A0, names, var):
    global E
    R, has = len(C0), A0.any(1); Th0 = np.concatenate([C0, A0]); C, A = C0.copy(), A0.copy(); Xtr = d.V[d.train]
    for it in range(ITERS):
        E = Enc(C, A, names, var)
        with mp.Pool(8) as p: codes = p.map(_enc, list(Xtr), chunksize=20)
        M = np.zeros((len(codes), 2 * R))
        for i, (_, S2, v) in enumerate(codes):
            c, a = E.weights(S2); M[i, S2] += c; M[i, [R + r for r in S2]] += a * s * np.array(v)
        Y = M @ np.concatenate([C, A]); T = np.linalg.norm(Y, axis=1)[:, None] * Xtr
        Th = unit(np.linalg.solve(M.T @ M + LAM * np.eye(2 * R), M.T @ T + LAM * Th0))
        for i in range(2 * R): Th[i] = 0 if (i >= R and not has[i - R]) else clamp(Th[i], Th0[i], TAU)
        C, A = Th[:R], Th[R:]
        print(f"   итерация {it+1}: cos на обучении {np.mean([c[0] for c in codes]):.3f}", flush=True)
    return C, A
# проверка на словах сайта
m = json.load(open('site/data/math.json')); W = m['words']
VS = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(np.float32)
VS /= np.linalg.norm(VS, axis=1, keepdims=True) + 1e-9
zc = lambda q: (q - q.mean(0)) / q.std(0)
def evalw(i):
    c, R, v = E(VS[i]); P = E.parts(R, v); Sv = VS @ unit(sum(P)); Z = zc(VS @ unit(np.stack(P)).T)
    cw, aw = E.weights(R); pw = cw + aw; soft = -np.log((np.exp(-2 * Z) * pw / pw.max()).sum(1)) / 2
    mix = 0.5 * zc(2 * Sv - HUB) + 0.5 * soft; rk = lambda q: int((q > q[i]).sum()) + 1
    sw = None
    if len(R) > 1:
        R2, v2 = [R[1], R[0]] + R[2:], [v[1], v[0]] + v[2:]; P2 = E.parts(R2, v2); S2 = VS @ unit(sum(P2)); Z2 = zc(VS @ unit(np.stack(P2)).T)
        c2, a2 = E.weights(R2); p2 = c2 + a2; soft2 = -np.log((np.exp(-2 * Z2) * p2 / p2.max()).sum(1)) / 2
        sw = rk(0.5 * zc(2 * S2 - HUB) + 0.5 * soft2)
    return dict(cos=c, R=R, v=v, mix=rk(mix), sum=rk(Sv), swap=sw)
if __name__ == '__main__':
    specs = root_specs(); d = Data([specs]); names, C0, A0 = d.dictionary(specs)
    train = {d.vocab[i] for i in d.train}
    r5 = json.load(open(SP + 'r5_8421.json')); ev = [i for i in r5['idx'] if W[i] not in train][:int(sys.argv[1])]
    print("проверочных слов:", len(ev), " из них частых (список 2700, не в обучении):", sum(W[i] in set(d.vocab) for i in ev), flush=True)
    out = {'idx': ev}; st = lambda r: f"top1 {np.mean(r==1):5.1%} top3 {np.mean(r<=3):5.1%} top10 {np.mean(r<=10):5.1%} медиана {np.median(r):.0f}"
    for key, var in VARS.items():
        t0 = time.time(); print(key, flush=True)
        for lab, (C, A) in (("из полюсов", (C0, A0)), ("обученный", learn(d, C0, A0, names, var))):
            E = Enc(C, A, names, var); g = np.random.default_rng(0); Y = []
            for _ in range(3000):
                k = g.integers(1, 4); R = list(g.choice(len(C), k, replace=False)); Y.append(unit(sum(E.parts(R, [int(g.integers(-5, 6)) if E.has[r] else 0 for r in R]))))
            HUB = np.sort(VS @ np.stack(Y).T, 1)[:, -10:].mean(1)
            with mp.Pool(8) as p: res = p.map(evalw, ev, chunksize=10)
            out[f"{key}|{lab}"] = res; r = np.array([e['mix'] for e in res]); sw = np.array([e['swap'] for e in res if e['swap']]); r1 = np.array([e['mix'] for e in res if e['swap']])
            print(f"   {lab:10s} cos {np.mean([e['cos'] for e in res]):.3f} | смесь {st(r)} | сумма top1 {np.mean(np.array([e['sum'] for e in res])==1):5.1%}"
                  f" | перестановка 1↔2 теряет 1-е место {np.sum((sw>1)&(r1==1))/max(np.sum(r1==1),1):.0%} ({time.time()-t0:.0f} с)", flush=True)
            if lab == "обученный": np.savez(SP + f"r8_dict_{key.replace(' ', '_')}.npz", C=C, A=A, names=np.array(names))
    json.dump(out, open(SP + 'r8.json', 'w'))
