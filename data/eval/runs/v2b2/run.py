"""v2b2 (dec.md): v2b (v1 + шесть корней, ось SHAPE по пропорциям) против min-co v1 и Toki Pona на bench1 dev — обычный текст.

mc и v2b кодируются в этом прогоне по одной процедуре (base1); коды tp берутся из ../base1/codes.json. Все три плеча
перечитываются новыми читателями. Рабочие папки агентов — вне репозитория (SC, например scratchpad/v2b2); итоги копируются сюда.
    .venv/bin/python data/eval/runs/v2b2/run.py make SC      → SC/enc/<плечо>_<кусок>/ (8 кодировщиков)
    .venv/bin/python data/eval/runs/v2b2/run.py collect SC   → codes.json (mc, v2b), check.txt (правила, кавычки, плотность, новые корни)
    .venv/bin/python data/eval/runs/v2b2/run.py readers SC   → lists.json, SC/read/<плечо><k>/ (6 слепых читателей)
    .venv/bin/python data/eval/runs/v2b2/run.py judges SC    → pairs.json, SC/judge/s1..s3 (предложения), f1 (факты)
    .venv/bin/python data/eval/runs/v2b2/run.py score SC     → result.txt, answers/, judge/
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
BASE = D.parent / "base1"
ITEMS = R / "data/eval/items/bench1"
sys.path.insert(0, str(R / "scripts/mincode"))
ARMS = ["mc", "tp", "v2b"]          # tp — коды base1; mc, v2b — новые
NEW = ["mc", "v2b"]
MINCO = ["mc", "v2b"]
VERSION = {"mc": "v1", "v2b": "v2b"}
NEWROOTS = ["SHAPE", "OPEN", "STRONG", "TRUE", "LIGHT", "COLOR"]
CHUNK = 20
READERS = 2
JUDGES = 3
OVERLAP = 30                        # пар у каждого судьи, которые судит и следующий (по кругу)
SENTS = json.load(open(ITEMS / "sents_dev.json"))
PARAS = json.load(open(ITEMS / "paras_dev.json"))
N = len(SENTS)
TP_FUNC = set("li e la pi en o anu taso kin ala a seme".split())
STOP = set(("a an the of to in on at by for with and or but is are was were be been being it its this that these those he she "
            "they his her their him them i we you my our your as from not no so than then there here which who whom what when "
            "where would could should will can may might have has had do does did").split())


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def spec(arm, kind):
    return (D / f"specs/{arm}_{kind}.md").read_text().rstrip() + "\n\n"


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
    for arm in NEW:
        for c in range(0, N, CHUNK):
            put(sc / f"enc/{arm}_s{c // CHUNK + 1}", {"spec.md": spec(arm, "enc") + (D / "tasks/enc_sents.md").read_text(),
                                                      "items.md": numbered(x["s"] for x in SENTS[c:c + CHUNK])})
        put(sc / f"enc/{arm}_p", {"spec.md": spec(arm, "enc") + (D / "tasks/enc_paras.md").read_text(), "items.md": paras_md(PARAS, "sents")})
    print("кодировщиков", len(list((sc / "enc").iterdir())))


def all_codes():
    codes = {"tp": json.load(open(BASE / "codes.json"))["tp"]}
    codes.update(json.load(open(D / "codes.json")))
    return codes


def lines_of(c):
    return c["sents"] + [x for p in c["paras"].values() for x in p]


def roots_in(code):
    """Корни min-co: слова в фигурных скобках до `|`, без кавычек."""
    return [r for w in re.findall(r"\{([^}|]*)\|", code) for r in re.findall(r"\b[A-Z][A-Z]+\b", re.sub(r'"[^"]*"', "", w))]


def density(arm, x):
    """(слов, содержательных единиц) в одной строке: min-co — слова в скобках и корни; Toki Pona — слова и слова без частиц."""
    if arm in MINCO:
        return x.count("{"), len(roots_in(x))
    toks = re.findall(r"[A-Za-z]+", x)
    return len(toks), len([t for t in toks if t not in TP_FUNC])


def collect(sc):
    import spec as langspec
    from validator import Validator
    codes = {}
    for arm in NEW:
        sents = []
        for c in range(0, N, CHUNK):
            got = parse_numbered(sc / f"enc/{arm}_s{c // CHUNK + 1}/codes.md")
            sents += [got.get(k + 1, "") for k in range(len(SENTS[c:c + CHUNK]))]
        paras = parse_blocks(sc / f"enc/{arm}_p/codes.md")
        codes[arm] = {"sents": sents, "paras": {p["id"]: paras.get(p["id"], []) for p in PARAS}}
    json.dump(codes, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    for f in (sc / "enc").rglob("codes.md"):
        dst = D / "raw" / f.relative_to(sc)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(f, dst)
    codes = all_codes()
    eng = np.mean([len([w for w in re.findall(r"[A-Za-z']+", x["s"].lower()) if w not in STOP]) for x in SENTS])
    out = [f"содержательных слов в английском предложении (dev): {eng:.1f}", ""]
    for arm in MINCO:
        v = Validator(langspec.load(version=VERSION[arm]))
        ls = lines_of(codes[arm])
        bad_s = sum(bool([i for i in v.check_braced(x) if i.level == "error"]) for x in codes[arm]["sents"])
        bad = sum(bool([i for i in v.check_braced(x) if i.level == "error"]) for x in ls)
        nosign = sum(bool([i for i in v.check_braced(x) if i.level == "error" and "со знаком" not in i.msg]) for x in ls)
        quotes = sorted({q for x in ls for q in re.findall(r'"([^"]*)"', x)})
        out.append(f"{arm}: строк {len(ls)}, с ошибками правил {bad} (предложений {bad_s} из {N}; без учёта пропущенного знака {nosign}), пустых {sum(not x for x in ls)}")
        out.append("  в кавычках: " + ", ".join(quotes))
    for arm in ARMS:
        d = np.array([density(arm, x) for x in codes[arm]["sents"]])
        unit = "корней" if arm in MINCO else "слов без частиц"
        out.append(f"плотность {arm}: слов на предложение {d[:, 0].mean():.1f}, {unit} {d[:, 1].mean():.1f}"
                   + (f", корней на слово {d[:, 1].sum() / d[:, 0].sum():.2f}" if arm in MINCO else ""))
    used = [[r for r in NEWROOTS if r in roots_in(x)] for x in codes["v2b"]["sents"]]
    out.append(f"v2b: предложений с новым корнем {sum(map(bool, used))} из {N}; употреблений по корням: "
               + ", ".join(f"{r} {sum(r in u for u in used)}" for r in NEWROOTS)
               + f"; строк абзацев с новым корнем {sum(any(r in roots_in(x) for r in NEWROOTS) for p in codes['v2b']['paras'].values() for x in p)}")
    (D / "check.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


def readers(sc):
    codes = all_codes()
    lists = []
    for arm in ARMS:
        for k in range(1, READERS + 1):
            rng = random.Random(f"v2b2-{arm}{k}")
            order = list(range(N))
            rng.shuffle(order)
            porder = [p["id"] for p in PARAS]
            rng.shuffle(porder)
            name = f"{arm}{k}"
            lists.append({"r": name, "lang": arm, "order": order, "porder": porder})
            put(sc / f"read/{name}", {"spec.md": spec(arm, "dec") + (D / "tasks/dec_sents.md").read_text() + "\n" + (D / "tasks/dec_paras.md").read_text(),
                                      "sents.md": numbered(codes[arm]["sents"][i] or "(no code)" for i in order),
                                      "paras.md": "".join(f"## {pid}\n" + "".join(x + "\n" for x in codes[arm]["paras"][pid]) + "\n" for pid in porder)})
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
    rng = random.Random(19)
    keys = sorted(rs)
    rng.shuffle(keys)
    parts = [keys[j::JUDGES] for j in range(JUDGES)]
    pairs = []
    for j in range(1, JUDGES + 1):
        prev = parts[(j - 2) % JUDGES][:OVERLAP]          # общие с предыдущим судьёй
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
        put(sc / f"judge/s{j}", {"task.md": (D / "tasks/judge_sents.md").read_text(), "items.md": "".join(lines)})
    facts = json.load(open(BASE / "facts.json"))
    blocks = sorted(rp)
    rng.shuffle(blocks)
    fb = []
    for t, (r, pid) in enumerate(blocks, 1):
        fb.append(f"## {t}\nREADING: {rp[(r, pid)]}\nFACTS:\n" + numbered(facts[pid]) + "\n")
        pairs.append({"kind": "facts", "r": r, "pid": pid, "j": "f1", "t": t})
    put(sc / "judge/f1", {"task.md": (D / "tasks/judge_facts.md").read_text(), "items.md": "".join(fb)})
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    sizes = [sum(p.get("j") == j for p in pairs) for j in range(1, JUDGES + 1)]
    print("листы судей предложений:", sizes, "; блоков фактов:", len(blocks))


def boot(a, b, n=5000):
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(a), (n, len(a)))
    d = (a - b)[idx].mean(1)
    return (a - b).mean(), np.percentile(d, 2.5), np.percentile(d, 97.5)


def score(sc):
    lists, rs, rp = readings(sc)
    pairs = json.load(open(D / "pairs.json"))
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    sj = {j: parse_numbered(sc / f"judge/s{j}/scores.md") for j in range(1, JUDGES + 1)}
    fj = parse_blocks(sc / "judge/f1/scores.md")
    S, anc = {}, {}
    for p in pairs:
        if p["kind"] == "facts":
            continue
        v = sj[p["j"]].get(p["t"])
        v = int(v[0]) if v and v[0].isdigit() else None
        p["s"] = v
        if p["kind"] == "anchor":
            anc[(p["j"], p["a"])] = v
        else:
            S.setdefault((p["r"], p["i"]), []).append((p["j"], v))
    out = ["# v2b2 — результат", ""]
    per = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        per[arm] = np.array([np.mean([v for r in rr for j, v in S[(r, i)] if v is not None]) for i in range(N)])
    out.append(f"## Предложения (dev, {N}), смысл 0–3 (судьи Sonnet, по {READERS} читателя Haiku на плечо)")
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        vals = [v for r in rr for i in range(N) for j, v in S[(r, i)][:1] if v is not None]
        out.append(f"  {arm}: среднее {per[arm].mean():.2f}, доля ≥ 2: {np.mean([v >= 2 for v in vals]):.0%}, доля 3: {np.mean([v == 3 for v in vals]):.0%}")
    for a, b in (("v2b", "mc"), ("v2b", "tp"), ("mc", "tp")):
        d, lo, hi = boot(per[a], per[b])
        out.append(f"  {a} − {b}: {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    codes = all_codes()
    hit = [i for i in range(N) if any(r in roots_in(codes["v2b"]["sents"][i]) for r in NEWROOTS)]
    rest = [i for i in range(N) if i not in hit]
    for name, idx in (("с новым корнем в v2b", hit), ("без него", rest)):
        if idx:
            d, lo, hi = boot(per["v2b"][idx], per["mc"][idx])
            out.append(f"  {name} ({len(idx)}): v2b − mc {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    cats = sorted({x["cat"] for x in SENTS})
    out.append("  по жанрам (" + " / ".join(ARMS) + "): " + "; ".join(
        f"{c} " + "/".join(f"{np.mean([per[a][i] for i in range(N) if SENTS[i]['cat'] == c]):.1f}" for a in ARMS) for c in cats))
    ov = [(a, b) for k, v in S.items() if len(v) == 2 for (_, a), (_, b) in [v] if a is not None and b is not None]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судьи " + "/".join(str(j) for j in range(1, JUDGES + 1)) + "): " + "; ".join(
        f"{anchors[a]['want']}→" + "/".join(str(anc.get((j, a))) for j in range(1, JUDGES + 1)) for a in range(len(anchors))))
    facts = json.load(open(BASE / "facts.json"))
    cov = {}
    for p in pairs:
        if p["kind"] != "facts":
            continue
        vals = [int(m[1]) for x in fj.get(str(p["t"]), []) if (m := re.match(r"\s*\d+\.\s*([0-2])", x))]
        n = len(facts[p["pid"]])
        p["s"] = vals
        cov[(p["r"], p["pid"])] = sum(vals[:n]) / (2 * n) if n else None
    out += ["", f"## Абзацы (dev, {len(PARAS)}), доля фактов (2 есть, 1 частично)"]
    pf = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        pf[arm] = np.array([np.mean([cov[(r, p["id"])] for r in rr]) for p in PARAS])
        out.append(f"  {arm}: {pf[arm].mean():.0%}")
    for a, b in (("v2b", "mc"), ("v2b", "tp"), ("mc", "tp")):
        d, lo, hi = boot(pf[a], pf[b])
        out.append(f"  {a} − {b}: {d * 100:+.0f} п. п. [{lo * 100:+.0f} … {hi * 100:+.0f}]")
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        for f in ("sents.md", "sents_out.md", "paras.md", "paras_out.md"):
            shutil.copy(sc / f"read/{l['r']}/{f}", D / f"answers/{l['r']}_{f}")
    for j in [f"s{k}" for k in range(1, JUDGES + 1)] + ["f1"]:
        for f in ("items.md", "scores.md"):
            shutil.copy(sc / f"judge/{j}/{f}", D / f"judge/{j}_{f}")
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "collect": collect, "readers": readers, "judges": judges, "score": score}[cmd](sc)
