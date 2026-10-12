"""Эталон Токипоны: те же 100 слов dev (смысл — толкование WordNet), Haiku кодирует в Токипону и в min-co, два слепых Haiku читают.
Меры как в ../mathread/sem.py: cos первого ответа со словом (полный Numberbatch), близко — cos ≥ 0,5, точно; плюс лучший из трёх.
Рядом — коды математики на тех же словах (../mathread/dec_dev_base_*).   .venv/bin/python data/eval/runs/toki/score.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); MR = os.path.join(D, "..", "mathread")
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]  # noqa: E731
def load(pattern, key, name_of):
    out = []   # (слово, [ответы])
    for f in sorted(glob.glob(pattern)):
        ws = key[name_of(f)]
        for l in open(f):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if m and int(m[1]) <= len(ws): out.append((ws[int(m[1]) - 1], [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:3]))
    return out
key = json.load(open(f"{D}/key.json")); kb = json.load(open(f"{MR}/key_dev_base.json"))
A = {"Токипона (Haiku)": load(f"{D}/ans_tp_*_[ab].md", key, lambda f: os.path.basename(f)[7:9]),
     "min-co (Haiku)": load(f"{D}/ans_mc_*_[ab].md", key, lambda f: os.path.basename(f)[7:9]),
     **({"min-co v2 (Haiku)": load(f"{D}/ans_mc2_*_[ab].md", key, lambda f: os.path.basename(f)[8:10])} if glob.glob(f"{D}/ans_mc2_*") else {}),
     "min-co (математика)": load(f"{MR}/dec_dev_base_*_[ab].md", kb, lambda f: os.path.basename(f)[4:-5])}
need = {w for a in A.values() for w, ps in a for p in ps for w in toks(p) + ["_".join(toks(p))]} | {w for a in A.values() for w, _ in a}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
cos = lambda p, w: float(pv(p) @ vec[w]) if pv(p) is not None and w in vec else 0.0  # noqa: E731
same = lambda p, w: (lambda t: t == w or t.rstrip("s") == w.rstrip("s") or t.rstrip("ed") == w.rstrip("e") or t.rstrip("ing") == w.rstrip("e") or t.rstrip("ly") == w.rstrip("ly"))(" ".join(toks(p)))  # noqa: E731
L = ["| язык (кто кодирует) | прочтений | cos первого | лучший из трёх | близко (cos ≥ 0,5) | точно первым | точно среди трёх |", "|---|--:|--:|--:|--:|--:|--:|"]
for n, a in A.items():
    c1 = [cos(ps[0], w) if ps else 0 for w, ps in a]; cb = [max([cos(p, w) for p in ps] or [0]) for w, ps in a]
    L.append(f"| {n} | {len(a)} | {np.mean(c1):.2f} | {np.mean(cb):.2f} | {sum(c >= .5 for c in c1)} | {sum(bool(ps) and same(ps[0], w) for w, ps in a)} | {sum(any(same(p, w) for p in ps) for w, ps in a)} |")
tp = {}; mc = {}
for d, a in ((tp, A["Токипона (Haiku)"]), (mc, A["min-co (Haiku)"])):
    for w, ps in a: d.setdefault(w, []).append(ps[0] if ps else "—")
cods = {}
for k, ws in key.items():
    for pref in ("tp", "mc"):
        for i, l in enumerate(open(f"{D}/codes_{pref}_{k}.md")):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if m and int(m[1]) <= len(ws): cods[(pref, ws[int(m[1]) - 1])] = m[2].strip()
L += ["", "| слово | Токипона | прочтения | min-co | прочтения |", "|---|---|---|---|---|"]
for k, ws in key.items():
    for w in ws: L.append(f"| {w} | {cods.get(('tp', w), '')} | {', '.join(tp.get(w, []))} | `{cods.get(('mc', w), '')}` | {', '.join(mc.get(w, []))} |")
open(f"{D}/score.md", "w").write("\n".join(L) + "\n"); print("\n".join(L[:5]))

# Размер неопределённости: место загаданного слова среди словаря сайта (math.json words) по cos с ответом читателя.
# «В N раз точнее» = среднее геометрическое места в N раз меньше. Доли точных так не сравнить: 21 × 10 > 200.
words = json.load(open(os.path.join(D, "../../../../site/data/math.json")))["words"]
miss = [w for w in words if w not in vec]
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh); want = set(miss)
    for l in fh:
        w = l[:l.find(" ")]
        if w in want: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
W = [w for w in words if w in vec]; M = np.stack([vec[w] for w in W])
def place(p, w):
    v = pv(p)
    if v is None or w not in vec: return len(W)
    s = M @ v; return int((s > float(vec[w] @ v)).sum()) + 1
L2 = ["", f"Место загаданного слова среди {len(W)} слов словаря по близости к ответу (1 — ответ ближе всего к нему):", "",
      "| язык | среднее геометрическое (первый ответ) | медиана | среднее геометрическое (лучший из трёх) | медиана |", "|---|--:|--:|--:|--:|"]
gm, PL = {}, {}
for n, a in A.items():
    p1 = [place(ps[0], w) if ps else len(W) for w, ps in a]; pb = [min([place(p, w) for p in ps] or [len(W)]) for w, ps in a]
    g1, gb = float(np.exp(np.mean(np.log(p1)))), float(np.exp(np.mean(np.log(pb)))); gm[n] = (g1, gb); PL[n] = [(w, x) for (w, _), x in zip(a, p1)]
    L2.append(f"| {n} | {g1:.0f} | {int(np.median(p1))} | {gb:.0f} | {int(np.median(pb))} |")
t = gm["Токипона (Haiku)"]
L2 += ["", "Во сколько раз неопределённость меньше, чем у Токипоны: " + "; ".join(f"{n} — {t[0] / g[0]:.1f} (первый), {t[1] / g[1]:.1f} (лучший из трёх)" for n, g in gm.items() if not n.startswith("Токи"))]
txt = open(f"{D}/score.md").read().split("\n\n| слово")
open(f"{D}/score.md", "w").write(txt[0] + "\n" + "\n".join(L2) + "\n\n| слово" + txt[1]); print("\n".join(L2))
json.dump(PL, open(f"{D}/places.json", "w"), ensure_ascii=False)   # место первого ответа по словам — для разбора ошибок

# Варианты меры «в N раз точнее» (те же ответы): биты неопределённости = log2 места; место с синонимами (любое слово
# из синсетов WordNet загаданного слова в его части речи считается попаданием); ошибка 1 − cos; доля попаданий в первые k.
from nltk.corpus import wordnet as wn
POS = {}
for f in glob.glob(f"{D}/items_*.md"):
    for l in open(f):
        m = re.match(r"\s*\d+\.\s*(\S+) \((\w+)\)", l)
        if m: POS[m[1]] = {"noun": "n", "verb": "v", "adjective": "as", "adverb": "r"}[m[2]]
WI = {w: i for i, w in enumerate(W)}
def syns(w):
    s = {l.name().lower() for ss in wn.synsets(w) if ss.pos() in POS.get(w, "nvasr") for l in ss.lemmas()}
    return [WI[x] for x in s | {w} if x in WI]
def place_syn(p, w):
    v = pv(p); ix = syns(w)
    if v is None or not ix: return len(W)
    s = M @ v; return int((s > float(s[ix].max())).sum()) + 1
L3 = ["", "Варианты меры (первый ответ):", "", "| язык | место | бит (log2 места) | место с синонимами | бит | 1 − cos | в первых 10 | в первых 10 с синонимами |", "|---|--:|--:|--:|--:|--:|--:|--:|"]
for n, a in A.items():
    p1 = np.array([place(ps[0], w) if ps else len(W) for w, ps in a]); s1 = np.array([place_syn(ps[0], w) if ps else len(W) for w, ps in a])
    e = np.mean([1 - cos(ps[0], w) if ps else 1 for w, ps in a])
    L3.append(f"| {n} | {np.exp(np.log(p1).mean()):.0f} | {np.log2(p1).mean():.1f} | {np.exp(np.log(s1).mean()):.0f} | {np.log2(s1).mean():.1f} | {e:.2f} | {(p1 <= 10).sum()} | {(s1 <= 10).sum()} |")
txt = open(f"{D}/score.md").read().split("\n\n| слово")
open(f"{D}/score.md", "w").write(txt[0] + "\n" + "\n".join(L3) + "\n\n| слово" + txt[1]); print("\n".join(L3))
