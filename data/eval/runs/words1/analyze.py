"""words1 (README.md): где теряется смысл — разбор прочтений base1 и retell1 по содержательным словам, без новых агентов.

    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/words1/analyze.py   → result.txt, words.json

Разведка (exploratory), только dev. Источники: ../base1, ../retell1 (коды, прочтения, оценки судей).
"""
import collections
import json
import re
from pathlib import Path

import nltk
import numpy as np
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer

D = Path(__file__).resolve().parent
RUNS = {"base1": D.parent / "base1", "retell1": D.parent / "retell1"}
R = D.parents[3]
SENTS = json.load(open(R / "data/eval/items/bench1/sents_dev.json"))
N = len(SENTS)
LEM = WordNetLemmatizer()
STOP = set(("a an the of to in on at by for with and or but is are was were be been being am it its this that these those he she "
            "they his her their him them i we you my our your me us as from not no so than then there here which who whom what when "
            "where why how would could should will shall can may might must have has had do does did also just very too more most "
            "such only own same other into out up down over about after before again once all any both each few some nor off "
            "yet s t don get got make made one").split())
POSMAP = {"N": wn.NOUN, "V": wn.VERB, "J": wn.ADJ, "R": wn.ADV}
out = []


def say(*a):
    out.append(" ".join(str(x) for x in a))
    print(*a)


# ---------- данные ----------

def parse_numbered(path):
    return {int(m[1]): m[2].strip() for x in open(path) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}


def load_readings():
    """[(run, reader, arm, i, text, оценка — среднее судей)]"""
    rows = []
    for run, d in RUNS.items():
        lists = json.load(open(d / "lists.json"))
        pairs = json.load(open(d / "pairs.json"))
        sc = collections.defaultdict(list)
        for p in pairs:
            if p["kind"] in ("sent", "overlap") and p.get("s") is not None:
                sc[(p["r"], p["i"])].append(p["s"])
        for l in lists:
            a = parse_numbered(d / f"answers/{l['r']}_sents_out.md")
            for k, i in enumerate(l["order"]):
                rows.append((run, l["r"], l["lang"], i, a.get(k + 1, ""), float(np.mean(sc[(l["r"], i)]))))
    return rows


def codes():
    c = {"mc": json.load(open(RUNS["base1"] / "codes.json"))["mc"]["sents"],
         "tp": json.load(open(RUNS["base1"] / "codes.json"))["tp"]["sents"],
         "v2a": json.load(open(RUNS["retell1"] / "codes.json"))["v2a"]["sents"]}
    return c


# ---------- слова ----------

def content(text):
    """[(слово, лемма, pos wn)] содержательных слов (существительные, глаголы, прилагательные, наречия)."""
    toks = re.findall(r"[A-Za-z]+(?:'[a-z]+)?", text)
    res = []
    for w, t in nltk.pos_tag(toks):
        lw = w.lower()
        if t[0] not in POSMAP or lw in STOP or len(lw) < 3 or t.startswith("NNP"):
            continue
        p = POSMAP[t[0]]
        res.append((lw, LEM.lemmatize(lw, p), p))
    return res


def lemmas_any(text):
    s = set()
    for w in re.findall(r"[A-Za-z]+", text.lower()):
        s.add(w)
        for p in (wn.NOUN, wn.VERB, wn.ADJ, wn.ADV):
            s.add(LEM.lemmatize(w, p))
    return s


_rel = {}


def related(lemma, pos, loose):
    """Синонимы (общий синсет) и производные; loose — ещё гиперонимы и гипонимы на 1 шаг и похожие прилагательные."""
    key = (lemma, pos, loose)
    if key in _rel:
        return _rel[key]
    s = {lemma}
    for syn in wn.synsets(lemma, pos=pos)[:4]:
        nb = [syn]
        if loose:
            nb += syn.hypernyms() + syn.hyponyms()[:10] + syn.similar_tos()
        for x in nb:
            for l in x.lemmas():
                s.add(l.name().lower())
                if not loose:
                    continue
                for dl in l.derivationally_related_forms():
                    s.add(dl.name().lower())
        for l in syn.lemmas():
            for dl in l.derivationally_related_forms():
                s.add(dl.name().lower())
    _rel[key] = s
    return s


def kept(word, reading_lemmas, loose):
    w, lemma, pos = word
    return bool(related(lemma, pos, loose) & reading_lemmas) or lemma in reading_lemmas or w in reading_lemmas


# ---------- 1. мера «слово сохранено»: согласуется ли с судьями ----------

def recall_table(rows, loose):
    per = []
    for run, r, arm, i, text, s in rows:
        words = content(SENTS[i]["s"])
        if not words:
            continue
        rl = lemmas_any(text)
        per.append((arm, i, run, r, np.mean([kept(w, rl, loose) for w in words]), s))
    return per


# ---------- главное ----------

def main():
    rows = load_readings()
    C = codes()
    say("# words1 — где теряется смысл (разведка, dev)", "")
    say(f"прочтений: {len(rows)} (" + ", ".join(f"{a} {sum(x[2] == a for x in rows)}" for a in ("mc", "tp", "v2a")) + ")")

    say("", "## 1. Мера «слово сохранено» против оценки судей (по прочтениям)")
    tabs = {}
    for loose in (False, True):
        per = recall_table(rows, loose)
        tabs[loose] = per
        x = np.array([p[4] for p in per])
        y = np.array([p[5] for p in per])
        name = "свободная (синонимы, производные, гиперонимы/гипонимы)" if loose else "строгая (синонимы и производные)"
        say(f"  {name}: r = {np.corrcoef(x, y)[0, 1]:.2f}; доля сохранённых: " +
            ", ".join(f"{a} {np.mean([p[4] for p in per if p[0] == a]):.0%}" for a in ("mc", "v2a", "tp")))
    LOOSE = True
    per = tabs[LOOSE]

    say("", "## 2. Код или читатель: разброс оценок по 4 прочтениям одного кода (mc, tp: base1 + retell1)")
    for arm in ("mc", "tp"):
        by = collections.defaultdict(list)
        for run, r, a, i, text, s in rows:
            if a == arm:
                by[i].append(s)
        m = np.array([np.mean(by[i]) for i in range(N)])
        within = np.mean([np.var(by[i]) for i in range(N)])
        between = np.var(m)
        low = [i for i in range(N) if m[i] < 1.5]
        agree = [i for i in low if max(by[i]) - min(by[i]) <= 1]
        say(f"  {arm}: доля разброса между кодами {between / (between + within):.0%}, внутри кода (читатели и судьи) "
            f"{within / (between + within):.0%}; плохих кодов (среднее < 1,5) {len(low)}, из них все 4 прочтения "
            f"в пределах 1 балла — {len(agree)} ({len(agree) / max(len(low), 1):.0%})")

    say("", "## 3. Слова: сохранены ли (свободная мера), по всем прочтениям плеча")
    # kept[arm][(i, слово)] = доля прочтений, где сохранено
    K = collections.defaultdict(dict)
    for arm in ("mc", "v2a", "tp"):
        rs = [(i, text) for run, r, a, i, text, s in rows if a == arm]
        for i in range(N):
            texts = [t for j, t in rs if j == i]
            for w in content(SENTS[i]["s"]):
                K[arm][(i, w[1])] = np.mean([kept(w, lemmas_any(t), LOOSE) for t in texts])
    keys = list(K["mc"])
    by_pos = collections.defaultdict(lambda: collections.defaultdict(list))
    for i in range(N):
        for w in content(SENTS[i]["s"]):
            for arm in ("mc", "v2a", "tp"):
                by_pos[w[2]][arm].append(K[arm][(i, w[1])])
    names = {wn.NOUN: "существительные", wn.VERB: "глаголы", wn.ADJ: "прилагательные", wn.ADV: "наречия"}
    for p, d in by_pos.items():
        say(f"  {names[p]} ({len(d['mc'])}): " + ", ".join(f"{a} {np.mean(d[a]):.0%}" for a in ("mc", "v2a", "tp")))
    lost_both = [k for k in keys if K["mc"][k] == 0 and K["v2a"][k] == 0]
    tp_keeps = [k for k in lost_both if K["tp"][k] >= 0.5]
    say(f"  слов всего {len(keys)}; потеряны всеми прочтениями и mc, и v2a: {len(lost_both)} ({len(lost_both) / len(keys):.0%}); "
        f"из них Toki Pona сохраняет (≥ половины прочтений): {len(tp_keeps)}")
    one = [k for k in keys if (K["mc"][k] == 0) != (K["v2a"][k] == 0)]
    say(f"  потеряны в одном из двух кодирований min-co (выбор кодировщика): {len(one)} ({len(one) / len(keys):.0%})")
    say("  кандидаты в нехватку корней (потеряны в mc и v2a, сохранены в Toki Pona): " + ", ".join(sorted({k[1] for k in tp_keeps})))
    say("  потеряны везде (и в Toki Pona): " + ", ".join(sorted({k[1] for k in lost_both if K['tp'][k] == 0})))

    say("", "## 4. Покрытие словарём: есть ли понятие в глоссах спецификации читателя")
    glosses = {}
    mc_dec = (RUNS["base1"] / "specs/mc_dec.md").read_text()
    roots = mc_dec.split("## Roots", 1)[1].split("## Form marks", 1)[0]
    marks = mc_dec.split("## Form marks", 1)[1].split("## Two words", 1)[0]
    glosses["mc"] = lemmas_any(roots + " " + marks)
    tp_dec = (RUNS["base1"] / "specs/tp_dec.md").read_text()
    glosses["tp"] = lemmas_any(tp_dec.split("no other words exist):", 1)[1].split("\nPhrases:", 1)[0])
    for lang, arms in (("mc", ("mc", "v2a")), ("tp", ("tp",))):
        ins, outs = collections.defaultdict(list), collections.defaultdict(list)
        n_in = n = 0
        for i in range(N):
            for w in content(SENTS[i]["s"]):
                g = kept(w, glosses[lang], False)
                n += 1
                n_in += g
                for a in arms:
                    (ins if g else outs)[a].append(K[a][(i, w[1])])
        say(f"  {lang}: в глоссах {n_in / n:.0%} слов; сохранено: " + "; ".join(
            f"{a} — в глоссах {np.mean(ins[a]):.0%}, вне {np.mean(outs[a]):.0%}" for a in arms))

    say("", "## 5. Буквальное чтение имени корня (mc и v2a)")
    lit = collections.defaultdict(lambda: [0, 0])
    base = collections.defaultdict(lambda: [0, 0])
    for run, r, a, i, text, s in rows:
        if a not in ("mc", "v2a"):
            continue
        code = C[a][i]
        rl = lemmas_any(text)
        vals = collections.defaultdict(set)
        for root, v in re.findall(r"\b([A-Z]{2,})\(=([+-]?\d)\)", code):
            vals[root].add(int(v))
        for root in set(re.findall(r"\b([A-Z]{2,})\b", code)) - {"LA", "PI", "AND", "FROM", "FOR", "LIKE", "PE", "E"}:
            name = root.lower()
            hit = name in rl
            if vals[root] and max(vals[root]) <= -3:
                lit[root][0] += hit
                lit[root][1] += 1
            elif not vals[root] or min(vals[root]) >= 0:
                base[root][0] += hit
                base[root][1] += 1
    tot = [sum(v[0] for v in lit.values()), sum(v[1] for v in lit.values())]
    totb = [sum(v[0] for v in base.values()), sum(v[1] for v in base.values())]
    say(f"  корень только с отрицательным значением (≤ −3): имя корня в прочтении {tot[0]}/{tot[1]} ({tot[0] / max(tot[1], 1):.0%}); "
        f"корень без значения или ≥ 0: {totb[0]}/{totb[1]} ({totb[0] / max(totb[1], 1):.0%})")
    worst = sorted(((v[0] / v[1], k, v) for k, v in lit.items() if v[1] >= 4), reverse=True)[:10]
    say("  чаще всего читаются буквально при отрицательном значении: " + "; ".join(f"{k} {v[0]}/{v[1]}" for _, k, v in worst))

    (D / "result.txt").write_text("\n".join(out) + "\n")
    json.dump({a: {f"{i}:{w}": v for (i, w), v in K[a].items()} for a in K}, open(D / "words.json", "w"), indent=0, ensure_ascii=False)


if __name__ == "__main__":
    main()
