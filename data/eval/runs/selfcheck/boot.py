# Парный бутстреп (5000) ① первыми на 2000 слов (1000 + другие 1000) против «сейчас» (weights/results.json, 0,6/0,6).
import json, random, os
D = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(D, "../weights/results.json")))["0.6,0.6"]
V = {**json.load(open(os.path.join(D, "results_head.json"))), **json.load(open(os.path.join(D, "results2.json")))}
def first(v): return [1 if x["r"] == 1 else 0 for x in v["r1"] + v["r2"]]
def boot(a, b, B=5000, seed=1):
    rnd = random.Random(seed); n = len(a); d = [x - y for x, y in zip(a, b)]
    s = sorted(sum(d[rnd.randrange(n)] for _ in range(n)) for _ in range(B))
    return sum(d), s[int(.025 * B)], s[int(.975 * B)]
for k, v in V.items():
    f, lo, hi = boot(first(v), first(base))
    print(f"{k}: ① 2000 {f:+d} (95 % {lo:+d}…{hi:+d})")
f, lo, hi = boot(first(V["самопроверка (голова та же) + штраф"]), first(V["самопроверка, голова та же"]))
print(f"штраф поверх самопроверки: {f:+d} (95 % {lo:+d}…{hi:+d})")
