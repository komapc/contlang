"""r16: один кодировщик — каскад от простого к сложному, берётся первый вариант, который ставит слово первым:
  1. код корнями (кодер через декодер или, с --plain, простой кодер сайта; ≤ 3 корня: из 40 лучших по cos — тот, что смесь ставит выше);
  2. одно слово: главное (гипероним r13; у прилагательных и наречий — похожее, «не + антоним», признак r14);
  3. главное слово + уровень pi(d) (r13);
  4. основа + суффикс (прил. / нареч., r15; читатель знает морфологию — кандидаты начинаются как основа);
  5. главное + уточнение (с уровнем, если он помогает).
Если ни один не ставит первым — берётся вариант с лучшим местом. Запуск: r16.py [текст.txt] (по умолчанию «Уолден»)."""
import sys, re, itertools
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
PLAIN = '--plain' in sys.argv; ARGS = [a for a in sys.argv[1:] if a != '--plain']   # --plain: простой кодер сайта
exec(open(SP + 'r14.py').read().split("\nif __name__ == '__main__':")[0])
_r5 = {'__file__': SP + 'r5.py', '__name__': 'r5'}
exec(open(SP + 'r5.py').read().split('def ranks')[0], _r5)                 # в своём пространстве: у r5 своя HUB
cands, co8 = _r5['cands'], _r5['co8']
FMT = lambda S_, v: " ".join(se.m['names'][r] + (f"(={int(x):+d})" if se.m['has_axis'][r] else "") for r, x in zip(S_, v))

def code1(t):
    if PLAIN:
        S_, v, _ = co(se.V[t], 3); v = [int(x) for x in v]; _, mx = se.scores(se.parts(se.C, se.A, S_, v), se.HUB)
        return int((np.delete(mx, t) > mx[t]).sum()) + 1, FMT(S_, v)
    cs = sorted(cands(co8, se.V[t], 3), key=lambda c: -c[0])[:40]; best = None
    for c, S_, v in cs:
        _, mx = se.scores(se.parts(se.C, se.A, S_, v), se.HUB); r = int((np.delete(mx, t) > mx[t]).sum()) + 1
        if best is None or (r, -c) < (best[0], -best[1]): best = (r, c, S_, v)
    return best[0], FMT(best[2], best[3])

# суффиксы: средний сдвиг по парам WordNet (без самой цели)
SUF = collections.defaultdict(list)
for i, w in enumerate(W):
    for s in wn.synsets(w)[:3]:
        if s.pos() not in 'asr': continue
        for l in s.lemmas():
            if l.name().lower() != w: continue
            for p in l.pertainyms():
                b = wi.get(p.name().lower())
                if b is not None and b != i: SUF['нареч.' if s.pos() == 'r' else 'прил.'].append((i, b))
SUFV = {k: (np.sum([V[i] - V[b] for i, b in v], 0), len(v)) for k, v in SUF.items()}
def suffix(t):
    best = None
    for k, ps in SUF.items():
        for i, b in ps:
            if i != t: continue
            tot, n = SUFV[k]; off = (tot - (V[i] - V[b])) / (n - 1); y = V[b] + off; y /= np.linalg.norm(y)
            sc = zc(2 * (V @ y) - se.HUB); sc[b] = -np.inf
            m_ = np.array([w.startswith(W[b][:4]) for w in W]); sc = np.where(m_, sc, -np.inf)
            r = int((sc > sc[t]).sum()) + 1
            if best is None or r < best[0]: best = (r, f"{W[b]} +{k}")
    return best

def encode(w):
    if w not in wi: return None
    t = wi[w]; steps = []
    r, c = code1(t); steps.append((r, 1, f"`{c}`"))
    if r == 1: return steps[0], steps
    b13 = run(t) or {}; b14 = run14(t) if (wn.synsets(w) and wn.synsets(w)[0].pos() in 'asr') else {}
    for k, v in b13.items():
        if k == 'head': steps.append((v[0], 2, v[1]))
        elif k == 'depth': steps.append((v[0], 3, f"{v[1][0]} pi({v[1][1]})"))
        elif k == 'neigh': steps.append((v[0], 5, f"{v[1][0]} + {v[1][1]}"))
        elif k == 'depth+neigh': steps.append((v[0], 5, f"{v[1][0]} pi({v[1][1]}) + {v[1][2]}"))
    for k, v in b14.items():
        neg = 'не ' if k.startswith('not') else ''
        if '+neigh' in k: steps.append((v[0], 5, f"{neg}{v[1][0]} + {v[1][1]}"))
        else: steps.append((v[0], 2, f"{neg}{v[1]}"))
    s = suffix(t)
    if s: steps.append((s[0], 4, s[1]))
    ok = sorted(x for x in steps if x[0] == 1)
    if ok: return min(ok, key=lambda x: x[1]), steps
    return min(steps), steps

if __name__ == '__main__':
    TEXT = open(ARGS[0]).read() if ARGS else """I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if
I could not learn what it had to teach, and not, when I came to die, discover that I had not lived. I did not wish to live
what was not life, living is so dear; nor did I wish to practise resignation, unless it was quite necessary. I wanted to
live deep and suck out all the marrow of life, to live so sturdily and Spartan-like as to put to rout all that was not
life, to cut a broad swath and shave close, to drive life into a corner, and reduce it to its lowest terms, and, if it
proved to be mean, why then to get the whole and genuine meanness of it, and publish its meanness to the world; or if it
were sublime, to know it by experience, and be able to give a true account of it in my next excursion."""
    STOP = set('i to the because only of and see if could not what it had when that did was is so nor unless quite as put all into a its be why then or were by my in out get next able give'.split())
    ws = []
    for w in re.findall(r"[a-z]+", TEXT.lower()):
        if w not in STOP and w not in ws and wn.synsets(w): ws.append(w)
    NAME = {1: 'код', 2: 'одно слово', 3: 'слово + уровень', 4: 'основа + суффикс', 5: 'два слова'}
    cnt = collections.Counter(); first = 0
    print("| слово | форма | что передаётся | место |\n|---|---|---|--:|")
    for w in ws:
        e = encode(w)
        if e is None: print(f"| {w} | — | нет в словаре | |"); cnt['нет в словаре'] += 1; continue
        (r, k, s), _ = e; cnt[NAME[k]] += 1; first += r == 1
        print(f"| {w} | {NAME[k]} | {s} | {r} |", flush=True)
    n = len(ws) - cnt['нет в словаре']
    print(f"\nслов {len(ws)}, в словаре {n}, первыми {first} ({first/n:.0%}); формы: {dict(cnt)}")
