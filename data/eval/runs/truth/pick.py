# Слова теста: худшие (worst.json: всегда мимо при ≥ 3 прочтениях, без шума) + слова поля TRUE (codes.js --field), без слов-полюсов
# оси, без слов из строки спецификации и их форм, без прочитанных раньше (и их баз).   python pick.py FIELD.json → words.json
import json, re, sys, os, nltk
D = os.path.dirname(os.path.abspath(__file__)); nltk.data.path.insert(0, f"{D}/../../../raw/nltk")
from nltk.corpus import wordnet as wn
def bs(w): return {w} | {b for p in "nva" for b in wn._morphy(w, p)}  # все базы формы (lying → lying, lie)
r = json.load(open(f"{D}/root.json")); ex = set().union(*(bs(w) for w in r["pos"] + r["neg"] + re.findall(r"[a-z]+", r["spec"].split(":", 1)[1])))
rd = json.load(open(f"{D}/../reader2/readings_all.json")); read = {o["w"] for o in rd} | set(json.load(open(f"{D}/../occam/codes.json")))
rb = set().union(*(bs(w) for w in read))
bad = [w for w in json.load(open(f"{D}/worst.json"))["bad"] if w not in {"henry", "maria", "matt", "chuck"}]
field, seen = [], set()
for w in json.load(open(sys.argv[1])):
    b = bs(w)
    if b & (ex | rb | seen): continue
    seen |= b; field.append(w)
json.dump({"worst": bad, "field": field}, open(f"{D}/words.json", "w"), indent=0)
print(len(bad), "худших,", len(field), "слов поля:", " ".join(field))
