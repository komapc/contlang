# Объединённый кодер математики: SZ с новыми корнями (../newroots/sz.py) + значения уточнений по правилу (../reader/values.py:
# ConceptNet → |z| ≥ 1,5 → ConceptNet с синонимами полюсов; у новых корней — |z| ≥ 1,5) + словообразование и роль (bases.py:
# у производного от глагола кодируется глагол, роль agent / result; у орудий — tool).  → items.json, combo/ codes_K.md
import json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [f"{D}/../reader", f"{D}/../newroots", D]
import lib, values, sz, bases
it = json.load(open(f"{D}/../measure/items.json")); words = [o["w"] for o in it]; sexok = {o["w"] for o in it if "SEX" in o["SZ"]}
B = {w: bases.base(w) for w in words}
SP2 = lib.spec_from(f"{D}/../newroots/spec.md")
V = lib.vecs(set(words) | {b for b, _ in B.values() if b} | {w for r in SP2.values() for _, ws in r["pts"] for w in ws} | {w for r in SP2.values() for w in r["plain"]})
def modval(w, r, z):
    if r in values.NI and w in V: return values.value(V, w, r, 1.5)[0] or 0
    return int(np.sign(z) * 5) if abs(z) >= 1.5 else 0
opts = {"base": {w: b for w, (b, _) in B.items() if b}, "role": {w: r for w, (_, r) in B.items() if r}, "modval": modval}
out = sz.build(True, words, V, sexok, opts)
os.makedirs(f"{D}/combo", exist_ok=True)
for k in (1, 2): open(f"{D}/combo/codes_{k}.md", "w").write("".join(f"{i + 1}. {out[w]}\n" for i, w in enumerate(words[(k - 1) * 50:k * 50])))
json.dump([{"w": w, "SZ": o["SZ"], "H": o["H"], "CO": out[w], "base": B[w][0], "role": B[w][1]} for w, o in zip(words, it)], open(f"{D}/items.json", "w"), indent=1)
print("отличается от SZ:", sum(out[w] != o["SZ"] for w, o in zip(words, it)))
for w, o in zip(words, it):
    if out[w] != o["SZ"]: print(f"  {w}: {o['SZ']} → {out[w]}   [H {o['H']}]")
