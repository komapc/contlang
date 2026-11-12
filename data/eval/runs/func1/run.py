"""func1 (dec.md): называть вещь по назначению (FOR / AGAINST, фраза до 3 слов) — читается ли лучше, чем как в min-co v1.

60 конкретных существительных (WordNet: предмет, вещество, еда, тело, животное, растение), ранг 1000–8000 в Brown, seed.
Плечо A — спецификация mc (v2b2), как есть (одно слово или X LINK Y). Плечо B — та же спецификация, но раздел «Two words»
заменён на «Phrases» (до 3 слов, новая связка AGAINST) и добавлено правило «сначала назначение».
По 2 кодировщика Sonnet на плечо (по 30 слов), по 2 читателя Haiku на плечо (все 60, без контекста), 2 судьи Sonnet судят все
240 первых ответов (0–2, как в lex).
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/func1/run.py make SC     → items.json, specs/, SC/w/A1..B2
    .venv/bin/python data/eval/runs/func1/run.py readers SC  → codes.json, lists.json, SC/r/A1..B2
    .venv/bin/python data/eval/runs/func1/run.py judges SC   → SC/j/j1, j2
    .venv/bin/python data/eval/runs/func1/run.py score SC    → result.txt, answers/
"""
import json
import random
import re
import shutil
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
V2B2 = D.parent / "v2b2"
SEED = 20261113
NW = 60
LEX = {"noun.artifact", "noun.substance", "noun.food", "noun.body", "noun.animal", "noun.plant", "noun.object"}
ARMS = ["A", "B"]


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def spec_b(s):
    a = s.index("## Two words")
    b = s.index("\n## ", a + 3)
    return s[:a] + (D / "tasks/phrases.md").read_text().strip() + "\n" + s[b:]


def specs():
    out = {}
    for kind in ("enc", "dec"):
        s = (V2B2 / f"specs/mc_{kind}.md").read_text().rstrip() + "\n"
        out[("A", kind)] = s
        sb = spec_b(s)
        if kind == "enc":
            sb += (D / "tasks/function_rule.md").read_text()
        out[("B", kind)] = sb.replace("(E PI FROM FOR LIKE LA PE AND)", "(E PI FROM FOR AGAINST LIKE LA PE AND)")
    return out


def make(sc):
    from nltk.corpus import wordnet as wn
    ranks = json.load(open(D.parent / "lexn1/ranks.json"))
    pool = []
    for w, r in ranks.items():
        if not (1000 <= r <= 8000) or not w.isalpha() or len(w) < 3:
            continue
        ss = wn.synsets(w, "n")
        if ss and ss[0].lexname() in LEX and ss[0].name().split(".")[0] == w and not wn.synsets(w, "v")[:1]:
            pool.append({"w": w, "lex": ss[0].lexname(), "gloss": ss[0].definition(), "rank": r})
    rng = random.Random(SEED)
    items = rng.sample(pool, NW)
    json.dump(items, open(D / "items.json", "w"), indent=0)
    print(f"пул {len(pool)}; взято {NW}:", ", ".join(x["w"] for x in items))
    sp = specs()
    (D / "specs").mkdir(exist_ok=True)
    for (arm, kind), s in sp.items():
        (D / f"specs/{arm}_{kind}.md").write_text(s)
    task = (D / "tasks/write.md").read_text()
    for arm in ARMS:
        for k in (1, 2):
            part = items[(k - 1) * 30:k * 30]
            put(sc / f"w/{arm}{k}", {"spec.md": sp[(arm, "enc")] + "\n" + task,
                                     "list.md": numbered(f"{x['w']} (noun): {x['gloss']}" for x in part)})


def readers(sc):
    items = json.load(open(D / "items.json"))
    codes = {}
    for arm in ARMS:
        cs = []
        for k in (1, 2):
            a = parse_numbered(sc / f"w/{arm}{k}/answers.md")
            assert len(a) == 30, (arm, k, len(a))
            cs += [a[i] for i in range(1, 31)]
        codes[arm] = cs
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    sp = specs()
    task = (D / "tasks/read.md").read_text()
    lists = []
    for arm in ARMS:
        for k in (1, 2):
            rng = random.Random(f"func1-{arm}{k}")
            order = list(range(NW))
            rng.shuffle(order)
            put(sc / f"r/{arm}{k}", {"spec.md": sp[(arm, "dec")] + "\n" + task, "codes.md": numbered(codes[arm][i] for i in order)})
            lists.append({"r": f"{arm}{k}", "arm": arm, "order": order})
    json.dump(lists, open(D / "lists.json", "w"))
    for arm in ARMS:
        nw = [len(re.findall(r"\{", c)) for c in codes[arm]]
        print(arm, "слов в коде:", np.mean(nw).round(2), "; AGAINST:", sum("AGAINST" in c for c in codes[arm]),
              "; FOR:", sum(" FOR " in c for c in codes[arm]), "; tool:", sum("tool" in c for c in codes[arm]))


def answers(sc):
    lists = json.load(open(D / "lists.json"))
    out = {}
    for l in lists:
        a = parse_numbered(sc / f"r/{l['r']}/answers.md")
        for k, i in enumerate(l["order"]):
            out[(l["r"], i)] = a.get(k + 1, "—").split("|")[0].strip()
    return lists, out


def judges(sc):
    items = json.load(open(D / "items.json"))
    lists, ans = answers(sc)
    keys = sorted(ans)
    random.Random(37).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    lines = [f"{t}. {items[i]['w']} (noun: {items[i]['gloss']}) — {ans[(r, i)]}" for t, (r, i) in enumerate(keys, 1)]
    for j in ("j1", "j2"):
        put(sc / f"j/{j}", {"task.md": (D / "tasks/judge.md").read_text(), "items.md": "\n".join(lines) + "\n"})
    print("пунктов у судьи:", len(lines))


def score(sc):
    items = json.load(open(D / "items.json"))
    lists, ans = answers(sc)
    keys = [tuple(k) for k in json.load(open(D / "judge_keys.json"))]
    sj = [parse_numbered(sc / f"j/{j}/scores.md") for j in ("j1", "j2")]
    S = {}
    for t, k in enumerate(keys, 1):
        S[k] = [int(s[t][0]) for s in sj if t in s and s[t][:1].isdigit()]
    per = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["arm"] == arm]
        per[arm] = {"close": np.array([np.mean([v == 2 for r in rr for v in S[(r, i)]]) for i in range(NW)]),
                    "rel": np.array([np.mean([v >= 1 for r in rr for v in S[(r, i)]]) for i in range(NW)])}
    rng = np.random.default_rng(0)
    idx = rng.integers(0, NW, (5000, NW))
    out = ["# func1 — результат", "", f"## Слова ({NW}), первый ответ читателя, 2 судьи"]
    for m in ("close", "rel"):
        a, b = per["A"][m], per["B"][m]
        d = (b - a)[idx].mean(1)
        out.append(f"  {m}: A {a.mean():.0%}, B {b.mean():.0%}, B − A {100 * (b - a).mean():+.1f} п. п. "
                   f"[{100 * np.percentile(d, 2.5):+.1f} … {100 * np.percentile(d, 97.5):+.1f}]")
    art = np.array([x["lex"] == "noun.artifact" for x in items])
    for name, msk in (("предметы (noun.artifact)", art), ("остальные", ~art)):
        a, b = per["A"]["close"][msk], per["B"]["close"][msk]
        out.append(f"  close, {name} ({msk.sum()}): A {a.mean():.0%}, B {b.mean():.0%}, B − A {100 * (b - a).mean():+.1f} п. п.")
    both = [tuple(v) for v in S.values() if len(v) == 2]
    out.append(f"  согласие судей: точно {np.mean([a == b for a, b in both]):.0%}")
    codes = json.load(open(D / "codes.json"))
    out += ["", "## По словам (close A → B)"]
    for i in sorted(range(NW), key=lambda i: per["B"]["close"][i] - per["A"]["close"][i]):
        ra = " / ".join(ans[(f"A{k}", i)] for k in (1, 2))
        rb = " / ".join(ans[(f"B{k}", i)] for k in (1, 2))
        out.append(f"- {items[i]['w']}: {per['A']['close'][i]:.2f} → {per['B']['close'][i]:.2f} | A `{codes['A'][i]}` → {ra} | "
                   f"B `{codes['B'][i]}` → {rb}")
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        shutil.copy(sc / f"r/{l['r']}/answers.md", D / f"answers/read_{l['r']}.md")
    for arm in ARMS:
        for k in (1, 2):
            shutil.copy(sc / f"w/{arm}{k}/answers.md", D / f"answers/write_{arm}{k}.md")
    for j in ("j1", "j2"):
        shutil.copy(sc / f"j/{j}/scores.md", D / f"answers/judge_{j}.md")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out[:6]))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
