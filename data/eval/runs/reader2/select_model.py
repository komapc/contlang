# Правило выбора кода (условный логит по парам кодов одного слова): разница признаков → кто прочитан лучше.
# Признаки: число корней, нулей, слабых значений (|v| ≤ 1), среднее |v|, cos модели читателя v2 (без слова), cos математики.
# Перекрёстная проверка по словам: доля верных пар, отдельно — пар кодов математики.   python select_model.py
import json, re, sys, os, itertools, collections, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../three2")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proxy import vec, X, ix, m, ri, LINK
from choose import f2
D = os.path.dirname(os.path.abspath(__file__))
C, A = np.array(m["dict"]["C"]), np.array(m["dict"]["A"]); S, HW = m["s"], m["head_w"]
def toks(c): return [(r, int(v) if v else None) for r, v in re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", c.split("|")[0]) if r in ri]
def mcos(c, t):
    y = np.zeros(300)
    for k, (r, v) in enumerate(toks(c)): y += (1 if k == 0 else HW) * (C[ri[r]] + S * (v or 0) * A[ri[r]])
    return float(y @ t / (np.linalg.norm(y) + 1e-9))
def struct(c):
    t = toks(c); v = [x for _, x in t if x is not None]
    return [len(t), sum(x == 0 for x in v), sum(abs(x) <= 1 for x in v), np.mean([abs(x) for x in v]) / 5 if v else 0]
NAMES = ["корней", "нулей", "слабых", "ср.|v|", "cos модели", "cos математики"]
def feat(c, t, B):
    p = f2(c) @ B; return np.array(struct(c) + [float(p @ t / np.linalg.norm(p)), mcos(c, t)])
def logit(Xd, lam=1.0, it=300):
    w = np.zeros(Xd.shape[1])
    for _ in range(it):
        p = 1 / (1 + np.exp(-Xd @ w)); g = Xd.T @ (p - 1) + lam * w; H = (Xd.T * (p * (1 - p))) @ Xd + lam * np.eye(len(w)); w -= np.linalg.solve(H, g)
    return w
if __name__ == "__main__":
    rd = [o for o in json.load(open(f"{D}/readings_all.json")) if o["w"] in ix and vec(o["ans"]) is not None and not LINK.search(o["code"])]
    words = sorted({o["w"] for o in rd}); g = {w: i % 5 for i, w in enumerate(np.random.default_rng(1).permutation(words))}
    from choose import train
    Fz = np.zeros((len(rd), 6))
    for k in range(5):
        B = train([o for o in rd if g[o["w"]] != k])
        for i, o in enumerate(rd):
            if g[o["w"]] == k: Fz[i] = feat(o["code"], X[ix[o["w"]]], B)
    by = collections.defaultdict(list)
    for i, o in enumerate(rd): by[o["w"]].append(i)
    P = [(a, b) if rd[a]["score"] > rd[b]["score"] else (b, a) for ii in by.values() for a, b in itertools.combinations(ii, 2) if rd[a]["code"] != rd[b]["code"] and rd[a]["score"] != rd[b]["score"]]
    mu, sd = Fz.mean(0), Fz.std(0) + 1e-9; Z = (Fz - mu) / sd
    ok, okm, W = [], [], []
    for k in range(5):
        tr = [(a, b) for a, b in P if g[rd[a]["w"]] != k]; te = [(a, b) for a, b in P if g[rd[a]["w"]] == k]
        Xd = np.concatenate([Z[[a for a, _ in tr]] - Z[[b for _, b in tr]], Z[[b for _, b in tr]] - Z[[a for a, _ in tr]]])
        y = np.r_[np.ones(len(tr)), np.zeros(len(tr))]
        w = logit(Xd * (2 * y[:, None] - 1)); W.append(w)  # знак: лучший − худший → «1»
        for a, b in te:
            r = (Z[a] - Z[b]) @ w > 0; ok.append(r)
            if "llm" not in rd[a]["run"] and "llm" not in rd[b]["run"]: okm.append(r)
    w = np.mean(W, 0); print("веса (z):", ", ".join(f"{n} {x:+.2f}" for n, x in zip(NAMES, w)))
    print(f"пары: {np.mean(ok):.1%} (n {len(ok)});  пары кодов математики: {np.mean(okm):.1%} (n {len(okm)})")
    for j, n in enumerate(NAMES):
        print(f"   один признак «{n}»: {np.mean([(Z[a, j] - Z[b, j]) * np.sign(w[j]) > 0 for a, b in P if 'llm' not in rd[a]['run'] and 'llm' not in rd[b]['run']]):.1%} на парах математики")
    json.dump({"w": w.tolist(), "mu": mu.tolist(), "sd": sd.tolist()}, open(f"{D}/select_w.json", "w"))
