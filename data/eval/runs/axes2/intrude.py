# Тест на лишнее слово: 20 новых осей (набор «новые», k = 20), 38 осей корней (semaxis), 20 осей PCA.
#   python intrude.py make SC → items.json, SC/iN/items.md (каждое задание — у двух читателей);  python intrude.py score SC → intrusion.md
import json, random, re, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from space import D, Z, V, direction, words, rank, unit
cmd, S = sys.argv[1], sys.argv[2]
if cmd == "make":
    C = {c["name"] + "|" + c["src"]: c for c in json.load(open(D / "candidates.json"))}
    sets = {"новые": [C[k] for k in json.load(open(D / "chosen.json"))["новые|20"]],
            "корни": [c for c in C.values() if c["src"] == "roots"],
            "PCA": [{"name": f"PC{j + 1}", "pos": [], "neg": [], "src": "pca"} for j in range(20)]}
    for c in sets["новые"] + sets["корни"]: c["d"] = direction(c["pos"], c["neg"])[0]
    for j, c in enumerate(sets["PCA"]): c["d"] = V[j]
    ok = rank < 6000; rnd = random.Random(20261014); its = []
    for st, axes in sets.items():
        reps = 2 if st == "новые" else 1
        tops = []
        for a in axes:
            ex = set(a["pos"]) | set(a["neg"]); p = Z @ a["d"]
            for sg in (1, -1):
                o = [i for i in np.argsort(-sg * p) if ok[i] and words[i] not in ex][:20]; tops.append((a, sg, o))
        for a, sg, o in tops:
            p = np.abs(Z @ a["d"]); low = set(np.where(p < np.quantile(p, 0.5))[0])
            others = [i for b, _, ob in tops if b is not a for i in ob if i in low and i not in o]
            for r in range(reps):
                four = rnd.sample(o[:20], 4); intr = rnd.choice(others); ws = [words[i] for i in four] + [words[intr]]; rnd.shuffle(ws)
                its.append({"set": st, "axis": a["name"], "sign": sg, "words": ws, "intruder": words[intr]})
    rnd.shuffle(its); json.dump(its, open(D / "items.json", "w"), indent=0)
    half = len(its) // 2
    for h, ch in enumerate((its[:half], its[half:])):
        for rep in (1, 2):
            d = Path(S) / f"i{2 * h + rep}"; d.mkdir(parents=True, exist_ok=True); order = list(range(len(ch))); random.Random(rep).shuffle(order)
            (d / "items.md").write_text("".join(f"{k + 1}. {', '.join(ch[i]['words'])}\n" for k, i in enumerate(order)))
            (d / "order.json").write_text(json.dumps([i + h * half for i in order]))
    print(len(its), "заданий", {s: sum(i["set"] == s for i in its) for s in sets}); sys.exit()
its = json.load(open(D / "items.json")); hits = {}
for k in range(1, 5):
    d = Path(S) / f"i{k}"; order = json.loads((d / "order.json").read_text())
    a = {int(m[1]): m[2].strip().strip("*`").lower() for x in open(d / "answers.md") if (m := re.match(r"\s*(\d+)\.\s*(\S+)", x))}
    for n, i in enumerate(order): hits.setdefault(i, []).append(a.get(n + 1) == its[i]["intruder"])
(D / "answers").mkdir(exist_ok=True)
for k in range(1, 5): (D / "answers" / f"i{k}.md").write_text((Path(S) / f"i{k}" / "answers.md").read_text())
L = ["# Тест на лишнее слово", "", "Каждое задание — у двух читателей Haiku; доля верно найденных лишних слов (случайно 20 %).", "",
     "| набор | заданий | верно | 95 % |", "|---|--:|--:|---|"]
for st in ("новые", "корни", "PCA"):
    x = np.array([h for i, it in enumerate(its) if it["set"] == st for h in hits[i]], float); rng = np.random.default_rng(0)
    ids = [i for i, it in enumerate(its) if it["set"] == st]
    bs = [np.mean([h for i in rng.choice(ids, len(ids)) for h in hits[i]]) for _ in range(3000)]
    L.append(f"| {st} | {len(ids)} | {x.mean():.0%} | {np.percentile(bs, 2.5):.0%} … {np.percentile(bs, 97.5):.0%} |")
L += ["", "## По осям (доля верных по обоим полюсам и читателям)", "", "| набор | ось | верно | слабый полюс: слова → ответ |", "|---|---|--:|---|"]
for st in ("новые", "корни", "PCA"):
    ax = {}
    for i, it in enumerate(its):
        if it["set"] == st: ax.setdefault(it["axis"], []).append(i)
    for a, ids in sorted(ax.items(), key=lambda t: np.mean([h for i in t[1] for h in hits[i]])):
        w = min(ids, key=lambda i: np.mean(hits[i]))
        L.append(f"| {st} | {a} | {np.mean([h for i in ids for h in hits[i]]):.0%} | {', '.join(its[w]['words'])} (лишнее {its[w]['intruder']}) |")
(D / "intrusion.md").write_text("\n".join(L) + "\n"); print("\n".join(L[:9]))
