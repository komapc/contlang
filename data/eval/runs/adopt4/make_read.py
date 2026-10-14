# Папки читателей для обоих тестов → items.json (test, w, old, new), lists.json; SCRATCH/rN/{spec,codes}.md
import json, os, random, sys
D = os.path.dirname(os.path.abspath(__file__)); S = sys.argv[1]; random.seed(20261019)
sc = json.load(open(f"{D}/site_codes.json"))
its = [{"test": "site", "w": w, "old": a, "new": b} for w, (a, b) in sc.items() if a != b]
its += [{"test": "model", "w": o["w"], "old": o["old"], "new": o["new"]} for f in ("items.json", "items2.json") for o in json.load(open(f"{D}/model/{f}")) if o["old"] != o["new"]]
json.dump(its, open(f"{D}/items.json", "w"), indent=1); lists = []; k = 0
for test, reps in (("site", 2), ("model", 4)):
    for var, spec in (("old", "spec_old.md"), ("new", "spec_land.md")):
        ws = [o for o in its if o["test"] == test]
        for rep in range(reps):
            random.shuffle(ws); k += 1; d = f"{S}/r{k}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/../adopt3/{spec}").read()); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[var]}\n" for i, o in enumerate(ws)))
            lists.append({"r": k, "var": f"{test}_{var}", "words": [o["w"] for o in ws]})
json.dump(lists, open(f"{D}/lists.json", "w"), indent=1); print("читателей", k, {t: sum(o["test"] == t for o in its) for t in ("site", "model")})
