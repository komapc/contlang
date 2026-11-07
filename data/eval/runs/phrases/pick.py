# Фразы для теста (dec.md): двусловные леммы WordNet (имена и фразовые глаголы), у которых есть вектор фразы в Numberbatch,
# оба слова среди 5000 частых слов сайта, частота в SemCor ≥ 2, слитного написания нет в словаре, без чисел и be/have.
# Сложение смысла: comp = cos(вектор фразы, среднее векторов слов). Нижняя треть — «устойчивые», верхняя — «свободные»;
# по 15 случайных (seed) в каждой клетке «часть речи × группа» → 60 фраз. Векторы фраз и среднего — в vecs.json (как у сайта: int8).
#   .venv/bin/python data/eval/runs/phrases/pick.py
import gzip, json, os, random, nltk, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../..")
nltk.data.path.insert(0, f"{REPO}/data/raw/nltk")
from nltk.corpus import wordnet as wn
m = json.load(open(f"{REPO}/site/data/math.json")); rank = {w: i for i, w in enumerate(m["words"])}
BAD = {"be", "have", "one", "two", "three", "ten", "hundred", "thousand", "million"}
cand = {}
for p in "nv":
    for s in wn.all_synsets(p):
        for le in s.lemmas():
            n = le.name()
            if n.count("_") != 1 or n != n.lower() or n in cand: continue
            a, b = n.split("_")
            if a in BAD or b in BAD or rank.get(a, 1e9) > 5000 or rank.get(b, 1e9) > 5000 or a + b in rank: continue
            if sum(x.count() for x in wn.lemmas(n, p)) >= 2: cand[n] = p
need = set(cand) | {w for n in cand for w in n.split("_")}; vec = {}
with gzip.open(f"{REPO}/data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
    next(f)
    for l in f:
        k = l[:l.index(" ")]
        if k in need: vec[k] = np.array(l.split()[1:], dtype=float)
q = lambda x: (lambda y: y / np.linalg.norm(y))(np.round(x / np.linalg.norm(x) * 127))  # как vocab.bin
rows = []
for n, p in cand.items():
    a, b = n.split("_")
    if n not in vec or a not in vec or b not in vec: continue
    mean = q(vec[a]) + q(vec[b]); rows.append((n, p, float(q(vec[n]) @ (mean / np.linalg.norm(mean)))))
random.seed(20261107); items = []
for p in "nv":
    r = sorted((x for x in rows if x[1] == p), key=lambda x: x[2]); t = len(r) // 3
    for g, part in (("fixed", r[:t]), ("free", r[-t:])):
        items += [{"phrase": n.replace("_", " "), "pos": p, "group": g, "comp": round(c, 3)} for n, _, c in random.sample(part, 15)]
    print(p, len(r), "кандидатов; граница трети", round(r[t][2], 3), round(r[-t][2], 3))
json.dump(items, open(f"{D}/items.json", "w"), indent=0, ensure_ascii=False)
V = {}
for it in items:
    n = it["phrase"].replace(" ", "_"); a, b = n.split("_"); mean = q(vec[a]) + q(vec[b])
    V[it["phrase"]] = {"B": np.round(q(vec[n]), 6).tolist(), "C": np.round(mean / np.linalg.norm(mean), 6).tolist()}
json.dump(V, open(f"{D}/vecs.json", "w"))
for g in ("fixed", "free"):
    for p in "nv": print(g, p, ", ".join(f"{i['phrase']} {i['comp']}" for i in items if i["group"] == g and i["pos"] == p))
