# Новые слова (все доступные; 150 для теста выбирает occam.py): из ../reader2/pool_words.json без прочитанных в reader2, без шумовых и без общих баз с прочитанными.   python pick_words.py
import json, random, os
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../reader2"
pool, used = json.load(open(f"{R}/pool_words.json")), set(json.load(open(f"{R}/test_words.json")))
NOISE = {"dos", "gilbert", "jay", "semi", "rick", "entity", "smith", "harry", "franklin", "cooper", "brad", "turkey", "eagles", "herald"}  # шум и имена
from nltk.corpus import wordnet as wn
def base(w):
    for p in ("n", "v", "a"):
        b = wn._morphy(w, p)
        if b: return b[0]
    return w
ub = {base(w) for w in used}
rest = [w for w in pool if w not in used and w not in NOISE and base(w) not in ub]
ws = rest; json.dump(ws, open(f"{D}/test_words.json", "w"))
print(len(rest), "доступно;", ws[:20])
