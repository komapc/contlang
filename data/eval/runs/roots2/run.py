"""roots2 (dec.md): the v2c curve "learn X roots → how surely is a word guessed", X = 1 … 300, one protocol, one judging.

X ≤ 51: the v2c spec with only its X most used roots (order of roots1/rank.json).
X > 51: all 51 v2c roots + (X − 51) word roots: the most frequent Brown content lemmas (size1 order), skipping lemmas that are
already a root name or a link word, adverbs, and inflected forms (WordNet morphy finds another base); a word root means just that English word and takes no value.
Each encoder writes ONE code (≤ 3 words) per word; 2 Sonnet encoders (60 words each) and 2 Haiku readers (all 120 codes,
own shuffle) per arm; 6 Sonnet judges, every answer scored by 2.
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/roots2/run.py make SC   → word_roots.json, specs/, leak.txt, SC/w/*
    .venv/bin/python data/eval/runs/roots2/run.py readers SC → codes.json, lists.json, SC/r/*
    .venv/bin/python data/eval/runs/roots2/run.py judges SC  → SC/j/*
    .venv/bin/python data/eval/runs/roots2/run.py score SC   → result.txt, points.json, answers/
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
sys.path.insert(0, str(RUNS / "roots1"))
import run as r1  # noqa: E402

ITEMS = r1.ITEMS
NW = len(ITEMS)
RANK = r1.RANK
XS = (1, 3, 10, 20, 30, 51, 100, 200, 300)
ARMS = [f"X{x}" for x in XS]
JUDGES = 6
LINKS = {"from", "for", "against", "like", "pi", "and"}
WR_NOTE = ("\n\nRoots after COLOR are **word roots**: each means just that English word (in any of its common senses) and "
           "takes no value. Combine them, give them roles and FORM marks like any other root.\n")


def word_roots():
    p = D / "word_roots.json"
    if p.exists():
        return json.load(open(p))
    import importlib.util
    spc = importlib.util.spec_from_file_location("size1run", S1 / "run.py")
    m = importlib.util.module_from_spec(spc)
    spc.loader.exec_module(m)
    brown_counts = m.brown_counts
    from nltk.corpus import wordnet as wn
    c = brown_counts()
    tot = {w: sum(v.values()) for w, v in c.items()}
    order = sorted(tot, key=lambda w: -tot[w])
    names = {x.lower() for x in RANK}
    out = []
    for w in order:
        if len(out) == 300 - 51:
            break
        if w in names or w in LINKS or len(w) < 2:
            continue
        pos = c[w].most_common(1)[0][0]
        if pos == "r" or set(wn._morphy(w, pos)) - {w} or not wn.synsets(w, pos):  # adverbs; inflected forms (years, men, felt, af)
            continue
        ss = wn.synsets(w, pos={"n": "n", "v": "v", "a": "a", "r": "r"}[pos]) or wn.synsets(w)
        out.append({"w": w, "pos": pos, "gloss": ss[0].definition() if ss else ""})
    json.dump(out, open(p, "w"), indent=0)
    return out


def spec(x, kind):
    s = r1.spec("V2C", kind)
    a, b = r1.section(s, "## Roots (51)\n", "\n## Form marks")
    lines = s[a:b].strip().splitlines()[1:]
    if x <= 51:
        keep = set(RANK[:x])
        lines = [y for y in lines if not (m := re.match(r"- ([A-Z]+):", y)) or m[1] in keep]
        tail = (f"\n\nOnly these {x} roots exist. Examples elsewhere in this spec may use other roots — those are not available; "
                f"build every meaning from the {x} roots above, roles and phrases.\n")
    else:
        lines += [f"- {r['w'].upper()}: {r['w']} — {r['gloss']}" for r in word_roots()[:x - 51]]
        tail = WR_NOTE
    body = f"## Roots ({x})\n\n" + "\n".join(y for y in lines if y.strip()) + tail
    s = s[:a] + body + s[b:]
    s = s.replace("Use ONLY the 51 roots below", f"Use ONLY the {x} roots below")
    if kind == "enc":
        s = s[:s.index("## Task")] + (D / "tasks/write.md").read_text()
    return s


def make(sc):
    names = set(re.findall(r"^- ([A-Z]+):", (r1.ROOT / "lang/v2c/roots_en.md").read_text(), re.M))
    assert names == set(RANK), names ^ set(RANK)
    wr = [r["w"] for r in word_roots()]
    leak = ["Targets that are themselves a root (fixed before codes):", ""]
    band = collections.Counter(x["band"] for x in ITEMS)
    for x in XS:
        roots = {n.lower() for n in RANK[:min(x, 51)]} | set(wr[:max(0, x - 51)])
        hit = collections.Counter(it["band"] for it in ITEMS if it["w"] in roots)
        leak.append(f"  X{x}: {sum(hit.values())} of {NW} — " + ", ".join(f"band {b}: {hit[b]}/{band[b]}" for b in sorted(band)))
    (D / "leak.txt").write_text("\n".join(leak) + "\n")
    print("\n".join(leak))
    (D / "specs").mkdir(exist_ok=True)
    for x in XS:
        for kind in ("enc", "dec"):
            (D / f"specs/X{x}_{kind}.md").write_text(spec(x, kind))
        for k in (1, 2):
            part = ITEMS[(k - 1) * 60:k * 60]
            r1.put(sc / f"w/X{x}_{k}", {"spec.md": spec(x, "enc"),
                                         "list.md": r1.numbered(f"{it['w']} ({it['pos']}): {it['gloss']}" for it in part)})


def readers(sc):
    codes = {}
    for x in XS:
        rows = []
        for k in (1, 2):
            a = r1.parse_numbered(sc / f"w/X{x}_{k}/answers.md")
            assert len(a) == 60, (x, k, len(a))
            rows += [a[i].strip().strip("`") for i in range(1, 61)]
        codes[f"X{x}"] = rows
        allowed = {n for n in RANK[:min(x, 51)]} | {r["w"].upper() for r in word_roots()[:max(0, x - 51)]}
        bad = [(i, w) for i, c in enumerate(rows) for w in re.findall(r"\b([A-Z]{2,})\b", c)
               if w not in allowed and w.lower() not in LINKS]
        print(f"X{x} roots outside the list:", len(bad), bad[:8])
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    lists = []
    for arm in ARMS:
        for s in (1, 2):
            rid = f"{arm}_{s}"
            order = list(range(NW))
            random.Random(f"roots2-{rid}").shuffle(order)
            r1.put(sc / f"r/{rid}", {"spec.md": spec(int(arm[1:]), "dec"), "codes.md": r1.numbered(codes[arm][i] for i in order)})
            lists.append({"r": rid, "arm": arm, "order": order})
    json.dump(lists, open(D / "lists.json", "w"))


def answers(sc):
    out = {}
    for l in json.load(open(D / "lists.json")):
        a = r1.parse_numbered(sc / f"r/{l['r']}/answers.md")
        for t, i in enumerate(l["order"], 1):
            out[(l["r"], i)] = a.get(t, "—").split("|")[0].strip()
    return out


def judges(sc):
    ans = answers(sc)
    keys = sorted(ans)
    random.Random(61).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    parts = [keys[j::JUDGES] for j in range(JUDGES)]
    for j in range(JUDGES):
        ks = parts[j] + parts[(j + 1) % JUDGES]
        random.Random(f"r2j{j}").shuffle(ks)
        lines = [f"{t}. {ITEMS[i]['w']} ({ITEMS[i]['pos']}: {ITEMS[i]['gloss']}) — {ans[(r, i)]}" for t, (r, i) in enumerate(ks, 1)]
        r1.put(sc / f"j/j{j + 1}", {"task.md": (S1 / "tasks/judge.md").read_text(), "items.md": "\n".join(lines) + "\n",
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
    wr = [r["w"] for r in word_roots()]
    rng = np.random.default_rng(0)
    boot = [np.concatenate([rng.choice(np.flatnonzero(band == b), (band == b).sum()) for b in bands]) for _ in range(2000)]
    U = lambda v, ix=None: sum(shares[str(b)] * np.nanmean(v[ix][band[ix] == b] if ix is not None else v[band == b]) for b in bands)
    out = ["# roots2 — result (v2c, one code ≤ 3 words, 120 words, 2 readers × 2 judges)", "",
           "| roots X | close | token-weighted U [95 %] | targets that are roots | close, target not a root |", "|---|---|---|---|---|"]
    pts = []
    for x in XS:
        arm = f"X{x}"
        rr = [l["r"] for l in lists if l["arm"] == arm]
        v = np.array([np.mean([s == 2 for r in rr for s in S.get((r, i), [])] or [np.nan]) for i in range(NW)])
        roots = {n.lower() for n in RANK[:min(x, 51)]} | set(wr[:max(0, x - 51)])
        isroot = np.array([it["w"] in roots for it in ITEMS])
        u = U(v)
        bu = [U(v, ix) for ix in boot]
        lo, hi = np.percentile(bu, [2.5, 97.5])
        nr = np.nanmean(v[~isroot])
        pts.append({"X": x, "close": float(np.nanmean(v)), "U": float(u), "lo": float(lo), "hi": float(hi),
                    "roots_hit": int(isroot.sum()), "close_not_root": float(nr)})
        out.append(f"| {x} | {np.nanmean(v):.0%} | {u:.0%} [{lo:.0%} … {hi:.0%}] | {isroot.sum()} | {nr:.0%} |")
    both = [tuple(v) for v in S.values() if len(v) == 2]
    out.append(f"\nJudges: exact agreement {np.mean([a == b for a, b in both]):.0%} on {len(both)} answers")
    codes = json.load(open(D / "codes.json"))
    nr = lambda c: sum(len(re.findall(r"\b[A-Z]{2,}\b", w.split("|")[0])) for w in (re.findall(r"\{([^{}]*)\}", c) or [c]))
    nw = lambda c: max(1, len(re.findall(r"\{", c)))
    out += ["", "## Roots / words per code"] + [f"  {a}: {np.mean([nr(c) for c in codes[a]]):.2f} roots, "
                                                 f"{np.mean([nw(c) for c in codes[a]]):.2f} words" for a in ARMS]
    json.dump(pts, open(D / "points.json", "w"), indent=0)
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        shutil.copy(sc / f"r/{l['r']}/answers.md", D / f"answers/read_{l['r']}.md")
    for x in XS:
        for k in (1, 2):
            shutil.copy(sc / f"w/X{x}_{k}/answers.md", D / f"answers/write_X{x}_{k}.md")
    for j in range(1, JUDGES + 1):
        shutil.copy(sc / f"j/j{j}/scores.md", D / f"answers/judge_j{j}.md")
        shutil.copy(sc / f"j/j{j}/keys.json", D / f"answers/judge_j{j}_keys.json")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
