# Доля «близко» по вариантам и парные сравнения по словам (бутстрэп).  python compare.py A H HP HO  [--pairs X/Y,...]
import json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R = json.load(open(f"{D}/readings.json")); L = json.load(open(f"{D}/labels.json"))
args = [a for a in sys.argv[1:] if not a.startswith("--")]; pr = next((a[8:] for a in sys.argv if a.startswith("--pairs=")), "")
S = {}; CODE = {(o["v"], o["i"]): o["code"] for o in R}
for o in R:
    if o["v"] in args: S.setdefault(o["v"], {}).setdefault(o["i"], []).append(L.get(f"{o['w']}\t{o['ans'][0] if o['ans'] else '—'}", -1))
rng = np.random.default_rng(0)
for v in args:
    a = np.array([x for xs in S[v].values() for x in xs]); assert (a >= 0).all(), f"нет оценок у {v}"
    print(f"{v}: близко {(a == 2).mean():.0%}, рядом+ {(a >= 1).mean():.0%}  (n {len(a)})")
for p in (pr.split(",") if pr else [f"{x}/{args[0]}" for x in args[1:]]):
    x, y = p.split("/"); I = sorted(set(S[x]) & set(S[y]))
    if "--changed" in sys.argv: I = [i for i in I if CODE[(x, i)].split("|")[0].strip() != CODE[(y, i)].split("|")[0].strip() or CODE[(x, i)] != CODE[(y, i)]]
    d = np.array([np.mean(np.array(S[x][i]) == 2) - np.mean(np.array(S[y][i]) == 2) for i in I])
    bs = [d[rng.integers(0, len(d), len(d))].mean() for _ in range(5000)]
    print(f"{x} − {y} ({len(I)} слов): {d.mean():+.0%} [{np.percentile(bs, 2.5):+.0%} … {np.percentile(bs, 97.5):+.0%}]")
