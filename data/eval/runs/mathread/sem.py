"""Слепое чтение математических кодов Haiku (②): cos первого ответа со словом (полный Numberbatch; фраза — склеенный токен или сумма слов),
«близко» — cos ≥ 0,5, точное попадание — вторичная мера. Рядом — круг математики (①) и бесплатные признаки кода: какие предсказывают, что Haiku понял код.
    .venv/bin/python data/eval/runs/mathread/sem.py data/raw/numberbatch-en-19.08.txt.gz dev base"""
import glob, gzip, json, os, re, sys
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); nb, SET, VAR = sys.argv[1], sys.argv[2], sys.argv[3]
key = json.load(open(f"{D}/key_{SET}_{VAR}.json")); codes = {c["w"]: c for c in json.load(open(f"{D}/codes_{SET}_{VAR}.json"))}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = []   # (лист, декодер, номер, [ответы])
for f in sorted(glob.glob(f"{D}/dec_{SET}_{VAR}_*_[ab].md")):
    sh = os.path.basename(f)[4:-3]
    for l in open(f):
        m = re.match(r"\s*(\d+)\.\s*(.*)", l)
        if m: ans.append((sh, sh[-1], int(m[1]), [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:3]))
need = set(codes)
for *_, a in ans:
    for p in a: need |= set(toks(p)) | {"_".join(toks(p))}
vec = {}
with gzip.open(nb, "rt") as fh:
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
same = lambda p, w: (lambda t: t == w or t.rstrip("s") == w or t.rstrip("d") == w or t.rstrip("ed") == w or t.rstrip("ing") == w)(" ".join(toks(p)))
rows = []
for sh, dec, i, a in ans:
    w = key[sh[:-2]][i - 1]; c = codes[w]; cs = [cos(vec.get(w), pv(p)) for p in a] or [0]
    rows.append(dict(w=w, form=c["form"], code=c["code"], pair=bool(c["pair"]), first=a[0] if a else "—", c1=cs[0], c3=max(cs), h1=bool(a) and same(a[0], w),
                     mrank=c["rank"], mcos=c["cos1"], n=len(c["roots"]), minsingle=min(r["single"] for r in c["roots"]), meansingle=np.mean([r["single"] for r in c["roots"]]),
                     maxplace=max(r["place"] for r in c["roots"]), weak=sum(1 for r in c["roots"] if r["v"] in (-1, 0, 1, 2, -2) and r["name"] not in ("PLACE", "THING", "TEXT", "BODY", "SOMEONE")),
                     head_single=c["roots"][0]["single"]))
R = lambda rs, k: np.mean([r[k] for r in rs])
print(f"## {SET}/{VAR}: {len(rows)} прочтений ({len(codes)} слов × декодеры)\n")
print(f"- Haiku: cos первого {R(rows, 'c1'):.2f}, лучший из трёх {R(rows, 'c3'):.2f}, близко (cos ≥ 0,5) {sum(r['c1'] >= .5 for r in rows)}, точно {sum(r['h1'] for r in rows)}")
print(f"- математика (те же коды): первыми {sum(c['rank'] == 1 for c in codes.values())}/{len(codes)}, cos первого {np.mean([c['cos1'] for c in codes.values()]):.2f}")
for f in "oiae": rs = [r for r in rows if r["form"] == f]; print(f"- часть речи {f}: n {len(rs)}, Haiku cos {R(rs, 'c1'):.2f}, близко {sum(r['c1'] >= .5 for r in rs)}")
for p in (False, True): rs = [r for r in rows if r["pair"] == p]; print(f"- {'пара' if p else 'одно слово'}: n {len(rs)}, Haiku cos {R(rs, 'c1'):.2f}, близко {sum(r['c1'] >= .5 for r in rs)}")
print("\n## Признаки кода и читаемость (корреляция Спирмена с cos первого ответа Haiku)\n")
def sp(x, y):
    rx, ry = np.argsort(np.argsort(x)), np.argsort(np.argsort(y)); return float(np.corrcoef(rx, ry)[0, 1])
y = [r["c1"] for r in rows]
for k, name in [("minsingle", "наименьшая близость корня к слову"), ("meansingle", "средняя близость корней"), ("head_single", "близость главного корня"),
                ("maxplace", "худшее место корня среди ближайших к слову"), ("n", "число корней"), ("weak", "корней со слабым уровнем (|v| ≤ 2)"), ("mcos", "cos первого прочтения математики"), ("mrank", "место у математики")]:
    print(f"- {name}: {sp([r[k] for r in rows], y):+.2f}")
print("\n## По словам\n\n| слово | код | Haiku первым (cos) | математика |\n|---|---|---|---|")
by = {}
for r in rows: by.setdefault(r["w"], []).append(r)
for w, rs in sorted(by.items(), key=lambda t: -np.mean([r["c1"] for r in t[1]])):
    print(f"| {w} | `{rs[0]['code']}` | " + ", ".join(f"{r['first']} ({r['c1']:.2f})" for r in rs) + f" | {codes[w]['top'][0]} ({codes[w]['rank']}) |")
