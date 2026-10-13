# Общее: векторы Numberbatch (кэш vec.npz), спецификация корней (spec.md), разбор кода.
import gzip, json, os, re, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); REPO = f"{D}/../../../.."; NB = f"{REPO}/data/raw/numberbatch-en-19.08.txt.gz"
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to", "or", "and", "one"}]
def spec_from(path):
    """{ROOT: {"axis": bool, "pts": [(v, [words])], "plain": [words]}}"""
    out = {}; t = open(path).read(); t = t[t.index("## Roots"):t.index("## Form")]
    for l in t.splitlines():
        m = re.match(r"- ([A-Z]+): (.*)", l)
        if not m: continue
        r, t, plain = m[1], m[2], [m[1].lower()]
        pm = re.search(r"\(the plain root means ([^)]*)\)", t)
        if pm: plain = toks(pm[1])
        t = re.sub(r"\([^)]*(no axis|size only|pleasant|direction|only for|plain root)[^)]*\)", "", t)
        t = re.sub(r"\((-1 just now, \+1 soon)\)", r"… \1 …", t).replace("(", " ").replace(")", " ").replace(", +", " … +").replace(", -", " … -")
        if "no axis" in m[2]: out[r] = {"axis": False, "pts": [], "plain": toks(t) or plain}; continue
        pts = [(int(x[0]), toks(x[1])) for x in re.findall(r"([+-]?\d)\s+([^…]+)", t)]
        out[r] = {"axis": True, "pts": sorted(pts), "plain": plain}
    return out
spec = lambda: spec_from(f"{D}/spec.md")
SPEC = spec_from(f"{D}/spec.md"); NAMES = list(SPEC)
def parse(code):
    """'A(=+3) B | o tool' → [(root, v|None)], pos, role"""
    s, _, f = code.partition("|"); rs = [(m[1], int(m[2]) if m[2] else None) for m in re.finditer(r"([A-Z]+)(?:\(=([+-]?\d)\))?", s) if m[1] in SPEC]
    f = f.split(); return rs, (f[0] if f else "o"), next((x for x in f[1:] if x in {"agent", "tool", "result", "quality"}), None)
def syn(w):
    out = {w}
    for p in "nvar": b = wn.morphy(w, p) or w; out |= {b} | {l.name().lower() for s in wn.synsets(b, p) for l in s.lemmas()}
    return out
_V = None
def vecs(extra=()):
    """словарь {слово: единичный вектор}: словарь сайта + extra; кэш в vec.npz (пересобирается, если чего-то не хватает)"""
    global _V
    words = json.load(open(f"{REPO}/site/data/math.json"))["words"]
    want = set(words) | set(extra) | {w for r in SPEC.values() for _, ws in r["pts"] for w in ws} | {w for r in SPEC.values() for w in r["plain"]}
    want |= {"person", "agent", "tool", "instrument", "result", "product", "quality", "state"}
    f = f"{D}/vec.npz"
    if _V is None and os.path.exists(f):
        z = np.load(f, allow_pickle=True); _V = dict(zip(z["w"], z["x"]))
    if _V is not None and all(w in _V or w in _V.get("__miss__", ()) for w in want): return _V
    have = dict(_V or {}); have.pop("__miss__", None)
    with gzip.open(NB, "rt") as fh:
        next(fh)
        for l in fh:
            w = l[:l.find(" ")]
            if w in want and w not in have: x = np.array(l.split()[1:], np.float32); have[w] = x / np.linalg.norm(x)
    miss = np.array(sorted(want - set(have)), dtype=object)
    np.savez(f, w=np.array(list(have), dtype=object), x=np.stack(list(have.values())), miss=miss)
    _V = have; _V["__miss__"] = set(miss); return _V
def pv(V, p):
    t = toks(p); j = "_".join(t)
    if j in V: return V[j]
    vs = [V[w] for w in t if w in V]; return (np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0))) if vs else None
def interp(V, r, v):
    """вектор прочтения корня r со значением v по подписям шкалы в spec.md (линейно между подписанными точками)"""
    sp = SPEC[r]; vec = lambda ws: pv(V, " ".join(ws))
    if v is None or not sp["axis"]: return vec(sp["plain"])
    pts = sorted(sp["pts"])
    if v <= pts[0][0]: return vec(pts[0][1])
    if v >= pts[-1][0]: return vec(pts[-1][1])
    for (a, wa), (b, wb) in zip(pts, pts[1:]):
        if a <= v <= b: t = (v - a) / (b - a); return (1 - t) * vec(wa) + t * vec(wb)
ROLEW = {"agent": "person", "tool": "tool", "result": "result", "quality": "quality"}
def gloss(V, code, w=(1, .6, .6), role=.5, plain_mix=.5):
    """читатель по спецификации: сумма прочтений корней с весами позиции + слово роли"""
    rs, pos, ro = parse(code); y = 0
    for k, (r, v) in enumerate(rs[:3]):
        g = interp(V, r, v)
        if v is not None and plain_mix and SPEC[r]["axis"]: g = g / np.linalg.norm(g) + plain_mix * interp(V, r, None)
        y = y + w[k] * g / np.linalg.norm(g)
    if ro: y = y + role * V[ROLEW[ro]]
    return y / np.linalg.norm(y)
