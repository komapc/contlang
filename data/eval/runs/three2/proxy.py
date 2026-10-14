# Модель слепого читателя: код одного слова → вектор ожидаемого первого ответа (гребневая регрессия по признакам кода:
# корень есть / корень × значение / корень × значение² / голова, часть речи, роль). Обучение — readings.json (одно слово, без связок).
# Проверка — 5 групп по словам: cos предсказания с вектором ответа и с целью; AUC «близко (2) против мимо (0)» по cos(предсказание, цель)
# против того же у вектора, который строит математика сайта (центр корней, как читает Reader).  python proxy.py [--save]
import json, re, sys, os, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."
m = json.load(open(f"{R}/site/data/math.json")); W = m["words"]; ix = {w: i for i, w in enumerate(W)}; NM = m["names"]; ri = {n: i for i, n in enumerate(NM)}
X = np.frombuffer(open(f"{R}/site/data/vocab.bin", "rb").read(), np.int8).reshape(len(W), 300).astype(np.float32); X /= np.linalg.norm(X, axis=1, keepdims=True)
NR = len(NM); FORMS = "oiae"; ROLES = ["agent", "tool", "result", "quality"]
LINK = re.compile(r"\b(PI|FROM|FOR|LIKE)\b")
def feats(code):
    head = LINK.split(code)[0]; f = np.zeros(4 * NR + 4 + 4 + 1)
    toks = re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", head.split("|")[0]); fm = (re.search(r"\|\s*([oiae])\b", head) or [0, "o"])[1]
    for k, (r, v) in enumerate(toks):
        if r not in ri: continue
        j = ri[r]; x = int(v) / 5 if v else 0.0; f[j] = 1; f[NR + j] = x; f[2 * NR + j] = x * x - 0.3
        if k == 0: f[3 * NR + j] = 1
    f[4 * NR + FORMS.index(fm)] = 1
    for q, rl in enumerate(ROLES):
        if re.search(rf"\b{rl}\b", head): f[4 * NR + 4 + q] = 1
    f[-1] = 1; return f
def vec(w):
    w = w.strip().lower().replace(" ", "_")
    return X[ix[w]] if w in ix else None
def fit(F, Y, lam=3.0):
    return np.linalg.solve(F.T @ F + lam * np.eye(F.shape[1]), F.T @ Y)
if __name__ == "__main__":
    rd = [o for o in json.load(open(f"{D}/readings.json")) if not LINK.search(o["code"]) and vec(o["ans"]) is not None and o["w"] in ix]
    F = np.stack([feats(o["code"]) for o in rd]); Y = np.stack([vec(o["ans"]) for o in rd]); T = np.stack([X[ix[o["w"]]] for o in rd])
    sc = np.array([o["score"] for o in rd]); words = sorted({o["w"] for o in rd}); g = {w: i % 5 for i, w in enumerate(np.random.default_rng(0).permutation(words))}
    G = np.array([g[o["w"]] for o in rd]); P = np.zeros_like(Y)
    for k in range(5):
        tr = G != k; B = fit(F[tr], Y[tr]); P[~tr] = F[~tr] @ B
    P /= np.linalg.norm(P, axis=1, keepdims=True) + 1e-9
    ca, ct = (P * Y).sum(1), (P * T).sum(1)
    def auc(s, y): pos, neg = s[y == 2], s[y == 0]; return np.mean([(p > neg).mean() + 0.5 * (p == neg).mean() for p in pos])
    print(f"прочтений {len(rd)}, слов {len(words)}; cos(предсказание, ответ) {ca.mean():.3f}, cos(предсказание, цель) {ct.mean():.3f}, cos(ответ, цель) {(Y * T).sum(1).mean():.3f}")
    print(f"AUC близко/мимо по cos(предсказание, цель): {auc(ct, sc):.3f}")
    # математика сайта: вектор кода = сумма частей корней (Coder.parts) — через node дорого, грубо: среднее центров корней кода
    Cc = np.array(m["dict"]["C"]); Cc /= np.linalg.norm(Cc, axis=1, keepdims=True)
    M = np.stack([Cc[[ri[r] for r, _ in re.findall(r"([A-Z]{2,})(?:\(=([+-]?\d)\))?", o["code"].split("|")[0]) if r in ri]].mean(0) for o in rd]); M /= np.linalg.norm(M, axis=1, keepdims=True)
    print(f"AUC у центров корней (грубая математика): {auc((M * T).sum(1), sc):.3f}")
    if "--save" in sys.argv: np.save(f"{D}/proxy_B.npy", fit(F, Y)); print("сохранено proxy_B.npy")
