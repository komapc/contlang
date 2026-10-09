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
            if b and b != w and _WL.get(b) == wl:
                return b, mk or ('i A0' if w.endswith('ing') else 'i' if w.endswith('s') else 'i T-2')
    p = pos_of(w)
    if p is None:                                            # не лемма: словоизменение (went, facts, wished)
        for q, mk in ((wn.VERB, None), (wn.NOUN, 'o N+3')):
            b = wn.morphy(w, q)
            if b and b != w:
                if mk: return b, mk
                return b, 'i A0' if w.endswith('ing') else 'i' if w.endswith('s') else 'i T-2'
        return w, 'o'
    if p in 'ar':                                            # производное: deliberately → deliberate | e, presidential → president | a
        for s in wn.synsets(w)[:3]:
            if s.pos().replace('s', 'a') != p: continue
            for l in s.lemmas():
                if l.name().lower() != w: continue
                for pp in l.pertainyms():
                    b = pp.name().lower()
                    if b in wi and len(b) >= 4: return b, POS[p]
    return w, POS[p]

if __name__ == '__main__':
    TEXT = open(ARGS[0]).read() if ARGS else re.search(r'TEXT = open\(ARGS\[0\]\)\.read\(\) if ARGS else """(.*?)"""', open(SP + 'r16.py').read(), re.S).group(1)
    STOP = set('i to the because only of and see if could not what it had when that did was is so nor unless quite as put all into a its be why then or were by my in out get next able give'.split())
    ws = []
    for w in re.findall(r"[a-z]+", TEXT.lower()):
        if w not in STOP and w not in ws and wn.synsets(w): ws.append(w)
    NAME = {1: 'код', 2: 'одно слово', 3: 'слово + уровень', 4: 'основа + суффикс', 5: 'два слова'}
    cnt = collections.Counter(); first = 0; n = 0; cache = {}
    print("| слово | основная форма | формой основы | что передаётся | место основы |\n|---|---|---|---|--:|")
    for w in ws:
        b, mk = grammar(w)
        if b not in cache: cache[b] = encode(b)
        e = cache[b]
        if e is None: print(f"| {w} | {b} | — | нет в словаре | |"); cnt['нет в словаре'] += 1; continue
        (r, k, s), _ = e; cnt[NAME[k]] += 1; first += r == 1; n += 1
        print(f"| {w} | {b} \\| {mk} | {NAME[k]} | {s} \\| {mk} | {r} |", flush=True)
    print(f"\nслов {len(ws)}, основа в словаре {n}, первыми {first} ({first/n:.0%}); формы: {dict(cnt)}")
