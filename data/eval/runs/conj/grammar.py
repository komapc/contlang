# Связки между частями предложения (dec.md): несколько частиц, как уже существующие AND, LA, FOR. Патч к спецификации; репозиторий не меняется.
OLD_LA = "- `LA [ … ]`: a context or condition clause before the main clause (if, when, although)."
NEW_LA = """- `LA [ … ]`: a time clause before the main clause (when, while, as, after, before).
- `IF [ … ]`: a condition clause (if; unless = M-5 inside). `THOUGH [ … ]`: a concession clause (although, even if, even though).
- Between two clauses, in place of `;`: `BUT` (but, yet, however), `BECAUSE` (the next clause is the cause), `SO` (the next clause is the result), `OR` (or)."""
OLD_NEST = "- `[ … ]`: a clause used inside another, as its object or modifier."
NEW_NEST = "- `[ … ]`: a clause used inside another, as its object or modifier. Right after a noun, `[ … ]` describes that noun (who, which, that); the noun is not repeated inside."
NEW_PARTICLES = ["IF", "THOUGH", "BUT", "BECAUSE", "SO", "OR"]
def patch(s):
    for a, b in [(OLD_LA, NEW_LA), (OLD_NEST, NEW_NEST)]:
        assert s.count(a) == 1, a; s = s.replace(a, b)
    return s
