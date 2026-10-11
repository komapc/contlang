"""Тест связок (A — PI, B — FROM/FOR/PI, C — FROM/FOR/LIKE/PI, D — коды C со связками → PI): смысловая близость ответов декодеров к слову (cos в полном Numberbatch, фраза — склеенный токен или сумма слов)
и точное попадание (слово первым / среди трёх ответов). Сводка по вариантам, по группам слов (задуманная связка) и по словам.
    .venv/bin/python data/eval/runs/links/sem.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
from collections import defaultdict
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); k = json.load(open(f"{D}/key.json"))
ans = []
for f in sorted(glob.glob(f"{D}/dec_*_[ab].md")):
    s = str(int(os.path.basename(f)[4:6])); a = {}
    for l in open(f):
        m = re.match(r"\s*(\d+)\.\s*(.*)", l)
        if m: a[int(m[1])] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:3]
    ans.append((s, a))
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of"}]
need = set()
for s, a in ans:
    for i, (w, c, t) in enumerate(k["sheets"][s], 1):
        need |= set(toks(w)); [need.update(set(toks(p)) | {"_".join(toks(p))}) for p in a.get(i, [])]
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
same = lambda p, w: (lambda t: t == w or t.rstrip("s") == w or w in t.split())(" ".join(toks(p)))
rows = []
for s, a in ans:
    for i, (w, c, t) in enumerate(k["sheets"][s], 1):
        x = a.get(i, []); cs = [cos(vec.get(w), pv(p)) for p in x] or [0]
        rows.append(dict(v=k["variant"][s] if t else "fill", enc=k["encoder"][s], w=w, c=c, first=x[0] if x else "—", c1=cs[0], c3=max(cs),
                         h1=bool(x) and same(x[0], w), h3=any(same(p, w) for p in x)))
def summ(rs): return f"n {len(rs)}: первым {sum(r['h1'] for r in rs)}, среди трёх {sum(r['h3'] for r in rs)}, cos первого {np.mean([r['c1'] for r in rs]):.2f}, лучший из трёх {np.mean([r['c3'] for r in rs]):.2f}"
GROUP = {w: g for g, ws in {"FROM": "wine paper cheese leather candle", "FOR": "key lid saddle wallet sheath",
         "LIKE": "starfish seahorse jellyfish catfish sunflower", "PI": "roof petal hoof nest yolk"}.items() for w in ws.split()}
V = "ABCD"; NAME = {"A": "A — только PI", "B": "B — FROM/FOR/PI", "C": "C — FROM/FOR/LIKE/PI", "D": "D — коды C, связки → PI"}
print("## Сводка\n")
for v in V: print(f"- **{NAME[v]}**: " + summ([r for r in rows if r["v"] == v]))
print("- **наполнители**: " + summ([r for r in rows if r["v"] == "fill"]))
print("\n## По группам слов (слово первым / из n; cos первого)\n\n| группа | " + " | ".join(V) + " |\n|---|" + "---|" * len(V))
for g in ("FROM", "FOR", "LIKE", "PI"):
    cell = lambda v: (lambda rs: f"{sum(r['h1'] for r in rs)}/{len(rs)}; {np.mean([r['c1'] for r in rs]):.2f}")([r for r in rows if r["v"] == v and GROUP[r["w"]] == g])
    print(f"| {g} | " + " | ".join(cell(v) for v in V) + " |")
print("\nПо кодерам: " + "; ".join(f"{e} {v} — " + summ([r for r in rows if r["enc"] == e and r["v"] == v]) for v in V for e in sorted({r["enc"] for r in rows if r["v"] == v})))
print("\n## По словам (cos первого ответа, среднее по декодерам; что прочитано первым)\n\n| слово | " + " | ".join(V) + " |\n|---|" + "---|" * len(V))
by = defaultdict(lambda: defaultdict(list))
for r in rows:
    if r["v"] != "fill": by[r["w"]][r["v"]].append(r)
for w in GROUP:
    print(f"| {w} | " + " | ".join(f"{np.mean([r['c1'] for r in by[w][v]]):.2f} (" + ", ".join(r["first"] for r in by[w][v]) + ")" for v in V) + " |")
