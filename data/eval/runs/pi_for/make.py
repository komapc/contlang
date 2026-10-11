"""Листы слепого теста PI против FOR: на листе 8 слов одного кодера (половина его 16) и 4 наполнителя, порядок случайный.
Листы 1–4 — вариант P (только PI), 5–8 — вариант F (FOR). key.json: {"sheets": {s: [[слово, код, 1 — цель / 0 — наполнитель]]},
"variant": {s: "P"|"F"}, "encoder": {s: "enc_P_a"...}}; pairs.json — коды-цели для scripts/site/eval_math.js."""
import json, random
FILL = {"book": "TEXT PART(=+2) | o", "brush": "TOUCH(=-3) MOVE DO(=+5) | o", "car": "DO(=+5) MOVE(=+4) | o", "hammer": "TOUCH(=+5) MOVE(=+4) DO(=+5) | o",
        "kitchen": "PLACE HEAT(=+3) CONSUME(=+5) | o", "knife": "JOIN(=-4) TOUCH(=+4) DO(=+5) | o", "ladder": "MOVE ABOVE(=+4) DO(=+5) | o",
        "library": "PLACE TEXT PART(=+5) | o", "mountain": "PLACE ABOVE(=+5) BIG(=+4) | o", "sand": "GRAIN(=0) THING(=-5) PART(=-5) | o"}
rnd = random.Random(5); sheets, variant, encoder, pairs = {}, {}, {}, []
s = 0
for enc in ("enc_P_a", "enc_P_b", "enc_F_a", "enc_F_b"):
    codes = [l.strip().split(": ", 1) for l in open(enc + ".md") if ": " in l]
    pairs += [{"word": w, "code": c, "variant": enc[4]} for w, c in codes]
    rnd.shuffle(codes)
    for half in (codes[:8], codes[8:]):
        s += 1
        items = [(w, c, 1) for w, c in half] + [(w, c, 0) for w, c in rnd.sample(sorted(FILL.items()), 4)]
        rnd.shuffle(items); sheets[s] = items; variant[s] = enc[4]; encoder[s] = enc
        open(f"sheet_{s:02}.md", "w").write("".join(f"{i}. {c}\n" for i, (_, c, _) in enumerate(items, 1)))
json.dump({"sheets": sheets, "variant": variant, "encoder": encoder}, open("key.json", "w"), indent=1)
json.dump(pairs, open("pairs.json", "w"), indent=1)
print(s, "листов,", len(pairs), "кодов")
