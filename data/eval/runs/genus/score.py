"""Слепое чтение кодов «род + отличие» (идея 5) против кодов сайта на тех же 100 словах dev: cos первого ответа Haiku со словом
и со значением (единичная сумма: слово ×2, синонимы и слова толкования WordNet, как в genus.js), «близко» — cos ≥ 0,5, точно — вторичная мера.
Отдельно — слова, у которых есть род (гипероним), и остальные (у них код сайта и код рода совпадают по построению или почти).
    .venv/bin/python data/eval/runs/genus/score.py data/raw/numberbatch-en-19.08.txt.gz"""
import glob, gzip, json, os, re, sys
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); MR = os.path.join(D, "..", "mathread")
S = json.load(open(f"{D}/senses.json")); codes = {c["w"]: c for c in json.load(open(f"{D}/codes_dev_genus.json"))}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
def answers(d, var):
    key = json.load(open(f"{d}/key_dev_{var}.json")); out = []   # (слово, декодер, [ответы])
    for f in sorted(glob.glob(f"{d}/dec_dev_{var}_*_[ab].md")):
        sh = os.path.basename(f)[4:-5]
        for l in open(f):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if m and int(m[1]) <= len(key[sh]): out.append((key[sh][int(m[1]) - 1], f[-4], [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:3]))
    return out
A = {"сайт": answers(MR, "base"), "род+отличие": answers(D, "genus")}
need = set(codes)
for w in codes: need |= set(S[w]["lemmas"]) | set(S[w]["gloss"])
for a in A.values():
    for *_, ps in a:
        for p in ps: need |= set(toks(p)) | {"_".join(toks(p))}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
unit = lambda v: v / (np.linalg.norm(v) + 1e-9)  # noqa: E731
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]
    return unit(np.sum(vs, 0)) if vs else None
def sense(w):
    s = S[w]; parts = [vec[w], vec[w]] + [vec[x] for x in s["lemmas"] + s["gloss"] if x in vec]
    return unit(np.mean(parts, 0))
cos = lambda a, b: float(a @ b) if a is not None and b is not None else 0.0  # noqa: E731
same = lambda p, w: (lambda t: t == w or t.rstrip("s") == w or t.rstrip("d") == w or t.rstrip("ed") == w or t.rstrip("ing") == w)(" ".join(toks(p)))  # noqa: E731
lines = ["| коды | слова | прочтений | cos со словом | cos со значением | близко к слову | близко к значению | точно |", "|---|---|--:|--:|--:|--:|--:|--:|"]
for grp, keep in (("все", lambda w: True), ("с родом", lambda w: bool(codes[w].get("genus"))), ("без рода", lambda w: not codes[w].get("genus"))):
    for name, a in A.items():
        r = [(w, ps) for w, _, ps in a if w in vec and keep(w)]
        cw = [cos(pv(ps[0]), vec[w]) if ps else 0 for w, ps in r]; cs = [cos(pv(ps[0]), sense(w)) if ps else 0 for w, ps in r]
        ex = sum(bool(ps) and same(ps[0], w) for w, ps in r)
        lines.append(f"| {name} | {grp} | {len(r)} | {np.mean(cw):.2f} | {np.mean(cs):.2f} | {sum(c >= .5 for c in cw)} | {sum(c >= .5 for c in cs)} | {ex} |")
# по словам с родом: первые ответы обоих кодов рядом
rows = ["", "| слово | значение | код рода | ответы | код сайта | ответы |", "|---|---|---|---|---|---|"]
by = {n: {} for n in A}
for n, a in A.items():
    for w, d, ps in a: by[n].setdefault(w, []).append(ps[0] if ps else "—")
for w, c in codes.items():
    if c.get("genus"): rows.append(f"| {w} | {c['synset']} | `{c['code']}` | {', '.join(by['род+отличие'].get(w, []))} | `{c['base']}` | {', '.join(by['сайт'].get(w, []))} |")
open(f"{D}/score.md", "w").write("\n".join(lines + rows) + "\n"); print("\n".join(lines))
