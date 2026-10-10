"""r17: грамматика — метками формы, а не словами: слово → основная форма | часть речи и метки (docs/syntax.md).
went = go | i T-2, facts = fact | o N+3, lowest = low | a C+5, deliberately = deliberate | e, presidential = president | a.
Основная форма кодируется каскадом r16 (код → одно слово → слово + уровень → два слова; суффикса r15 больше нет:
словообразование — это часть речи). Служебные глаголы (be, have, do) не бывают главным словом.
Читатель восстанавливает основную форму и ставит её в форму по меткам (английская морфология считается известной);
мерило — место основной формы. Запуск: r17.py [текст.txt] [--plain]."""
import sys, re
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
exec(open(SP + 'r16.py').read().split("\nif __name__ == '__main__':")[0])
AUXH = set('be am is are was were been being have has had having do does did done doing'.split())
_heads2 = heads2
def heads2(t): return {h: v for h, v in _heads2(t).items() if W[h] not in AUXH}
def suffix(t): return None                                   # словообразование — часть речи, а не суффикс-сдвиг
POS = {'n': 'o', 'v': 'i', 'a': 'a', 's': 'a', 'r': 'e'}
_WL = {r.split('\t')[0]: r.split('\t')[1] for r in list(open('data/wordlist_en_x5.tsv'))[1:]}
_WLP = {'noun': 'n', 'verb': 'v', 'adj': 'a', 'adv': 'r'}

def pos_of(w):
    """основная часть речи слова-леммы: список частых слов, иначе частоты значений WordNet; None — не лемма."""
    if w in _WL: return _WLP[_WL[w]]
    c = collections.Counter()
    for s in wn.synsets(w):
        for l in s.lemmas():
            if l.name().lower() == w: c[s.pos().replace('s', 'a')] += l.count() + 0.01
    return c.most_common(1)[0][0] if c else None

_EXC_V = None
def vform(w, b):
    """метки глагольной формы: -ing → A0; 3-е лицо (base+s) — без меток; неправильное причастие (known, gone) → A+5; иначе T-2."""
    global _EXC_V
    if _EXC_V is None: wn.synsets('dog'); _EXC_V = wn._exception_map['v']
    if w.endswith('ing'): return 'i A0'
    BE = {'was': 'i T-2 N+1', 'were': 'i T-2 N+3', 'is': 'i N+1', 'are': 'i N+3', 'am': 'i N+1'}   # число подлежащего (лицо не отмечается)
    if w in BE: return BE[w]
    if w in ('has', 'does') or w in (b + 's', b + 'es', b[:-1] + 'ies'): return 'i N+1'
    if w in _EXC_V and w.endswith(('en', 'ne', 'wn', 'un', 'rn')) and w not in ('was', 'were'): return 'i A+5'
    return 'i T-2'

def grammar(w):
    """основная форма и метки (без контекста предложения): словоизменение — метки, производное — часть речи."""
    nv = any(l.name().lower() == w for s in wn.synsets(w) if s.pos() in 'nv' for l in s.lemmas())
    if not nv and w not in _WL:                              # степени: lowest → low | a C+5, broader → broad | a C+3
        for suf, mk in (('est', 'C+5'), ('er', 'C+3')):
            if w.endswith(suf):
                st = w[:-len(suf)]
                for b in (st, st + 'e', st[:-1] if len(st) > 2 and st[-1] == st[-2] else None, st[:-1] + 'y' if st.endswith('i') else None):
                    if b and len(b) >= 3 and b in wi and any(x.pos() in 'as' for x in wn.synsets(b)): return b, 'a ' + mk
    if w not in _WL:                                         # форма частого глагола или существительного (proved, terms) — словоизменение
        for q, wl, mk in ((wn.VERB, 'verb', None), (wn.NOUN, 'noun', 'o N+3')):
            b = wn.morphy(w, q)
            if b and b != w and (_WL.get(b) == wl or b not in _WL and pos_of(b) == wl[0]):   # make нет в списке — части речи по WordNet
                return b, mk or vform(w, b)
    p = pos_of(w)
    if p is None:                                            # не лемма: словоизменение (went, facts, wished)
        for q, mk in ((wn.VERB, None), (wn.NOUN, 'o N+3')):
            b = wn.morphy(w, q)
            if b and b != w:
                if mk: return b, mk
                return b, vform(w, b)
        return w, 'o'
    if p in 'ar':                                            # производное: deliberately → deliberate | e, presidential → president | a
        for s in wn.synsets(w)[:3]:
            if s.pos().replace('s', 'a') != p: continue
            for l in s.lemmas():
                if l.name().lower() != w: continue
                for pp in l.pertainyms():
                    b = pp.name().lower()
                    if b in wi and len(b) >= 4 and b[:4] == w[:4]: return b, POS[p]   # однокоренное (domestic ≠ home)
    return w, POS[p]

# числа — цифрами в кавычках (docs/encoding.md): six = "6", twenty-five = "25"; порядковые — признак: first = "1" | a
_U = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
_T = 'twenty thirty forty fifty sixty seventy eighty ninety'.split()
CARD = {w: i for i, w in enumerate(_U)} | {w: 20 + 10 * i for i, w in enumerate(_T)}
_ORD = {'first': 'one', 'second': 'two', 'third': 'three', 'fifth': 'five', 'eighth': 'eight', 'ninth': 'nine', 'twelfth': 'twelve'}
def _ord_base(w):
    if w in _ORD: return _ORD[w]
    if w.endswith('ieth') and w[:-4] + 'y' in CARD: return w[:-4] + 'y'
    if w.endswith('th') and w[:-2] in CARD: return w[:-2]
def number(w):
    """слово-число → (n, порядковое?) или None; части через дефис складываются (twenty-five)."""
    ps = w.split('-'); n = 0; o = False
    for k, x in enumerate(ps):
        if x in CARD: n += CARD[x]
        elif k == len(ps) - 1 and _ord_base(x): n += CARD[_ord_base(x)]; o = True
        elif x.isdigit() and len(ps) == 1: n = int(x)
        else: return None
    return n, o
def number_word(n, o):
    """обратно: "6" → six, "25" | a → twenty-fifth (до 99)."""
    w = _U[n] if n < 20 else _T[n // 10 - 2] + ('-' + _U[n % 10] if n % 10 else '')
    if not o: return w
    last = w.split('-')[-1]; inv = {v: k for k, v in _ORD.items()}
    last = inv.get(last) or (last[:-1] + 'ieth' if last.endswith('y') else last + 'th')
    return '-'.join(w.split('-')[:-1] + [last])


if __name__ == '__main__':
    TEXT = open(ARGS[0]).read() if ARGS else re.search(r'TEXT = open\(ARGS\[0\]\)\.read\(\) if ARGS else """(.*?)"""', open(SP + 'r16.py').read(), re.S).group(1)
    # служебные слова — в min-co частицы и метки, не коды; имена собственные не кодируются
    STOP = set('''a an the and or but nor if so as than then that this these those it its i me my we our you your he him his she her
    they them their who whom whose which what when where why how to of in on at by for from with without into onto about across
    over under between among through during before after since until up down out off not no only also very quite all any each
    every some such both either neither one there here can could will would shall should may might must be am is are was were
    been being have has had do does did because unless while although though whether able next get put give see'''.split())
    ws = []
    def known(w): return w not in STOP and wn.synsets(w) and (w in _low or w in _freq or wn.morphy(w) in _low)
    for w in re.findall(r"[a-z]+(?:-[a-z]+)*|\d+", TEXT.lower()):             # grown-ups — одно слово из частей
        if w not in ws and (number(w) or (known(w) if '-' not in w else any(known(x) for x in w.split('-')))): ws.append(w)
    NAME = {1: 'код', 2: 'одно слово', 3: 'слово + уровень', 4: 'основа + суффикс', 5: 'два слова'}
    cnt = collections.Counter(); first = 0; n = 0; cache = {}
    import forms
    full = 0
    print("| слово | основная форма | формой основы | что передаётся | место основы | восстановлено |\n|---|---|---|---|--:|---|")
    def compound(w):
        """слово через дефис: части — основные формы, метки целого — на последней части (grown-ups = grow | i A+5 - up | o N+3).
        Целое по WordNet (grownups → grownup): метки числа; иначе каждая часть сама по себе."""
        ps = w.split('-'); j = ''.join(ps); m = wn.morphy(j, wn.NOUN)
        out = [grammar(x) for x in ps]
        if m and m != j and j.startswith(m):                   # множественное целого: снять окончание с последней части
            last = ps[-1][:len(ps[-1]) - (len(j) - len(m))]
            out[-1] = (last, 'o N+3')
        return out
    for w in ws:
        if number(w):                                           # число: цифрами, не кодом
            v, o = number(w); c = f'"{v}"' + (' | a' if o else ''); back = w if w.isdigit() else number_word(v, o)
            n += 1; first += 1; full += back == w; cnt['число'] += 1
            print(f"| {w} | {c} | число | {c.replace('|', '\\|')} | 1 | {back}{'' if back == w else ' ✗'} |", flush=True); continue
        if '-' in w:
            parts = compound(w); res = []
            for b, mk in parts:
                if b not in cache: cache[b] = encode(b)
                res.append((b, mk, cache[b]))
            if any(e is None for _, _, e in res):
                print(f"| {w} | {' - '.join(b for b, _, _ in res)} | — | часть нет в словаре | |"); cnt['нет в словаре'] += 1; continue
            r = max(e[0][0] for _, _, e in res); n += 1; first += r == 1; cnt['составное'] += 1
            back = '-'.join(forms.realize(b, mk) for b, mk, _ in res) if r == 1 else '—'; full += back == w
            print(f"| {w} | {' - '.join(f'{b} \\| {mk}' for b, mk, _ in res)} | составное | {' - '.join(f'{e[0][2]} \\| {mk}' for _, mk, e in res)} | {r} | {back}{'' if back == w else ' ✗'} |", flush=True)
            continue
        b, mk = grammar(w)
        if b not in cache: cache[b] = encode(b)
        e = cache[b]
        if e is None: print(f"| {w} | {b} | — | нет в словаре | |"); cnt['нет в словаре'] += 1; continue
        (r, k, s), _ = e; cnt[NAME[k]] += 1; first += r == 1; n += 1
        back = forms.realize(b, mk) if r == 1 else '—'; full += back == w
        print(f"| {w} | {b} \\| {mk} | {NAME[k]} | {s} \\| {mk} | {r} | {back}{'' if back == w else ' ✗'} |", flush=True)
    print(f"\nслов {len(ws)}, основа в словаре {n}, основа первой {first} ({first/n:.0%}), слово восстановлено целиком {full} ({full/n:.0%}); формы: {dict(cnt)}")
