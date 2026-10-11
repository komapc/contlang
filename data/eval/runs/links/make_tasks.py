"""Задания кодерам: 20 слов, по 5 на связку (по замыслу; кодер выбирает сам). A — только PI, B — FROM/FOR/PI, C — FROM/FOR/LIKE/PI."""
WORDS = [("wine", "the alcoholic drink made from grapes"), ("paper", "the thin sheets made from wood pulp, for writing"),
 ("cheese", "the solid food made from milk"), ("leather", "the material made from animal skin"), ("candle", "the stick of wax with a wick, burned for light"),
 ("key", "the small metal object that opens a lock or door"), ("lid", "the removable cover of a pot, jar or box"),
 ("saddle", "the seat strapped on a horse's back"), ("wallet", "the small flat case for carrying money and cards"), ("sheath", "the cover for a knife or sword blade"),
 ("starfish", "the sea animal shaped like a star"), ("seahorse", "the small fish whose head looks like a horse's"),
 ("jellyfish", "the soft sea animal shaped like a bell or umbrella"), ("catfish", "the fish with whiskers like a cat"), ("sunflower", "the tall plant with a big yellow flower like the sun"),
 ("roof", "the top covering of a house"), ("petal", "one of the coloured leaves of a flower"), ("hoof", "the hard foot of a horse"),
 ("nest", "the structure a bird builds for its eggs"), ("yolk", "the yellow inner part of an egg")]
JOIN = {"A": "Join the two words with `PI`.",
        "B": "Join the two words with one of the links `FROM`, `FOR`, `PI` exactly as the spec's LINKS section says (ask in its order, take the first that fits).",
        "C": "Join the two words with one of the links `FROM`, `FOR`, `LIKE`, `PI` exactly as the spec's LINKS section says (ask in its order, take the first that fits)."}
for v in "ABC":
    s = ("# Encoder task\n\nRead spec_enc.md (the min-co spec). Encode each word below as a TWO-WORD code: a head noun (the general kind: drink, material, tool, cover, seat, case, animal, fish, plant, part…) "
         "and a second noun that narrows it. " + JOIN[v] + " Each word has its own form `| o` and at most 3 roots; every axis value has a sign. "
         "Do not use quoted Latin or English names for the second noun: write it with roots.\n\n"
         "Pick for each word the code most likely to be read as exactly that word by a reader who has only the spec. The second noun must itself be readable (a reader must recognise it as that thing).\n\n"
         + "".join(f"- **{w}** — {g}\n" for w, g in WORDS)
         + "\nWrite ONLY the codes to the file given to you, one per line, in this order:\n```\n" + "".join(f"{w}: <code>\n" for w, _ in WORDS) + "```\nNo other text.\n")
    open(f"task_enc_{v}.md", "w").write(s)
print("ok")
