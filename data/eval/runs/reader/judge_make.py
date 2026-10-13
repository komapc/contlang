# Пары (слово, первый ответ) без оценки судьи → 6 файлов; 60 уже оцененных пар — для проверки согласия судей. → judge_pairs.json
import json, os, re, random, sys
D = os.path.dirname(os.path.abspath(__file__)); M = f"{D}/../measure"
old = {}
P0 = json.load(open(f"{M}/judge_pairs.json"))
sc = {(j, int(m[1])): int(m[2]) for j in range(1, 5) for l in open(f"{M}/judge/j{j}.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
for p in P0: old[(p["w"], p["a"])] = sc[(p["j"], p["t"])]
R = json.load(open(f"{D}/readings.json"))
keys = sorted({(o["w"], o["ans"][0] if o["ans"] else "—") for o in R} - set(old))
rnd = random.Random(1); chk = rnd.sample(sorted(old), 60); keys += chk; rnd.shuffle(keys); n = 6; per = -(-len(keys) // n); out = []
for j in range(n):
    ch = keys[j * per:(j + 1) * per]; d = f"{sys.argv[1]}/j{j + 1}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch)))
    out += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
json.dump({"old": [[w, a, s] for (w, a), s in old.items()], "new": out}, open(f"{D}/judge_pairs.json", "w"), indent=0); print(len(keys), per)
