# Объединённый кодер математики: SZ с новыми корнями (../newroots/sz.py) + значения уточнений по правилу (../reader/values.py:
# прямая связь ConceptNet с полюсами сильнее 0,3 → |z| ≥ 1,5; у новых корней — |z| ≥ 1,5; иначе голый) + роль (bases.py):
# tool — потомок instrumentality.n.03, agent — noun.person, если род не SOMEONE. Словообразование (кодировать глагол-основу) отброшено:
# векторы глаголов слишком общие, коды портились (testimony → MANY(=-5) JOIN(=+5) SEE).  → items.json, combo/ codes_K.md
import json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [f"{D}/../reader", f"{D}/../newroots", D]
import lib, values, sz, bases
it = json.load(open(f"{D}/../measure/items.json")); words = [o["w"] for o in it]; sexok = {o["w"] for o in it if "SEX" in o["SZ"]}
B = {w: bases.base(w) for w in words}
SP2 = lib.spec_from(f"{D}/../newroots/spec.md")
V = lib.vecs(set(words) | {b for b, _ in B.values() if b} | {w for r in SP2.values() for _, ws in r["pts"] for w in ws} | {w for r in SP2.values() for w in r["plain"]})
def modval(w, r, z):
    if r in values.NI and w in V: return values.value(V, w, r, 1.5, use=("cn", "z"), CN=.3)[0] or 0
    return int(np.sign(z) * 5) if abs(z) >= 1.5 else 0
from nltk.corpus import wordnet as wn
def role(w):
    s = wn.synsets(w, "n")
    if not s: return None
    if any(p.name() == "instrumentality.n.03" for p in s[0].closure(lambda x: x.hypernyms())): return "tool"
    if s[0].lexname() == "noun.person" and (sz.head(w, sz.NEW_ANCH + sz.ANCH0) or ("",))[0] != "SOMEONE": return "agent"
    return None
opts = {"role": {w: r for w in words if (r := role(w))}, "modval": modval}
out = sz.build(True, words, V, sexok, opts)
os.makedirs(f"{D}/combo", exist_ok=True)
for k in (1, 2): open(f"{D}/combo/codes_{k}.md", "w").write("".join(f"{i + 1}. {out[w]}\n" for i, w in enumerate(words[(k - 1) * 50:k * 50])))
json.dump([{"w": w, "SZ": o["SZ"], "H": o["H"], "CO": out[w], "base": B[w][0], "role": B[w][1]} for w, o in zip(words, it)], open(f"{D}/items.json", "w"), indent=1)
sz2 = {w: l.split(". ", 1)[1].strip() for k in (1, 2) for w, l in zip(words[(k - 1) * 50:k * 50], open(f"{D}/../newroots/sz2/codes_{k}.md"))}
print("отличается от SZ2:", sum(out[w] != sz2[w] for w in words), "от A:", sum(out[w] != o["A"] for w, o in zip(words, it)))
for w in words:
    if out[w] != sz2[w]: print(f"  {w}: {sz2[w]} → {out[w]}")
