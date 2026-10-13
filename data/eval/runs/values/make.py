# Значения без модели (../reader/values.py: ConceptNet → проекция |z| ≥ 1,5 → ConceptNet с синонимами полюсов → голый корень).
# Hc — корни и форма H, значения по правилу. SZp — корни SZ (../measure) голыми (род — как в SZ). SZc — SZ, значения уточнений по правилу.
# SZcR — SZc + роль по WordNet: noun.person (и род не SOMEONE) → agent, потомок instrumentality.n.03 → tool.
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, f"{D}/../reader"); import lib, values
from nltk.corpus import wordnet as wn
items = json.load(open(f"{D}/../measure/items.json")); V = lib.vecs({it["w"] for it in items})
fmt = lambda r, v: r if v is None else f"{r}(={v:+d})" if v else f"{r}(=0)"
def role(w, head):
    s = wn.synsets(w, "n")
    if not s: return None
    if s[0].lexname() == "noun.person" and head != "SOMEONE": return "agent"
    if any(p.name() == "instrumentality.n.03" for p in s[0].closure(lambda x: x.hypernyms())): return "tool"
    return None
out = []; src = {}
for it in items:
    w = it["w"]; h, _, hf = it["H"].partition("|")
    hr = lib.parse(it["H"])[0]
    Hc = " ".join(fmt(r, values.value(V, w, r, 1.5)[0]) for r, _ in hr) + " |" + hf
    sr = lib.parse(it["SZ"])[0]
    SZp = " ".join([fmt(*sr[0]) if sr[0][1] == 0 else sr[0][0]] + [r for r, _ in sr[1:]]) + " | o"
    head = fmt(*sr[0])
    mods = []
    for r, _ in sr[1:]:
        v, s = values.value(V, w, r, 1.5); src[s] = src.get(s, 0) + 1; mods.append(fmt(r, v))
    SZc = " ".join([head] + mods) + " | o"; ro = role(w, sr[0][0]); SZcR = SZc + (f" {ro}" if ro else "")
    out.append({"w": w, "H": it["H"], "SZ": it["SZ"], "Hc": Hc, "SZp": SZp, "SZc": SZc, "SZcR": SZcR})
json.dump(out, open(f"{D}/items.json", "w"), indent=1)
for v in ("Hc", "SZp", "SZc", "SZcR"):
    os.makedirs(f"{D}/{v.lower()}", exist_ok=True)
    for k in (1, 2): open(f"{D}/{v.lower()}/codes_{k}.md", "w").write("".join(f"{i + 1}. {o[v]}\n" for i, o in enumerate(out[(k - 1) * 50:k * 50])))
print("источники значений уточнений SZc:", src, "; ролей:", sum(o["SZcR"] != o["SZc"] for o in out))
for o in out[::9]: print(f"{o['w']}: H {o['H']} → Hc {o['Hc']} | SZ {o['SZ']} → SZc {o['SZc']} | SZcR {o['SZcR']}")
