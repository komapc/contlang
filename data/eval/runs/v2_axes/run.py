"""Пилот осей (dec.md): читаются ли промежуточные значения оси, если читатель знает только полюса.

    .venv/bin/python data/eval/runs/v2_axes/run.py make     → codes.json, t1..t3/ (карточка, коды, задание читателя)
    .venv/bin/python data/eval/runs/v2_axes/run.py judges   → pairs.json, u1..u2/ (пары для судей)
    .venv/bin/python data/eval/runs/v2_axes/run.py score    → result.txt
Папки t*/ и u*/ — рабочие (агенты пишут туда answers.md и scores.md); итоги копируются в answers/ и judge/.
"""
import json
import random
import re
import sys
from pathlib import Path

import numpy as np
import yaml

D = Path(__file__).resolve().parent
R = D.parents[3]
VALUES = [-4, -2, 0, 2, 4]
READERS, JUDGES = 3, 2
TYPES = {
    "степень": "GOOD BIG ABOVE HEAT WANT FRIEND CARE JOIN TOUCH MOVE SAY FEEL CAN CHANGE MOOD TIME INSIDE NEAR",
    "смешанная": "MANY VALUE SIDE LIVE SAME",
    "лестница": "GRAIN THING LONG LAND FIGHT MEASURE SOMEONE PART KNOW GIVE BEGIN CONSUME ART THINK RULE",
}  # SEX не берётся: у него нет середины (допустимы только ±3…±5)
TYPE = {r: t for t, s in TYPES.items() for r in s.split()}
fmt = lambda v: f"{v:+d}" if v else "0"


def axis_parts(text):
    """'-5 a, b … 0 c … +5 d (note)' → {-5: 'a, b', 0: 'c', 5: 'd'}"""
    text = re.sub(r"\s*\((?:[^()]|\([^)]*\))*\)", "", text)
    out = {}
    for seg in text.split("…"):
        m = re.match(r"\s*([+-]?\d)\s+(.+)", seg)
        if m:
            out[int(m[1])] = m[2].strip(" ,;")
    return out


def make():
    doc = yaml.safe_load(open(R / "roots.yaml"))
    axes = {r["name"]: axis_parts(r["en_axis"]) for r in doc["roots"] if r["name"] in TYPE}
    assert len(axes) == len(TYPE) == 38, len(axes)
    card = ["# min-co axis card", "",
            "Each code is a min-co ROOT with a value on its axis: `ROOT(=v)`, v from -5 to +5.",
            "Only the two ends of each axis are given. 0 is the middle of the axis; values between are positions between the ends",
            "(±2 a little toward that end, ±4 close to that end).", ""]
    for r in sorted(axes):
        lo, hi = min(axes[r]), max(axes[r])
        card.append(f"- {r}: {fmt(lo)} {axes[r][lo]} … {fmt(hi)} {axes[r][hi]}")
    codes = [{"root": r, "v": v, "code": f"{r}(={fmt(v)})", "type": TYPE[r], "anchor": axes[r].get(v) if v not in (min(axes[r]), max(axes[r])) else None} for r in sorted(axes) for v in VALUES]
    json.dump(codes, open(D / "codes.json", "w"), ensure_ascii=False, indent=1)
    task = open(D / "reader_task.md").read()
    lists = []
    for t in range(1, READERS + 1):
        order = list(range(len(codes)))
        random.Random(100 + t).shuffle(order)
        lists.append(order)
        (D / f"t{t}").mkdir(exist_ok=True)
        (D / f"t{t}/card.md").write_text("\n".join(card) + "\n")
        (D / f"t{t}/task.md").write_text(task)
        (D / f"t{t}/codes.md").write_text("".join(f"{k + 1}. {codes[i]['code']}\n" for k, i in enumerate(order)))
    json.dump(lists, open(D / "lists.json", "w"))
    print(len(codes), "кодов,", sum(c["anchor"] is not None for c in codes), "с опорой в roots.yaml,", READERS, "читателя")


def readings():
    codes, lists = json.load(open(D / "codes.json")), json.load(open(D / "lists.json"))
    rd = {}
    for t, order in enumerate(lists, 1):
        ans = {int(m[1]): m[2].split("|")[0].strip() for x in open(D / f"t{t}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
        for k, i in enumerate(order):
            rd[(t, i)] = ans.get(k + 1, "—")
    return codes, rd


def judges():
    codes, rd = readings()
    pairs = []
    for i, c in enumerate(codes):
        for a in range(1, READERS + 1):
            for b in range(a + 1, READERS + 1):
                pairs.append({"kind": "agree", "i": i, "a": a, "b": b, "x": rd[(a, i)], "y": rd[(b, i)]})
            if c["anchor"]:
                pairs.append({"kind": "anchor", "i": i, "a": a, "x": c["anchor"], "y": rd[(a, i)]})
    rng = random.Random(9)
    rng.shuffle(pairs)
    for p in pairs:
        if rng.random() < 0.5:
            p["x"], p["y"] = p["y"], p["x"]
    per = -(-len(pairs) // JUDGES)
    task = open(D / "judge_task.md").read()
    for j in range(JUDGES):
        ch = pairs[j * per:(j + 1) * per]
        for t, p in enumerate(ch, 1):
            p["j"], p["t"] = j + 1, t
        (D / f"u{j + 1}").mkdir(exist_ok=True)
        (D / f"u{j + 1}/task.md").write_text(task)
        (D / f"u{j + 1}/pairs.md").write_text("".join(f"{p['t']}. A: {p['x']}  ||  B: {p['y']}\n" for p in ch))
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    print(len(pairs), "пар,", JUDGES, "судьи")


def score():
    codes, rd = readings()
    pairs = json.load(open(D / "pairs.json"))
    sc = {}
    for j in range(1, JUDGES + 1):
        sc[j] = {int(m[1]): int(m[2]) for x in open(D / f"u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([0-2])", x))}
    for p in pairs:
        p["s"] = sc[p["j"]].get(p["t"])
    miss = sum(p["s"] is None for p in pairs)
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for t in range(1, READERS + 1):
        (D / f"answers/t{t}.md").write_text((D / f"t{t}/codes.md").read_text() + "---\n" + (D / f"t{t}/answers.md").read_text())
    for j in range(1, JUDGES + 1):
        (D / f"judge/u{j}.md").write_text((D / f"u{j}/pairs.md").read_text() + "---\n" + (D / f"u{j}/scores.md").read_text())
    agree = {}  # корень → доли «близко» по парам читателей
    for p in pairs:
        if p["kind"] == "agree" and p["s"] is not None:
            agree.setdefault(codes[p["i"]]["root"], []).append(p["s"] == 2)
    root_ag = {r: float(np.mean(v)) for r, v in agree.items()}
    out = [f"пар {len(pairs)}, без оценки {miss}", "", "согласие читателей (доля пар «близко»), среднее по корням:"]
    by = {t: np.array([root_ag[r] for r in s.split() if r in root_ag]) for t, s in TYPES.items()}
    for t, a in by.items():
        out.append(f"  {t:10s} n {len(a):2d}  {a.mean():.0%}")
    rng = np.random.default_rng(0)
    deg, lad = by["степень"], by["лестница"]
    bs = [rng.choice(deg, len(deg)).mean() - rng.choice(lad, len(lad)).mean() for _ in range(5000)]
    diff = deg.mean() - lad.mean()
    lo, hi = np.percentile(bs, [2.5, 97.5])
    out.append(f"степень − лестница: {diff * 100:+.1f} п. п. [{lo * 100:+.1f} … {hi * 100:+.1f}]")
    ok = diff >= 0.15 and lo > 0
    out.append("критерий (≥ +15 п. п., нижняя граница > 0): " + ("ВЫПОЛНЕН — деление подтверждено" if ok else "не выполнен"))
    out += ["", "по значению (все корни):"]
    for v in VALUES:
        a = [p["s"] == 2 for p in pairs if p["kind"] == "agree" and p["s"] is not None and codes[p["i"]]["v"] == v]
        out.append(f"  {fmt(v):>3s}  {np.mean(a):.0%}")
    anc = [p for p in pairs if p["kind"] == "anchor" and p["s"] is not None]
    out += ["", f"опоры roots.yaml, угаданные по полюсам (доля «близко»): {np.mean([p['s'] == 2 for p in anc]):.0%} из {len(anc)} прочтений"]
    for p in sorted(anc, key=lambda p: (codes[p["i"]]["code"], p["a"])):
        c = codes[p["i"]]
        out.append(f"  {c['code']:14s} опора «{c['anchor']}» — {rd[(p['a'], p['i'])]}: {p['s']}")
    out += ["", "корни по согласию (тип; прочтения −4 / −2 / 0 / +2 / +4 у читателя 1):"]
    for r in sorted(root_ag, key=root_ag.get):
        reads = " / ".join(rd[(1, i)] for i, c in enumerate(codes) if c["root"] == r)
        out.append(f"  {r:8s} {root_ag[r]:4.0%}  {TYPE[r]:10s} {reads}")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


{"make": make, "judges": judges, "score": score}[sys.argv[1]]()
