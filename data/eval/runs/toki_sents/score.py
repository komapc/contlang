"""Тест 9: те же 100 слов dev, но в предложении; слово отмечено `< >`. Haiku переводит предложение в Токипону и в min-co (v2),
два слепых Haiku читают всё предложение и называют отмеченное слово. Мера как в ../toki: место с синонимами WordNet среди
10 721 слова словаря сайта (+ загаданные слова), рядом — те же слова из теста на одиночных словах (../toki/places.json не хватает: считается заново).
    .venv/bin/python data/eval/runs/toki_sents/score.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
import numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(D, "..", "toki")
key = json.load(open(f"{T}/key.json"))
POS = {}
for f in glob.glob(f"{T}/items_*.md"):
    for l in open(f):
        m = re.match(r"\s*\d+\.\s*(\S+) \((\w+)\)", l)
        if m: POS[m[1]] = {"noun": "n", "verb": "v", "adjective": "as", "adverb": "r"}[m[2]]
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]  # noqa: E731
def load(pattern, sents):
    out = []
    for f in sorted(glob.glob(pattern)):
        k = re.search(r"_(\d\d)_[ab]\.md$", f)[1]; ws = key[k]
        for l in open(f):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if not m or int(m[1]) > 20: continue
            body = m[2].split("||")[-1] if sents else m[2]
            out.append((ws[int(m[1]) - 1], [x.strip() for x in re.split(r"[|,]", body) if x.strip()][:3]))
    return out
A = {"Токипона, слово": load(f"{T}/ans_tp_*_[ab].md", 0), "min-co v2, слово": load(f"{T}/ans_mc2_*_[ab].md", 0),
     "Токипона, предложение": load(f"{D}/ans_tp_*_[ab].md", 1), "min-co v2, предложение": load(f"{D}/ans_mc_*_[ab].md", 1)}
words = json.load(open(os.path.join(D, "../../../../site/data/math.json")))["words"]; words += [w for w in POS if w not in set(words)]
need = set(words) | {x for a in A.values() for _, ps in a for p in ps for x in toks(p) + ["_".join(toks(p))]}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
W = [w for w in words if w in vec]; WI = {w: i for i, w in enumerate(W)}; M = np.stack([vec[w] for w in W])
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
def place(p, w):
    v = pv(p); ix = [WI[x] for x in {l.name().lower() for s in wn.synsets(w) if s.pos() in POS[w] for l in s.lemmas()} | {w} if x in WI]
    if v is None or not ix: return len(W)
    s = M @ v; return int((s > s[ix].max()).sum()) + 1
g = lambda x: float(np.exp(np.mean(np.log(x))))  # noqa: E731
L = [f"Место с синонимами среди {len(W)} слов (первый ответ; лучший из трёх), 200 прочтений:", "", "| язык, что читают | прочтений | место | бит | лучший из трёх | точно первым |", "|---|--:|--:|--:|--:|--:|"]
PL = {}
for n, a in A.items():
    p1 = np.array([place(ps[0], w) if ps else len(W) for w, ps in a]); pb = np.array([min([place(p, w) for p in ps] or [len(W)]) for w, ps in a])
    PL[n] = {}; [PL[n].setdefault(w, []).append(int(x)) for (w, _), x in zip(a, p1)]
    L.append(f"| {n} | {len(a)} | {g(p1):.1f} | {np.log2(p1).mean():.1f} | {g(pb):.1f} | {(p1 == 1).sum()} |")
rng = np.random.default_rng(0); ws = sorted(POS)
def ratio(x, y):  # во сколько раз место x больше места y, бутстреп по словам
    lr = np.array([np.mean(np.log(PL[x][w])) - np.mean(np.log(PL[y][w])) for w in ws if w in PL[x] and w in PL[y]])
    bs = [np.exp(lr[rng.integers(0, len(lr), len(lr))].mean()) for _ in range(5000)]
    return f"{np.exp(lr.mean()):.2f} (95 %: {np.percentile(bs, 2.5):.2f}–{np.percentile(bs, 97.5):.2f})"
L += ["", f"- Токипона / min-co на предложениях: {ratio('Токипона, предложение', 'min-co v2, предложение')}",
      f"- Токипона / min-co на словах: {ratio('Токипона, слово', 'min-co v2, слово')}",
      f"- min-co: слово / предложение: {ratio('min-co v2, слово', 'min-co v2, предложение')}",
      f"- Токипона: слово / предложение: {ratio('Токипона, слово', 'Токипона, предложение')}"]
open(f"{D}/score.md", "w").write("\n".join(L) + "\n"); print("\n".join(L))
json.dump(PL, open(f"{D}/places.json", "w"), ensure_ascii=False)
