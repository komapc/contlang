# Новые пары (слово, первый ответ) без оценки → $1/jN/pairs.md (по ~160), new_pairs.json; после судей: judge_new.py --merge $1
import json, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); L = json.load(open(f"{D}/labels.json")); R = json.load(open(f"{D}/readings.json"))
if sys.argv[1] == "--merge":
    P = json.load(open(f"{D}/new_pairs.json")); d = sys.argv[2]
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{d}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]
    os.makedirs(f"{D}/judge", exist_ok=True); n0 = len([f for f in os.listdir(f"{D}/judge")])
    for j in {p["j"] for p in P}: open(f"{D}/judge/n{n0}_{j}.md", "w").write(open(f"{d}/j{j}/pairs.md").read() + "---\n" + open(f"{d}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(f"{D}/labels.json", "w")); print("добавлено", len(P)); sys.exit()
keys = sorted({(o["w"], o["ans"][0] if o["ans"] else "—") for o in R} - {tuple(k.split("\t")) for k in L})
n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); out = []
for j in range(n):
    ch = keys[j * per:(j + 1) * per]; d = f"{sys.argv[1]}/j{j + 1}"; os.makedirs(d, exist_ok=True)
    open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); out += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
json.dump(out, open(f"{D}/new_pairs.json", "w")); print(len(keys), "пар,", n, "судей")
