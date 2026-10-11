"""Листы слепого теста связок. На листе 10 слов одного кодера (половина его 20) и 4 наполнителя, порядок случайный.
A, B, C — коды кодеров своего варианта; D — коды C, где все связки (FROM / FOR / LIKE) заменены на PI, читаются по спецификации A.
key.json: {"sheets": {s: [[слово, код, 1 — цель / 0 — наполнитель]]}, "variant": {s: "A"…"D"}, "encoder": {s: "enc_C_a"…}, "spec": {s: "A"|"B"|"C"}};
pairs.json — коды-цели для scripts/site/eval_math.js. Папка декодеров: spec_1 = A, spec_2 = B, spec_3 = C; list_NN.md."""
import json, random, re, sys, os
FILL = {"book": "TEXT PART(=+2) | o", "brush": "TOUCH(=-3) MOVE DO(=+5) | o", "car": "DO(=+5) MOVE(=+4) | o", "hammer": "TOUCH(=+5) MOVE(=+4) DO(=+5) | o",
        "kitchen": "PLACE HEAT(=+3) CONSUME(=+5) | o", "knife": "JOIN(=-4) TOUCH(=+4) DO(=+5) | o", "ladder": "MOVE ABOVE(=+4) DO(=+5) | o",
        "library": "PLACE TEXT PART(=+5) | o", "mountain": "PLACE ABOVE(=+5) BIG(=+4) | o", "sand": "GRAIN(=0) THING(=-5) PART(=-5) | o"}
LINK = re.compile(r"\b(FROM|FOR|LIKE|PI)\b")
rnd = random.Random(11); sheets, variant, encoder, spec, pairs = {}, {}, {}, {}, []
read = lambda f: [l.strip().split(": ", 1) for l in open(f) if ": " in l]
jobs = [(v, f"enc_{v}_{e}", read(f"enc_{v}_{e}.md")) for v in "ABC" for e in "ab"]
jobs += [("D", f"enc_C_{e}", [(w, LINK.sub("PI", c)) for w, c in read(f"enc_C_{e}.md")]) for e in "ab"]
s = 0
for v, enc, codes in jobs:
    pairs += [{"word": w, "code": c, "variant": v} for w, c in codes]
    codes = codes[:]; rnd.shuffle(codes)
    for half in (codes[:10], codes[10:]):
        s += 1
        items = [(w, c, 1) for w, c in half] + [(w, c, 0) for w, c in rnd.sample(sorted(FILL.items()), 4)]
        rnd.shuffle(items); sheets[s] = items; variant[s] = v; encoder[s] = enc; spec[s] = "A" if v == "D" else v
        open(f"sheet_{s:02}.md", "w").write("".join(f"{i}. {c}\n" for i, (_, c, _) in enumerate(items, 1)))
json.dump({"sheets": sheets, "variant": variant, "encoder": encoder, "spec": spec}, open("key.json", "w"), indent=1)
json.dump(pairs, open("pairs.json", "w"), indent=1)
if len(sys.argv) > 1:   # папка декодеров
    d = sys.argv[1]; os.makedirs(d, exist_ok=True)
    for i, v in enumerate("ABC", 1): open(f"{d}/spec_{i}.md", "w").write(open(f"spec_dec_{v}.md").read())
    for t in sheets: open(f"{d}/list_{t:02}.md", "w").write(open(f"sheet_{t:02}.md").read())
print(s, "листов,", len(pairs), "кодов")
