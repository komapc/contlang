"""r12: варианты «главное слово + уточнение» для слов, которые код (≤3 корня, кодер через декодер) не ставит первыми.
Главное — гипероним по WordNet (3 значения, до 3 уровней, среди 300 ближайших, без имён), как в r11 near3, но
главное не однокоренное цели (delegates ≠ delegate) и допускается главное, чей собственный код раскодируется не ниже 2-го места (instrument для guitar). Уточнение:
  neigh — хорошее слово из 300 ближайших (как r11, но с ослабленным главным);
  gloss — хорошее слово из толкований WordNet (служебные слова отпадают: у них нет значений в WordNet);
  mero  — хорошее слово из частей (part/substance meronyms): bicycle → pedal, chain;
  lemma — слово из составного имени гиперонима: stringed_instrument → string;
  resid — не слово, а код корнями: остаток x ⊥ h (часть вектора слова, перпендикулярная главному), вес β.
Читатель получает главное слово точно (и уточнение точно, если оно слово) и ищет слово смесью (как r11 / сайт)."""
import sys
sys.argv = ['r11.py', '0.6', 'near3']
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
__file__ = SP + 'r11.py'
exec(open(SP + 'r11.py').read().split('def heads')[0])
sys.path.insert(0, SP); sys.argv = ['x']
import site_eval as se
from lib_code import Coder
co = Coder(se.C, se.A, head_w=0.6)
rk5 = {i: r['mix'] for i, r in zip(idx, res)}
_okh = {}
def okh(i):                                                         # главное: свой код на 1-2 месте
    if i in rk5: return rk5[i] <= 2
    if i not in _okh:                                               # нет в 8421 (instrument): простой кодер сайта
        S_, v, _ = co(V[i], 3); _, mx = se.scores(se.parts(se.C, se.A, S_, [int(a) for a in v]), se.HUB)
        _okh[i] = int((np.delete(mx, i) > mx[i]).sum()) + 1 <= 2
    return _okh[i]
_nm = {}
def namey(i):
    if i not in _nm: _nm[i] = PROPER[np.argsort(-(V @ V[i]))[1:21]].mean() >= 0.3
    return _nm[i]
BETAS = (0.5, 1.0, 1.5)

def vocab_forms(tok):
    out = set()
    for f in {tok, wn.morphy(tok) or tok, wn.morphy(tok, wn.NOUN) or tok, wn.morphy(tok, wn.VERB) or tok}:
        for g in (f, f + 's'):
            if g in wi: out.add(wi[g])
    return out

def read_words(t, h, ms):
    """места цели при паре (h, m) для каждого m из ms — формула r11 по векторам слов."""
    sh = V @ V[h]; Sm = V @ V[ms].T
    zh = (sh - sh.mean()) / sh.std(); Zm = (Sm - Sm.mean(0)) / Sm.std(0)
    S = (sh[:, None] + HW * Sm) / np.sqrt(1 + HW**2 + 2 * HW * (V[ms] @ V[h]))
    soft = -np.log(np.exp(-2 * zh[:, None]) + np.exp(-2 * HW * Zm)) / 2; cs = 2 * S - HUB[:, None]
    mix = 0.5 * (cs - cs.mean(0)) / cs.std(0) + 0.5 * (soft - soft.mean(0)) / soft.std(0)
    mix[h] = -np.inf; mix[ms, np.arange(len(ms))] = -np.inf
    return (mix > mix[t]).sum(0) + 1

def read_resid(t, h):
    x, vh = V[t], V[h]; r = x - (x @ vh) * vh
    S_, v, _ = co(r / np.linalg.norm(r), 3); v = [int(a) for a in v]
    P = se.parts(se.C, se.A, S_, v); n = np.linalg.norm(P.sum(0)); out = []
    ex = [j for j, w in enumerate(W) if (j == h or same(w, W[h])) and j != t]
    for b in BETAS:
        _, mx = se.scores(np.concatenate([vh[None] * n / b, P]), se.HUB); mx[ex] = -np.inf
        out.append(int((mx > mx[t]).sum()) + 1)
    return out, (list(map(int, S_)), v)

def heads2(t):
    out = {}
    for s in wn.synsets(W[t])[:3]:
        if s.instance_hypernyms(): continue
        for hs in up(s, 3):
            for l in hs.lemma_names():
                i = wi.get(l.lower())
                if i is not None and i != t and not same(W[i], W[t]) and not namey(i) and okh(i): out.setdefault(i, (hs, s))
    near300 = set(int(j) for j in np.argsort(-(V @ V[t]))[:300])
    return {h: v for h, v in out.items() if h in near300}

def run(t):
    hs = heads2(t)
    if not hs: return None
    ss = wn.synsets(W[t])[:3]; syn = {l.lower() for s in ss for l in s.lemma_names()}
    near = [int(j) for j in np.argsort(-(V @ V[t]))[:300]]
    best = {}
    def keep(k, rk, h, m_):
        if k not in best or rk < best[k][0]: best[k] = (rk, W[h], m_)
    for h, (hsyn, sense) in hs.items():
        def ok(m_):
            w = W[m_]
            if m_ == h or m_ == t or m_ not in gset or not wn.synsets(W[m_]) or namey(m_) or w in syn or same(w, W[t]) or same(w, W[h]): return False
            return not any(hsyn in up(s, 8) or s == hsyn for s in syns(w))
        cand = {
            'neigh': [m_ for m_ in near if ok(m_)],
            'gloss': sorted({m_ for s in ss for tok in re.findall(r"[a-z]+", s.definition().lower()) for m_ in vocab_forms(tok) if ok(m_)}),
            'mero': sorted({m_ for s in ss for mm in s.part_meronyms() + s.substance_meronyms() for l in mm.lemma_names()
                            for tok in l.lower().split('_') for m_ in vocab_forms(tok) if ok(m_)}),
            'lemma': sorted({m_ for l in hsyn.lemma_names() for tok in l.lower().split('_') for m_ in vocab_forms(tok) if ok(m_)}),
        }
        for k, ms in cand.items():
            if not ms: continue
            rr = read_words(t, h, ms); j = int(np.argmin(rr)); keep(k, int(rr[j]), h, W[ms[j]])
        rs, code = read_resid(t, h)
        for b, r in zip(BETAS, rs): keep(f'resid{b}', r, h, code)
    return best

import re, time, collections
import multiprocessing as mp
if __name__ == '__main__':
    t0 = time.time(); targets = [i for i, r in bad]; out = {}
    with mp.Pool(8) as P:
        for n, (t, b) in enumerate(zip(targets, P.imap(run, targets, chunksize=4))):
            if b: out[W[t]] = b
            if n % 100 == 0: print(n, f"{time.time()-t0:.0f} с", flush=True)
    json.dump(out, open(SP + 'r12.json', 'w'))
    base = {o[0]: o[2] for o in json.load(open(SP + 'r11_near3.json'))}
    N = len(idx); G = len(good)
    print(f"\nплохих {len(targets)}; с главным словом (ослабленным) {len(out)}; в r11 near3 {len(base)}")
    print('вариант | есть уточнение | top1 | top3 | top10 | всего первыми из 8421')
    def row(name, rks):
        rks = np.array(rks); print(f"{name} | {len(rks)} | {np.mean(rks==1):.1%} | {np.mean(rks<=3):.1%} | {np.mean(rks<=10):.1%} | {(G + (rks==1).sum())/N:.1%}")
    row('r11 near3 (как было)', list(base.values()))
    for k in ['neigh', 'gloss', 'mero', 'lemma'] + [f'resid{b}' for b in BETAS]:
        row(k, [b[k][0] for b in out.values() if k in b])
    row('лучшее из слов (neigh/gloss/mero/lemma)', [min(b[k][0] for k in b if not k.startswith('resid')) for b in out.values() if any(not k.startswith('resid') for k in b)])
    row('лучшее из всего', [min(v[0] for v in b.values()) for b in out.values()])
    for w in ['guitar', 'bicycle', 'garlic', 'angels', 'west', 'mainland']:
        if w in out: print(w, {k: v for k, v in out[w].items()})
    print(f"{time.time()-t0:.0f} с")
