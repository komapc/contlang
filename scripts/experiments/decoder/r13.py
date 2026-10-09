"""r13: что добавить к главному слову (гиперониму, как в r12), кроме слова-уточнения. Те же 1339 слов, где код не первый.
  head      — только главное слово (для сравнения);
  depth     — главное + уровень d (на сколько ступеней WordNet вниз лежит цель): читатель берёт только слова,
              у которых главное — гипероним ровно на глубине d, и ранжирует их по главному;
  ord       — главное + номер k: место цели среди всех видов главного (глубина ≤ 3), ранжированных по главному
              («k-й самый типичный вид»); раскодируется всегда, мерило — величина k;
  ord_d     — главное + уровень + номер;
  not       — главное + «но не n»: n — хорошее слово из тех, что читатель ставит выше цели; оценка − λ·z(cos(w, n));
  neigh     — главное + слово-уточнение из 300 ближайших (r12), и комбинации depth+neigh, neigh+not;
  domain    — главное + область WordNet (topic domain значения цели, music, medicine…): фильтр кандидатов по области.
Читатель знает WordNet (это общий словарь), но не знает цель."""
import sys
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
src = open(SP + 'r12.py').read().split("import re, time, collections")[0]
exec(src)
import re, time, collections, json

# ступени вниз: для каждого слова словаря — его гиперонимы (3 значения, до 3 уровней) с глубиной
def ancestors(w):
    out = {}
    for s in wn.synsets(w)[:3]:
        if s.instance_hypernyms(): continue
        fr, d = [s], 0
        while fr and d < 3:
            d += 1; nx = []
            for x in fr:
                for hs in x.hypernyms():
                    if hs not in out or out[hs] > d: out[hs] = d
                    nx.append(hs)
            fr = nx
    return out
KIND = collections.defaultdict(set); KIND_D = collections.defaultdict(set)   # (главное) → виды, (главное, d) → виды
DOM = collections.defaultdict(set)                                             # область → слова
for i, w in enumerate(W):
    for hs, d in ancestors(w).items():
        for l in hs.lemma_names():
            j = wi.get(l.lower())
            if j is not None and j != i: KIND[j].add(i); KIND_D[j, d].add(i)
    for s in wn.synsets(w)[:3]:
        for ds in s.topic_domains(): DOM[ds].add(i)
LAMS = (0.5, 1.0)

def zc(a): return (a - a.mean()) / a.std()
def head_scores(h):
    _, mx = se.scores(V[h][None].astype(float), se.HUB); return mx
def pair_mix(h, m_):
    sh = V @ V[h]; sm = V @ V[m_]
    S = (sh + HW * sm) / np.sqrt(1 + HW**2 + 2 * HW * (V[m_] @ V[h]))
    soft = -np.log(np.exp(-2 * zc(sh)) + np.exp(-2 * HW * zc(sm))) / 2
    return 0.5 * zc(2 * S - HUB) + 0.5 * zc(soft)
def rank_in(sc, t, cand=None, excl=()):
    sc = sc.copy()
    for j in excl: sc[j] = -np.inf
    if cand is not None:
        c = np.fromiter(cand, int); return int((sc[c] > sc[t]).sum()) + 1, len(c)
    return int((sc > sc[t]).sum()) + 1, len(sc)
def best_not(sc, t, excl):
    """лучшее «но не n»: n — хорошее слово выше цели (до 20), не однокоренное цели."""
    s0 = sc.copy(); s0[list(excl)] = -np.inf
    above = [int(j) for j in np.argsort(-s0)[:30] if s0[j] > s0[t] and int(j) in gset and not same(W[j], W[t])][:20]
    best = (rank_in(sc, t, excl=excl)[0], None)
    for n in above:
        zn = zc(V @ V[n])
        for lam in LAMS:
            ex = set(excl) | {n}
            r = rank_in(sc - lam * zn, t, excl=ex)[0]
            if r < best[0]: best = (r, f"{W[n]} λ{lam}")
    return best

def run(t):
    hs = heads2(t)
    if not hs: return None
    ss = wn.synsets(W[t])[:3]; syn = {l.lower() for s in ss for l in s.lemma_names()}
    near = [int(j) for j in np.argsort(-(V @ V[t]))[:300]]
    best = {}
    def keep(k, r, info):
        if k not in best or r < best[k][0]: best[k] = (r, info)
    for h, (hsyn, sense) in hs.items():
        ex = {h} | {j for j, w in enumerate(W) if same(w, W[h]) and j != t}   # однокоренные главного не считаются
        sc = head_scores(h)
        keep('head', rank_in(sc, t, excl=ex)[0], W[h])
        d = ancestors(W[t]).get(hsyn)
        if d is not None:
            r, n = rank_in(sc, t, KIND_D[h, d] - ex); keep('depth', r, (W[h], d, n))
        r, n = rank_in(sc, t, KIND[h] - ex); keep('ord', r, (W[h], n))
        r, n = best_not(sc, t, ex); keep('not', r, (W[h], n))
        for s in ss:
            for ds in s.topic_domains():
                r, n = rank_in(sc, t, DOM[ds] - ex); keep('domain', r, (W[h], ds.name(), n))
        # слово-уточнение (r12 neigh) и комбинации
        def ok(m_):
            w = W[m_]
            if m_ == h or m_ == t or m_ not in gset or not wn.synsets(w) or namey(m_) or w in syn or same(w, W[t]) or same(w, W[h]): return False
            return not any(hsyn in up(s, 8) or s == hsyn for s in syns(w))
        ms = [m_ for m_ in near if ok(m_)]
        if ms:
            rr = read_words(t, h, ms); j = int(np.argmin(rr)); m_ = ms[j]; keep('neigh', int(rr[j]), (W[h], W[m_]))
            pm = pair_mix(h, m_); exm = ex | {m_}
            if d is not None:
                r, n = rank_in(pm, t, KIND_D[h, d] - exm); keep('depth+neigh', r, (W[h], d, W[m_]))
            r, n = best_not(pm, t, exm); keep('neigh+not', r, (W[h], W[m_], n))
    return best

if __name__ == '__main__':
    import multiprocessing as mp
    t0 = time.time(); targets = [i for i, r in bad]; out = {}
    with mp.Pool(8) as P:
        for n, (t, b) in enumerate(zip(targets, P.imap(run, targets, chunksize=4))):
            if b: out[W[t]] = b
            if n % 100 == 0: print(n, f"{time.time()-t0:.0f} с", flush=True)
    json.dump(out, open(SP + 'r13.json', 'w'))
    N = len(idx); G = len(good)
    print(f"\nплохих {len(targets)}; с главным словом {len(out)}")
    print('вариант | есть | top1 | top3 | top10 | медиана | всего первыми из 8421')
    def row(name, rks):
        rks = np.array(rks); print(f"{name} | {len(rks)} | {np.mean(rks==1):.1%} | {np.mean(rks<=3):.1%} | {np.mean(rks<=10):.1%} | {np.median(rks):.0f} | {(G + (rks==1).sum())/N:.1%}")
    for k in ['head', 'depth', 'not', 'domain', 'neigh', 'depth+neigh', 'neigh+not', 'ord']:
        row(k, [b[k][0] for b in out.values() if k in b])
    sz = [b['depth'][1][2] for b in out.values() if 'depth' in b]; print('кандидатов при depth: медиана', np.median(sz))
    sz = [b['ord'][1][1] for b in out.values() if 'ord' in b]; print('видов главного (ord): медиана', np.median(sz))
    for w in ['west', 'mainland', 'angels', 'terrorism', 'cancer', 'railroad', 'fourteen']:
        if w in out: print(w, out[w])
    print(f"{time.time()-t0:.0f} с")
