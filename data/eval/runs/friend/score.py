# Место с синонимами: CARE/FRIEND против прежних CARE/TONE (логика как в ../toki/score.py; загаданные слова добавлены к кандидатам).
#   .venv/bin/python data/eval/runs/friend/score.py data/eval/runs/friend data/raw/numberbatch-en-19.08.txt.gz
import gzip, json, re, sys, numpy as np
from nltk.corpus import wordnet as wn
D = sys.argv[1]; NB = sys.argv[2]
items = [re.match(r"\d+\. (\S+) \((\w+)\)", l).groups() for l in open(f"{D}/friend/items.md") if l.strip()]
P = {"noun": "n", "verb": "v", "adjective": "as", "adverb": "r"}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for v in ("friend", "tone"):
    for r in "ab":
        for l in open(f"{D}/{v}/d/ans_{r}.md"):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if m and int(m[1]) <= 20: ans[(v, r, int(m[1]))] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()]
words = json.load(open("site/data/math.json"))["words"]; words += [w for w, _ in items if w not in set(words)]
vec = {}
with gzip.open(NB, "rt") as fh:
    next(fh); want = set(words) | {w for ps in ans.values() for p in ps for w in toks(p) + ["_".join(toks(p))]}
    for l in fh:
        w = l[:l.find(" ")]
        if w in want: x = np.array(l.split()[1:], float); vec[w] = x / np.linalg.norm(x)
W = [w for w in words if w in vec]; WI = {w: i for i, w in enumerate(W)}; M = np.stack([vec[w] for w in W])
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
def place(p, w, pos):
    v = pv(p); ix = [WI[x] for x in {l.name().lower() for s in wn.synsets(w) if s.pos() in P[pos] for l in s.lemmas()} | {w} if x in WI]
    if v is None or not ix: return len(W)
    s = M @ v; return int((s > s[ix].max()).sum()) + 1
out = {}
for v in ("friend", "tone"):
    pl = [place(ans[(v, r, i + 1)][0], w, pos) for r in "ab" for i, (w, pos) in enumerate(items)]
    out[v] = pl; print(v, "место с синонимами", round(float(np.exp(np.mean(np.log(pl)))), 1), "первым", sum(p == 1 for p in pl), "из", len(pl))
for i, (w, _) in enumerate(items):
    print(w, [ans[("friend", r, i + 1)][0] for r in "ab"], out["friend"][i], out["friend"][20 + i], "|", [ans[("tone", r, i + 1)][0] for r in "ab"], out["tone"][i], out["tone"][20 + i])
rat = np.log(np.array(out["friend"])) - np.log(np.array(out["tone"])); rng = np.random.default_rng(0)
bs = [np.exp(rat[rng.integers(0, len(rat), len(rat))].mean()) for _ in range(5000)]
print("FRIEND / TONE", round(float(np.exp(rat.mean())), 2), "95 %", np.round(np.percentile(bs, [2.5, 97.5]), 2))
