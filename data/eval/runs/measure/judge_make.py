# Пары (слово, первый ответ) для слепого судьи: A, SZ, H, E, без повторов, перемешаны. → judge_pairs.json, $1/jN/pairs.md
import json, os, re, random, sys
D = os.path.dirname(os.path.abspath(__file__)); E = f"{D}/.."
items = json.load(open(f"{E}/twowords2/items.json"))
V = {"A": "twowords2/a", "SZ": "measure/sz", "H": "twowords3/h", "E": "twowords2/e"}
P = {}
for n, d in V.items():
    for k in "12":
        for r in "12":
            for l in open(f"{E}/{d}/ans_{k}_{r}.md"):
                m = re.match(r"\s*(\d+)\.\s*(.*)", l)
                if m and 1 <= int(m[1]) <= 50:
                    i = (int(k) - 1) * 50 + int(m[1]) - 1; a = re.split(r"[|,]", m[2])[0].strip().lower()
                    P.setdefault((items[i]["w"], a), []).append([n, r, i])
keys = list(P); random.Random(0).shuffle(keys); per = -(-len(keys) // 4)
out = []
for j in range(4):
    ch = keys[j * per:(j + 1) * per]; d = f"{sys.argv[1]}/j{j + 1}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch)))
    out += [{"j": j + 1, "t": t + 1, "w": w, "a": a, "who": P[(w, a)]} for t, (w, a) in enumerate(ch)]
json.dump(out, open(f"{D}/judge_pairs.json", "w"), indent=0); print(len(keys), per)
