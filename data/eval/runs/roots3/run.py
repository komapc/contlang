"""roots3 (dec.md): v2c with exactly 4 or 5 roots per code, at X = 10, 30, 51, 100, 300 roots — next to roots2 (up to 3 words,
free number of roots) re-judged in the same batch, and PCA with 4 / 5 values.

Specs are roots2's (same roots, same word roots above 51); only the encoder task changes: ONE code, ≤ 3 words, EXACTLY N roots
in total (each word still ≤ 3 roots). Readers get roots2's decoder spec unchanged. 2 Sonnet encoders (60 words each) and
2 Haiku readers (all 120) per arm; the roots2 answers for the same X (arm N3) are re-judged with the new ones; 10 Sonnet
judges, every answer scored by 2.
    .venv/bin/python data/eval/runs/roots3/run.py make SC    → specs/, SC/w/*
    .venv/bin/python data/eval/runs/roots3/run.py readers SC → codes.json, lists.json, SC/r/*
    .venv/bin/python data/eval/runs/roots3/run.py judges SC  → SC/j/*
    .venv/bin/python data/eval/runs/roots3/run.py score SC   → result.txt, points.json, answers/
"""
import collections
import importlib.util
import json
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
RUNS = D.parent
R2D = RUNS / "roots2"
spc = importlib.util.spec_from_file_location("roots2run", R2D / "run.py")
r2 = importlib.util.module_from_spec(spc)
spc.loader.exec_module(r2)
r1 = r2.r1
ITEMS, NW, RANK = r2.ITEMS, r2.NW, r2.RANK
XS = (10, 30, 51, 100, 300)
NS = (4, 5)
NEW = [f"X{x}N{n}" for x in XS for n in NS]
JUDGES = 10


def task(n):
    return (D / "tasks/write.md").read_text().replace("{N}", str(n))


def enc_spec(x, n):
    s = r2.spec(x, "enc")
    return s[:s.index("## Task")] + task(n)


def nroots(c):
    return sum(len(re.findall(r"\b[A-Z]{2,}\b", w.split("|")[0])) for w in (re.findall(r"\{([^{}]*)\}", c) or [c]))


def make(sc):
    (D / "specs").mkdir(exist_ok=True)
    for x in XS:
        for n in NS:
            (D / f"specs/X{x}N{n}_enc.md").write_text(enc_spec(x, n))
            for k in (1, 2):
                part = ITEMS[(k - 1) * 60:k * 60]
                r1.put(sc / f"w/X{x}N{n}_{k}", {"spec.md": enc_spec(x, n),
                                                 "list.md": r1.numbered(f"{it['w']} ({it['pos']}): {it['gloss']}" for it in part)})


def readers(sc):
    codes = {}
    for arm in NEW:
        x, n = map(int, arm[1:].split("N"))
        rows = []
        for k in (1, 2):
            a = r1.parse_numbered(sc / f"w/{arm}_{k}/answers.md")
            assert len(a) == 60, (arm, k, len(a))
            rows += [a[i].strip().strip("`") for i in range(1, 61)]
        codes[arm] = rows
        allowed = set(RANK[:min(x, 51)]) | {r["w"].upper() for r in r2.word_roots()[:max(0, x - 51)]}
        bad = [(i, w) for i, c in enumerate(rows) for w in re.findall(r"\b([A-Z]{2,})\b", c)
               if w not in allowed and w.lower() not in r2.LINKS]
        cnt = collections.Counter(nroots(c) for c in rows)
        print(arm, "outside list:", len(bad), bad[:6], "; roots per code:", dict(sorted(cnt.items())))
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    lists = []
    for arm in NEW:
        x = int(arm[1:].split("N")[0])
        for s in (1, 2):
            rid = f"{arm}_{s}"
            order = list(range(NW))
            random.Random(f"roots3-{rid}").shuffle(order)
            r1.put(sc / f"r/{rid}", {"spec.md": r2.spec(x, "dec"), "codes.md": r1.numbered(codes[arm][i] for i in order)})
            lists.append({"r": rid, "arm": arm, "order": order})
    for l in json.load(open(R2D / "lists.json")):
        x = int(l["arm"][1:])
        if x in XS:
            lists.append({"r": f"X{x}N3_{l['r'][-1]}", "arm": f"X{x}N3", "order": l["order"], "src": l["r"]})
    json.dump(lists, open(D / "lists.json", "w"))


def answers(sc):
    out = {}
    for l in json.load(open(D / "lists.json")):
        path = R2D / f"answers/read_{l['src']}.md" if "src" in l else sc / f"r/{l['r']}/answers.md"
        a = r1.parse_numbered(path)
        for t, i in enumerate(l["order"], 1):
            out[(l["r"], i)] = a.get(t, "—").split("|")[0].strip()
    return out


def judges(sc):
    ans = answers(sc)
    keys = sorted(ans)
    random.Random(71).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    parts = [keys[j::JUDGES] for j in range(JUDGES)]
    for j in range(JUDGES):
        ks = parts[j] + parts[(j + 1) % JUDGES]
        random.Random(f"r3j{j}").shuffle(ks)
        lines = [f"{t}. {ITEMS[i]['w']} ({ITEMS[i]['pos']}: {ITEMS[i]['gloss']}) — {ans[(r, i)]}" for t, (r, i) in enumerate(ks, 1)]
        r1.put(sc / f"j/j{j + 1}", {"task.md": (RUNS / "size1/tasks/judge.md").read_text(), "items.md": "\n".join(lines) + "\n",
                                    "keys.json": json.dumps([list(k) for k in ks])})
    print("answers:", len(keys), "; per judge:", 2 * len(parts[0]))


def score(sc):
    lists = json.load(open(D / "lists.json"))
    S = collections.defaultdict(list)
    for j in range(1, JUDGES + 1):
        ks = [tuple(k) for k in json.loads((sc / f"j/j{j}/keys.json").read_text())]
        s = r1.parse_numbered(sc / f"j/j{j}/scores.md")
        for t, key in enumerate(ks, 1):
            if t in s and s[t][:1].isdigit():
                S[key].append(int(s[t][0]))
    band = np.array([it["band"] for it in ITEMS])
    bands = sorted(set(band))
    shares = json.load(open(RUNS / "roots1/band_shares.json"))
    rng = np.random.default_rng(0)
    boot = [np.concatenate([rng.choice(np.flatnonzero(band == b), (band == b).sum()) for b in bands]) for _ in range(2000)]
    U = lambda v: sum(shares[str(b)] * np.nanmean(v[band == b]) for b in bands)
    close = {}
    for arm in sorted({l["arm"] for l in lists}):
        rr = [l["r"] for l in lists if l["arm"] == arm]
        close[arm] = np.array([np.mean([s == 2 for r in rr for s in S.get((r, i), [])] or [np.nan]) for i in range(NW)])
    out = ["# roots3 — result (v2c; N3 = roots2 codes, free number of roots; N4 / N5 = exactly 4 / 5 roots)", "",
           "| roots X | N3 (roots2) | N4 | N5 | N4 − N3, pp [95 %] | N5 − N3, pp [95 %] |", "|---|---|---|---|---|---|"]
    pts = []
    for x in XS:
        row = [f"| {x} "]
        for n in (3, 4, 5):
            v = close[f"X{x}N{n}"]
            bu = [U(v[ix]) if False else sum(shares[str(b)] * np.nanmean(v[ix][band[ix] == b]) for b in bands) for ix in boot]
            lo, hi = np.percentile(bu, [2.5, 97.5])
            pts.append({"X": x, "N": n, "U": float(U(v)), "lo": float(lo), "hi": float(hi), "close": float(np.nanmean(v))})
            row.append(f"| {U(v):.0%} [{lo:.0%} … {hi:.0%}] ")
        for n in (4, 5):
            d = close[f"X{x}N{n}"] - close[f"X{x}N3"]
            bd = [np.nanmean(d[ix]) for ix in boot]
            row.append(f"| {100 * np.nanmean(d):+.1f} [{100 * np.percentile(bd, 2.5):+.1f} … {100 * np.percentile(bd, 97.5):+.1f}] ")
        out.append("".join(row) + "|")
    out.append("\n(cells: token-weighted U [95 % bootstrap]; differences: unweighted close, paired over words)")
    both = [tuple(v) for v in S.values() if len(v) == 2]
    out.append(f"\nJudges: exact agreement {np.mean([a == b for a, b in both]):.0%} on {len(both)} answers")
    codes = json.load(open(D / "codes.json"))
    out += ["", "## Roots per code (N4 / N5 arms)"] + [f"  {a}: " + str(dict(sorted(collections.Counter(nroots(c) for c in codes[a]).items())))
                                                      for a in NEW]
    json.dump(pts, open(D / "points.json", "w"), indent=0)
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        if "src" not in l:
            shutil.copy(sc / f"r/{l['r']}/answers.md", D / f"answers/read_{l['r']}.md")
    for arm in NEW:
        for k in (1, 2):
            shutil.copy(sc / f"w/{arm}_{k}/answers.md", D / f"answers/write_{arm}_{k}.md")
    for j in range(1, JUDGES + 1):
        shutil.copy(sc / f"j/j{j}/scores.md", D / f"answers/judge_j{j}.md")
        shutil.copy(sc / f"j/j{j}/keys.json", D / f"answers/judge_j{j}_keys.json")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
