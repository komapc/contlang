# Доля первых ответов в том же смысловом поле (судья Haiku: 2 близко, 1 рядом, 0 мимо), по вариантам. Ответы судьи — judge/jN.md.
import json, os, re, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); pairs = json.load(open(f"{D}/judge_pairs.json")); sc = {}
for j in range(1, 5):
    for l in open(f"{D}/judge/j{j}.md"):
        m = re.match(r"\s*(\d+)\.\s*([012])", l)
        if m: sc[(j, int(m[1]))] = int(m[2])
X = {}
for p in pairs:
    for n, r, i in p["who"]: X.setdefault(n, {})[(r, i)] = sc.get((p["j"], p["t"]), 0)
rng = np.random.default_rng(0); miss = sum((p["j"], p["t"]) not in sc for p in pairs)
print(f"пар {len(pairs)}, без оценки {miss}")
for n in ["A", "SZ", "H", "E"]:
    a = np.array([X[n].get((r, i), 0) for i in range(100) for r in "12"]); bs = [(a[rng.integers(0, 200, 200)] == 2).mean() for _ in range(2000)]
    print(f"{n}: близко {(a == 2).mean():.0%} [{np.percentile(bs, 2.5):.0%}–{np.percentile(bs, 97.5):.0%}], хотя бы рядом {(a >= 1).mean():.0%}, мимо {(a == 0).mean():.0%}")
