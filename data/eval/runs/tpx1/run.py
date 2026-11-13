"""tpx1 (dec.md): Toki Pona с зашифрованными словами (tpx) против обычного Toki Pona (tp) и min-co v1 (mc) — проверка,
не объясняется ли преимущество Toki Pona тем, что читатель (Haiku) знает его по обучению.

Коды не пишутся заново: tpx — коды tp из ../base1/codes.json, где каждое слово Toki Pona заменено бессмысленным словом
(тот же словарь из 120 слов с теми же толкованиями, та же спецификация, заменены только сами слова). Прочтения tp и mc —
из ../v2b2 (те же читатели Haiku, вчера); tpx читают 2 новых читателя. Все три плеча судят заново одни и те же судьи.
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/tpx1/run.py make SC      → cipher.json, codes.json, specs/tpx_dec.md, SC/read/tpx1, tpx2
    .venv/bin/python data/eval/runs/tpx1/run.py judges SC    → lists.json, pairs.json, SC/judge/s1..s3, f1
    .venv/bin/python data/eval/runs/tpx1/run.py score SC     → result.txt, answers/, judge/
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
PREV = D.parent / "v2b2"
ITEMS = R / "data/eval/items/bench1"
ARMS = ["mc", "tp", "tpx"]
READERS = 2
JUDGES = 3
OVERLAP = 30
SENTS = json.load(open(ITEMS / "sents_dev.json"))
PARAS = json.load(open(ITEMS / "paras_dev.json"))
N = len(SENTS)
SEED = 20261112
# слова Toki Pona вне pu — тоже нельзя брать как шифр
NONPU = set("kin namako oko kipisi leko monsuta misikeke tonsi epiku jasima lanpan n kokosila majuna linluwi meso soko "
            "su ku lanpan apeja pake powe isipin kiki kijetesantakalu wuwojiti yupekosi".split())
CONS, VOW = "ptksmnljw", "aeiou"


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


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


def tp_words(spec_text):
    line = [x for x in spec_text.splitlines() if x.startswith("a (emotion")][0]
    ws = []
    for item in re.findall(r"(?:^|\), )([a-z/]+) \(", line):
        ws += item.split("/")
    return ws


def syllables(w):
    return len(re.findall(r"[aeiou]", w))


def english():
    """Слова, похожие на английские, шифром не берутся (no, we, sun, pen…): леммы WordNet и служебные слова."""
    from nltk.corpus import wordnet as wn
    ws = {w.lower() for w in wn.all_lemma_names()}
    ws |= set(("a an the of to in on at by for with and or but is are was we us he she it me my no so do go be am as if up "
               "oh ok hi yes not non nan pa ma pi po se si ta ti ki ko le la lo mo mu ne nu pe pu su tu wa wi").split())
    return ws


def make_cipher(words):
    rng = random.Random(SEED)
    taken = set(words) | NONPU | english()
    out = {}
    for w in words:
        tries = 0
        while True:
            tries += 1
            n = syllables(w) + tries // 300        # нет свободного короткого — на слог длиннее
            c = "".join(rng.choice(CONS) + rng.choice(VOW) for _ in range(n))
            if w[0] in VOW and rng.random() < 0.5:
                c = rng.choice(VOW) + c[2:] if n > 1 else rng.choice(VOW)
            if rng.random() < 0.25:
                c += "n"
            bad = re.search(r"ji|ti|wo|wu|nn", c)
            if not bad and c not in taken and len(c) >= 2:
                break
        taken.add(c)
        out[w] = c
    return out


def encipher(text, cipher):
    def sub(m):
        return cipher.get(m[0], m[0])
    return re.sub(r"\b[a-z]+\b", sub, text)


def make(sc):
    spec = (BASE / "specs/tp_dec.md").read_text()
    words = tp_words(spec)
    assert len(words) == 121, len(words)          # 120 слов, ale/ali — два написания
    cipher = make_cipher(words)
    json.dump(cipher, open(D / "cipher.json", "w"), indent=1)
    lines = spec.splitlines()
    dic, rest = lines[3], "\n".join(lines[4:])
    # словарь: шифруются заголовочные слова, толкования в скобках остаются
    new_dic = re.sub(r"(^|\), )([a-z/]+) \(", lambda m: m[1] + "/".join(cipher[w] for w in m[2].split("/")) + " (", dic)
    new_dic = re.sub(r'"([A-Za-z ]+)"', lambda m: '"' + encipher(m[1], cipher) + '"', new_dic)   # примеры в толкованиях (X la Y)
    new_dic = "Dictionary (120 words; no other words exist):\n" + new_dic
    # грамматика: шифруются только слова Toki Pona в кавычках и в `...`
    ex = re.sub(r'"([a-z ]+)"', lambda m: '"' + encipher(m[1], cipher) + '"', rest)
    ex = re.sub(r"`([a-z]+) ([A-Z][a-z]+)`", lambda m: f"`{cipher[m[1]]} {m[2]}`", ex)
    spec_x = "# Decoder instructions (Language X)\n\n" + new_dic + "\n" + ex + "\n"
    (D / "specs").mkdir(exist_ok=True)
    (D / "specs/tpx_dec.md").write_text(spec_x)
    tp = json.load(open(BASE / "codes.json"))["tp"]
    tpx = {"sents": [encipher(x, cipher) for x in tp["sents"]],
           "paras": {k: [encipher(x, cipher) for x in v] for k, v in tp["paras"].items()}}
    json.dump({"tpx": tpx}, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    left = {w for x in tpx["sents"] + [y for v in tpx["paras"].values() for y in v] for w in re.findall(r"\b[a-z]+\b", x)} & set(words)
    print("слов Toki Pona, оставшихся в кодах:", sorted(left))
    task = (D.parent / "retell1/tasks/dec_sents.md").read_text() + "\n" + (D.parent / "retell1/tasks/dec_paras.md").read_text()
    lists = json.load(open(PREV / "lists.json"))
    for k in range(1, READERS + 1):
        rng = random.Random(f"tpx1-tpx{k}")
        order = list(range(N))
        rng.shuffle(order)
        porder = [p["id"] for p in PARAS]
        rng.shuffle(porder)
        lists.append({"r": f"tpx{k}", "lang": "tpx", "order": order, "porder": porder})
        put(sc / f"read/tpx{k}", {"spec.md": spec_x + "\n" + task,
                                   "sents.md": numbered(tpx["sents"][i] for i in order),
                                   "paras.md": "".join(f"## {pid}\n" + "".join(x + "\n" for x in tpx["paras"][pid]) + "\n" for pid in porder)})
    lists = [l for l in lists if l["lang"] in ARMS]
    json.dump(lists, open(D / "lists.json", "w"))
    print("читатели:", [l["r"] for l in lists])


def readings(sc):
    lists = json.load(open(D / "lists.json"))
    rs, rp = {}, {}
    for l in lists:
        if l["lang"] == "tpx":
            fs, fp = sc / f"read/{l['r']}/sents_out.md", sc / f"read/{l['r']}/paras_out.md"
        else:
            fs, fp = PREV / f"answers/{l['r']}_sents_out.md", PREV / f"answers/{l['r']}_paras_out.md"
        a = parse_numbered(fs)
        for k, i in enumerate(l["order"]):
            rs[(l["r"], i)] = a.get(k + 1, "—")
        b = parse_blocks(fp)
        for pid in l["porder"]:
            rp[(l["r"], pid)] = " ".join(b.get(pid, [])) or "—"
    return lists, rs, rp


def judges(sc):
    lists, rs, rp = readings(sc)
    anchors = json.load(open(ITEMS / "judge_anchors.json"))
    rng = random.Random(23)
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
    facts = json.load(open(BASE / "facts.json"))
    blocks = sorted(rp)
    rng.shuffle(blocks)
    fb = []
    for t, (r, pid) in enumerate(blocks, 1):
        fb.append(f"## {t}\nREADING: {rp[(r, pid)]}\nFACTS:\n" + numbered(facts[pid]) + "\n")
        pairs.append({"kind": "facts", "r": r, "pid": pid, "j": "f1", "t": t})
    put(sc / "judge/f1", {"task.md": (D.parent / "retell1/tasks/judge_facts.md").read_text(), "items.md": "".join(fb)})
    json.dump(pairs, open(D / "pairs.json", "w"), ensure_ascii=False)
    print("листы судей:", [sum(p.get("j") == j for p in pairs) for j in range(1, JUDGES + 1)], "; блоков фактов:", len(blocks))


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
            S.setdefault((p["r"], p["i"]), []).append(v)
    per = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        per[arm] = np.array([np.mean([v for r in rr for v in S[(r, i)] if v is not None]) for i in range(N)])
    out = ["# tpx1 — результат", "", f"## Предложения (dev, {N}), смысл 0–3"]
    for arm in ARMS:
        out.append(f"  {arm}: {per[arm].mean():.2f}")
    for a, b in (("tpx", "tp"), ("mc", "tpx"), ("mc", "tp")):
        d, lo, hi = boot(per[a], per[b])
        out.append(f"  {a} − {b}: {d:+.2f} [{lo:+.2f} … {hi:+.2f}]")
    ov = [tuple(v) for v in S.values() if len(v) == 2 and None not in v]
    out.append(f"  согласие судей на {len(ov)} общих парах: точно {np.mean([a == b for a, b in ov]):.0%}, ±1 {np.mean([abs(a - b) <= 1 for a, b in ov]):.0%}")
    out.append("  якоря (ожидалось → судьи): " + "; ".join(
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
    out += ["", f"## Абзацы (dev, {len(PARAS)}), доля фактов"]
    pf = {}
    for arm in ARMS:
        rr = [l["r"] for l in lists if l["lang"] == arm]
        pf[arm] = np.array([np.mean([cov[(r, p["id"])] for r in rr]) for p in PARAS])
        out.append(f"  {arm}: {pf[arm].mean():.0%}")
    for a, b in (("tpx", "tp"), ("mc", "tpx"), ("mc", "tp")):
        d, lo, hi = boot(pf[a], pf[b])
        out.append(f"  {a} − {b}: {d * 100:+.0f} п. п. [{lo * 100:+.0f} … {hi * 100:+.0f}]")
    for sub in ("answers", "judge"):
        (D / sub).mkdir(exist_ok=True)
    for l in lists:
        if l["lang"] == "tpx":
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
    {"make": make, "judges": judges, "score": score}[cmd](sc)
