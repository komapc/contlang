"""lexn1 (dec.md): сколько дал бы общий словарь размера N — симуляция подсказками diag1.

Плечи (предложения bench1 dev, 60): mc (прочтения v2b2), mcg (все подсказки, прочтения diag1), tpx (прочтения tpx1) и
новые g300, g1000, g3000 — те же коды mc, но подсказка `<…>` оставлена только у слов, чья подсказка целиком из лемм
в первых N по частоте в корпусе Brown; подсказки без содержательных слов (местоимения, «be», «have», «why»…) скрыты.
По 2 новых читателя Haiku; все 720 прочтений судят заново 4 судьи Sonnet.
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/lexn1/run.py make SC   → ranks.json, codes.json, coverage.txt, SC/read/g*
    .venv/bin/python data/eval/runs/lexn1/run.py judges SC   → lists.json, pairs.json, SC/judge/s1..s4
    .venv/bin/python data/eval/runs/lexn1/run.py score SC    → result.txt, answers/, judge/
"""
import collections
import json
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
R = D.parents[3]
V2B2, TPX1, DIAG1 = D.parent / "v2b2", D.parent / "tpx1", D.parent / "diag1"
ITEMS = R / "data/eval/items/bench1"
SIZES = [300, 1000, 3000]
ARMS = ["mc", "g300", "g1000", "g3000", "mcg", "tpx"]
READERS = 2
JUDGES = 4
OVERLAP = 30
SENTS = json.load(open(ITEMS / "sents_dev.json"))
N = len(SENTS)
# служебные слова: подсказка только из них — скрыта (общий словарь не знает, что SOMEONE(=-5) здесь «она»)
FUNC = set("""i me my mine myself you your yours yourself he him his himself she her hers herself it its itself we us our
ours ourselves they them their theirs themselves one someone something this that these those who whom whose which what
why how when where be have a an the of to in on at by for with from into onto out up down off over under about as than
and or but not no so if there here""".split())


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def brown_ranks():
    from nltk.corpus import brown, wordnet as wn
    pos = {"NN": "n", "VB": "v", "JJ": "a", "RB": "r"}
    cnt = collections.Counter()
    for w, t in brown.tagged_words():
        p, w = pos.get(t[:2]), w.lower()
        if p and w.isalpha():
            cnt[wn.morphy(w, p) or w] += 1
    return {w: k + 1 for k, (w, _) in enumerate(cnt.most_common())}


def gloss_rank(g, ranks):
    """Ранг подсказки = худший ранг её содержательных слов; None — содержательных слов нет (скрыть всегда)."""
    from nltk.corpus import wordnet as wn
    rs = []
    for w in re.findall(r"[a-z]+", g.lower()):
        if w in FUNC:
            continue
        forms = {w} | {m for p in "nvar" if (m := wn.morphy(w, p))}
        rs.append(min(ranks.get(f, 10 ** 6) for f in forms))
    return max(rs) if rs else None


def make(sc):
    ranks = brown_ranks()
    json.dump(dict(sorted(ranks.items(), key=lambda x: x[1])[:5000]), open(D / "ranks.json", "w"), indent=0)
    mc = json.load(open(V2B2 / "codes.json"))["mc"]["sents"]
    gl = json.load(open(DIAG1 / "glosses.json"))
    gr = [[gloss_rank(g, ranks) for g in gs] for gs in gl]
    codes, cov = {}, ["# доля слов (в `{ }`) с подсказкой", ""]
    total = sum(len(x) for x in gl)
    for n in SIZES:
        codes[f"g{n}"] = [show(mc[i], gl[i], gr[i], n) for i in range(N)]
        k = sum(r is not None and r <= n for x in gr for r in x)
        cov.append(f"g{n}: {k} из {total} ({k / total:.0%})")
    k = sum(r is None for x in gr for r in x)
    cov.append(f"скрыто всегда (служебные): {k}; mcg: {total} из {total}")
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    (D / "coverage.txt").write_text("\n".join(cov) + "\n")
    print("\n".join(cov))
    spec = (V2B2 / "specs/mc_dec.md").read_text().rstrip() + "\n\n" + (D / "tasks/gloss_note.md").read_text()
    (D / "specs").mkdir(exist_ok=True)
    (D / "specs/mcl_dec.md").write_text(spec)
    task = (D.parent / "retell1/tasks/dec_sents.md").read_text()
    lists = []
    for n in SIZES:
        for k in range(1, READERS + 1):
            name = f"g{n}r{k}"
            rng = random.Random(f"lexn1-{name}")
            order = list(range(N))
            rng.shuffle(order)
            put(sc / f"read/{name}", {"spec.md": spec + "\n" + task, "sents.md": numbered(codes[f"g{n}"][i] for i in order)})
            lists.append({"r": name, "lang": f"g{n}", "order": order})
    json.dump(lists, open(sc / "lists_new.json", "w"))
    print("пример g1000:", codes["g1000"][54])


def show(code, gs, rs, n):
    it = iter(zip(gs, rs))

    def one(m):
        g, r = next(it)
        return m[0] + (f"<{g}>" if r is not None and r <= n else "")
    return re.sub(r"\{[^{}]*\}", one, code)


def readings(sc):
    old = [l for l in json.load(open(DIAG1 / "lists.json")) if l["lang"] in ("mc", "tpx", "mcg")]
    lists = old + json.load(open(sc / "lists_new.json"))
    rs = {}
    for l in lists:
        f = {"mc": V2B2 / f"answers/{l['r']}_sents_out.md", "tpx": TPX1 / f"answers/{l['r']}_sents_out.md",
             "mcg": DIAG1 / f"answers/{l['r']}_sents_out.md"}.get(l["lang"], sc / f"read/{l['r']}/sents_out.md")
        a = parse_numbered(f)
        for k, i in enumerate(l["order"]):
            rs[(l["r"], i)] = a.get(k + 1, "—")
    return lists, rs


def judges(sc):
    lists, rs = readings(sc)
    json.dump(lists, open(D / "lists.json", "w"))
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    rng = random.Random(31)
    keys = sorted(rs)
    rng.shuffle(keys)
    parts = [keys[j::JUDGES] for j in range(JUDGES)]
    pairs = []
    for j in range(1, JUDGES + 1):
        prev = parts[(j - 2) % JUDGES][:OVERLAP]
        items = [{"kind": "sent", "r": r, "i": i} for r, i in parts[j - 1]]
        items += [{"kind": "overlap", "r": r, "i": i} for r, i in prev]
        items += [{"kind": "anchor", "a": a} for a in range(len(anchors))]
        rng.shuffle(items)
        lines = []
        for t, it in enumerate(items, 1):
            it.update(j=j, t=t)
            o, rd = (anchors[it["a"]]["o"], anchors[it["a"]]["r"]) if it["kind"] == "anchor" else (SENTS[it["i"]]["s"], rs[(it["r"], it["i"])])
            lines.append(f"{t}. ORIGINAL: {o}\n   READING: {rd}\n")
        pairs += items
        put(sc / f"judge/s{j}", {"task.md": (D.parent / "retell1/tasks/judge_sents.md").read_text(), "items.md": "".join(lines)})
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    print("листы судей:", [sum(p.get("j") == j for p in pairs) for j in range(1, JUDGES + 1)])


def boot(a, b, n=5000):
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(a), (n, len(a)))
    d = (a - b)[idx].mean(1)
    return (a - b).mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)


def score(sc):
    lists, rs = readings(sc)
    pairs = json.load(open(D / "pairs.json"))
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    sj = {j: parse_numbered(sc / f"judge/s{j}/scores.md") for j in range(1, JUDGES + 1)}
    S, anc = {}, {}
    for p in pairs:
        v = sj[p["j"]].get(p["t"])
        v = int(v[0]) if v and v[0].isdigit() else None
        p["s"] = v
        if p["kind"] == "anchor":
            anc[(p["j"], p["a"])] = v
        else:
            S.setdefault((p["r"], p["i"]), []).append(v)
    per = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        per[arm] = np.array([np.mean([v for r in rr for v in S[(r, i)] if v is not None]) for i in range(N)])
    out = ["# lexn1 — результат", "", f"## Предложения (dev, {N}), смысл 0–3"]
    out += [f"  {arm}: {per[arm].mean():.2f}" for arm in ARMS]
    for a, b in [(f"g{n}", "mc") for n in SIZES] + [("g3000", "mcg"), ("g1000", "tpx"), ("mc", "tpx"), ("mcg", "tpx")]:
        d, lo, hi = boot(per[a], per[b])
        out.append(f"  {a} − {b}: {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    ov = [tuple(v) for v in S.values() if len(v) == 2 and None not in v]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судьи): " + "; ".join(
        f"{anchors[a]['want']}→" + "/".join(str(anc.get((j, a))) for j in range(1, JUDGES + 1)) for a in range(len(anchors))))
    out += ["", (D / "coverage.txt").read_text().strip()]
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        if l["lang"].startswith("g"):
            for f in ("sents.md", "sents_out.md"):
                shutil.copy(sc / f"read/{l['r']}/{f}", D / f"answers/{l['r']}_{f}")
    for j in range(1, JUDGES + 1):
        for f in ("items.md", "scores.md"):
            shutil.copy(sc / f"judge/s{j}/{f}", D / f"judge/s{j}_{f}")
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "judges": judges, "score": score}[cmd](sc)
