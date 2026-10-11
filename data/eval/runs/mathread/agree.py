"""Тест 3: согласие двух слепых читателей. Для каждого кода — cos первых ответов декодеров a и b (полный Numberbatch); мера без правильного ответа.
Отделяет «непонятно» (читатели расходятся) от «понятно, но не то» (сошлись, но не на слове). Коды математики (этот тест) и моделей (links, pi_for).
    .venv/bin/python data/eval/runs/mathread/agree.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
from collections import defaultdict
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); RUNS = os.path.dirname(D)
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
def read(f):
    a = {}
    for l in open(f):
        m = re.match(r"\s*(\d+)\.\s*(.*)", l)
        if m: a[int(m[1])] = ([x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()] or ["—"])[0]
    return a
pairs = defaultdict(dict)   # (src, лист, номер) → {a/b: ответ}, слово
words = {}
for run in ("links", "pi_for"):
    k = json.load(open(f"{RUNS}/{run}/key.json"))
    for f in sorted(glob.glob(f"{RUNS}/{run}/dec_*_[ab].md")):
        s = str(int(os.path.basename(f)[4:6])); d = os.path.basename(f)[-4]
        for i, ans in read(f).items():
            if i <= len(k["sheets"][s]): pairs[(run, s, i)][d] = ans; words[(run, s, i)] = k["sheets"][s][i - 1][0]
for kf in glob.glob(f"{D}/key_*.json"):
    name = os.path.basename(kf)[4:-5]; key = json.load(open(kf))
    for f in sorted(glob.glob(f"{D}/dec_{name}_*_[ab].md")):
        sh = os.path.basename(f)[4:-5]; d = os.path.basename(f)[-4]
        for i, ans in read(f).items(): pairs[("math", sh, i)][d] = ans; words[("math", sh, i)] = key[sh][i - 1]
need = set()
for k, v in pairs.items(): need |= {words[k]} | {t for p in v.values() for t in toks(p) + ["_".join(toks(p))]}
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
cos = lambda a, b: float(a @ b) if a is not None and b is not None else 0.0
rows = []
for k, v in pairs.items():
    if "a" not in v or "b" not in v: continue
    w = vec.get(words[k]); a, b = pv(v["a"]), pv(v["b"])
    rows.append(dict(src="математика" if k[0] == "math" else "модели", agree=cos(a, b), hit=(cos(w, a) + cos(w, b)) / 2, same=v["a"].lower() == v["b"].lower()))
print("## Тест 3. Согласие двух слепых читателей\n")
print("| коды | n | ответы совпали | согласие cos ≥ 0,5 | из них близко к слову | расходятся (cos < 0,3) | среднее согласие | Спирмен согласия с близостью к слову |\n|---|--:|--:|--:|--:|--:|--:|--:|")
def sp(x, y):
    rx, ry = np.argsort(np.argsort(x)), np.argsort(np.argsort(y)); return float(np.corrcoef(rx, ry)[0, 1])
for s in ("модели", "математика"):
    rs = [r for r in rows if r["src"] == s]; ag = [r for r in rs if r["agree"] >= .5]
    print(f"| {s} | {len(rs)} | {sum(r['same'] for r in rs)} | {len(ag)} | {sum(r['hit'] >= .5 for r in ag)} | {sum(r['agree'] < .3 for r in rs)} | {np.mean([r['agree'] for r in rs]):.2f} | {sp([r['agree'] for r in rs], [r['hit'] for r in rs]):.2f} |")
