# «Буквальный читатель»: вектор корня со значением — из слов спецификации (DEC_SPEC, строки корней): опорные точки оси
# (−5 terrible … 0 … +5 excellent), между ними — линейно; корень без значения — среднее всех его слов (или слов без оси).
# Вектор кода = Σ вес позиции × вектор корня. Меры — как в exp.py.   python specread.py
import json, re, sys, os, itertools, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../three2"))
from proxy import vec, X, ix, m, ri, LINK
D = os.path.dirname(os.path.abspath(__file__)); sp = open(f"{D}/../three2/spec.md").read()
roots = {}
for name, body in re.findall(r"^- ([A-Z]+): (.+)$", sp[sp.index("## Roots"):sp.index("## Form")], re.M):
    body = re.sub(r"\([^)]*\)", lambda t: " " + t[0][1:-1].replace("only for", "") + " ", body)  # пояснения в скобках — тоже слова
    pts = []
    for seg in body.split("…"):
        mm = re.match(r"\s*([+-]?\d)\s+(.+)", seg)
        ws = re.findall(r"[a-z]+", (mm[2] if mm else seg).lower())
        vs = [vec(w) for w in ws if vec(w) is not None and w not in {"also", "the", "of", "a", "and", "or", "it", "is", "no", "axis", "plain", "root", "means", "what", "made", "them", "unspecified", "going", "coming"}]
        if vs: pts.append((int(mm[1]) if mm else None, np.mean(vs, 0)))
    roots[name] = pts
def rv(r, v):
    pts = roots[r]; allm = np.mean([p for _, p in pts], 0)
    ax = sorted([(k, p) for k, p in pts if k is not None], key=lambda t: t[0])
    if v is None or not ax: return allm
    if v <= ax[0][0]: return ax[0][1]
    if v >= ax[-1][0]: return ax[-1][1]
    for (k1, p1), (k2, p2) in zip(ax, ax[1:]):
        if k1 <= v <= k2: t = (v - k1) / (k2 - k1); return (1 - t) * p1 + t * p2
HW = 0.6
def svec(code, hw=HW):
    t = [(r, int(v) if v else None) for r, v in re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", LINK.split(code)[0].split("|")[0]) if r in roots]
    y = sum((1 if k == 0 else hw) * rv(r, v) / np.linalg.norm(rv(r, v)) for k, (r, v) in enumerate(t)) if t else np.zeros(300)
    return y / (np.linalg.norm(y) + 1e-9)
if __name__ == "__main__":
    rd = [o for o in json.load(open(f"{D}/../three2/readings.json")) if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] in ix and o["score"] is not None]
    sc = np.array([o["score"] for o in rd]); T = np.stack([X[ix[o["w"]]] for o in rd]); Y = np.stack([vec(o["ans"]) for o in rd])
    by = {}
    for i, o in enumerate(rd): by.setdefault(o["w"], []).append(i)
    PAIRS = [(a, b) if rd[a]["score"] > rd[b]["score"] else (b, a) for ii in by.values() for a, b in itertools.combinations(ii, 2) if rd[a]["code"] != rd[b]["code"] and rd[a]["score"] != rd[b]["score"]]
    mp = [(a, b) for a, b in PAIRS if "llm" not in rd[a]["run"] and "llm" not in rd[b]["run"]]
    for hw in (0.3, 0.6, 1.0):
        S = np.stack([svec(o["code"], hw) for o in rd]); s = (S * T).sum(1)
        auc = np.mean([(p > s[sc == 0]).mean() for p in s[sc == 2]])
        print(f"вес {hw}: AUC {auc:.3f}  пары {np.mean([s[a] > s[b] for a, b in PAIRS]):.1%}  пары математики {np.mean([s[a] > s[b] for a, b in mp]):.1%}  cos(чтение, ответ) {(S * Y).sum(1).mean():.3f}")
