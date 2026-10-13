# Кодер-«определение», шаг 0: из WordNet для каждого существительного — толкование первого смысла и род (гипероним).
# Род: лемма гиперонима первого смысла, одно слово из словаря сайта; если такой нет — уровнем выше (до 5).
# Слова: 100 слов ../twowords2 и 300 случайных существительных из «других 1000» (для круга математики). → wn.json
#   .venv/bin/python data/eval/runs/definition/wn.py
import json, os, random
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.join(D, "../../../..")
vocab = set(json.load(open(f"{REPO}/site/data/math.json"))["words"])
test = [l.split("\t")[0] for l in open(f"{D}/../twowords2/words.tsv")]
nouns = [w for w in open(f"{D}/../twowords2/nouns.txt").read().split() if w not in set(test)]
random.Random(3).shuffle(nouns)
def genus(s):
    lvl = [s]
    for _ in range(5):
        lvl = [h for x in lvl for h in x.hypernyms() + x.instance_hypernyms()]
        for h in lvl:
            for l in h.lemmas():
                n = l.name().lower()
                if "_" not in n and n in vocab: return n
    return None
out = {}
for w in test + nouns[:300]:
    ss = wn.synsets(w, "n")
    if not ss: continue
    out[w] = {"gloss": ss[0].definition(), "genus": genus(ss[0]), "test": w in test}
json.dump(out, open(f"{D}/wn.json", "w"), indent=1)
print(len(out), "без рода:", [w for w, e in out.items() if not e["genus"]][:20])
print({w: out[w]["genus"] for w in test[:30]})
