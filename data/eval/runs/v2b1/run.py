"""v2b1 (dec.md): v2b (v1 + шесть корней) против min-co v1 на целевом наборе roots6 (42 целевых + 18 контрольных).

Оба плеча кодируются в этом прогоне по одной процедуре (base1: Sonnet, один проход, куски по 20, целевые и контрольные вперемешку).
Рабочие папки агентов — вне репозитория (SC, например scratchpad/v2b1); итоги копируются сюда.
    .venv/bin/python data/eval/runs/v2b1/run.py make SC      → SC/enc/<плечо>_s<k>/ (6 кодировщиков)
    .venv/bin/python data/eval/runs/v2b1/run.py collect SC   → codes.json, check.txt
    .venv/bin/python data/eval/runs/v2b1/run.py readers SC   → lists.json, SC/read/<плечо><k>/ (4 слепых читателя)
    .venv/bin/python data/eval/runs/v2b1/run.py judges SC    → pairs.json, SC/judge/s1, s2
    .venv/bin/python data/eval/runs/v2b1/run.py score SC     → result.txt, answers/, judge/
"""
import json
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
R = D.parents[3]
ITEMS = R / "data/eval/items"
sys.path.insert(0, str(R / "scripts/mincode"))
ARMS = ["mc", "v2b"]
VERSION = {"mc": "v1", "v2b": "v2b"}
NEWROOTS = ["SHAPE", "OPEN", "STRONG", "TRUE", "LIGHT", "COLOR"]
CHUNK = 20
READERS = 2
OVERLAP = 30
SENTS = json.load(open(ITEMS / "roots6/sents.json"))
N = len(SENTS)
TARGET = [i for i, x in enumerate(SENTS) if x["kind"] == "target"]
CONTROL = [i for i, x in enumerate(SENTS) if x["kind"] == "control"]


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def spec(arm, kind):
    return (D / f"specs/{arm}_{kind}.md").read_text().rstrip() + "\n\n"


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def roots_in(code):
    return [r for w in re.findall(r"\{([^}|]*)\|", code) for r in re.findall(r"\b[A-Z][A-Z]+\b", re.sub(r'"[^"]*"', "", w))]


def make(sc):
    for arm in ARMS:
        for c in range(0, N, CHUNK):
            put(sc / f"enc/{arm}_s{c // CHUNK + 1}", {"spec.md": spec(arm, "enc") + (D / "tasks/enc_sents.md").read_text(),
                                                      "items.md": numbered(x["s"] for x in SENTS[c:c + CHUNK])})
    print("кодировщиков", len(list((sc / "enc").iterdir())))


def collect(sc):
    import spec as langspec
    from validator import Validator
    codes = {}
    for arm in ARMS:
        sents = []
        for c in range(0, N, CHUNK):
            got = parse_numbered(sc / f"enc/{arm}_s{c // CHUNK + 1}/codes.md")
            sents += [got.get(k + 1, "") for k in range(len(SENTS[c:c + CHUNK]))]
        codes[arm] = sents
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    for f in (sc / "enc").rglob("codes.md"):
        dst = D / "raw" / f.relative_to(sc)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(f, dst)
    out = []
    for arm in ARMS:
        v = Validator(langspec.load(version=VERSION[arm]))
        ls = codes[arm]
        bad = sum(bool([i for i in v.check_braced(x) if i.level == "error"]) for x in ls)
        quotes = sorted({q for x in ls for q in re.findall(r'"([^"]*)"', x)})
        out.append(f"{arm}: строк {len(ls)}, с ошибками правил {bad}, пустых {sum(not x for x in ls)}; "
                   f"корней на предложение {np.mean([len(roots_in(x)) for x in ls]):.1f}")
        out.append("  в кавычках: " + ", ".join(quotes))
    used = {i: [r for r in NEWROOTS if r in roots_in(codes["v2b"][i])] for i in range(N)}
    own = [i for i in TARGET if SENTS[i]["root"] in used[i]]
    out.append(f"v2b: целевых предложений, где есть свой новый корень, {len(own)} из {len(TARGET)}; с любым новым корнем — "
               f"целевых {sum(bool(used[i]) for i in TARGET)}, контрольных {sum(bool(used[i]) for i in CONTROL)} из {len(CONTROL)}")
    out.append("  по корням (свой корень в целевых): " + ", ".join(
        f"{r} {sum(1 for i in TARGET if SENTS[i]['root'] == r and r in used[i])}/{sum(1 for i in TARGET if SENTS[i]['root'] == r)}" for r in NEWROOTS))
    (D / "check.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def readers(sc):
    codes = json.load(open(D / "codes.json"))
    lists = []
    for arm in ARMS:
        for k in range(1, READERS + 1):
            rng = random.Random(f"v2b1-{arm}{k}")
            order = list(range(N))
            rng.shuffle(order)
            name = f"{arm}{k}"
            lists.append({"r": name, "lang": arm, "order": order})
            put(sc / f"read/{name}", {"spec.md": spec(arm, "dec") + (D / "tasks/dec_sents.md").read_text(),
                                      "sents.md": numbered(codes[arm][i] or "(no code)" for i in order)})
    json.dump(lists, open(D / "lists.json", "w"))
    print(len(lists), "читателей")


def readings(sc):
    lists = json.load(open(D / "lists.json"))
    rs = {}
    for l in lists:
        a = parse_numbered(sc / f"read/{l['r']}/sents_out.md")
        for k, i in enumerate(l["order"]):
            rs[(l["r"], i)] = a.get(k + 1, "—")
    return lists, rs


def judges(sc):
    lists, rs = readings(sc)
    anchors = json.load(open(ITEMS / "bench1/judge_anchors.json"))
    rng = random.Random(17)
    keys = sorted(rs)
    rng.shuffle(keys)
    parts = [keys[0::2], keys[1::2]]
    pairs = []
    for j in (1, 2):
        items = [{"kind": "sent", "r": r, "i": i} for r, i in parts[j - 1]]
        items += [{"kind": "overlap", "r": r, "i": i} for r, i in parts[2 - j][:OVERLAP // 2]]
        items += [{"kind": "anchor", "a": a} for a in range(len(anchors))]
        rng.shuffle(items)
        lines = []
        for t, it in enumerate(items, 1):
            it.update(j=j, t=t)
            o, rd = (anchors[it["a"]]["o"], anchors[it["a"]]["r"]) if it["kind"] == "anchor" else (SENTS[it["i"]]["s"], rs[(it["r"], it["i"])])
            lines.append(f"{t}. ORIGINAL: {o}\n   READING: {rd}\n")
        pairs += items
        put(sc / f"judge/s{j}", {"task.md": (D / "tasks/judge_sents.md").read_text(), "items.md": "".join(lines)})
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    print("листы судей:", [sum(p["j"] == j for p in pairs) for j in (1, 2)])


def boot(a, b, n=5000):
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(a), (n, len(a)))
    d = (a - b)[idx].mean(1)
    return (a - b).mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)


def score(sc):
    lists, rs = readings(sc)
    pairs = json.load(open(D / "pairs.json"))
    anchors = json.load(open(ITEMS / "bench1/judge_anchors.json"))
    sj = {j: parse_numbered(sc / f"judge/s{j}/scores.md") for j in (1, 2)}
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
    out = ["# v2b1 — результат", "", f"## Предложения roots6 ({N}: {len(TARGET)} целевых, {len(CONTROL)} контрольных), смысл 0–3"]
    for name, idx in (("целевые", TARGET), ("контрольные", CONTROL), ("все", list(range(N)))):
        a, b = per["v2b"][idx], per["mc"][idx]
        d, lo, hi = boot(a, b)
        out.append(f"  {name}: mc {b.mean():.2f}, v2b {a.mean():.2f}; v2b − mc {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    dt = per["v2b"][TARGET] - per["mc"][TARGET]
    dc = per["v2b"][CONTROL] - per["mc"][CONTROL]
    rng = np.random.default_rng(0)
    bs = [rng.choice(dt, len(dt)).mean() - rng.choice(dc, len(dc)).mean() for _ in range(5000)]
    out.append(f"  (целевые − контрольные) по разнице v2b − mc: {dt.mean() - dc.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]")
    codes = json.load(open(D / "codes.json"))
    own = [i for i in TARGET if SENTS[i]["root"] in roots_in(codes["v2b"][i])]
    notown = [i for i in TARGET if i not in own]
    out.append(f"  целевые, где v2b употребил свой корень ({len(own)}): v2b − mc {np.mean(per['v2b'][own] - per['mc'][own]):+.2f}; "
               f"без него ({len(notown)}): {np.mean(per['v2b'][notown] - per['mc'][notown]) if notown else float('nan'):+.2f}")
    out.append("  по корням (mc → v2b): " + "; ".join(
        f"{r} {np.mean([per['mc'][i] for i in TARGET if SENTS[i]['root'] == r]):.1f}→{np.mean([per['v2b'][i] for i in TARGET if SENTS[i]['root'] == r]):.1f}" for r in NEWROOTS))
    ov = [tuple(v) for v in S.values() if len(v) == 2 and None not in v]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судьи 1/2): " + "; ".join(f"{anchors[a]['want']}→{anc.get((1, a))}/{anc.get((2, a))}" for a in range(len(anchors))))
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        for f in ("sents.md", "sents_out.md"):
            shutil.copy(sc / f"read/{l['r']}/{f}", D / f"answers/{l['r']}_{f}")
    for j in ("s1", "s2"):
        for f in ("items.md", "scores.md"):
            shutil.copy(sc / f"judge/{j}/{f}", D / f"judge/{j}_{f}")
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "collect": collect, "readers": readers, "judges": judges, "score": score}[cmd](sc)
