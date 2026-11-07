# 120 фраз: 60 из ../phrases (устойчивые/свободные, имена/глаголы) + 60 из ../phrases2 (4 класса свободных сочетаний) → items.json,
# коды математики A (пословно, как в тех тестах) → codes.json["A"].  .venv/bin/python data/eval/runs/phrases3/make.py
import json, os
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); P1, P2 = f"{D}/../phrases", f"{D}/../phrases2"
it, A = [], {}
for x in json.load(open(f"{P1}/items.json")):
    ph = x["phrase"]; ss = wn.synsets(ph.replace(" ", "_"), x["pos"])
    it.append({"phrase": ph, "src": "phrases", "grp": x["group"] + "_" + x["pos"], "form": "i" if x["pos"] == "v" else "o",
               "gloss": ss[0].definition() if ss else None})
    A[ph] = json.load(open(f"{P1}/codes.json"))[ph]["A"]
c2 = json.load(open(f"{P2}/codes.json"))
for x in json.load(open(f"{P2}/items.json")):
    ph = x["phrase"]; it.append({"phrase": ph, "src": "phrases2", "grp": x["cls"], "form": None, "gloss": None}); A[ph] = c2[ph]["A"]
assert len(it) == 120 == len(A) == len({i["phrase"] for i in it})
json.dump(it, open(f"{D}/items.json", "w"), indent=0); json.dump({"A": A}, open(f"{D}/codes.json", "w"), indent=0)
print(len(it), "фраз;", sum(bool(i["gloss"]) for i in it), "с толкованием WordNet")
