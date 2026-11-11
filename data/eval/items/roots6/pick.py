"""Целевой набор для v2b (шесть новых корней): предложения Brown с понятиями корней и контрольные без них.

    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/items/roots6/pick.py cand   → candidates.json (по 20 на корень)
    (вручную: screen.json — решение по каждому кандидату по правилу ниже, до любых кодов)
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/items/roots6/pick.py final  → sents.json (42 целевых + 18 контрольных)

Слова-признаки — из глосс корней в lang/v2b/roots.yaml (en_axis), не из потерь на dev. Фильтр предложений — как у абзацев bench1
(4–25 слов, без цифр, кавычек, скобок, `;`/`:`, не больше 3 запятых). Исключены все предложения bench1 (dev и hold, абзацы),
sents120 и pipe. Seed 20261112.

Правило отбора (screen.json): слово-признак употреблено в **буквальном** смысле корня — физический цвет; свет, яркость, тьма,
белое/чёрное; форма предмета (круглое, плоское, брусок); вместилище или проём, открыть/закрыть; физическая или иная сила,
слабость; правда, ложь, реальность. Отклоняются переносные и посторонние значения (*light* = лёгкий, *table* = таблица,
*ring* = звонок, *board* = совет, *real estate*, *Black* как фамилия), а также предложения без понятного смысла вне контекста.
Берутся первые 7 принятых на корень в порядке кандидатов; отклонённые остаются в screen.json.
"""
import json
import random
import re
import sys
from pathlib import Path

from nltk.corpus import brown

D = Path(__file__).resolve().parent
R = D.parents[3]
SEED = 20261112
PER_ROOT = 7
N_CONTROL = 18
KEYS = {
    "SHAPE": "round ball balls circle circles ring rings block blocks cube cubes lump flat sheet sheets board boards table tables floor floors bed beds",
    "OPEN": "closed container containers box boxes bag bags cup cups sack lid cover open opened opening hole holes door doors window windows",
    "STRONG": "weak fragile helpless strong stronger strongest powerful force strength weakness",
    "TRUE": "false lie lies fiction true truth real really actually",
    "LIGHT": "black dark darkness grey gray dim white bright light lights shining",
    "COLOR": "red orange yellow green blue violet purple colour color colors colored",
}
ALL_KEYS = {w for v in KEYS.values() for w in v.split()}


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


def used():
    b = D.parent / "bench1"
    s = {x["s"] for f in ("sents_dev.json", "sents_hold.json", "sents120.json") for x in json.load(open(b / f))}
    s |= {x for f in ("paras_dev.json", "paras_hold.json") for p in json.load(open(b / f)) for x in p["sents"]}
    s |= {x["s"] for v in json.load(open(R / "data/eval/runs/pipe/sents.json")).values() for x in v}
    return s


def pool():
    u = used()
    out = []
    for fid in brown.fileids():
        cat = brown.categories(fid)[0]
        for t in brown.sents(fid):
            if sent_ok(t):
                s = det(t)
                if s not in u:
                    out.append({"s": s, "cat": cat, "words": {x.lower() for x in t}})
    return out


def cand():
    P = pool()
    rng = random.Random(SEED)
    res, seen = {}, set()
    for root, ws in KEYS.items():
        ks = set(ws.split())
        xs = [x for x in P if x["words"] & ks and x["s"] not in seen]
        rng.shuffle(xs)
        res[root] = [{"id": f"{root.lower()}{k + 1}", "s": x["s"], "cat": x["cat"], "hit": sorted(x["words"] & ks)} for k, x in enumerate(xs[:20])]
        seen |= {x["s"] for x in xs[:20]}
    ctrl = [x for x in P if not x["words"] & ALL_KEYS and x["s"] not in seen]
    rng.shuffle(ctrl)
    res["CONTROL"] = [{"id": f"c{k + 1}", "s": x["s"], "cat": x["cat"]} for k, x in enumerate(ctrl[:N_CONTROL])]
    json.dump(res, open(D / "candidates.json", "w"), indent=1, ensure_ascii=False)
    print({k: len(v) for k, v in res.items()})


def final():
    c = json.load(open(D / "candidates.json"))
    scr = json.load(open(D / "screen.json"))
    items = []
    for root in KEYS:
        acc = [x for x in c[root] if scr[x["id"]] == "ok"][:PER_ROOT]
        assert len(acc) == PER_ROOT, root
        items += [{"id": x["id"], "kind": "target", "root": root, "s": x["s"], "cat": x["cat"]} for x in acc]
    items += [{"id": x["id"], "kind": "control", "root": None, "s": x["s"], "cat": x["cat"]} for x in c["CONTROL"]]
    random.Random(SEED + 1).shuffle(items)
    json.dump(items, open(D / "sents.json", "w"), indent=1, ensure_ascii=False)
    print(len(items), "предложений:", sum(x["kind"] == "target" for x in items), "целевых")


{"cand": cand, "final": final}[sys.argv[1]]()
