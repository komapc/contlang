"""base1 (dec.md): базовые линии min-co v1 и Toki Pona на постоянном наборе bench1 (dev).

Рабочие папки агентов — вне репозитория (SC, например scratchpad/base1); итоги копируются сюда.
    .venv/bin/python data/eval/runs/base1/run.py make SC      → SC/enc/<язык>_<кусок>/ (кодировщики), SC/facts/ (факты абзацев)
    .venv/bin/python data/eval/runs/base1/run.py collect SC   → codes.json, facts.json, check.txt (проверка кодов скриптом)
    .venv/bin/python data/eval/runs/base1/run.py readers SC   → lists.json, SC/read/<язык><k>/ (слепые читатели)
    .venv/bin/python data/eval/runs/base1/run.py judges SC    → pairs.json, SC/judge/s1, s2 (предложения), f1 (факты)
    .venv/bin/python data/eval/runs/base1/run.py score SC     → result.txt, answers/, judge/
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
ITEMS = R / "data/eval/items/bench1"
sys.path.insert(0, str(R / "scripts/mincode"))
LANGS = ["mc", "tp"]
CHUNK = 20
READERS = 2
OVERLAP = 30
SENTS = json.load(open(ITEMS / "sents_dev.json"))
PARAS = json.load(open(ITEMS / "paras_dev.json"))
N = len(SENTS)


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def spec(lang, kind):
    return (D / f"specs/{lang}_{kind}.md").read_text().rstrip() + "\n\n"


def paras_md(ps, key):
    return "".join(f"## {p['id']}\n" + "".join(x + "\n" for x in p[key]) + "\n" for p in ps)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def parse_blocks(path):
    out, cur = {}, None
    for x in open(path):
        m = re.match(r"\s*##\s*(\S+)", x)
        if m:
            cur = m[1]
            out[cur] = []
        elif cur and x.strip():
            out[cur].append(x.strip())
    return out


def make(sc):
    for lang in LANGS:
        for c in range(0, N, CHUNK):
            put(sc / f"enc/{lang}_s{c // CHUNK + 1}", {"spec.md": spec(lang, "enc") + (D / "tasks/enc_sents.md").read_text(),
                                                       "items.md": numbered(x["s"] for x in SENTS[c:c + CHUNK])})
        put(sc / f"enc/{lang}_p", {"spec.md": spec(lang, "enc") + (D / "tasks/enc_paras.md").read_text(), "items.md": paras_md(PARAS, "sents")})
    put(sc / "facts", {"task.md": (D / "tasks/facts.md").read_text(), "paras.md": paras_md(PARAS, "sents")})
    print("кодировщиков", len(list((sc / "enc").iterdir())), "+ факты")


TP_WORDS = None


def tp_words():
    txt = (D / "specs/tp_dec.md").read_text()
    body = txt.split("no other words exist):", 1)[1].split("\nPhrases:", 1)[0]
    words = set()
    for item in re.split(r"\),\s*", body):
        head = item.strip().split(" (")[0]
        words |= set(head.split("/"))
    return words


def collect(sc):
    from validator import Validator
    codes = {}
    for lang in LANGS:
        sents = []
        for c in range(0, N, CHUNK):
            got = parse_numbered(sc / f"enc/{lang}_s{c // CHUNK + 1}/codes.md")
            sents += [got.get(k + 1, "") for k in range(len(SENTS[c:c + CHUNK]))]
        paras = parse_blocks(sc / f"enc/{lang}_p/codes.md")
        codes[lang] = {"sents": sents, "paras": {p["id"]: paras.get(p["id"], []) for p in PARAS}}
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    facts = parse_blocks(sc / "facts/facts.md")
    facts = {p["id"]: [re.sub(r"^\d+\.\s*", "", f) for f in facts.get(p["id"], [])] for p in PARAS}
    json.dump(facts, open(D / "facts.json", "w"), indent=1, ensure_ascii=False)
    for sub in ("enc", "facts"):
        for f in (sc / sub).rglob("*.md"):
            if f.name in ("codes.md", "facts.md"):
                dst = D / "raw" / f.relative_to(sc)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(f, dst)
    out = []
    v = Validator()
    lines = codes["mc"]["sents"] + [x for p in codes["mc"]["paras"].values() for x in p]
    bad = [x for x in lines if [i for i in v.check_braced(x) if i.level == "error"]]
    quotes = sorted({q for x in lines for q in re.findall(r'"([^"]*)"', x)})
    out.append(f"min-co: строк {len(lines)}, с ошибками правил {len(bad)}, пустых {sum(not x for x in lines)}")
    out.append("  в кавычках: " + ", ".join(quotes))
    tw = tp_words()
    lines = codes["tp"]["sents"] + [x for p in codes["tp"]["paras"].values() for x in p]
    toks = [t for x in lines for t in re.findall(r"[A-Za-z]+", x)]
    names = sorted({t for t in toks if t[0].isupper()})
    unknown = sorted({t for t in toks if t[0].islower() and t not in tw})
    out.append(f"Toki Pona: строк {len(lines)}, слов {len(toks)}, не из словаря {len(unknown)}: {', '.join(unknown)}; пустых {sum(not x for x in lines)}")
    out.append("  имена: " + ", ".join(names))
    out.append(f"фактов: {sum(len(f) for f in facts.values())} на {len(facts)} абзацев")
    (D / "check.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def readers(sc):
    codes = json.load(open(D / "codes.json"))
    lists = []
    for lang in LANGS:
        for k in range(1, READERS + 1):
            rng = random.Random(f"{lang}{k}")
            order = list(range(N))
            rng.shuffle(order)
            porder = [p["id"] for p in PARAS]
            rng.shuffle(porder)
            name = f"{lang}{k}"
            lists.append({"r": name, "lang": lang, "order": order, "porder": porder})
            put(sc / f"read/{name}", {"spec.md": spec(lang, "dec") + (D / "tasks/dec_sents.md").read_text() + "\n" + (D / "tasks/dec_paras.md").read_text(),
                                      "sents.md": numbered(codes[lang]["sents"][i] or "(no code)" for i in order),
                                      "paras.md": "".join(f"## {pid}\n" + "".join(x + "\n" for x in codes[lang]["paras"][pid]) + "\n" for pid in porder)})
    json.dump(lists, open(D / "lists.json", "w"))
    print(len(lists), "читателей")


def readings(sc):
    lists = json.load(open(D / "lists.json"))
    rs, rp = {}, {}
    for l in lists:
        a = parse_numbered(sc / f"read/{l['r']}/sents_out.md")
        for k, i in enumerate(l["order"]):
            rs[(l["r"], i)] = a.get(k + 1, "—")
        b = parse_blocks(sc / f"read/{l['r']}/paras_out.md")
        for pid in l["porder"]:
            rp[(l["r"], pid)] = " ".join(b.get(pid, [])) or "—"
    return lists, rs, rp


def judges(sc):
    lists, rs, rp = readings(sc)
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    rng = random.Random(9)
    keys = sorted(rs)
    rng.shuffle(keys)
    half = len(keys) // 2
    shared = keys[:OVERLAP]
    parts = [keys[:half], keys[half:]]
    pairs = []
    for j in (1, 2):
        items = [{"kind": "sent", "r": r, "i": i} for r, i in parts[j - 1]]
        items += [{"kind": "overlap", "r": r, "i": i} for r, i in shared if (r, i) not in set(map(tuple, parts[j - 1]))]
        items += [{"kind": "anchor", "a": a} for a in range(len(anchors))]
        rng.shuffle(items)
        lines = []
        for t, it in enumerate(items, 1):
            it.update(j=j, t=t)
            o, rd = (anchors[it["a"]]["o"], anchors[it["a"]]["r"]) if it["kind"] == "anchor" else (SENTS[it["i"]]["s"], rs[(it["r"], it["i"])])
            lines.append(f"{t}. ORIGINAL: {o}\n   READING: {rd}\n")
        pairs += items
        put(sc / f"judge/s{j}", {"task.md": (D / "tasks/judge_sents.md").read_text(), "items.md": "".join(lines)})
    facts = json.load(open(D / "facts.json"))
    blocks = sorted(rp)
    rng.shuffle(blocks)
    fb = []
    for t, (r, pid) in enumerate(blocks, 1):
        fb.append(f"## {t}\nREADING: {rp[(r, pid)]}\nFACTS:\n" + numbered(facts[pid]) + "\n")
        pairs.append({"kind": "facts", "r": r, "pid": pid, "j": "f1", "t": t})
    put(sc / "judge/f1", {"task.md": (D / "tasks/judge_facts.md").read_text(), "items.md": "".join(fb)})
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    print(sum(p["kind"] != "facts" for p in pairs), "пар предложений (2 судьи, с якорями и общими),", len(blocks), "блоков фактов")


def boot(a, b, n=5000):
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(a), (n, len(a)))
    d = (a - b)[idx].mean(1)
    return (a - b).mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)


def score(sc):
    lists, rs, rp = readings(sc)
    pairs = json.load(open(D / "pairs.json"))
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    sj = {j: parse_numbered(sc / f"judge/s{j}/scores.md") for j in (1, 2)}
    fj = parse_blocks(sc / "judge/f1/scores.md")
    lang_of = {l["r"]: l["lang"] for l in lists}
    S = {}  # (r, i) → [оценки]
    anc = []
    for p in pairs:
        if p["kind"] == "facts":
            continue
        v = sj[p["j"]].get(p["t"])
        v = int(v[0]) if v and v[0].isdigit() else None
        p["s"] = v
        if p["kind"] == "anchor":
            anc.append((p["j"], p["a"], v))
        else:
            S.setdefault((p["r"], p["i"]), []).append((p["j"], v))
    out = ["# base1 — результат", ""]
    per = {}
    for lang in LANGS:
        rr = [l["r"] for l in lists if l["lang"] == lang]
        per[lang] = np.array([np.mean([v for r in rr for j, v in S[(r, i)] if v is not None]) for i in range(N)])
    out.append(f"## Предложения (dev, {N}), смысл 0–3 (судьи Sonnet, по {READERS} читателя Haiku на язык)")
    for lang in LANGS:
        rr = [l["r"] for l in lists if l["lang"] == lang]
        vals = [v for r in rr for i in range(N) for j, v in S[(r, i)][:1] if v is not None]
        out.append(f"  {lang}: среднее {per[lang].mean():.2f}, доля ≥ 2: {np.mean([v >= 2 for v in vals]):.0%}, доля 3: {np.mean([v == 3 for v in vals]):.0%}")
    d, lo, hi = boot(per["mc"], per["tp"])
    out.append(f"  min-co − Toki Pona: {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    cats = sorted({x["cat"] for x in SENTS})
    out.append("  по жанрам (mc / tp): " + "; ".join(f"{c} {np.mean([per['mc'][i] for i in range(N) if SENTS[i]['cat'] == c]):.1f}/{np.mean([per['tp'][i] for i in range(N) if SENTS[i]['cat'] == c]):.1f}" for c in cats))
    ov = [(a, b) for k, v in S.items() if len(v) == 2 for (_, a), (_, b) in [v] if a is not None and b is not None]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судья 1 / судья 2): " + "; ".join(
        f"{anchors[a]['want']}→{dict(((j, x), v) for j, x, v in anc).get((1, a))}/{dict(((j, x), v) for j, x, v in anc).get((2, a))}" for a in range(len(anchors))))
    facts = json.load(open(D / "facts.json"))
    cov = {}
    for p in pairs:
        if p["kind"] != "facts":
            continue
        sc_ = fj.get(str(p["t"]), [])
        vals = [int(m[1]) for x in sc_ if (m := re.match(r"\s*\d+\.\s*([0-2])", x))]
        n = len(facts[p["pid"]])
        p["s"] = vals
        cov[(p["r"], p["pid"])] = sum(vals[:n]) / (2 * n) if n else None
    out += ["", f"## Абзацы (dev, {len(PARAS)}), доля фактов (2 есть, 1 частично; среднее по фактам)"]
    pf = {}
    for lang in LANGS:
        rr = [l["r"] for l in lists if l["lang"] == lang]
        pf[lang] = np.array([np.mean([cov[(r, p["id"])] for r in rr]) for p in PARAS])
        out.append(f"  {lang}: {pf[lang].mean():.0%}")
    d, lo, hi = boot(pf["mc"], pf["tp"])
    out.append(f"  min-co − Toki Pona: {d * 100:+.0f} п. п. [{lo * 100:+.0f} … {hi * 100:+.0f}]")
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        for f in ("sents.md", "sents_out.md", "paras.md", "paras_out.md"):
            shutil.copy(sc / f"read/{l['r']}/{f}", D / f"answers/{l['r']}_{f}")
    for j in ("s1", "s2", "f1"):
        for f in ("items.md", "scores.md"):
            shutil.copy(sc / f"judge/{j}/{f}", D / f"judge/{j}_{f}")
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


cmd, sc = sys.argv[1], Path(sys.argv[2])
{"make": make, "collect": collect, "readers": readers, "judges": judges, "score": score}[cmd](sc)
