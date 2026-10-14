# SZ (../measure/make.js) на Python, с новыми корнями или без: род — ближайший якорь-гипероним WordNet (../taxonomy/anchors.py ANCH),
# уточнения — самые выраженные корни (max(|z оси|, z центра)), второе при ≥ Z2; значение ±5 по знаку z оси при |z| ≥ Z0, иначе голый.
# Новые корни (выраженность — только по центру: ось из трёх слов шумная): центр — среднее слов подписи (spec.md), ось — среднее полюса + минус среднее полюса −; якоря — NEW_ANCH.
#   python sz.py --check  (сверка со старым SZ)   python sz.py  → sz2/ codes_K.md, items.json
import json, os, re, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{D}/../reader"); import lib
from nltk.corpus import wordnet as wn
m = json.load(open(f"{lib.REPO}/site/data/math.json")); Z0, Z2 = .5, 2.0
src = open(f"{D}/../taxonomy/anchors.py").read(); g = {"wn": wn}; exec(src[src.index("ANCH = ["):src.index("for s, _, _ in ANCH")], g); ANCH0 = g["ANCH"]
NEW_ANCH = [("container.n.01", "CONTAINER", None), ("vessel.n.03", "CONTAINER", None), ("body_of_water.n.01", "LAND", -5), ("land.n.04", "LAND", 5),
    ("region.n.03", "LAND", None), ("country.n.02", "LAND", None), ("administrative_district.n.01", "LAND", None), ("geological_formation.n.01", "LAND", None),
    ("celestial_body.n.01", "LAND", None), ("religion.n.01", "SACRED", None), ("spiritual_being.n.01", "SACRED", None), ("place_of_worship.n.01", "SACRED", None),
    ("clergyman.n.01", "SACRED", None), ("religious_person.n.01", "SACRED", None), ("magic.n.01", "SACRED", 0), ("rite.n.02", "SACRED", None)]
def head(w, ANCH):
    ss = wn.synsets(w, "n")
    if not ss: return None
    dist = {ss[0]: 0}; fr = [ss[0]]
    while fr:
        nx = []
        for s in fr:
            for h in s.hypernyms() + s.instance_hypernyms():
                if h not in dist: dist[h] = dist[s] + 1; nx.append(h)
        fr = nx
    best = None
    for i, (s, r, v) in enumerate(ANCH):
        d = dist.get(wn.synset(s))
        if d is not None and (best is None or (d, i) < best[0]): best = ((d, i), r, v)
    return best and (best[1], best[2])
def build(new, items, V, sexok, opts=None):
    opts = opts or {}
    names = list(m["names"]); C = list(np.array(m["dict"]["C"])); A = list(np.array(m["dict"]["A"])); ax = list(m["has_axis"])
    spec = lib.spec_from(f"{D}/spec.md") if new else lib.SPEC
    LD = opts.get("dict")  # обученный словарь {names, C, A} вместо math.json; выраженность у всех корней одна
    if LD is not None:
        names = list(LD["names"]); C = list(LD["C"]); A = list(LD["A"]); ax = [bool(a.any()) for a in A]
    if new and LD is None:
        for r in ("LAND", "SACRED", "CONTAINER"):
            sp = spec[r]; vec = lambda ws: np.mean([V[w] for w in ws if w in V], 0)
            c = vec(sp["plain"] + [w for _, ws in sp["pts"] for w in ws]); a = vec([w for v, ws in sp["pts"] if v > 0 for w in ws]) - vec([w for v, ws in sp["pts"] if v < 0 for w in ws])
            names.append(r); C.append(c / np.linalg.norm(c)); A.append(a / np.linalg.norm(a)); ax.append(True)
    C, A = np.stack(C), np.stack(A); W = np.stack([V[w] for w in m["words"][::5] if w in V])
    dC, dA = W @ C.T, W @ A.T; mC, sC, mA, sA = dC.mean(0), dC.std(0), dA.mean(0), dA.std(0)
    ANCH = opts["anch"] if "anch" in opts else [a for a in ((NEW_ANCH + [a for a in ANCH0 if not (a[0] == "container.n.01" or a[0] == "body_of_water.n.01")]) if new else ANCH0) if a[1] not in opts.get("drop", ())]
    lv = lambda r: m["levels"].get(r, list(range(-5, 6)))
    out = {}
    for w in items:
        bw = opts.get("base", {}).get(w); x = V[bw] if bw and bw in V else V[w]; zC = (x @ C.T - mC) / sC; zA = (x @ A.T - mA) / sA
        sal = np.where(np.array(ax) & ((np.arange(len(names)) < 44) | (LD is not None)), np.maximum(np.abs(zA), zC), zC)  # у новых корней — только центр
        def val(i):
            if not ax[i] or abs(zA[i]) < Z0: return 0
            t = int(np.sign(zA[i]) * 5); L = lv(names[i]); return t if t in L else (max(L) if t > 0 else min(L))
        one = lambda i, v: names[i] if not ax[i] or not v else f"{names[i]}(={v:+d})"
        ban = (set() if w in sexok else {names.index("SEX")}) | {names.index(r) for r in opts.get("drop", ()) if r in names}
        rank = [i for i in np.argsort(-sal) if i not in ban]
        h = None if (bw and bw in V) else head(w, ANCH)
        if h: hi, hv = names.index(h[0]), h[1]
        else: hi = rank[0]; hv = val(hi)
        rest = [i for i in rank if i != hi]; S = [rest[0]] + ([rest[1]] if sal[rest[1]] >= Z2 else [])
        hs = f"{names[hi]}(=0)" if h and hv == 0 else one(hi, hv)
        mv = opts.get("modval")
        mods = [one(i, mv(bw if bw and bw in V else w, names[i], zA[i]) if mv else val(i)) for i in S]
        ro = opts.get("role", {}).get(w)
        out[w] = " ".join([hs] + mods) + " | o" + (f" {ro}" if ro else "")
    return out
if __name__ == "__main__":
    it = json.load(open(f"{D}/../measure/items.json")); words = [o["w"] for o in it]; SP2 = lib.spec_from(f"{D}/spec.md"); V = lib.vecs(set(words) | {w for r in SP2.values() for _, ws in r["pts"] for w in ws} | {w for r in SP2.values() for w in r["plain"]})
    sexok = {o["w"] for o in it if "SEX" in o["SZ"]}
    if sys.argv[1:] == ["--check"]:
        o = build(False, words, V, sexok); same = sum(o[x["w"]] == x["SZ"] for x in it); print(f"совпало со старым SZ {same}/100")
        for x in it:
            if o[x["w"]] != x["SZ"]: print(" ", x["w"], x["SZ"], "|", o[x["w"]])
        sys.exit()
    o2 = build(True, words, V, sexok); os.makedirs(f"{D}/sz2", exist_ok=True)
    for k in (1, 2): open(f"{D}/sz2/codes_{k}.md", "w").write("".join(f"{i + 1}. {o2[w]}\n" for i, w in enumerate(words[(k - 1) * 50:k * 50])))
    ch = [(w, x["SZ"], o2[w]) for w, x in zip(words, it) if o2[w] != x["SZ"]]
    print(f"изменилось {len(ch)}:"); [print(" ", *c) for c in ch]
