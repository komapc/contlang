# Пары через связку у кодера сайта: что не так с PI (137 кодов-пар из ../big1000).
#   A — код сайта как есть (голова + PI + сосед по вектору, закодированный двумя корнями)
#   B — только голова (вторая часть отброшена)
#   D — голова + связка по типу ребра ConceptNet + опорное слово (рецепт из site/data/recipes.json):
#       PartOf / AtLocation / HasA⁻¹ → PI, UsedFor → FOR, MadeOf → FROM; вес ≥ 2, иначе RelatedTo ≥ 2 → PI, иначе только голова
#   F — голова + PI + ближайшее по вектору опорное слово (без графа)
# Опорное слово не совпадает со словом по лемме и не его синоним (общий синсет WordNet).
import json, os, re, collections
import numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."
site = json.load(open(f"{D}/../big1000/site_codes.json")); m = json.load(open(f"{R}/site/data/math.json")); W = m["words"]
ix = {w: i for i, w in enumerate(W)}; meta = json.load(open(f"{R}/site/data/words.json"))
X = np.frombuffer(open(f"{R}/site/data/vocab.bin", "rb").read(), np.int8).reshape(len(W), 300).astype(np.float32) / 127
rec = {x["en"]: x["code"] for x in json.load(open(f"{R}/site/data/recipes.json")) if re.search(r"\|\s*o\b", x["code"]) and " PI " not in x["code"] and " FOR " not in x["code"]}
anc = [a for a in rec if a in ix]
lem = lambda w: meta["lemma"][ix[w]] if meta["lemma"][ix[w]] >= 0 else ix[w]
syn = lambda w: {l.name().lower() for s in wn.synsets(w, "n") for l in s.lemmas()} | {w}
def ok(w, a): return lem(a) != lem(w) and a not in syn(w) and w not in syn(a)
g = json.load(open(f"{R}/data/raw/conceptnet/graph.json")); REL = g["rel"]
LINK = {"PartOf": "PI", "AtLocation": "PI", "HasA^-1": "PI", "UsedFor": "FOR", "MadeOf": "FROM"}
ai = {ix[a]: a for a in anc}; E = collections.defaultdict(list)
for a, b, r, w in g["edges"]:
    r = REL[r]
    if b in ai: E[a].append((r, ai[b], w))
    if a in ai and r == "HasA": E[b].append(("HasA^-1", ai[a], w))
    if a in ai and r == "RelatedTo": E[b].append((r, ai[a], w))
words = [w for w in json.load(open(f"{D}/../big1000/words.json")) if site.get(w) and " PI " in site[w]]
out = {}; why = {}
for w in words:
    head = site[w].split(" PI ")[0].strip()
    e = [x for x in E.get(lem(w), []) + E.get(ix[w], []) if ok(w, x[1])]
    typed = sorted([x for x in e if x[0] in LINK and x[2] >= 2], key=lambda x: -x[2])
    rel = sorted([x for x in e if x[0] == "RelatedTo" and x[2] >= 2], key=lambda x: -x[2])
    if typed: r, a, wt = typed[0]; d = f"{head} {LINK[r]} {rec[a]}"; why[w] = f"{r} {a} {wt}"
    elif rel: r, a, wt = rel[0]; d = f"{head} PI {rec[a]}"; why[w] = f"{r} {a} {wt}"
    else: d = head; why[w] = "—"
    c = [a for a in anc if ok(w, a)]; s = X[[ix[a] for a in c]] @ X[ix[w]]; fa = c[int(np.argmax(s))]
    out[w] = {"A": site[w], "B": head, "D": d, "F": f"{head} PI {rec[fa]}", "why": why[w], "f_anchor": fa}
json.dump(out, open(f"{D}/codes.json", "w"), indent=1, ensure_ascii=False)
c = collections.Counter(v["why"].split()[0] for v in out.values()); print(len(out), "слов;", dict(c))
print("D = B у", sum(v["D"] == v["B"] for v in out.values()))
