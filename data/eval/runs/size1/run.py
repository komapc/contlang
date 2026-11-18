"""size1 (dec.md): how accuracy depends on lexicon size, separately for concepts written in 1, up to 2, up to 3 words;
min-co (v2b) and Toki Pona (cipher, tpx) on the same 120 words, the same readers' protocol and the same judges.

120 content lemmas (noun / verb / adjective), 30 from each Brown frequency band 1–300, 301–1000, 1001–3000, 3001–10000.
Encoders (Sonnet, 2 per language, 60 words each) write three codes per word: 1 word, ≤ 2 words, ≤ 3 words.
Readers (Haiku): per language 3 Latin-square lists (each word once, in one of the three variants), 2 readers per list.
Judges (Sonnet): 3, each scores 2/3 of the 720 first answers (every answer scored twice), 0 off / 1 related / 2 close.
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size1/run.py make SC     → items.json, specs/, SC/w/*
    .venv/bin/python data/eval/runs/size1/run.py readers SC  → codes.json, lists.json, SC/r/*
    .venv/bin/python data/eval/runs/size1/run.py judges SC   → judge_keys.json, SC/j/*
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size1/run.py score SC → result.txt, curve.json, answers/
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
R = D.parent
SEED = 20261112
BANDS = [(1, 300), (301, 1000), (1001, 3000), (3001, 10000)]
NB = 30
NW = NB * len(BANDS)
LANGS = ["mc", "tp"]
KS = [1, 2, 3]
BASE = {"mc": 82, "tp": 120}
FUNC = set((R / "lexn1/run.py").read_text().split('FUNC = set("""')[1].split('"""')[0].split())
PN = {"NN": "n", "VB": "v", "JJ": "a"}
POSNAME = {"n": "noun", "v": "verb", "a": "adjective"}


def put(d, files):
    d.mkdir(parents=True, exist_ok=True)
    for k, v in files.items():
        (d / k).write_text(v)


def numbered(xs):
    return "".join(f"{k + 1}. {x}\n" for k, x in enumerate(xs))


def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def brown_counts():
    """lemma → Counter(pos → count) over Brown nouns, verbs, adjectives, adverbs (adverbs count only for rank)."""
    from nltk.corpus import brown, wordnet as wn
    P = dict(PN, RB="r")
    c = collections.defaultdict(collections.Counter)
    for w, t in brown.tagged_words():
        p, w = P.get(t[:2]), w.lower()
        if p and w.isalpha():
            c[wn.morphy(w, p) or w][p] += 1
    for f in FUNC:
        c.pop(f, None)
    return c


def specs():
    enc = (R / "v2b2/specs/v2b_enc.md").read_text()
    dec = (R / "v2b2/specs/v2b_dec.md").read_text()
    ph = (D / "tasks/phrases.md").read_text()
    head = enc[:enc.index("# min-co: how a word is written")]
    head = head.replace("(sentences)", "(words)").replace("You will translate English text into min-co.",
                                                           "You will encode single English words into min-co.")
    body = lambda s: s[s.index("# min-co: how a word is written"):s.index("## Two words")]
    out = {("mc", "enc"): head + body(enc) + ph + "\n" + (D / "tasks/write_mc.md").read_text(),
           ("mc", "dec"): body(dec) + ph + "\n" + (D / "tasks/read_mc.md").read_text()}
    tl = (R / "toki/enc_tp.md").read_text().splitlines()
    tl = [x for x in tl if not x.startswith("- A phrase may have any length") and not x.startswith("- Give exactly one phrase")]
    out[("tp", "enc")] = "\n".join(tl) + "\n" + (D / "tasks/write_tp.md").read_text()
    dl = (R / "toki/dec_tp.md").read_text().splitlines()
    xl = (R / "tpx1/specs/tpx_dec.md").read_text().splitlines()
    out[("tp", "dec")] = ("# Decoder instructions (single-word test, Language X)\n\n" + dl[2].replace("Toki Pona phrase", "Language X phrase")
                          + "\n\n" + "\n".join(xl[2:5]) + "\n" + (D / "tasks/read_tp.md").read_text())
    return out


def make(sc):
    from nltk.corpus import wordnet as wn
    c = brown_counts()
    rank = {w: k + 1 for k, (w, _) in enumerate(sorted(c.items(), key=lambda x: -sum(x[1].values())))}
    used = {x["w"] for x in json.load(open(R / "func1/items.json"))}
    rng = random.Random(SEED)
    items = []
    for lo, hi in BANDS:
        pool = []
        for w, r in rank.items():
            if not (lo <= r <= hi) or len(w) < 3 or w in used or (w.endswith("s") and w[:-1] in c):
                continue
            p = max(("n", "v", "a"), key=lambda q: c[w][q])
            if c[w][p] == 0 or c[w][p] < 0.5 * sum(c[w].values()):
                continue
            ss = [s for s in wn.synsets(w, p) if w in s.lemma_names()]
            if ss:
                pool.append({"w": w, "pos": POSNAME[p], "gloss": ss[0].definition(), "rank": r, "band": lo})
        items += rng.sample(pool, NB)
    rng.shuffle(items)
    json.dump(items, open(D / "items.json", "w"), indent=0)
    print("by pos:", collections.Counter(x["pos"] for x in items))
    sp = specs()
    (D / "specs").mkdir(exist_ok=True)
    for (lang, kind), s in sp.items():
        (D / f"specs/{lang}_{kind}.md").write_text(s)
    for lang in LANGS:
        for k in (1, 2):
            part = items[(k - 1) * 60:k * 60]
            put(sc / f"w/{lang}{k}", {"spec.md": sp[(lang, "enc")],
                                      "list.md": numbered(f"{x['w']} ({x['pos']}): {x['gloss']}" for x in part)})


def encipher(text, cipher):
    return re.sub(r"\b[a-z]+\b", lambda m: cipher.get(m[0], m[0]), text)


def nwords(lang, code):
    return len(re.findall(r"\{", code)) if lang == "mc" else len(code.split())


def readers(sc):
    cipher = json.load(open(R / "tpx1/cipher.json"))
    codes, raw = {}, {}
    for lang in LANGS:
        rows = []
        for k in (1, 2):
            a = parse_numbered(sc / f"w/{lang}{k}/answers.md")
            assert len(a) == 60, (lang, k, len(a))
            for i in range(1, 61):
                v = [x.strip().strip("`") for x in a[i].split("||")]
                assert len(v) == 3, (lang, k, i, a[i])
                rows.append(v)
        raw[lang] = rows
        codes[lang] = [[encipher(x, cipher) if lang == "tp" else x for x in v] for v in rows]
    json.dump({"codes": codes, "tp_plain": raw["tp"]}, open(D / "codes.json", "w"), indent=1, ensure_ascii=False)
    sp = specs()
    lists = []
    for lang in LANGS:
        for s in range(3):
            for rep in (1, 2):
                rid = f"{lang}{s + 1}{'ab'[rep - 1]}"
                rng = random.Random(f"size1-{rid}")
                order = [(i, (i + s) % 3 + 1) for i in range(NW)]
                rng.shuffle(order)
                put(sc / f"r/{rid}", {"spec.md": sp[(lang, "dec")], "codes.md": numbered(codes[lang][i][k - 1] for i, k in order)})
                lists.append({"r": rid, "lang": lang, "order": order})
    json.dump(lists, open(D / "lists.json", "w"))
    for lang in LANGS:
        for k in KS:
            n = [nwords(lang, raw[lang][i][k - 1]) for i in range(NW)]
            print(lang, k, "words per code:", np.mean(n).round(2), collections.Counter(n))


def answers(sc):
    lists = json.load(open(D / "lists.json"))
    out = {}
    for l in lists:
        a = parse_numbered(sc / f"r/{l['r']}/answers.md")
        for t, (i, k) in enumerate(l["order"]):
            out[(l["r"], i, k)] = a.get(t + 1, "—").split("|")[0].strip()
    return lists, out


def judges(sc):
    items = json.load(open(D / "items.json"))
    lists, ans = answers(sc)
    keys = sorted(ans)
    random.Random(41).shuffle(keys)
    json.dump([list(k) for k in keys], open(D / "judge_keys.json", "w"))
    third = len(keys) // 3
    parts = [keys[:third], keys[third:2 * third], keys[2 * third:]]
    for j, (a, b) in enumerate(((0, 1), (1, 2), (2, 0))):
        ks = parts[a] + parts[b]
        random.Random(f"j{j}").shuffle(ks)
        lines = [f"{t}. {items[i]['w']} ({items[i]['pos']}: {items[i]['gloss']}) — {ans[(r, i, k)]}" for t, (r, i, k) in enumerate(ks, 1)]
        put(sc / f"j/j{j + 1}", {"task.md": (D / "tasks/judge.md").read_text(), "items.md": "\n".join(lines) + "\n",
                                 "keys.json": json.dumps([list(x) for x in ks])})
    print("answers:", len(keys), "; per judge:", 2 * third)


def score(sc):
    items = json.load(open(D / "items.json"))
    lists, ans = answers(sc)
    S = collections.defaultdict(list)
    for j in (1, 2, 3):
        ks = [tuple(x) for x in json.loads((sc / f"j/j{j}/keys.json").read_text())]
        s = parse_numbered(sc / f"j/j{j}/scores.md")
        for t, key in enumerate(ks, 1):
            if t in s and s[t][:1].isdigit():
                S[key].append(int(s[t][0]))
    close = {}
    for lang in LANGS:
        for k in KS:
            rr = [l["r"] for l in lists if l["lang"] == lang]
            close[(lang, k)] = np.array([np.mean([v == 2 for r in rr for v in S.get((r, i, k), [])]) for i in range(NW)])
    rng = np.random.default_rng(0)
    idx = rng.integers(0, NW, (5000, NW))
    ci = lambda d: (100 * d.mean(), 100 * np.percentile(d[idx].mean(1), 2.5), 100 * np.percentile(d[idx].mean(1), 97.5))
    out = ["# size1 — result", "", f"## Close (judge 2 of 0–2), {NW} words, first answer, 2 readers × 2 judges per cell", ""]
    out.append("| | 1 word | ≤ 2 words | ≤ 3 words |")
    out.append("|---|---|---|---|")
    for lang in LANGS:
        out.append(f"| {lang} | " + " | ".join(f"{close[(lang, k)].mean():.0%}" for k in KS) + " |")
    out += ["", "## Paired differences, pp [95 % bootstrap over words]"]
    for lang in LANGS:
        for a, b in ((2, 1), (3, 1), (3, 2)):
            out.append("  {} k{} − k{}: {:+.1f} [{:+.1f} … {:+.1f}]".format(lang, a, b, *ci(close[(lang, a)] - close[(lang, b)])))
    for k in KS:
        out.append("  tp − mc, k{}: {:+.1f} [{:+.1f} … {:+.1f}]".format(k, *ci(close[("tp", k)] - close[("mc", k)])))
    out += ["", "## By frequency band (close)", "", "| | " + " | ".join(f"{lo}–{hi}" for lo, hi in BANDS) + " |",
            "|---|" + "---|" * len(BANDS)]
    acc = {}
    for lang in LANGS:
        for k in KS:
            row = []
            for lo, _ in BANDS:
                m = np.array([x["band"] == lo for x in items])
                acc[(lang, k, lo)] = close[(lang, k)][m].mean()
                row.append(f"{acc[(lang, k, lo)]:.0%}")
            out.append(f"| {lang} k{k} | " + " | ".join(row) + " |")
    codes = json.load(open(D / "codes.json"))
    out += ["", "## Code length (words per code)"]
    for lang in LANGS:
        src = codes["tp_plain"] if lang == "tp" else codes["codes"]["mc"]
        for k in KS:
            n = [nwords(lang, src[i][k - 1]) for i in range(NW)]
            out.append(f"  {lang} k{k}: mean {np.mean(n):.2f}, " + ", ".join(f"{a} words: {b}" for a, b in sorted(collections.Counter(n).items())))
    pairs = [tuple(v) for v in S.values() if len(v) == 2]
    out.append(f"\nJudges: exact agreement {np.mean([a == b for a, b in pairs]):.0%} on {len(pairs)} answers")
    # curve: lexicon of the N most frequent Brown lemmas; entries read right with a_lex, the rest composed with acc(band)
    c = brown_counts()
    tot = {w: sum(v.values()) for w, v in c.items()}
    order = sorted(tot, key=lambda w: -tot[w])
    T = sum(tot.values())
    band = lambda r: max(lo for lo, _ in BANDS if lo <= r)
    curve = []
    for lang in LANGS:
        for k in KS:
            for N in (0, 10, 20, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000):
                for a_lex in (1.0, 0.9):
                    u = sum(tot[w] * (a_lex if r <= N else acc[(lang, k, band(r))]) for r, w in enumerate(order, 1)) / T
                    curve.append({"lang": lang, "k": k, "N": N, "L": BASE[lang] + N, "a_lex": a_lex, "U": u})
    json.dump(curve, open(D / "curve.json", "w"), indent=0)
    out += ["", "## Share of text understood U (a_lex 0.9; words beyond rank 10 000 use the 3001–10000 band)", "",
            "| N entries | " + " | ".join(f"{l} k{k}" for l in LANGS for k in KS) + " |", "|---|" + "---|" * 6]
    for N in (0, 50, 300, 1000, 3000, 10000):
        out.append(f"| {N} | " + " | ".join(f"{next(x['U'] for x in curve if x['lang'] == l and x['k'] == k and x['N'] == N and x['a_lex'] == 0.9):.0%}"
                                           for l in LANGS for k in KS) + " |")
    out += ["", "## Per word (mc k1/k2/k3 | tp k1/k2/k3)"]
    for i in range(NW):
        out.append(f"- {items[i]['w']} ({items[i]['pos']}, {items[i]['rank']}): mc " + "/".join(f"{close[('mc', k)][i]:.1f}" for k in KS)
                   + " | tp " + "/".join(f"{close[('tp', k)][i]:.1f}" for k in KS)
                   + f" | mc3 `{codes['codes']['mc'][i][2]}` | tp3 `{codes['tp_plain'][i][2]}`")
    (D / "answers").mkdir(exist_ok=True)
    for l in lists:
        shutil.copy(sc / f"r/{l['r']}/answers.md", D / f"answers/read_{l['r']}.md")
    for lang in LANGS:
        for k in (1, 2):
            shutil.copy(sc / f"w/{lang}{k}/answers.md", D / f"answers/write_{lang}{k}.md")
    for j in (1, 2, 3):
        shutil.copy(sc / f"j/j{j}/scores.md", D / f"answers/judge_j{j}.md")
        shutil.copy(sc / f"j/j{j}/keys.json", D / f"answers/judge_j{j}_keys.json")
    (D / "result.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out[:30]))


if __name__ == "__main__":
    cmd, sc = sys.argv[1], Path(sys.argv[2])
    {"make": make, "readers": readers, "judges": judges, "score": score}[cmd](sc)
