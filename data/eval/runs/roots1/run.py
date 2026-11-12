"""roots1 (dec.md): "learn X roots → how surely is a word guessed", min-co with 10 / 20 / 30 roots and v2c (51), next to v2b (51).

Same 120 words and protocol as size1: each encoder writes three codes per word (1 word, ≤ 2, ≤ 3 words); readers get
Latin-square lists (each word once, in one of the three variants). Arms:
  R10, R20, R30 — the v2b spec with only the X most used roots (ranked by use in the 1000 big1000 codes; [rank.json]);
  V2C — the v2c roots (whole-range anchors) and scale paragraph (as axes1 arm A);
  V2B — size1's own min-co readings (readers mc1a, mc2a, mc3a), re-judged here so that all arms share the same judges.
2 Sonnet encoders and 3 Haiku readers per new arm; 5 Sonnet judges, every answer scored by 2.
    .venv/bin/python data/eval/runs/roots1/run.py make SC     → specs/, SC/w/*
    .venv/bin/python data/eval/runs/roots1/run.py readers SC  → codes.json, lists.json, SC/r/*
    .venv/bin/python data/eval/runs/roots1/run.py judges SC   → SC/j/*
    .venv/bin/python data/eval/runs/roots1/run.py score SC    → result.txt, points.json, answers/
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
RUNS = D.parent
S1 = RUNS / "size1"
ROOT = D.parents[3]
ITEMS = json.load(open(S1 / "items.json"))
NW = len(ITEMS)
RANK = json.load(open(D / "rank.json"))
NEW = ["R10", "R20", "R30", "V2C"]
ARMS = NEW + ["V2B"]
NROOTS = {"R10": 10, "R20": 20, "R30": 30, "V2C": 51, "V2B": 51}
KS = (1, 2, 3)
JUDGES = 5


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def section(s, head, nxt):
    a = s.index(head)
    return a, s.index(nxt, a + len(head))


def spec(arm, kind):
    s = (S1 / f"specs/mc_{kind}.md").read_text()
    if arm == "V2C":
        a, b = section(s, "A root may carry a value", "## Roots (51)")
        s = s[:a] + (RUNS / "axes1/tasks/scale_v2c.md").read_text().strip() + "\n\n" + s[b:]
        a, b = section(s, "## Roots (51)\n", "\n## Form marks")
        return s[:a] + "## Roots (51)\n\n" + (ROOT / "lang/v2c/roots_en.md").read_text().strip() + "\n" + s[b:]
    n = NROOTS[arm]
    keep = set(RANK[:n])
    a, b = section(s, "## Roots (51)\n", "\n## Form marks")
    lines = [x for x in s[a:b].splitlines() if not (m := re.match(r"- ([A-Z]+):", x)) or m[1] in keep]
    body = "\n".join(lines).replace("## Roots (51)", f"## Roots ({n})")
    body += (f"\n\nOnly these {n} roots exist. Examples elsewhere in this spec may use other roots — those are not available; "
             f"build every meaning from the {n} roots above, roles and phrases.\n")
    s = s[:a] + body + s[b:]
    return s.replace("Use ONLY the 51 roots below", f"Use ONLY the {n} roots below")


def make(sc):
    (D / "specs").mkdir(exist_ok=True)
    for arm in NEW:
        for kind in ("enc", "dec"):
            (D / f"specs/{arm}_{kind}.md").write_text(spec(arm, kind))
        for k in (1, 2):
            part = ITEMS[(k - 1) * 60:k * 60]
            put(sc / f"w/{arm}{k}", {"spec.md": spec(arm, "enc"),
                                     "list.md": numbered(f"{x['w']} ({x['pos']}): {x['gloss']}" for x in part)})
    print("encoders:", 2 * len(NEW))


def readers(sc):
    codes = {}
    for arm in NEW:
        rows = []
        for k in (1, 2):
            a = parse_numbered(sc / f"w/{arm}{k}/answers.md")
            assert len(a) == 60, (arm, k, len(a))
            for i in range(1, 61):
                v = [x.strip().strip("`") for x in a[i].split("||")]
                assert len(v) == 3, (arm, k, i, a[i])
                rows.append(v)
        codes[arm] = rows
        bad = [(i, w) for i, v in enumerate(rows) for c in v for w in re.findall(r"\b([A-Z]{2,})\b", c)
               if w not in RANK and w not in ("FROM", "FOR", "AGAINST", "LIKE", "PI", "AND")]
        if arm != "V2C":
            bad = [(i, w) for i, v in enumerate(rows) for c in v for w in re.findall(r"\b([A-Z]{2,})\b", c)
                   if w in RANK and w not in RANK[:NROOTS[arm]]]
        print(arm, "roots outside the list:", len(bad), bad[:8])
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    lists = []
    for arm in NEW:
        for s in range(3):
            rid = f"{arm}_{s + 1}"
            rng = random.Random(f"roots1-{rid}")
            order = [(i, (i + s) % 3 + 1) for i in range(NW)]
            rng.shuffle(order)
            put(sc / f"r/{rid}", {"spec.md": spec(arm, "dec"), "codes.md": numbered(codes[arm][i][k - 1] for i, k in order)})
            lists.append({"r": rid, "arm": arm, "order": order})
    s1 = {l["r"]: l for l in json.load(open(S1 / "lists.json"))}
    for s in range(3):
        l = s1[f"mc{s + 1}a"]
        lists.append({"r": f"V2B_{s + 1}", "arm": "V2B", "order": l["order"], "src": f"mc{s + 1}a"})
    json.dump(lists, open(D / "lists.json", "w"))


def answers(sc):
    out = {}
    for l in json.load(open(D / "lists.json")):
        path = S1 / f"answers/read_{l['src']}.md" if "src" in l else sc / f"r/{l['r']}/answers.md"
        a = parse_numbered(path)
        for t, (i, k) in enumerate(l["order"], 1):
            out[(l["r"], i, k)] = a.get(t, "—").split("|")[0].strip()
    return out


def judges(sc):
    ans = answers(sc)
    keys = sorted(ans)
    random.Random(53).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    parts = [keys[j::JUDGES] for j in range(JUDGES)]
    for j in range(JUDGES):
        ks = parts[j] + parts[(j + 1) % JUDGES]
        random.Random(f"r1j{j}").shuffle(ks)
        lines = [f"{t}. {ITEMS[i]['w']} ({ITEMS[i]['pos']}: {ITEMS[i]['gloss']}) — {ans[(r, i, k)]}" for t, (r, i, k) in enumerate(ks, 1)]
        put(sc / f"j/j{j + 1}", {"task.md": (S1 / "tasks/judge.md").read_text(), "items.md": "\n".join(lines) + "\n",
                                 "keys.json": json.dumps([list(x) for x in ks])})
    print("answers:", len(keys), "; per judge:", len(parts[0]) * 2)


def score(sc):
    ans = answers(sc)
    lists = json.load(open(D / "lists.json"))
    S = collections.defaultdict(list)
    for j in range(1, JUDGES + 1):
        ks = [tuple(x) for x in json.loads((sc / f"j/j{j}/keys.json").read_text())]
        s = parse_numbered(sc / f"j/j{j}/scores.md")
        for t, key in enumerate(ks, 1):
            if t in s and s[t][:1].isdigit():
                S[key].append(int(s[t][0]))
    band = np.array([x["band"] for x in ITEMS])
    bands = sorted(set(band))
    out = ["# roots1 — result", "", "## Close (judge 2 of 0–2), 120 words, first answer; 3 readers × 2 judges per cell", "",
           "| arm (roots) | 1 word | ≤ 2 words | ≤ 3 words |", "|---|---|---|---|"]
    close, pts = {}, []
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["arm"] == arm]
        for k in KS:
            close[(arm, k)] = np.array([np.mean([v == 2 for r in rr for v in S.get((r, i, k), [])] or [np.nan]) for i in range(NW)])
        out.append(f"| {arm} ({NROOTS[arm]}) | " + " | ".join(f"{np.nanmean(close[(arm, k)]):.0%}" for k in KS) + " |")
    # token-weighted like size1's U at N = 0: band accuracy × band token share (shares from size1 curve inputs)
    shares = json.load(open(D / "band_shares.json"))
    for arm in ARMS:
        for k in KS:
            u = sum(shares[str(b)] * np.nanmean(close[(arm, k)][band == b]) for b in bands)
            pts.append({"arm": arm, "X": NROOTS[arm], "k": k, "U": u, "close": float(np.nanmean(close[(arm, k)]))})
    out += ["", "## Token-weighted (as size1's U at N = 0)", ""] + [f"  {p['arm']} k{p['k']}: {p['U']:.0%}" for p in pts]
    rng = np.random.default_rng(0)
    idx = rng.integers(0, NW, (5000, NW))
    out += ["", "## Paired differences vs V2B, ≤ 3 words, pp [95 % bootstrap over words]"]
    for arm in NEW:
        d = close[(arm, 3)] - close[("V2B", 3)]
        bd = np.nanmean(d[idx], 1)
        out.append(f"  {arm} − V2B: {100 * np.nanmean(d):+.1f} [{100 * np.percentile(bd, 2.5):+.1f} … {100 * np.percentile(bd, 97.5):+.1f}]")
    both = [tuple(v) for v in S.values() if len(v) == 2]
    out.append(f"\nJudges: exact agreement {np.mean([a == b for a, b in both]):.0%} on {len(both)} answers")
    codes = json.load(open(D / "codes.json"))
    nr = lambda c: sum(len(re.findall(r"\b[A-Z]{2,}\b", w.split("|")[0])) for w in (re.findall(r"\{([^{}]*)\}", c) or [c]))
    out += ["", "## Roots per code"] + [f"  {arm}: " + " / ".join(f"{np.mean([nr(v[k - 1]) for v in codes[arm]]):.2f}" for k in KS)
                                        for arm in NEW]
    json.dump(pts, open(D / "points.json", "w"), indent=0)
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        if "src" not in l:
            shutil.copy(sc / f"r/{l['r']}/answers.md", D / f"answers/read_{l['r']}.md")
    for arm in NEW:
        for k in (1, 2):
            shutil.copy(sc / f"w/{arm}{k}/answers.md", D / f"answers/write_{arm}{k}.md")
    for j in range(1, JUDGES + 1):
        shutil.copy(sc / f"j/j{j}/scores.md", D / f"answers/judge_j{j}.md")
        shutil.copy(sc / f"j/j{j}/keys.json", D / f"answers/judge_j{j}_keys.json")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
