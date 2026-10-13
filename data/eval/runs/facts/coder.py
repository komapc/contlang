# Кодер по фактам: род — по таксономии WordNet (../taxonomy/heads.json), уточнения — из фактов ConceptNet о слове
# (для чего, что умеет, какое, где, из чего…). Каждое слово факта переводится в корень: точно — по словам-подписям шкал spec.md
# (и их синонимам WordNet; подпись даёт и знак значения), иначе — ближайшей подписью по вектору (cos ≥ TAU).
# Значение уточнения — голосование знаков фактов; без явного знака — правило ../reader/values.py; иначе голый корень.
# Роль: noun.person (род не SOMEONE) → agent; потомок instrumentality.n.03 → tool.
#   python coder.py [слово…]   — печатает коды и факты
import json, os, re, sys, math, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{D}/../reader"); import lib, values
from nltk.corpus import wordnet as wn
E = json.load(open(f"{D}/../reader/cn_test.json")); HEADS = json.load(open(f"{D}/../taxonomy/heads.json"))
RELW = {"IsA": .6, "UsedFor": 1, "CapableOf": .8, "HasProperty": 1, "AtLocation": .6, "MadeOf": .6, "PartOf": .4, "ReceivesAction": .6,
        "HasA": .3, "Causes": .5, "MannerOf": 1, "DefinedAs": .8, "CreatedBy": .3, "HasSubevent": .4, "Desires": .4, "CausesDesire": .3, "SymbolOf": .4}
STOP = {"be", "do", "have", "get", "make", "use", "thing", "something", "someone", "people", "person", "very", "much", "can", "lot", "way", "type", "kind", "form", "part", "of", "for", "with", "on", "at", "by", "from", "it", "they", "you", "out", "in", "into", "off", "over", "up", "down", "around", "about", "after", "before", "one", "all", "many", "some", "other", "good", "well", "enough", "more", "most", "big", "body", "keep", "hold", "take", "give", "go", "come", "put", "find", "found", "look", "see"}
TAU = float(os.environ.get("TAU", .45))
TRIG = {}; GROWN = os.environ.get("GROWN") == "1"; PHRASE = float(os.environ.get("PHRASE", 1))
def add(t, r, v, s):
    if t in STOP or not t: return
    TRIG.setdefault(t, {}); TRIG[t][(r, v)] = max(TRIG[t].get((r, v), 0), s)
for r, sp in lib.SPEC.items():
    for t in sp["plain"] + [r.lower()]: add(t, r, None, 1)
    for v, ws in sp["pts"]:
        for t in ws: add(t, r, v if sp["axis"] else None, 1)
        if GROWN:
            for t in values.grow(ws): add(t, r, v if sp["axis"] else None, .7)
_V = None
def V(): 
    global _V
    if _V is None: _V = lib.vecs(set(E) | set(HEADS))
    return _V
_P = None
def protos():
    global _P
    if _P is None:
        _P = []
        for r, sp in lib.SPEC.items():
            _P.append((r, None, lib.interp(V(), r, None)))
            for v, _ in sp["pts"]: _P.append((r, v, lib.interp(V(), r, v)))
        _P = [(r, v, x / np.linalg.norm(x)) for r, v, x in _P]
    return _P
def lemma(t): return wn.morphy(t, "v") or wn.morphy(t, "n") or wn.morphy(t, "a") or t
def match(t):
    """слово факта → [(корень, значение, сила)]"""
    t = lemma(t)
    if t in STOP: return []
    if t in TRIG: return [(r, v, s) for (r, v), s in TRIG[t].items()]
    if t not in V(): return []
    x = V()[t]; best = max(protos(), key=lambda p: float(p[2] @ x)); c = float(best[2] @ x)
    return [(best[0], best[1], c)] if c >= TAU else []
def facts(w):
    out = []
    for rel, b, wt in E.get(w, []):
        if rel.startswith("~") or rel not in RELW: continue
        out.append((rel, b.replace("_", " "), RELW[rel] * math.sqrt(wt)))
    return out
def fmt(r, v): return r if v is None else f"{r}(={v:+d})" if v else f"{r}(=0)"
def role(w, head):
    s = wn.synsets(w, "n")
    if not s: return None
    if s[0].lexname() == "noun.person" and head != "SOMEONE": return "agent"
    if any(p.name() == "instrumentality.n.03" for p in s[0].closure(lambda x: x.hypernyms())): return "tool"
    return None
def encode(w, K2=.5, trace=False):
    sc, vote, why = {}, {}, {}
    for rel, ph, wt in facts(w):
        ts = [t for t in lib.toks(ph) if t != w]
        ms = [m for t in ts for m in match(t)]
        if PHRASE and len(ts) > 1 and (x := lib.pv(V(), " ".join(ts))) is not None:
            best = max(protos(), key=lambda p: float(p[2] @ x)); c = float(best[2] @ x)
            if c >= TAU: ms.append((best[0], best[1], PHRASE * c))
        for r, v, s in ms:
                g = wt * s / max(1, len(ms)) ** .5; sc[r] = sc.get(r, 0) + g; why.setdefault(r, []).append(f"{rel}:{ph}")
                if v is not None: vote.setdefault(r, {}); vote[r][v] = vote[r].get(v, 0) + g
    h = HEADS.get(w)
    head = (h["root"], h["v"]) if h else None
    rank = sorted(sc, key=lambda r: -sc[r])
    if head is None:
        if not rank: return None, {}
        head = (rank[0], None)
    mods = [r for r in rank if r != head[0]][:2]
    if len(mods) == 2 and sc[mods[1]] < K2 * sc[mods[0]]: mods = mods[:1]
    parts = [fmt(*head) if head[1] is not None or not lib.SPEC[head[0]]["axis"] else head[0]]
    for r in mods:
        v = None
        if lib.SPEC[r]["axis"] and r in vote:
            tot = sum(vote[r].values()); best = max(vote[r], key=vote[r].get)
            if vote[r][best] >= .6 * tot and vote[r][best] >= .3 * sc[r]: v = best
        if v is None: v = values.value(V(), w, r, 1.5)[0]
        parts.append(fmt(r, v))
    ro = role(w, head[0])
    code = " ".join(parts) + " | o" + (f" {ro}" if ro else "")
    return code, ({r: (round(sc[r], 2), why[r][:4]) for r in rank[:5]} if trace else {})
def jac_h():
    items = json.load(open(f"{D}/../taxonomy/items.json")); J = []; sg = [0, 0]
    for it in items:
        c, _ = encode(it["w"]); 
        if c is None: J.append(0); continue
        A = dict(lib.parse(c)[0]); B = dict(lib.parse(it["H"])[0]); J.append(len(set(A) & set(B)) / len(set(A) | set(B)))
        for r in set(A) & set(B):
            if A[r] and B[r]: sg[1] += 1; sg[0] += np.sign(A[r]) == np.sign(B[r])
    return np.mean(J), sg
if __name__ == "__main__" and sys.argv[1:] == ["--jac"]:
    j, sg = jac_h(); print(f"совпадение корней с H {j:.2f}, знаки {sg[0]}/{sg[1]}"); sys.exit()
if __name__ == "__main__":
    for w in sys.argv[1:]:
        c, t = encode(w, trace=True); print(w, "→", c)
        for r, (s, y) in t.items(): print("   ", r, s, "; ".join(y))
