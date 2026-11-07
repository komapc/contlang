# Новая грамматика (dec.md): служебные слова из тех же корней. Патч к строке спецификации build_spec; репозиторий не меняется.
OLD_SOMEONE = "- SOMEONE: -5 they, others … 0 someone … +3 you … +5 I"
NEW_SOMEONE = "- SOMEONE: -5 they … -3 he, she … 0 someone … +3 you … +5 I (see Pronouns)"
OLD_POS = "  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb."
NEW_POS = "  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb, `p` relation (see Relations)."
OLD_QUOTES = "## Quotes"
NEW_SECTION = """## Pronouns

- People already known from the context are SOMEONE with a value and nothing else: `SOMEONE(=+5) | o` I, me; `SOMEONE(=+5) | o N+3` we, us;
  `SOMEONE(=+3) | o` you; `SOMEONE(=-3) | o` he, him, she, her (add `SEX(=+5)` or `SEX(=-5)` when it matters); `SOMEONE(=-5) | o` they, them.
  Other people are `SAME(=-5) SOMEONE | o N+3`.
- A thing already known from the context (it, this, that) is `THING | o D+3`.
- Owner: a pronoun written as an adjective, right before a noun, is its owner: `{ SOMEONE(=-3) | a } { BODY | o }` = his body,
  `{ SOMEONE(=-5) | a } { DO | o result }` = their work, `{ SOMEONE(=+5) | a }` = my. A noun owner uses PI inside the noun:
  `PLACE LIVE | o PI RULE(=+4) SOMEONE | o` = the ruler's house.

## Relations

A relation word, part of speech `p`, stands right before a word and tells how that word relates to the rest of the sentence,
like an English preposition. It has one root and no marks; the root names the relation and is read on its own axis:
- place: `INSIDE(=+5) | p` in, into; `INSIDE(=-5) | p` out of; `ABOVE(=+5) | p` on, over; `ABOVE(=-5) | p` under;
  `NEAR(=+5) | p` at, to, toward; `NEAR(=-5) | p` from, away from; `SIDE(=+5) | p` in front of; `SIDE(=-5) | p` behind;
- time: `TIME(=-2) | p` before; `TIME(=+2) | p` after; `TIME(=0) | p` during, while;
- other: `JOIN(=+5) | p` with; `JOIN(=-5) | p` without; `HAPPEN | p` because of; `WANT | p` for, in order to;
  `GIVE | p` to (the receiver); `DO | p` by (the doer of a passive verb); `THINK | p` about; `SAME(=+5) | p` like, as;
  `SAME(=-5) | p` than, instead of; `PART | p` of, among.
Example: `{ SOMEONE(=-3) | o } { GIVE(=+5) | i T-2 } E { TEXT | o D-3 } { GIVE | p } { SOMEONE(=+5) | o }` = he gave a book to me.

## Quotes"""

def patch(s):
    for a, b in [(OLD_SOMEONE, NEW_SOMEONE), (OLD_POS, NEW_POS), (OLD_QUOTES, NEW_SECTION)]:
        assert s.count(a) == 1, a; s = s.replace(a, b)
    return s
