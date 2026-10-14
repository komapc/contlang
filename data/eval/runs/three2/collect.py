# Пары «код → первый ответ слепого читателя Haiku» из прошлых тестов (коды сайта и модели, одно слово) → readings.json
# [{w, code, ans, score, run}]; score — судья 2/1/0 из ../reader/labels.json (если есть).  python collect.py
import json, os, re
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/.."; L = json.load(open(f"{R}/reader/labels.json")); out = []
def ans(f): return {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
def add(run, l, f, code):
    a = ans(f)
    for i, w in enumerate(l["words"]):
        c = code(w)
        if c and i + 1 in a: out.append({"w": w, "code": c, "ans": a[i + 1], "score": L.get(f"{w}\t{a[i + 1]}"), "run": run})
for it, ls, ad, p in (("items.json", "lists.json", "answers", "r"), ("items2.json", "lists2.json", "answers2", "s")):
    I = {o["w"]: o for o in json.load(open(f"{R}/swap/{it}"))}
    for l in json.load(open(f"{R}/swap/{ls}")): add("swap", l, f"{R}/swap/{ad}/{p}{l['r']}_{l['set']}{l['var']}.md", lambda w, v=l["var"]: I[w][v])
C3 = json.load(open(f"{R}/three/codes.json"))
for l in json.load(open(f"{R}/three/lists.json")): add("three" + ("" if l["var"] == "A" else "_" + l["var"]), l, f"{R}/three/answers/t{l['r']}_{l['var']}.md", lambda w, v=l["var"]: C3[w][v])
I = {o["w"]: o for o in json.load(open(f"{R}/side_kind/items.json"))}
for l in json.load(open(f"{R}/side_kind/lists.json")): add("side_kind", l, f"{R}/side_kind/answers/r{l['r']}_{l['var']}.md", lambda w, v=l["var"]: I[w].get(v))
sc, lc = json.load(open(f"{R}/big1000/site_codes.json")), json.load(open(f"{R}/big1000/llm_codes.json"))
for l in json.load(open(f"{R}/big1000/lists.json")): add("big1000_" + l["var"], l, f"{R}/big1000/answers/r{l['r']}_{l['var']}.md", lambda w, v=l["var"]: (sc if v == "math" else lc).get(w))
F = json.load(open(f"{R}/fix1/codes.json"))
for l in json.load(open(f"{R}/fix1/lists.json")): add("fix1", l, f"{R}/fix1/answers/r{l['r']}_{l['var']}.md", lambda w, v=l["var"]: F[w]["A" if v == "V1" else v])
json.dump(out, open(f"{D}/readings.json", "w"), indent=0, ensure_ascii=False)
import collections; print(len(out), collections.Counter(o["run"] for o in out), "с оценкой", sum(o["score"] is not None for o in out))
