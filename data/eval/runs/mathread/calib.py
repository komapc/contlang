"""Калибровочный набор для бесплатных мер читаемости: коды с известным cos первого ответа слепого Haiku со словом (полный Numberbatch).
Коды математики (этот тест, codes_*.json) и коды моделей из слепых тестов links и pi_for (key.json; цели и наполнители).
    .venv/bin/python data/eval/runs/mathread/calib.py data/raw/numberbatch-en-19.08.txt.gz   → calib.json: [{w, code, src, c1}] (среднее по декодерам)"""
import glob, gzip, json, os, re, sys
from collections import defaultdict
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); RUNS = os.path.dirname(D)
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
def read(f):
    a = {}
    for l in open(f):
        m = re.match(r"\s*(\d+)\.\s*(.*)", l)
        if m: a[int(m[1])] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:1]
    return a
items = []   # (src, слово, код, ответ)
for run in ("links", "pi_for"):
    k = json.load(open(f"{RUNS}/{run}/key.json"))
    for f in sorted(glob.glob(f"{RUNS}/{run}/dec_*_[ab].md")):
        s = str(int(os.path.basename(f)[4:6])); a = read(f)
        for i, (w, c, t) in enumerate(k["sheets"][s], 1): items.append((run, w, c, (a.get(i) or ["—"])[0]))
for kf in glob.glob(f"{D}/key_*.json"):
    name = os.path.basename(kf)[4:-5]; key = json.load(open(kf)); codes = {c["w"]: c["code"] for c in json.load(open(f"{D}/codes_{name}.json"))}
    for f in sorted(glob.glob(f"{D}/dec_{name}_*_[ab].md")):
        sh = os.path.basename(f)[4:-5]; a = read(f)
        for i, w in enumerate(key[sh], 1): items.append((f"math_{name}", w, codes[w], (a.get(i) or ["—"])[0]))
need = set()
for _, w, _, p in items: need |= {w} | set(toks(p)) | {"_".join(toks(p))}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]
    return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
g = defaultdict(list)
for src, w, c, p in items:
    a, b = vec.get(w), pv(p); g[(src, w, c)].append(float(a @ b) if a is not None and b is not None else 0.0)
out = [{"src": s, "w": w, "code": c, "c1": float(np.mean(v)), "n": len(v)} for (s, w, c), v in g.items()]
json.dump(out, open(f"{D}/calib.json", "w"), indent=0)
for s in sorted({o["src"] for o in out}): rs = [o for o in out if o["src"] == s]; print(s, len(rs), f"cos {np.mean([o['c1'] for o in rs]):.2f}")
