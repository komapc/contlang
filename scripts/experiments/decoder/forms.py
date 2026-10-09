"""Генератор словоформ: основная форма + метки min-co → английское слово (обратный шаг к r17.grammar).
Два способа:
  naive — только правила (go + T-2 → goed, good + C+3 → gooder), с орфографией: e-drop, y → i, удвоение согласной;
  known — сначала неправильные формы из списков исключений WordNet (перевёрнутых: go → went), потом правила.
Для каждой формы отмечается, есть ли она в словаре (/usr/share/dict/words, словарь сайта, леммы и исключения WordNet).
Запуск: forms.py — «Уолден» (текст из r16.py) и «Ворон» (100 слов), сравнение с исходным словом."""
import re, json, collections
from nltk.corpus import wordnet as wn
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
wn.synsets('dog'); EXC = wn._exception_map
REV = collections.defaultdict(list)                       # (основа, часть речи) → неправильные формы
for p, d in EXC.items():
    for form, bases in d.items():
        for b in bases: REV[b, p.replace('s', 'a')].append(form)
VOW = 'aeiou'
PART = ('en', 'ne', 'wn', 'un', 'rn')                 # окончания неправильных причастий: seen, gone, known, begun, born
SITE = set(json.load(open('site/data/math.json'))['words'])
DICT = {l.strip() for l in open('/usr/share/dict/words')} | set(json.load(open('site/data/math.json'))['words']) \
       | {l.lower() for l in wn.all_lemma_names()} | {f for d in EXC.values() for f in d}

def _cvc(b):                                              # stop → stopp-ed: короткое слово на согласная-гласная-согласная
    return len(b) >= 3 and b[-1] not in VOW + 'wxy' and b[-2] in VOW and b[-3] not in VOW and sum(c in VOW for c in b) == 1

def _suf(b, s):
    """b + суффикс s по правилам орфографии."""
    if s in ('ed', 'er', 'est', 'ing'):
        if b.endswith('e'): return b + s if s == 'ing' and b.endswith(('ee', 'ye', 'oe')) else b[:-1] + s
        if b.endswith('y') and len(b) > 1 and b[-2] not in VOW and s != 'ing': return b[:-1] + 'i' + s
        if _cvc(b): return b + b[-1] + s
        return b + s
    if s == 's':
        if re.search(r'(s|x|z|ch|sh)$', b): return b + 'es'
        if b.endswith('y') and b[-2:-1] not in tuple(VOW): return b[:-1] + 'ies'
        return b + 's'
    if s == 'ly':
        if b.endswith('le'): return b[:-1] + 'y'
        if b.endswith('ic'): return b + 'ally'
        if b.endswith('y') and len(b) > 2: return b[:-1] + 'ily'
        return b + 'ly'
    return b + s

def realize(b, mk, known=True):
    m = mk.split(); pos = m[0] if m else 'o'; tags = set(m[1:])
    def irr(p, pick):
        fs = REV.get((b, p), [])
        return pick(fs) if known and fs else None
    if pos == 'i' and 'T-2' in tags:                      # прошедшее: из исключений берём не причастие (went, а не gone)
        # причастия (gone, proven, seen) и -ing, -s отбрасываются; нет прошедшего в исключениях — правило (prove → proved)
        if b == 'be': return 'was'
        r = _suf(b, 'ed')
        if known and wn.morphy(r, wn.VERB) == b and r in SITE: return r     # правильное, если оно настоящая форма (worked, а не wrought; но не seed ← see)
        return irr('v', lambda fs: min((f for f in fs if not f.endswith(PART + ('ing',)) and f != _suf(b, 's')), key=len, default=None)) \
            or irr('v', lambda fs: next((f for f in fs if not f.endswith('ing') and f != _suf(b, 's')), None)) or r
    if pos == 'i' and 'A+5' in tags:                      # причастие: known, gone, begun
        return irr('v', lambda fs: next((f for f in fs if f.endswith(PART)), None)) or realize(b, 'i T-2', known)
    if pos == 'i' and 'A0' in tags: return irr('v', lambda fs: next((f for f in fs if f.endswith('ing')), None)) or _suf(b, 'ing')
    if pos == 'o' and 'N+3' in tags:                      # правильное, если оно есть в словаре (brothers, а не brethren)
        r = _suf(b, 's') if not b.endswith('man') else b[:-3] + 'men'
        return r if not known or (r in SITE and r in DICT) else (irr('n', lambda fs: fs[0]) or r)
    if pos == 'a' and ('C+3' in tags or 'C+5' in tags):
        s = 'est' if 'C+5' in tags else 'er'
        return irr('a', lambda fs: next((f for f in fs if f.endswith(s)), None)) or _suf(b, s)
    if pos == 'e':                                        # наречие от прилагательного; само наречие (in, also) — как есть
        c = collections.Counter()                         # основа — прежде всего наречие (in, after) → как есть; прилагательное (real) → really
        for ss in wn.synsets(b):
            for l in ss.lemmas():
                if l.name().lower() == b and ss.pos() in 'asr': c['r' if ss.pos() == 'r' else 'a'] += l.count() + 0.01
        if c['r'] >= c['a']: return b
        return ADV.get(b) if known and b in ADV else _suf(b, 'ly')
    if pos == 'a' and wn.synsets(b, 'n') and not (wn.synsets(b, 'a') or wn.synsets(b, 's')):   # прил. от сущ.: president → presidential
        return (ADJ.get(b) if known else None) or b + 'al'
    return b

# производные из WordNet (обращённые pertainym): прил. → нареч., сущ. → прил.
ADV, ADJ = {}, {}
for ss in wn.all_synsets('r'):
    for l in ss.lemmas():
        for p in l.pertainyms():
            if p.name().lower()[:4] == l.name().lower()[:4]: ADV.setdefault(p.name().lower(), l.name().lower())
for ss in list(wn.all_synsets('a')) + list(wn.all_synsets('s')):
    for l in ss.lemmas():
        for p in l.pertainyms():
            if p.name().lower()[:4] == l.name().lower()[:4]: ADJ.setdefault(p.name().lower(), l.name().lower())

if __name__ == '__main__':
    src = open(SP + 'r17.py').read()
    g = {'wn': wn, 'collections': collections, 'wi': {w: i for i, w in enumerate(json.load(open('site/data/math.json'))['words'])}}
    exec(src[src.index('POS = {'):src.index("\nif __name__")], g)
    walden = re.search(r'TEXT = open\(ARGS\[0\]\)\.read\(\) if ARGS else """(.*?)"""', open(SP + 'r16.py').read(), re.S).group(1)
    STOP = set('i to the because only of and see if could not what it had when that did was is so nor unless quite as put all into a its be why then or were by my in out get next able give'.split())
    ws = []
    for w in re.findall(r"[a-z]+", walden.lower()):
        if w not in STOP and w not in ws and wn.synsets(w): ws.append(w)
    tot = collections.Counter()
    print("| слово | основа \\| метки | наивно | в словаре? | с исключениями | = слово? |\n|---|---|---|:-:|---|:-:|")
    for w in ws:
        b, mk = g['grammar'](w)
        if not mk.split()[1:] and mk not in ('e',) and b == w: tot['без меток'] += 1; continue
        nv, kn = realize(b, mk, False), realize(b, mk, True)
        tot['с метками'] += 1; tot['наивно = слово'] += nv == w; tot['с исключениями = слово'] += kn == w; tot['наивной формы нет в словаре'] += nv not in DICT
        print(f"| {w} | {b} \\| {mk} | {nv} | {'да' if nv in DICT else '**нет**'} | {kn} | {'✓' if kn == w else '✗'} |")
    print('\n', dict(tot))

    # шире: все слова словаря сайта, которым grammar() даёт метки или основу — точность генератора по типу метки
    c = collections.Counter(); bad = collections.defaultdict(list)
    for w in g['wi']:
        if not w.isalpha(): continue
        b, mk = g['grammar'](w)
        if b == w and len(mk.split()) == 1 and mk != 'e': continue
        t = (mk.split() + [''])[1] or mk
        nv, kn = realize(b, mk, False), realize(b, mk, True)
        c[t, 'n'] += 1; c[t, 'nv'] += nv == w; c[t, 'kn'] += kn == w; c[t, 'nd'] += nv not in DICT
        if kn != w: bad[t].append(f"{w} ← {b}: {kn}")
    print("\n| метка | слов | наивно = слово | с исключениями = слово | наивной формы нет в словаре | примеры ошибок |\n|---|--:|--:|--:|--:|---|")
    for t in sorted({k[0] for k in c}):
        n = c[t, 'n']
        print(f"| {t} | {n} | {c[t, 'nv']/n:.0%} | {c[t, 'kn']/n:.0%} | {c[t, 'nd']} | {'; '.join(bad[t][:5])} |")
