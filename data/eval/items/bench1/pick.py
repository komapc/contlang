"""Постоянный набор min-co 2.0 (bench1): предложения и абзацы Brown, рабочая (dev) и отложенная (hold) части.

    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/items/bench1/pick.py

Предложения — 120 из lexs (sents120.json, отобраны pick_sents_lexs.py, seed 20261110): по 6 из каждого жанра в dev и hold
(seed 20261111; s1–s5 видны в обзоре — всегда в dev). Абзацы — Brown paras(): 3–5 предложений, 40–110 слов, без цифр, кавычек,
скобок, `;`/`:`, не больше 3 запятых в предложении; без предложений из sents120 и pipe; по 2 из каждого жанра: один в dev, один в hold.
Hold не кодируется и не читается до первого решения по 2.0.
"""
import json
import random
import re
from pathlib import Path

from nltk.corpus import brown

D = Path(__file__).resolve().parent
R = D.parents[3]
CATS = ["news", "editorial", "reviews", "hobbies", "lore", "belles_lettres", "learned", "fiction", "adventure", "romance"]


def det(t):
    s = " ".join(t)
    s = re.sub(r" ([.,!?'])", r"\1", s)
    s = re.sub(r" n't", "n't", s)
    return s.replace(" 's", "'s")


def sent_ok(t):
    w = [x for x in t if re.match(r"[A-Za-z]", x)]
    if not 4 <= len(w) <= 25 or t[-1] not in ".!?" or not t[0][:1].isupper():
        return False
    if any(re.search(r"[0-9`'\"();:\-&/$%*]", x) and x not in ("'s", "n't") for x in t):
        return False
    return t.count(",") <= 3


S = json.load(open(D / "sents120.json"))
rng = random.Random(20261111)
dev, hold = [], []
for c in CATS:
    xs = [x for x in S if x["cat"] == c]
    first = [x for x in xs if x["id"] in {"s1", "s2", "s3", "s4", "s5"}]
    rest = [x for x in xs if x not in first]
    rng.shuffle(rest)
    k = 6 - len(first)
    dev += first + rest[:k]
    hold += rest[k:]
assert len(dev) == len(hold) == 60

used = {x["s"] for x in S} | {x["s"] for v in json.load(open(R / "data/eval/runs/pipe/sents.json")).values() for x in v}
paras = {"dev": [], "hold": []}
for c in CATS:
    cand = []
    for p in brown.paras(categories=c):
        if not 3 <= len(p) <= 5 or not all(sent_ok(t) for t in p):
            continue
        ss = [det(t) for t in p]
        n = sum(len([x for x in t if re.match(r"[A-Za-z]", x)]) for t in p)
        if 40 <= n <= 110 and not used & set(ss) and sum(1 for t in p for x in t[1:] if x[:1].isupper()) <= 3:
            cand.append(ss)
    cand = sorted({tuple(x) for x in cand})
    rng.shuffle(cand)
    for part, p in zip(("dev", "hold"), cand[:2]):
        paras[part].append({"id": f"p{len(paras[part]) + 1}{part[0]}", "cat": c, "sents": list(p)})
for part, xs in (("dev", dev), ("hold", hold)):
    json.dump(xs, open(D / f"sents_{part}.json", "w"), indent=1, ensure_ascii=False)
    json.dump(paras[part], open(D / f"paras_{part}.json", "w"), indent=1, ensure_ascii=False)
print("предложения", len(dev), len(hold), "абзацы", len(paras["dev"]), len(paras["hold"]))
