"""Листы для слепых декодеров: на каждом листе один вариант key, один вариант furniture и 8 наполнителей (проверенные рецепты)."""
import json, random
K = ["GRAIN(=+5) BIG(=-5) DO(=+5) | o", "DO(=+5) JOIN(=-5) GRAIN(=+5) | o", "DO(=+5) JOIN(=-5) TOUCH(=+4) | o", "DO(=+5) RULE(=+4) JOIN(=-5) | o",
     "DO(=+5) JOIN(=-5) BIG(=-5) | o", "INSIDE(=+4) CAN(=+4) DO(=+5) | o", "INSIDE(=+4) LONG(=+1) DO(=+5) | o", "INSIDE(=+4) BIG(=-4) DO(=+5) | o",
     "GRAIN(=+5) BIG(=-4) | o PI DO(=+5) JOIN(=-5) | o", "DO(=+5) JOIN(=-5) | o PI GRAIN(=+5) BIG(=-5) | o", "GRAIN(=+5) BIG(=-4) | o PI DO(=+5) RULE(=+4) | o",
     "DO(=+5) JOIN(=-5) | o PI DO(=+5) JOIN(=+5) | o", 'DO(=+5) JOIN(=-5) | o PI "iron" | o', "DO(=+5) BIG(=-4) | o PI INSIDE(=+5) JOIN(=+5) | o"]
F = ["PART(=+5) THING(=-5) INSIDE(=+5) | o", "PART(=+5) THING(=-5) MOVE(=-5) | o", "PART(=+5) THING(=-5) BIG(=+3) | o", "PART(=+5) THING(=-5) DO(=+5) | o",
     "PART(=+5) THING(=-5) PLACE | o", "PART(=+5) THING(=-5) BODY | o", "DO(=+5) PART(=+5) INSIDE(=+5) | o",
     "PART(=+5) THING(=-5) | o PI INSIDE(=+5) PLACE | o", "PART(=+5) THING(=-5) | o PI BODY | o", "PART(=+5) THING(=-5) | o PI MOVE(=-5) | o",
     "PART(=+5) THING(=-5) | o PI GRAIN(=+5) | o", "PART(=+5) THING(=-5) | o PI LONG(=+5) | o", "PART(=+5) THING(=-5) | o PI PLACE INSIDE(=+5) LIVE | o",
     "DO(=+5) PART(=+5) | o PI PLACE INSIDE(=+5) LIVE | o"]
FILL = {"book": "TEXT PART(=+2) | o", "brush": "TOUCH(=-3) MOVE DO(=+5) | o", "car": "DO(=+5) MOVE(=+4) | o", "hammer": "TOUCH(=+5) MOVE(=+4) DO(=+5) | o",
        "kitchen": "PLACE HEAT(=+3) CONSUME(=+5) | o", "knife": "JOIN(=-4) TOUCH(=+4) DO(=+5) | o", "ladder": "MOVE ABOVE(=+4) DO(=+5) | o",
        "library": "PLACE TEXT PART(=+5) | o", "machine": "THING(=-5) MOVE DO | o", "mountain": "PLACE ABOVE(=+5) BIG(=+4) | o"}
rnd = random.Random(7); key = {}
fo = list(F); rnd.shuffle(fo)
for s, (k, f) in enumerate(zip(K, fo), 1):
    items = [("key", k, K.index(k) + 1), ("furniture", f, F.index(f) + 1)] + [(w, c, 0) for w, c in rnd.sample(sorted(FILL.items()), 8)]
    rnd.shuffle(items)
    open(f"sheet_{s:02}.md", "w").write("".join(f"{i}. {c}\n" for i, (_, c, _) in enumerate(items, 1)))
    key[s] = [[w, c, v] for w, c, _ in [(a, b, n) for a, b, n in items] for v in [_]] if False else [[w, c, n] for w, c, n in items]
json.dump({"K": K, "F": F, "sheets": key}, open("key.json", "w"), indent=1)
