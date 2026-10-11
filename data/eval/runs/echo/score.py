"""Слепое чтение кодов с эхо-уровнями (A, кодер сайта) и без них (B): cos первого ответа Haiku со словом (полный Numberbatch), близко — cos ≥ 0,5,
точно — вторичная мера; попарно по словам — у какого кода ответ ближе.   .venv/bin/python data/eval/runs/echo/score.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); key = json.load(open(f"{D}/key.json")); codes = {c["w"]: c for c in json.load(open(f"{D}/codes.json"))}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]  # noqa: E731
ans = {"A": {}, "B": {}}   # версия → слово → [первые ответы]
for f in sorted(glob.glob(f"{D}/dec_echo_*_[ab].md")):
    sh = os.path.basename(f)[4:-5]
    for l in open(f):
        m = re.match(r"\s*(\d+)\.\s*(.*)", l)
        if m and int(m[1]) <= len(key[sh]): ans[sh.split("_")[1]].setdefault(key[sh][int(m[1]) - 1], []).append((re.split(r"[|,]", m[2])[0]).strip())
need = set(codes) | {t for v in ans.values() for a in v.values() for p in a for t in toks(p) + ["_".join(toks(p))]}
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
same = lambda p, w: " ".join(toks(p)).rstrip("s") == w.rstrip("s")  # noqa: E731
L = ["| коды | прочтений | cos со словом | близко | точно | математика первыми |", "|---|--:|--:|--:|--:|--:|"]
for v in "AB":
    cs = [cos(p, w) for w, a in ans[v].items() for p in a]; ex = sum(same(p, w) for w, a in ans[v].items() for p in a)
    L.append(f"| {v} | {len(cs)} | {np.mean(cs):.2f} | {sum(c >= .5 for c in cs)} | {ex} | {sum(c['r' + v] == 1 for c in codes.values())} |")
d = [np.mean([cos(p, w) for p in ans["B"].get(w, [])] or [0]) - np.mean([cos(p, w) for p in ans["A"].get(w, [])] or [0]) for w in codes]
L += ["", f"по словам: B лучше {sum(x > .05 for x in d)}, хуже {sum(x < -.05 for x in d)}, так же {sum(abs(x) <= .05 for x in d)}; средняя разница {np.mean(d):+.3f}", "",
      "| слово | A | ответы | B | ответы |", "|---|---|---|---|---|"]
for w, c in codes.items(): L.append(f"| {w} | `{c['A']}` | {', '.join(ans['A'].get(w, []))} | `{c['B']}` | {', '.join(ans['B'].get(w, []))} |")
open(f"{D}/score.md", "w").write("\n".join(L) + "\n"); print("\n".join(L[:6] + L[7:8]))
