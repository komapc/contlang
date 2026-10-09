"""r14: пары для прилагательных и наречий — у них в WordNet нет гиперонимов. Слова из 1339, где код не первый,
у которых первое значение — прилагательное или наречие. Главное слово (свой код на 1–2 месте, среди 300 ближайших,
не однокоренное цели, без имён) берётся из связей WordNet 3 значений:
  sim  — similar_to / also_see (genuine → real), для наречий — прилагательное-основа (deliberately → deliberate)
         и его similar_to; читатель ранжирует по главному;
  attr — существительное-признак (attribute: heavy → weight);
  not  — «не A», A — антоним (whole → not partial): читатель берёт антонимы A и их similar_to и ранжирует их по A.
К каждому — слово-уточнение из 300 ближайших (как r12), служебные глаголы (be, have, do…) не годятся."""
import sys
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
exec(open(SP + 'r13.py').read().split("if __name__ == '__main__':")[0])
_same = same
def same(a, b): return _same(a, b) or (min(len(a), len(b)) >= 4 and (a in b or b in a))   # necessary ~ unnecessary
AUX = set('be am is are was were been being have has had having do does did done doing get got make made go went'.split())

def lemmas(ss): return {l.name().lower() for s in ss for l in s.lemmas()}
def vix(names): return {wi[n] for n in names if n in wi}
def sim_heads(s):
    out = set(s.similar_tos() + s.also_sees())
    for l in s.lemmas():
        for p in l.pertainyms(): out |= {p.synset()} | set(p.synset().similar_tos())   # наречие → прилагательное
        for d in l.derivationally_related_forms(): out.add(d.synset())
    return out
def antonyms(s):
    out = set()
    for x in [s] + s.similar_tos():                    # у спутника (genuine) антоним — у главного прилагательного (real)
        for l in x.lemmas():
            for a in l.antonyms(): out.add(a.synset())
    return out
def not_set(A):
    """что читатель понимает под «не A»: антонимы A и их similar_to (все значения A)."""
    out = set()
    for s in wn.synsets(W[A]):
        for l in s.lemmas():
            for a in l.antonyms(): out |= {a.synset()} | set(a.synset().similar_tos())
    return vix(lemmas(out))

def run14(t):
    ss = wn.synsets(W[t])[:3]; syn = lemmas(ss)
    near = [int(j) for j in np.argsort(-(V @ V[t]))[:300]]; near300 = set(near)
    def okh2(i): return i != t and i in near300 and not same(W[i], W[t]) and not namey(i) and okh(i)
    H = {'sim': set(), 'attr': set(), 'not': set()}
    for s in ss:
        H['sim'] |= {i for i in vix(lemmas(sim_heads(s))) if okh2(i)}
        H['attr'] |= {i for i in vix(lemmas(s.attributes())) if okh2(i)}
        H['not'] |= {i for i in vix(lemmas(antonyms(s))) if i != t and not same(W[i], W[t]) and not namey(i) and okh(i)}
    best = {}
    def keep(k, r, info):
        if k not in best or r < best[k][0]: best[k] = (r, info)
    for k, hs in H.items():
        for h in hs:
            ex = {h} | {j for j, w in enumerate(W) if same(w, W[h]) and j != t}
            cand = not_set(h) - ex if k == 'not' else None
            if k == 'not' and t not in cand: continue
            sc = head_scores(h)
            keep(k, rank_in(sc, t, cand, ex)[0], W[h])
            ms = [m_ for m_ in near if m_ not in (h, t) and m_ in gset and W[m_] not in AUX and wn.synsets(W[m_]) and not namey(m_)
                  and W[m_] not in syn and not same(W[m_], W[t]) and not same(W[m_], W[h])]
            for m_ in ms:
                pm = pair_mix(h, m_); r = rank_in(pm, t, cand, ex | {m_})[0]
                keep(k + '+neigh', r, (W[h], W[m_]))
    return best

if __name__ == '__main__':
    import multiprocessing as mp
    t0 = time.time()
    targets = [i for i, r in bad if (lambda s: s and s[0].pos() in 'asr')(wn.synsets(W[i]))]
    r13 = json.load(open(SP + 'r13.json'))
    out = {}
    with mp.Pool(8) as P:
        for t, b in zip(targets, P.imap(run14, targets, chunksize=2)): out[W[t]] = b
    json.dump(out, open(SP + 'r14.json', 'w'))
    print(f"прилагательных и наречий среди плохих: {len(targets)}; из них с парой в r13: {sum(W[t] in r13 for t in targets)}")
    print('вариант | есть | top1 | top3 | top10')
    def row(name, rks):
        rks = np.array(rks)
        print(f"{name} | {len(rks)} | {np.mean(rks==1):.1%} | {np.mean(rks<=3):.1%} | {np.mean(rks<=10):.1%}" if len(rks) else f"{name} | 0")
    row('r13 (гипероним, лучшее)', [min(v[0] for k, v in r13[W[t]].items() if k != 'ord') for t in targets if W[t] in r13])
    for k in ['sim', 'sim+neigh', 'attr', 'attr+neigh', 'not', 'not+neigh']:
        row(k, [b[k][0] for b in out.values() if k in b])
    allb = {w: min(v[0] for v in b.values()) for w, b in out.items() if b}
    for t in targets:
        if W[t] in r13: allb[W[t]] = min(allb.get(W[t], 9e9), min(v[0] for k, v in r13[W[t]].items() if k != 'ord'))
    row('лучшее из всего (с r13)', list(allb.values()))
    print(f"без пары вообще: {len(targets) - len(allb)}")
    for w in list(out)[:12]: print(w, out[w])
    print('«Уолден» (код не первый, но не в 1339 — кодер с проверкой декодером их раскодирует):')
    for w in ['whole', 'genuine', 'necessary', 'deliberately']: print(w, run14(wi[w]))
    print(f"{time.time()-t0:.0f} с")
