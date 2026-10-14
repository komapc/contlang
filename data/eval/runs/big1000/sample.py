# 1000 случайных знаменательных слов словаря сайта (первые 10 000 по частоте, не служебные, не имена, есть в WordNet) → words.json
import json, os, random
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); S = f"{D}/../../../../site/data"
m = json.load(open(f"{S}/math.json")); wj = json.load(open(f"{S}/words.json")); bad = set(wj["stop"]) | set(wj["proper"])
pool = [w for i, w in enumerate(m["words"][:10000]) if i not in bad and w.isalpha() and len(w) > 2 and wn.synsets(w)]
random.seed(20261021); json.dump(random.sample(pool, 1000), open(f"{D}/words.json", "w")); print(len(pool))
