"""diag1 (dec.md): где теряется смысл — в словах или в связях.

Плечи (только предложения bench1 dev, 60):
  mc   — min-co v1, коды и прочтения из ../v2b2 (не перечитываются);
  mcg  — те же коды mc, но после каждого слова в <…> — что кодировщик им имел в виду (подсказка, пишут глоссаторы Sonnet,
         видя английский; только смысл самого слова, ничего сверх кода); 2 новых читателя Haiku;
  tpx  — зашифрованный Toki Pona, коды и прочтения из ../tpx1;
  tpxs — те же коды tpx без частиц li/e/pi/la (lun/ju/nisa/nen), их строки убраны из словаря; 2 новых читателя Haiku.
Все 480 прочтений судят заново 4 судьи Sonnet.
    .venv/bin/python data/eval/runs/diag1/run.py make SC      → codes.json (tpxs), specs/, SC/gloss/g1..g3, SC/read/tpxs1, tpxs2
    .venv/bin/python data/eval/runs/diag1/run.py glossed SC   → glosses.json, codes.json (mcg), SC/read/mcg1, mcg2
    .venv/bin/python data/eval/runs/diag1/run.py judges SC    → lists.json, pairs.json, SC/judge/s1..s4
    .venv/bin/python data/eval/runs/diag1/run.py score SC     → result.txt, answers/, judge/
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
V2B2 = D.parent / "v2b2"
TPX1 = D.parent / "tpx1"
ITEMS = R / "data/eval/items/bench1"
ARMS = ["mc", "mcg", "tpx", "tpxs"]
READERS = 2
JUDGES = 4
OVERLAP = 30
CHUNK = 20
SENTS = json.load(open(ITEMS / "sents_dev.json"))
N = len(SENTS)
STRIP = ["li", "e", "pi", "la"]


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def words(code):
    return re.findall(r"\{[^{}]*\}", code)


def task_sents():
    return (D.parent / "retell1/tasks/dec_sents.md").read_text()


def reader(sc, name, spec, codes):
    rng = random.Random(f"diag1-{name}")
    order = list(range(N))
    rng.shuffle(order)
    put(sc / f"read/{name}", {"spec.md": spec + "\n" + task_sents(), "sents.md": numbered(codes[i] for i in order)})
    return {"r": name, "lang": re.sub(r"\d", "", name), "order": order}


def strip_tpx(code, cx):
    li, e, pi, la = (cx[w] for w in STRIP)
    code = re.sub(rf"\s+{la}\b\s*(,)?", ",", code)          # «X la Y» → «X, Y»
    code = re.sub(rf"\b({li}|{e}|{pi})\b\s*", "", code)
    code = re.sub(r"\s+([,.:])", r"\1", re.sub(r"\s{2,}", " ", code))
    return re.sub(r",(?=\S)", ", ", code).strip()


def make(sc):
    cx = json.load(open(TPX1 / "cipher.json"))
    spec = (TPX1 / "specs/tpx_dec.md").read_text()
    lines = spec.splitlines()
    di = next(k for k, x in enumerate(lines) if x.startswith("Dictionary"))
    dic = lines[di + 1]
    for w in STRIP:                                         # убрать статьи частиц из словаря
        dic, n = re.subn(rf"(^|, ){cx[w]} \((?:[^()]|\([^()]*\))*\)(?=, |$)", r"\1", dic)
        assert n == 1, (w, n)
        dic = re.sub(r"^, |, (?=, )", "", dic)
    lines[di] = "Dictionary (116 words; no other words exist):"
    lines[di + 1] = dic
    lines = [re.sub(r' "' + cx["pi"] + r'" groups several modifiers \([^)]*\)\.', "", x) for x in lines]
    spec_s = "\n".join(lines) + "\n"
    assert all(re.search(rf"\b{cx[w]} \(", spec_s) is None for w in STRIP), "частица осталась в спецификации"
    (D / "specs").mkdir(exist_ok=True)
    (D / "specs/tpxs_dec.md").write_text(spec_s)
    tpx = json.load(open(TPX1 / "codes.json"))["tpx"]["sents"]
    tpxs = [strip_tpx(x, cx) for x in tpx]
    left = sum(len(re.findall(rf"\b({'|'.join(cx[w] for w in STRIP)})\b", x)) for x in tpxs)
    assert left == 0, left
    gone = sum(len(re.findall(rf"\b({'|'.join(cx[w] for w in STRIP)})\b", x)) for x in tpx)
    print(f"tpxs: убрано частиц {gone}, слов на предложение {np.mean([len(x.split()) for x in tpx]):.1f} → "
          f"{np.mean([len(x.split()) for x in tpxs]):.1f}")
    codes = {"tpxs": tpxs}
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    lists = [reader(sc, f"tpxs{k}", spec_s, tpxs) for k in range(1, READERS + 1)]
    json.dump(lists, open(sc / "lists_new.json", "w"))
    # задания глоссаторам
    mc = json.load(open(V2B2 / "codes.json"))["mc"]["sents"]
    task = (D / "tasks/gloss.md").read_text()
    for c in range(0, N, CHUNK):
        items = []
        for i in range(c, min(c + CHUNK, N)):
            ws = words(mc[i])
            items.append(f"{i - c + 1}. ENGLISH: {SENTS[i]['s']}\n   CODE: {mc[i]}\n   WORDS ({len(ws)}):\n"
                         + "".join(f"     [{k + 1}] {w}\n" for k, w in enumerate(ws)))
        put(sc / f"gloss/g{c // CHUNK + 1}", {"task.md": task, "items.md": "\n".join(items)})
    print("глоссаторы:", N // CHUNK, "; читатели:", [l["r"] for l in lists])


def glossed(sc):
    mc = json.load(open(V2B2 / "codes.json"))["mc"]["sents"]
    gl = {}
    for c in range(0, N, CHUNK):
        a = parse_numbered(sc / f"gloss/g{c // CHUNK + 1}/glosses.md")
        for k in range(min(CHUNK, N - c)):
            gl[c + k] = [g.strip() for g in a[k + 1].split("|")]
    bad = [i for i in range(N) if len(gl[i]) != len(words(mc[i])) or any(not g or len(g.split()) > 3 for g in gl[i])]
    assert not bad, [(i, len(gl[i]), len(words(mc[i]))) for i in bad]
    json.dump([gl[i] for i in range(N)], open(D / "glosses.json", "w"), indent=1, ensure_ascii=False)

    def add(code, gs):
        it = iter(gs)
        return re.sub(r"\{[^{}]*\}", lambda m: m[0] + "<" + next(it) + ">", code)
    mcg = [add(mc[i], gl[i]) for i in range(N)]
    codes = json.load(open(D / "codes.json"))
    codes["mcg"] = mcg
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    spec = (V2B2 / "specs/mc_dec.md").read_text().rstrip() + "\n\n" + (D / "tasks/gloss_note.md").read_text()
    (D / "specs/mcg_dec.md").write_text(spec)
    lists = json.load(open(sc / "lists_new.json"))
    lists = [l for l in lists if l["lang"] != "mcg"] + [reader(sc, f"mcg{k}", spec, mcg) for k in range(1, READERS + 1)]
    json.dump(lists, open(sc / "lists_new.json", "w"))
    print("пример:", mcg[0])


def readings(sc):
    lists = [l for l in json.load(open(TPX1 / "lists.json")) if l["lang"] in ("mc", "tpx")]
    lists += json.load(open(sc / "lists_new.json")) if (sc / "lists_new.json").exists() else json.load(open(D / "lists.json"))[4:]
    rs = {}
    for l in lists:
        if l["lang"] == "mc":
            f = V2B2 / f"answers/{l['r']}_sents_out.md"
        elif l["lang"] == "tpx":
            f = TPX1 / f"answers/{l['r']}_sents_out.md"
        else:
            f = sc / f"read/{l['r']}/sents_out.md"
        a = parse_numbered(f)
        for k, i in enumerate(l["order"]):
            rs[(l["r"], i)] = a.get(k + 1, "—")
    return lists, rs


def judges(sc):
    lists, rs = readings(sc)
    json.dump(lists, open(D / "lists.json", "w"))
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    rng = random.Random(29)
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
    out = ["# diag1 — результат", "", f"## Предложения (dev, {N}), смысл 0–3"]
    for arm in ARMS:
        out.append(f"  {arm}: {per[arm].mean():.2f}")
    for a, b in (("mcg", "tpx"), ("tpxs", "tpx"), ("mcg", "mc"), ("mc", "tpx"), ("mc", "tpxs")):
        d, lo, hi = boot(per[a], per[b])
        out.append(f"  {a} − {b}: {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    ov = [tuple(v) for v in S.values() if len(v) == 2 and None not in v]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судьи): " + "; ".join(
        f"{anchors[a]['want']}→" + "/".join(str(anc.get((j, a))) for j in range(1, JUDGES + 1)) for a in range(len(anchors))))
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        if l["lang"] in ("mcg", "tpxs"):
            for f in ("sents.md", "sents_out.md"):
                shutil.copy(sc / f"read/{l['r']}/{f}", D / f"answers/{l['r']}_{f}")
    for c in range(0, N, CHUNK):
        shutil.copy(sc / f"gloss/g{c // CHUNK + 1}/glosses.md", D / f"answers/gloss_g{c // CHUNK + 1}.md")
    for j in range(1, JUDGES + 1):
        for f in ("items.md", "scores.md"):
            shutil.copy(sc / f"judge/s{j}/{f}", D / f"judge/s{j}_{f}")
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "glossed": glossed, "judges": judges, "score": score}[cmd](sc)
