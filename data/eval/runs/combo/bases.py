# Основа словообразования (WordNet, первый смысл существительного): глагол, от которого слово образовано, и роль.
# noun.person → agent; noun.act / noun.event → действие («| o»); noun.communication / possession / artifact / cognition → result.
# Без глагольной основы: noun.person → нет основы (род SOMEONE); потомок instrumentality.n.03 → tool.
import json, os
from nltk.corpus import wordnet as wn
def base(w):
    ss = wn.synsets(w, "n")
    if not ss: return None, None
    s = ss[0]; lx = s.lexname()
    vs = [d.name() for l in s.lemmas() if l.name() == w for d in l.derivationally_related_forms() if d.synset().pos() == "v"]
    vs = [v for v in vs if v != w and "_" not in v]; v = vs[0] if vs else None
    if lx == "noun.person": return v, "agent" if v else None
    if v and lx in ("noun.act", "noun.event"): return v, None
    if v and lx in ("noun.communication", "noun.possession", "noun.artifact", "noun.cognition"): return v, "result"
    if any(p.name() == "instrumentality.n.03" for p in s.closure(lambda x: x.hypernyms())): return None, "tool"
    return None, None
if __name__ == "__main__":
    D = os.path.dirname(os.path.abspath(__file__)); it = json.load(open(f"{D}/../taxonomy/items.json"))
    for x in it:
        b, r = base(x["w"])
        if b or r: print(f"{x['w']}: {b} {r or ''}   (H {x['H']})")
