import sys, json, numpy as np
SPD = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
src = open(SPD + 'r5.py').read().split("if __name__")[0]; exec(src)
wi = {w: i for i, w in enumerate(W)}
fmt = lambda R, v: " ".join(names[r] + (f"(={x:+d})" if has[r] else "") for r, x in zip(R, v))
def dec(R, v, k=5):
    y = unit(sum(comp(R, v))); Ss = V @ y; P = unit(np.stack(comp(R, v))); Z = zc(V @ P.T)
    soft = -np.log(np.exp(-2 * Z).sum(1)) / 2; mix = 0.5 * zc(2 * Ss - HUB) + 0.5 * soft
    return [W[t] for t in np.argsort(-Ss)[:k]], [W[t] for t in np.argsort(-mix)[:k]], Ss, mix
rk = lambda a, i: int((a > a[i]).sum()) + 1
for w in sys.argv[1:]:
    if w not in wi: print(w, "— нет в словаре"); continue
    i = wi[w]; x = V[i]
    cs = sorted(cands(co8, x, 3), key=lambda c: -c[0])[:40]
    c0 = cs[0]; s0, m0, S0, M0 = dec(c0[1], c0[2])
    rm, _ = ranks(i, cs); j = min(range(len(cs)), key=lambda j: (rm[j], -cs[j][0])); c1 = cs[j]; _, m1, _, M1 = dec(c1[1], c1[2])
    print(f"\n### {w}\n- код (по сходству, как на сайте): `{fmt(c0[1], c0[2])}`  cos {c0[0]:.2f}")
    print(f"  - сумма: {', '.join(s0)} (#{rk(S0, i)})\n  - смесь: {', '.join(m0)} (#{rk(M0, i)})")
    print(f"- код (через декодер): `{fmt(c1[1], c1[2])}`  cos {c1[0]:.2f}\n  - смесь: {', '.join(m1)} (#{rk(M1, i)})")

import gzip
need = set(w for w in sys.argv[1:] if w not in wi); got = {}
if need:
    with gzip.open('data/raw/numberbatch-en-19.08.txt.gz', 'rt', encoding='utf8') as f:
        next(f)
        for line in f:
            a, rest = line.split(' ', 1)
            if a in need:
                got[a] = np.array(rest.split(), dtype=np.float32); got[a] /= np.linalg.norm(got[a])
                if len(got) == len(need): break
for w, x in got.items():
    cs = sorted(cands(co8, x, 3), key=lambda c: -c[0])[:40]; c0 = cs[0]; s0, m0, _, _ = dec(c0[1], c0[2])
    # через декодер: слова нет в словаре — берём код, у которого смесь ближе всего к самому слову (cos ближайшего слова к x)
    best = None
    for c in cs:
        _, mm, _, _ = dec(c[1], c[2], 1); sc = float(V[wi[mm[0]]] @ x)
        if best is None or sc > best[0]: best = (sc, c)
    c1 = best[1]; _, m1, _, _ = dec(c1[1], c1[2])
    print(f"\n### {w} (нет в словаре сайта)\n- код (по сходству): `{fmt(c0[1], c0[2])}`  cos {c0[0]:.2f}\n  - сумма: {', '.join(s0)}\n  - смесь: {', '.join(m0)}")
    print(f"- код (через декодер: первое прочтение ближе всего к слову): `{fmt(c1[1], c1[2])}`\n  - смесь: {', '.join(m1)}")
