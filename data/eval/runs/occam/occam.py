# Вариант O (dec.md): из всех наборов корней (cand.js) — max cos − λ·(k − 1), без нулей у не главных корней с осью.
# λ — наименьшее из сетки, при котором доля 3-корневых кодов на всех 230 словах ≤ 30 % (как у кодов LLM). В тест — 150 случайных из тех,
# где O ≠ M (одинаковые коды ничего не различают).   python occam.py → codes.json
import json, os, numpy as np, collections
D = os.path.dirname(os.path.abspath(__file__)); C = json.load(open(f"{D}/cand.json")); W = json.load(open(f"{D}/test_words.json"))  # здесь — все 230 доступных (pick_words.py)
def pick(w, lam): return max((c for c in C[w]["cands"] if c["zh"] == 0), key=lambda c: c["cos"] - lam * (c["k"] - 1))
for lam in np.arange(0, 0.101, 0.005):
    ks = collections.Counter(pick(w, lam)["k"] for w in W)
    if ks[3] / len(W) <= 0.30: break
P = {w: pick(w, lam) for w in W}; best = {w: max(C[w]["cands"], key=lambda c: c["cos"]) for w in W}
print(f"λ {lam:.3f}; корней: {dict(sorted(ks.items()))}; site: {dict(sorted(collections.Counter(len([t for t in C[w]['site'].split('|')[0].split()]) for w in W).items()))}")
print(f"cos: лучший {np.mean([best[w]['cos'] for w in W]):.3f}, O {np.mean([P[w]['cos'] for w in W]):.3f}; совпадает с сайтом: {sum(P[w]['code'] == C[w]['site'] for w in W)}")
import random; random.seed(20261014); dif = [w for w in W if P[w]["code"] != C[w]["site"]]; random.shuffle(dif); seen = set(); T = []
for w in dif:  # одна форма на базу
    if C[w]["base"] not in seen and len(T) < 150: seen.add(C[w]["base"]); T.append(w)
T.sort()
print("отличаются:", sum(P[w]["code"] != C[w]["site"] for w in W), "из", len(W))
json.dump({w: {"M": C[w]["site"], "O": P[w]["code"]} for w in T}, open(f"{D}/codes.json", "w"), indent=0)
for w in T[:12]: print(f"  {w:14s} {C[w]['site']:45s} → {P[w]['code']}")
