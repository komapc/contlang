# Все прошлые слепые чтения одного кода (100 слов × 2 читателя × вариант) → readings.json: {v, w, i, r, code, ans}
import glob, json, os, re
D = os.path.dirname(os.path.abspath(__file__)); E = f"{D}/.."
items = json.load(open(f"{E}/twowords2/items.json"))
V = {"A": "twowords2/a", "B": "twowords2/b", "H": "twowords3/h", "T": "taxonomy/t", "M": "taxonomy/mr", "N": "distill/n", "S": "definition/s",
     "GTS": "definition/gts", "B3": "bold/b3", "B5": "bold/b5", "MZ": "measure/mz", "TZ": "measure/tz", "SZ": "measure/sz", "HP": "diag/hp", "HO": "diag/ho", "Hc": "values/hc", "SZp": "values/szp", "H2": "newroots/h2", "SZ2": "newroots/sz2", "CO": "combo/combo"}
rd = lambda f: {int(m[1]): m[2].strip() for l in open(f) if (m := re.match(r"\s*(\d+)\.\s*(.*)", l))}
out = []
for v, d in V.items():
    for k in (1, 2):
        codes = rd(f"{E}/{d}/codes_{k}.md")
        for fn in sorted(glob.glob(f"{E}/{d}/ans_{k}_*.md")):
            r = int(fn.rsplit("_", 1)[1][:-3]); a = rd(fn)
            for n in range(1, 51):
                i = (k - 1) * 50 + n - 1
                out.append({"v": v, "w": items[i]["w"], "i": i, "r": r, "code": codes[n], "ans": [x.strip().lower() for x in re.split(r"[|,]", a.get(n, "")) if x.strip()][:3]})
json.dump(out, open(f"{D}/readings.json", "w"), indent=0)
u = {(o["w"], o["ans"][0] if o["ans"] else "") for o in out}; print(len(out), "чтений,", len(u), "уникальных пар")
