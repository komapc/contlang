"""r15: словообразование как суффикс — «основа + форма» (presidential = president + прил., increasingly = increasing + нареч.).
Пары (производное, основа) берутся из WordNet: pertainym прилагательного (presidential → president) и наречия
(increasingly → increasing), обе в словаре сайта. Смысл суффикса — средний сдвиг V[производное] − V[основа] по всем
парам этого типа, кроме проверяемой (leave-one-out). Читатель получает основу точно и тип суффикса:
  vec   — ищет слово, ближайшее к V[основа] + сдвиг (CSLS по хабовости сайта), основа исключена;
  stem  — то же, но только среди слов, начинающихся как основа (первые 4 буквы): читатель знает морфологию."""
import sys, json, collections
sys.argv = ['x']; SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
sys.path.insert(0, SP)
import site_eval as se, numpy as np
from nltk.corpus import wordnet as wn
W, V = se.W, se.V; wi = {w: i for i, w in enumerate(W)}
pairs = collections.defaultdict(set)
for i, w in enumerate(W):
    for s in wn.synsets(w)[:3]:
        if s.pos() not in 'asr': continue
        for l in s.lemmas():
            if l.name().lower() != w: continue
            for p in l.pertainyms():
                b = wi.get(p.name().lower())
                if b is not None and b != i: pairs['нареч.' if s.pos() == 'r' else 'прил.'].add((i, b))
def z(a): return (a - a.mean()) / a.std()
out = {}
for typ, ps in pairs.items():
    ps = sorted(ps); D = np.array([V[i] - V[b] for i, b in ps]); tot = D.sum(0)
    res = []
    for k, (i, b) in enumerate(ps):
        off = (tot - D[k]) / (len(ps) - 1); y = V[b] + off; y /= np.linalg.norm(y)
        sc = z(2 * (V @ y) - se.HUB); sc[b] = -np.inf
        r_vec = int((sc > sc[i]).sum()) + 1
        stem = W[b][:4]
        m = np.array([w.startswith(stem) for w in W]); s2 = np.where(m, sc, -np.inf)
        r_stem = int((s2 > s2[i]).sum()) + 1
        sb = z(2 * (V @ V[b]) - se.HUB); sb[b] = -np.inf; r_base = int((sb > sb[i]).sum()) + 1   # без суффикса
        res.append((W[i], W[b], r_base, r_vec, r_stem, W[int(np.argmax(sc))]))
    out[typ] = res
    a = np.array([x[2:5] for x in res])
    print(f"\n{typ}: пар {len(ps)}")
    print(f"  только основа: top1 {np.mean(a[:,0]==1):.1%} | основа + суффикс (вектор): top1 {np.mean(a[:,1]==1):.1%} top3 {np.mean(a[:,1]<=3):.1%}"
          f" | + морфология (та же основа): top1 {np.mean(a[:,2]==1):.1%}")
    for x in res[:: max(1, len(res) // 12)][:12]: print('  ', x)
json.dump(out, open(SP + 'r15.json', 'w'), ensure_ascii=False)
LEFT = ['presidential', 'parliamentary', 'diplomatic', 'jewish', 'increasingly', 'though']
print('\nостались без пары в r14:')
for typ, res in out.items():
    for x in res:
        if x[0] in LEFT: print(' ', typ, x)
