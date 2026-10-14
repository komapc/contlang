# Три слова для неудачных слов: цели — слова, нынешний код которых слепой читатель прочитал мимо (swap, вариант O, 188 слов);
# опорные слова — коды, проверенные слепым чтением: рецепты сайта (без пар) и коды сайта, прочитанные «близко» (swap O, big1000 при том же коде).
# Для каждой цели — 30 ближайших по вектору опорных слов той же части речи, не того же корня (первые 5 букв), не синонимы (WordNet).
#   python pool.py SCRATCH/failok.json → pool.json
import json, re, sys, os, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."
fo = json.load(open(sys.argv[1])); m = json.load(open(f"{R}/site/data/math.json")); W = m["words"]; ix = {w: i for i, w in enumerate(W)}
X = np.frombuffer(open(f"{R}/site/data/vocab.bin", "rb").read(), np.int8).reshape(len(W), 300).astype(np.float32); X /= np.linalg.norm(X, axis=1, keepdims=True)
pos = lambda c: (re.search(r"\|\s*([oiae])\b", c) or [None, None])[1]
anc = {x["en"]: x["code"] for x in json.load(open(f"{R}/site/data/recipes.json")) if not re.search(r"\b(PI|FOR|FROM|LIKE)\b", x["code"])}
anc.update(fo["ok"])
L = json.load(open(f"{D}/../reader/labels.json")); old = json.load(open(f"{D}/../big1000/site_codes.json")); cur = json.load(open(f"{D}/../swap/remove.json"))
for l in json.load(open(f"{D}/../big1000/lists.json")):
    if l["var"] != "math": continue
    a = {int(mm[1]): mm[2].split("|")[0].strip().strip("`").lower() for x in open(f"{D}/../big1000/answers/r{l['r']}_math.md") if (mm := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    for i, w in enumerate(l["words"]):
        if L.get(f"{w}\t{a.get(i + 1)}") == 2 and w in cur and cur[w]["code"] == old.get(w): anc.setdefault(w, cur[w]["code"])
anc = {w: c for w, c in anc.items() if w in ix and pos(c)}
syn = lambda w: {l.name().lower() for s in wn.synsets(w) for l in s.lemmas()} | {w}
out = {}
for w, c in fo["fail"].items():
    if w not in ix: continue
    sw = syn(w); cand = [a for a, ac in anc.items() if pos(ac) == pos(c) and a[:5] != w[:5] and a not in sw and w not in syn(a)]
    s = X[[ix[a] for a in cand]] @ X[ix[w]]; top = [cand[j] for j in np.argsort(-s)[:30]]
    out[w] = {"code": c, "anchors": [[a, anc[a], round(float(X[ix[a]] @ X[ix[w]]), 3)] for a in top]}
json.dump(out, open(f"{D}/pool.json", "w"), indent=0, ensure_ascii=False)
print(len(anc), "опорных слов;", len(out), "целей; пример:", list(out)[0], [a[0] for a in out[list(out)[0]]["anchors"][:5]])
