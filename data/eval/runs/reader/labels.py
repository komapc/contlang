# Оценки судьи для всех чтений → labels.json {"w\ta": 0|1|2}; согласие судей на 60 повторных парах; доля «близко» по вариантам.
import json, os, re, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); J = json.load(open(f"{D}/judge_pairs.json"))
old = {(w, a): s for w, a, s in J["old"]}
sc = {(j, int(m[1])): int(m[2]) for j in range(1, 7) for l in open(f"{D}/judge/j{j}.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
new = {(p["w"], p["a"]): sc[(p["j"], p["t"])] for p in J["new"]}
rep = [(old[k], new[k]) for k in new if k in old]
print(f"согласие на {len(rep)} повторах: точно {np.mean([a == b for a, b in rep]):.0%}, «близко» да/нет {np.mean([(a == 2) == (b == 2) for a, b in rep]):.0%}")
lab = {**new, **old}; json.dump({f"{w}\t{a}": s for (w, a), s in lab.items()}, open(f"{D}/labels.json", "w"))
R = json.load(open(f"{D}/readings.json"))
by = {}
for o in R: by.setdefault(o["v"], []).append(lab[(o["w"], o["ans"][0] if o["ans"] else "—")])
for v, a in sorted(by.items(), key=lambda x: -np.mean(np.array(x[1]) == 2)): a = np.array(a); print(f"{v}: близко {(a == 2).mean():.0%}, рядом+ {(a >= 1).mean():.0%}")
