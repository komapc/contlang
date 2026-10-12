# Место с синонимами: глаголы A (нынешняя спецификация) против B (значение головного корня = конечное состояние, K+3 = каузатив).
# Логика как в ../friend/score.py. Две кодировки (codes_1, codes_2) × два читателя (a, b) = 160 ответов на вариант.
#   .venv/bin/python data/eval/runs/verbs/score.py data/raw/numberbatch-en-19.08.txt.gz
import gzip, json, os, re, sys, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); NB = sys.argv[1]
items = [re.match(r"\d+\. (.+?) \(verb\)", l)[1] for l in open(f"{D}/items.md") if l.strip()]
N = len(items); CTRL = set(range(34, N))  # sit … walk: действия без смены состояния
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for v in "ab":
    for e in "12":
        for r in "ab":
            for l in open(f"{D}/{v}/ans_{e}_{r}.md"):
                m = re.match(r"\s*(\d+)\.\s*(.*)", l)
                if m and int(m[1]) <= N: ans[(v, e, r, int(m[1]))] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()]
key = lambda w: w.replace(" ", "_")
words = json.load(open(f"{D}/../../../../site/data/math.json"))["words"]; words += [key(w) for w in items if key(w) not in set(words)]
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
def place(p, w):
    v = pv(p); ix = [WI[x] for x in {l.name().lower() for s in wn.synsets(key(w)) if s.pos() == "v" for l in s.lemmas()} | {key(w)} if x in WI]
    if v is None or not ix: return len(W)
    s = M @ v; return int((s > s[ix].max()).sum()) + 1
gm = lambda xs: round(float(np.exp(np.mean(np.log(xs)))), 1)
out = {}; idx = [(e, r, i) for e in "12" for r in "ab" for i in range(N)]
for v in "ab": out[v] = np.array([place(ans[(v, e, r, i + 1)][0], items[i]) for e, r, i in idx])
ctrl = np.array([i in CTRL for _, _, i in idx]); rng = np.random.default_rng(0)
for name, mask in (("все 40", ~np.zeros_like(ctrl)), ("смена состояния (34)", ~ctrl), ("контроль (6)", ctrl)):
    a, b = out["a"][mask], out["b"][mask]; rat = np.log(b) - np.log(a)
    bs = [np.exp(rat[rng.integers(0, len(rat), len(rat))].mean()) for _ in range(5000)]
    print(f"{name}: A {gm(a)} (первым {int((a == 1).sum())}/{len(a)}), B {gm(b)} (первым {int((b == 1).sum())}/{len(b)}), B/A {np.exp(rat.mean()):.2f} 95 % {np.round(np.percentile(bs, [2.5, 97.5]), 2)}")
print()
for i, w in enumerate(items):
    sel = [k for k, (_, _, j) in enumerate(idx) if j == i]
    print(f"{w}: A {[ans[('a', e, r, i + 1)][0] for e, r, _ in [idx[k] for k in sel]]} {gm(out['a'][sel])} | B {[ans[('b', e, r, i + 1)][0] for e, r, _ in [idx[k] for k in sel]]} {gm(out['b'][sel])}")
