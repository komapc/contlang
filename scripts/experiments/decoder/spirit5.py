"""Кандидат SPIRIT на словаре сайта (10721): обученный словарь 45 корней + новый корень из полюсов."""
import sys, json, itertools
sys.path.insert(0, 'scripts')
import numpy as np
from lib_code import Coder
m = json.load(open('site/data/math.json')); W = m['words']; wi = {w: i for i, w in enumerate(W)}
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(float)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
names0 = m['names']; C0, A0 = (np.array(m['dict'][k]) for k in 'CA'); HW, s = m['head_w'], m['s']
unit = lambda x: x / (np.linalg.norm(x, axis=-1, keepdims=True) + 1e-9)
_pz = np.load(__import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/' + 'spirit_poles.npz'); PV = dict(zip(_pz['words'], _pz['X']))
emb = lambda ws: np.stack([PV[w] if w in PV else V[wi[w]] for w in ws.split() if w in PV or w in wi])
def root(p, n):
    P = emb(p); N = emb(n) if n else None
    return (unit(P.mean(0) + N.mean(0)), unit(P.mean(0) - N.mean(0))) if n else (unit(P.mean(0)), np.zeros(V.shape[1]))
rng = np.random.default_rng(5); pool = [w for w in W if w.isalpha()]
VAR = {"SPIRIT ось": ("spiritual religious sacred holy divine", "materialistic worldly mundane earthly material"),
       "SACRED без оси": ("religious sacred divine spiritual holy", None),
       "случайный": (" ".join(rng.choice(pool, 5, replace=False)), " ".join(rng.choice(pool, 5, replace=False)))}
POLES = set(w for p, n in VAR.values() for w in (p + " " + (n or "")).split())
OWN = ("church priest bishop monastery abbey clergy god pray prayer temple faith soul heaven hell angel sin worship rabbi monk saint "
       "archbishop cleric diocese mosque bible christian muslim religion belief bless miracle ritual ghost spirit pope nun prophet "
       "cathedral chapel sermon gospel jesus buddha islam hindu jewish catholic pilgrim").split()
MAT = "money wealth profit luxury greed stuff goods junk plastic possessions property shopping consumer petty trash comfort".split()
OWN = [w for w in OWN if w in wi and w not in POLES]; MAT = [w for w in MAT if w in wi and w not in POLES]
keep = np.array([w not in POLES for w in W])
g = np.random.default_rng(0); gen = [int(i) for i in g.choice(np.where(keep)[0], 800, replace=False)]
targets = [wi[w] for w in OWN + MAT] + gen
zc = lambda x: (x - x.mean(0)) / x.std(0)
def run(C, A):
    has = A.any(1); co = Coder(C, A, head_w=HW)
    comp = lambda R, v: [(1.0 if j == 0 else HW) * (C[r] + s * x * A[r]) for j, (r, x) in enumerate(zip(R, v))]
    g = np.random.default_rng(0); Y = []
    for _ in range(3000):
        k = g.integers(1, 4); R = list(g.choice(len(C), k, replace=False)); Y.append(unit(sum(comp(R, [int(g.integers(-5, 6)) if has[r] else 0 for r in R]))))
    hub = np.sort(V @ np.stack(Y).T, 1)[:, -10:].mean(1); out = []
    for i in targets:
        R, v, y = co(V[i]); S = V @ unit(y); S[~keep] = -9
        Z = zc(V @ unit(np.stack(comp(R, v))).T); soft = -np.log(np.exp(-2 * Z).sum(1)) / 2
        mix = 0.5 * zc(2 * S - hub) + 0.5 * soft; mix[~keep] = -99
        out.append(([int(r) for r in R], [int(x) for x in v], int((mix > mix[i]).sum()) + 1, int((S > S[i]).sum()) + 1, [W[t] for t in np.argsort(-mix)[:3]]))
    return out
nO, nM = len(OWN), len(MAT); res = {}
for lab, spec in [("база", None)] + list(VAR.items()):
    if spec: c, a = root(*spec); C, A, names = np.vstack([C0, c]), np.vstack([A0, a]), names0 + ["NEW"]
    else: C, A, names = C0, A0, names0
    r = run(C, A); res[lab] = (r, names, A)
    rk = np.array([x[2] for x in r]); used = np.mean([len(names) - 1 in x[0] for x in r[nO + nM:]]) if spec else 0
    print(f"{lab:15s} общие 800: смесь top1 {np.mean(rk[nO+nM:]==1):.1%} | кодов с новым {used:.1%} | религия ({nO}): top1 {np.mean(rk[:nO]==1):.0%} top3 {np.mean(rk[:nO]<=3):.0%} медиана {np.median(rk[:nO]):.0f}"
          f" | материальное ({nM}): top1 {np.mean(rk[nO:nO+nM]==1):.0%} медиана {np.median(rk[nO:nO+nM]):.0f}", flush=True)
fmt = lambda names, A, R, v: " ".join(names[r].replace("NEW", "SPIRIT") + (f"(={x:+d})" if A[r].any() else "") for r, x in zip(R, v))
print("\n| слово | база | место | с SPIRIT | место | читает |\n|---|---|--:|---|--:|---|")
b, sp = res["база"], res["SPIRIT ось"]
for j, w in enumerate(OWN + MAT):
    print(f"| {w} | `{fmt(b[1], b[2], *b[0][j][:2])}` | {b[0][j][2]} | `{fmt(sp[1], sp[2], *sp[0][j][:2])}` | {sp[0][j][2]} | {', '.join(sp[0][j][4])} |")
c, a = root(*VAR["SPIRIT ось"])
print("\nближайшие оси:", sorted(((round(float(a @ unit(A0[j])), 2), names0[j]) for j in range(len(names0)) if A0[j].any()), key=lambda x: -abs(x[0]))[:4])
print("крайние слова оси +:", [W[t] for t in np.argsort(-(V @ a))[:12]], "\n−:", [W[t] for t in np.argsort(V @ a)[:12]])
