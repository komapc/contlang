# lexs: 120 новых предложений Brown (те же фильтры, что ../pipe/pick.py), по 12 из 10 жанров, seed 20261110, без предложений pipe.
#   NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/lexs/pick.py
import json, os, random, re
from nltk.corpus import brown
D = os.path.dirname(os.path.abspath(__file__))
CATS = ["news", "editorial", "reviews", "hobbies", "lore", "belles_lettres", "learned", "fiction", "adventure", "romance"]
def det(t):
    s = " ".join(t); s = re.sub(r" ([.,!?'])", r"\1", s); s = re.sub(r" n't", "n't", s); s = s.replace(" 's", "'s")
    return s
def ok(t):
    w = [x for x in t if re.match(r"[A-Za-z]", x)]
    if not 8 <= len(w) <= 18 or t[-1] != "." or not t[0][:1].isupper(): return False
    if any(re.search(r"[0-9`'\"();:\-&/$%*]", x) and x not in ("'s", "n't") for x in t): return False
    if sum(1 for x in t[1:] if x[:1].isupper()) > 1: return False
    if t.count(",") > 2: return False
    return True
old = {x["s"] for v in json.load(open(f"{D}/../pipe/sents.json")).values() for x in v}
rng = random.Random(20261110); out = []
for c in CATS:
    S = [det(s) for s in brown.sents(categories=c) if ok(s)]; S = sorted(set(S)); rng.shuffle(S)
for c in CATS:
    S = sorted({det(s) for s in brown.sents(categories=c) if ok(s)} - old); rng.shuffle(S)
    out += [{"id": f"s{len(out) + i + 1}", "cat": c, "s": x} for i, x in enumerate(S[:12])]
json.dump(out, open(f"{D}/sents.json", "w"), indent=1, ensure_ascii=False); print(len(out))
