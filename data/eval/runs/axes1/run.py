"""axes1 (dec.md): whole-range axis anchors (v2c) and a root rule (one root for non-verbs, up to 3 for verbs) vs v2b.

Arms: B = v2b spec; A = v2c roots (anchors over the whole range, axes for BODY/SEE/DO/PLACE/TEXT, SAY = speech act) with a
"use every value" scale paragraph; AR = A + root rule. All arms get the same Phrases section (up to 3 words, AGAINST).
Items: 120 words of size1 (one code each) + 60 bench1 dev sentences. 2 Sonnet encoders per arm (60 words + 30 sentences
each); per arm 2 Haiku word readers and 2 Haiku sentence readers; 2 Sonnet word judges (all answers), 3 Sonnet sentence
judges (share + overlap + anchors).
    .venv/bin/python data/eval/runs/axes1/run.py make SC     → specs/, SC/w/*
    .venv/bin/python data/eval/runs/axes1/run.py readers SC  → codes.json, lists.json, SC/rw/*, SC/rs/*, check.txt
    .venv/bin/python data/eval/runs/axes1/run.py judges SC   → pairs.json, SC/jw/*, SC/js/*
    .venv/bin/python data/eval/runs/axes1/run.py score SC    → result.txt, answers/
"""
import collections
import json
import math
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
R = D.parents[3]
V2B2 = D.parent / "v2b2"
ITEMS = R / "data/eval/items/bench1"
ARMS = ["B", "A", "AR"]
WORDS = json.load(open(D.parent / "size1/items.json"))
SENTS = json.load(open(ITEMS / "sents_dev.json"))
NW, NS = len(WORDS), len(SENTS)
READERS, SJUDGES, OVERLAP = 2, 3, 30
T = lambda p: (D / "tasks" / p).read_text().strip() + "\n"


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def sub(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)


def section(s, head, nxt):
    a = s.index(head)
    b = s.index(nxt, a + len(head))
    return a, b


def spec(arm, kind):
    s = (V2B2 / f"specs/v2b_{kind}.md").read_text().rstrip() + "\n"
    a, b = section(s, "## Two words", "\n## ")
    s = s[:a] + T("phrases.md") + s[b:]
    s = s.replace("(E PI FROM FOR LIKE LA PE AND)", "(E PI FROM FOR AGAINST LIKE LA PE AND)")
    if arm == "B":
        return s
    a, b = section(s, "A root may carry a value", "## Roots (51)")
    s = s[:a] + T("scale_v2c.md") + "\n" + s[b:]
    a, b = section(s, "## Roots (51)\n", "\n## Form marks")
    s = s[:a] + "## Roots (51)\n\n" + (R / "lang/v2c/roots_en.md").read_text().strip() + "\n" + s[b:]
    if arm == "A":
        return s
    s = sub(s, "- ROOTS: 1 to 3 roots. The first is the head: what kind of thing, action or quality it is. "
               "Each next root narrows everything before it.\n", T("roots_rule.md"))
    s = sub(s, "`PLACE LIVE | o` = a place where one lives = house.", "`PLACE(=0) | o` = building; `{ PLACE(=0) | o } FOR { LIVE | i }` = house.")
    s = sub(s, "`JOIN(=-4) TOUCH(=+4) | o tool` = knife", "`JOIN(=-4) | o tool` = knife")
    s = sub(s, "`PLACE INSIDE(=+5) LIVE | o BIG | i` = the house is big", "`PLACE(=0) | o BIG | i` = the building is big")
    if kind == "enc":
        s = sub(s, "At most 3 roots per word.", "Follow the ROOTS rule below (one root for a noun, adjective or adverb).")
    return s


def make(sc):
    (D / "specs").mkdir(exist_ok=True)
    for arm in ARMS:
        for kind in ("enc", "dec"):
            (D / f"specs/{arm}_{kind}.md").write_text(spec(arm, kind))
        for k in (1, 2):
            w = WORDS[(k - 1) * NW // 2:k * NW // 2]
            st = SENTS[(k - 1) * NS // 2:k * NS // 2]
            put(sc / f"w/{arm}{k}", {"spec.md": spec(arm, "enc") + "\n" + T("encode.md"),
                                     "words.md": numbered(f"{x['w']} ({x['pos']}): {x['gloss']}" for x in w),
                                     "sents.md": numbered(x["s"] for x in st)})
    print("encoders:", len(ARMS) * 2)


def words_in(code):
    return re.findall(r"\{([^{}]*)\}", code) or [code]


def roots_of(word):
    head = word.split("|")[0]
    return re.findall(r"\b([A-Z]{2,})(?:\(=([+-]?\d+)\))?", head)


def check(codes):
    out = []
    for arm in ARMS:
        ws = [w for c in codes[arm]["words"] for w in words_in(c)]
        ws += [w for c in codes[arm]["sents"] for w in words_in(c)]
        rs = [roots_of(w) for w in ws]
        nr = [len(r) for r in rs if r]
        vals = collections.Counter(v for r in rs for _, v in r if v)
        withv = sum(1 for r in rs for _, v in r if v) / max(1, sum(len(r) for r in rs))
        p = np.array(list(vals.values())) / max(1, sum(vals.values()))
        ent = -(p * np.log2(p)).sum() if len(p) else 0
        mid = sum(c for v, c in vals.items() if abs(int(v)) <= 3) / max(1, sum(vals.values()))
        pos = collections.defaultdict(list)
        for w, r in zip(ws, rs):
            m = re.search(r"\|\s*([oiae])\b", w)
            if m and r:
                pos[m[1]].append(len(r))
        nwc = np.mean([len(words_in(c)) for c in codes[arm]["words"]])
        out.append(f"{arm}: roots/word {np.mean(nr):.2f}; " + ", ".join(f"{k} {np.mean(v):.2f}" for k, v in sorted(pos.items()))
                   + f"; roots with value {withv:.0%}; value entropy {ent:.2f} bits; |v|≤3 {mid:.0%}; words per word-code {nwc:.2f}")
    return out


def readers(sc):
    codes = {}
    for arm in ARMS:
        cw, cs = [], []
        for k in (1, 2):
            a = parse_numbered(sc / f"w/{arm}{k}/words_out.md")
            b = parse_numbered(sc / f"w/{arm}{k}/sents_out.md")
            assert len(a) == NW // 2 and len(b) == NS // 2, (arm, k, len(a), len(b))
            cw += [a[i] for i in range(1, NW // 2 + 1)]
            cs += [b[i] for i in range(1, NS // 2 + 1)]
        codes[arm] = {"words": cw, "sents": cs}
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    lists = []
    for arm in ARMS:
        for k in range(1, READERS + 1):
            rng = random.Random(f"axes1-{arm}{k}")
            ow, os_ = list(range(NW)), list(range(NS))
            rng.shuffle(ow)
            rng.shuffle(os_)
            dec = spec(arm, "dec")
            put(sc / f"rw/{arm}{k}", {"spec.md": dec + "\n" + T("read_words.md"), "codes.md": numbered(codes[arm]["words"][i] for i in ow)})
            put(sc / f"rs/{arm}{k}", {"spec.md": dec + "\n" + T("read_sents.md"), "sents.md": numbered(codes[arm]["sents"][i] for i in os_)})
            lists.append({"r": f"{arm}{k}", "arm": arm, "ow": ow, "os": os_})
    json.dump(lists, open(D / "lists.json", "w"))
    c = check(codes)
    (D / "check.txt").write_text("\n".join(c) + "\n")
    print("\n".join(c))


def answers(sc):
    lists = json.load(open(D / "lists.json"))
    aw, as_ = {}, {}
    for l in lists:
        a = parse_numbered(sc / f"rw/{l['r']}/answers.md")
        b = parse_numbered(sc / f"rs/{l['r']}/sents_out.md")
        for t, i in enumerate(l["ow"], 1):
            aw[(l["r"], i)] = a.get(t, "—").split("|")[0].strip()
        for t, i in enumerate(l["os"], 1):
            as_[(l["r"], i)] = b.get(t, "—")
    return lists, aw, as_


def judges(sc):
    lists, aw, as_ = answers(sc)
    keys = sorted(aw)
    random.Random(43).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    lines = [f"{t}. {WORDS[i]['w']} ({WORDS[i]['pos']}: {WORDS[i]['gloss']}) — {aw[(r, i)]}" for t, (r, i) in enumerate(keys, 1)]
    for j in ("w1", "w2"):
        put(sc / f"jw/{j}", {"task.md": T("judge_words.md"), "items.md": "\n".join(lines) + "\n"})
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    rng = random.Random(19)
    ks = sorted(as_)
    rng.shuffle(ks)
    parts = [ks[j::SJUDGES] for j in range(SJUDGES)]
    pairs = []
    for j in range(1, SJUDGES + 1):
        its = [{"kind": "sent", "r": r, "i": i} for r, i in parts[j - 1]]
        its += [{"kind": "overlap", "r": r, "i": i} for r, i in parts[(j - 2) % SJUDGES][:OVERLAP]]
        its += [{"kind": "anchor", "a": a} for a in range(len(anchors))]
        rng.shuffle(its)
        ls = []
        for t, it in enumerate(its, 1):
            it.update(j=j, t=t)
            o, rd = (anchors[it["a"]]["o"], anchors[it["a"]]["r"]) if it["kind"] == "anchor" else (SENTS[it["i"]]["s"], as_[(it["r"], it["i"])])
            ls.append(f"{t}. ORIGINAL: {o}\n   READING: {rd}\n")
        pairs += its
        put(sc / f"js/s{j}", {"task.md": T("judge_sents.md"), "items.md": "".join(ls)})
    json.dump(pairs, open(D / "pairs.json", "w"))
    print("word answers:", len(lines), "; sentence sheets:", [sum(p["j"] == j for p in pairs) for j in range(1, SJUDGES + 1)])


def boot(x, y, n=5000):
    idx = np.random.default_rng(0).integers(0, len(x), (n, len(x)))
    d = (x - y)[idx].mean(1)
    return (x - y).mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)


def score(sc):
    lists, aw, as_ = answers(sc)
    keys = [tuple(k) for k in json.load(open(D / "judge_keys.json"))]
    sw = [parse_numbered(sc / f"jw/{j}/scores.md") for j in ("w1", "w2")]
    W = {k: [int(s[t][0]) for s in sw if t in s and s[t][:1].isdigit()] for t, k in enumerate(keys, 1)}
    pairs = json.load(open(D / "pairs.json"))
    ss = {j: parse_numbered(sc / f"js/s{j}/scores.md") for j in range(1, SJUDGES + 1)}
    S, anc = collections.defaultdict(list), {}
    for p in pairs:
        v = ss[p["j"]].get(p["t"])
        v = int(v[0]) if v and v[0].isdigit() else None
        if p["kind"] == "anchor":
            anc[(p["j"], p["a"])] = v
        elif v is not None:
            S[(p["r"], p["i"])].append(v)
    rr = {arm: [l["r"] for l in lists if l["arm"] == arm] for arm in ARMS}
    close = {arm: np.array([np.mean([v == 2 for r in rr[arm] for v in W[(r, i)]]) for i in range(NW)]) for arm in ARMS}
    rel = {arm: np.array([np.mean([v >= 1 for r in rr[arm] for v in W[(r, i)]]) for i in range(NW)]) for arm in ARMS}
    sent = {arm: np.array([np.mean([np.mean(S[(r, i)]) for r in rr[arm] if S[(r, i)]]) for i in range(NS)]) for arm in ARMS}
    out = ["# axes1 — result", "", f"## Words ({NW}), first answer, 2 judges: share close"]
    for arm in ARMS:
        out.append(f"  {arm}: close {close[arm].mean():.0%}, close or related {rel[arm].mean():.0%}")
    for a, b in (("A", "B"), ("AR", "A"), ("AR", "B")):
        m, lo, hi = boot(close[a], close[b])
        out.append(f"  {a} − {b}: {100 * m:+.1f} pp [{100 * lo:+.1f} … {100 * hi:+.1f}]")
    pos = np.array([x["pos"] for x in WORDS])
    for p in ("noun", "verb", "adjective"):
        msk = pos == p
        out.append(f"  {p} ({msk.sum()}): " + ", ".join(f"{arm} {close[arm][msk].mean():.0%}" for arm in ARMS))
    both = [tuple(v) for v in W.values() if len(v) == 2]
    out.append(f"  judges agree exactly {np.mean([x == y for x, y in both]):.0%}")
    out += ["", f"## Sentences ({NS}), meaning 0–3, {SJUDGES} judges"]
    for arm in ARMS:
        out.append(f"  {arm}: {sent[arm].mean():.2f}")
    for a, b in (("A", "B"), ("AR", "A"), ("AR", "B")):
        m, lo, hi = boot(sent[a], sent[b])
        out.append(f"  {a} − {b}: {m:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    ov = [v for v in S.values() if len(v) == 2]
    out.append(f"  overlap pairs {len(ov)}: exact {np.mean([x == y for x, y in ov]):.0%}, ±1 {np.mean([abs(x - y) <= 1 for x, y in ov]):.0%}")
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    out.append("  anchors (want→judges): " + "; ".join(f"{anchors[a]['want']}→" + "/".join(str(anc.get((j, a))) for j in range(1, SJUDGES + 1))
                                              for a in range(len(anchors))))
    out += ["", "## Manipulation check (codes)"] + ["  " + x for x in (D / "check.txt").read_text().splitlines()]
    codes = json.load(open(D / "codes.json"))
    out += ["", "## Words (close B / A / AR)"]
    for i in sorted(range(NW), key=lambda i: close["AR"][i] + close["A"][i] - 2 * close["B"][i]):
        out.append(f"- {WORDS[i]['w']} ({WORDS[i]['pos']}): " + " / ".join(f"{close[arm][i]:.1f}" for arm in ARMS) + " | "
                   + " | ".join(f"{arm} `{codes[arm]['words'][i]}` → " + "/".join(aw[(r, i)] for r in rr[arm]) for arm in ARMS))
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        shutil.copy(sc / f"rw/{l['r']}/answers.md", D / f"answers/readw_{l['r']}.md")
        shutil.copy(sc / f"rs/{l['r']}/sents_out.md", D / f"answers/reads_{l['r']}.md")
    for arm in ARMS:
        for k in (1, 2):
            for f in ("words_out.md", "sents_out.md"):
                shutil.copy(sc / f"w/{arm}{k}/{f}", D / f"answers/write_{arm}{k}_{f}")
    for j in ("w1", "w2"):
        shutil.copy(sc / f"jw/{j}/scores.md", D / f"answers/judge_{j}.md")
    for j in range(1, SJUDGES + 1):
        shutil.copy(sc / f"js/s{j}/scores.md", D / f"answers/judge_s{j}.md")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out[:30]))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
