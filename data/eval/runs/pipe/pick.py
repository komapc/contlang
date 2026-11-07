# Выборка предложений из Brown (dec.md): 8–18 слов, без цифр, кавычек, скобок, «;» и «:», не больше одного имени собственного
# в середине, заканчивается точкой. Поровну из 10 жанров; seed 20261107. dev 30 (по 3 из жанра), holdout 60 (по 6).
#   NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/pipe/pick.py
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
rng = random.Random(20261107); dev, hold = [], []
for c in CATS:
    S = [det(s) for s in brown.sents(categories=c) if ok(s)]; S = sorted(set(S)); rng.shuffle(S)
    dev += [{"id": f"d{len(dev) + i + 1}", "cat": c, "s": x} for i, x in enumerate(S[:3])]
    hold += [{"id": f"h{len(hold) + i + 1}", "cat": c, "s": x} for i, x in enumerate(S[3:9])]
json.dump({"dev": dev, "holdout": hold}, open(f"{D}/sents.json", "w"), indent=1, ensure_ascii=False)
for x in dev: print(x["id"], x["cat"], "|", x["s"])
print(len(dev), len(hold))
