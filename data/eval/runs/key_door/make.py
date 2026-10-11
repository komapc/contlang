"""Листы: на каждом по одному варианту key, door, lock, open и 6 наполнителей; второе слово ключа не совпадает с door/lock/open того же листа."""
import json, random, re
def grab(f, w): return [l.split(": ", 1)[1].strip() for l in open(f) if l.startswith(w + " ")]
uniq = lambda xs: list(dict.fromkeys(xs))
G = {w: uniq(grab("enc_A.md", w) + grab("enc_B.md", w)) for w in ("door", "lock", "open", "key")}
G["open"] = [c for c in G["open"] if c != "JOIN(=-5) DO(=+3) | i"]  # тот же код, другой порядок
G["key"] += ["DO(=+5) BIG(=-4) | o PI DO(=+5) JOIN(=+5) CAN(=-3) | o", "DO(=+5) | o PI PART(=-2) PLACE SIDE(=+5) | o"]
FILL = {"book": "TEXT PART(=+2) | o", "brush": "TOUCH(=-3) MOVE DO(=+5) | o", "car": "DO(=+5) MOVE(=+4) | o", "hammer": "TOUCH(=+5) MOVE(=+4) DO(=+5) | o",
        "kitchen": "PLACE HEAT(=+3) CONSUME(=+5) | o", "knife": "JOIN(=-4) TOUCH(=+4) DO(=+5) | o", "ladder": "MOVE ABOVE(=+4) DO(=+5) | o",
        "library": "PLACE TEXT PART(=+5) | o", "house": "PLACE INSIDE(=+5) LIVE | o", "mountain": "PLACE ABOVE(=+5) BIG(=+4) | o"}
rnd = random.Random(11); n = len(G["key"]); sheets = {}
body = lambda c: re.sub(r"\s*\|.*", "", c).strip()
for s in range(1, n + 1):
    k = G["key"][s - 1]; second = body(k.split(" PI ")[1])
    while True:
        pick = {w: G[w][(s - 1 + rnd.randrange(len(G[w]))) % len(G[w])] for w in ("door", "lock", "open")}
        if all(body(c) != second for c in pick.values()): break
    items = [("key", k, s)] + [(w, c, G[w].index(c) + 1) for w, c in pick.items()] + [(w, c, 0) for w, c in rnd.sample(sorted(FILL.items()), 6)]
    rnd.shuffle(items); sheets[s] = items
    open(f"sheet_{s:02}.md", "w").write("".join(f"{i}. {c}\n" for i, (_, c, _) in enumerate(items, 1)))
json.dump({"G": G, "sheets": sheets}, open("key.json", "w"), indent=1)
from collections import Counter
print({w: len(v) for w, v in G.items()}, {w: Counter(x[2] for sh in sheets.values() for x in sh if x[0] == w) for w in ("door", "lock", "open")})
