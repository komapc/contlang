# min-co: how a word is written

A word is `ROOTS | FORM`.

- ROOTS: 1 to 3 roots. The first is the head: what kind of thing, action or quality it is. Each next root narrows everything before it.
- FORM: the part of speech, then optional marks.
  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb.
  - Example: `PLACE LIVE | o` = a place where one lives = house.

A root may carry a value on its axis, `ROOT(=v)`, with v from -5 to +5.
Every axis works the same way: -5 is the opposite pole, 0 the middle, +5 the full pole.
With no value, the root is meant plainly (`GOOD` = good, of unspecified degree).
Roots marked "no axis" never take a value.

## Roots ({{N_ROOTS}})

{{ROOTS}}

## Form marks

Marks go after the part of speech. They are not roots and do not count toward the limit of 3.

Noun roles turn the meaning into a related noun:
- `agent`: the one who does it (person or thing). `TEXT | o agent` = writer, `HAPPEN | o agent` = cause.
- `tool`: the means or instrument. `TEXT | o tool` = pen, `JOIN(=-4) TOUCH(=+4) | o tool` = knife.
- `result`: what comes out of it. `HAPPEN | o result` = consequence, `TEXT | o result` = a text.
- `quality`: the quality or state itself. `GOOD | o quality` = goodness, `CAN | o quality` = ability.

Grammar marks, each with a value from -5 to +5; not written means unspecified:
- T: tense (-2 past, +2 future).
- R: event before (-3) or after (+3) the reference time.
- A: aspect (-5 beginning … +5 completed).
- N: number (+1 few, +3 plural, +5 all).
- M: negation and probability (-5 not, -3 maybe, +4 certainly).
- C: comparison (-3 less, +3 more, +5 most).
- I: intensity (-5 barely … +4 very, +5 utterly).
- D: definiteness (-3 a, +3 the).
- V: voice (-4 passive, +4 deliberate).
- K: make someone do it (-5 prevent … 0 let … +5 force).
- `!`: command.
- `?`: question.

## Two words

A noun can be narrowed by a second noun: `X | o LINK Y | o`.
X is the kind, and Y narrows it. Each word has its own limit of 3 roots. LINK is the first of these that fits:
- `FROM`: X is made of Y.
- `FOR`: X is made for Y.
- `LIKE`: X looks like Y.
- `PI`: X is part of Y, or is found in Y.

## Quotes

Only proper names, digits and scientific names of particular species or substances are written in quotes: `"Rome"`, `"17"`, `"Canis"`, `"iodine"`.
Everything else is built from roots.
