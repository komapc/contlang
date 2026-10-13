# Парный бутстреп (5000) разниц против весов 0,6/0,6: ① первыми на r1+r2 (2000 слов) и cos кодов моделей.
import json, random, os
D = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(D, "results.json")))
base = d["0.6,0.6"]
def first(v): return [1 if x["r"] == 1 else 0 for x in v["r1"] + v["r2"]]
def boot(a, b, B=5000, seed=1):
    rnd = random.Random(seed); n = len(a); diff = [x - y for x, y in zip(a, b)]
    s = sorted(sum(diff[rnd.randrange(n)] for _ in range(n)) for _ in range(B))
    return sum(diff), s[int(.025 * B)], s[int(.975 * B)]
for k, v in d.items():
    if k == "0.6,0.6": continue
    f, lo, hi = boot(first(v), first(base))
    c, clo, chi = boot(v["calib"], base["calib"])
    n = len(v["calib"])
    print(f"{k:8} ① 2000: {f:+4d} (95 % {lo:+d}…{hi:+d}) | коды моделей cos {c/n:+.3f} (95 % {clo/n:+.3f}…{chi/n:+.3f})")
