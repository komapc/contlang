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

## Roots (10)

- GOOD: -5 terrible … +5 excellent
- PART: -5 particle, crumb … -2 a part, member … +2 the whole … +5 a group of many
- KNOW: -5 stupid, foolish, absurd … 0 aware … +5 know, inform, teach
- GIVE: -5 grab, seize, steal … 0 exchange, get … +5 give, donate, grant
- THINK: -5 doubt … 0 think … +5 decide
- SOMEONE: -5 they, others … 0 someone … +3 you … +5 I
- MOVE: -5 stand still … 0 walk … +5 rush
- RULE: -5 private, informal … +4 authority, institution … +5 law, official
- SAY: -5 whisper … 0 speak … +5 shout (also noises)
- DO: do, make, act (no axis)

Only these 10 roots exist. Examples elsewhere in this spec may use other roots — those are not available; build every meaning from the 10 roots above, roles and phrases.

## Form marks

Marks go after the part of speech. They are not roots and do not count toward the limit of 3.

Noun roles turn the meaning into a related noun:
- `agent`: the one who does it, or a person of that field (person or thing). `ART(=+5) | o agent` = artist. `TEXT | o agent` = writer, `HAPPEN | o agent` = cause.
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

Write the letter and the value together, without `(=`: `MOVE | i T-2` = moved, `SOMEONE | o N+3 D+3` = the people.

## Phrases

A concept is written as ONE word `{ ROOTS | FORM }`, or as a phrase of up to 3 words: `{ X } LINK { Y }` or
`{ X } LINK { Y } LINK { Z }`. X is the head and carries the part of speech of the whole concept; each next word narrows
the one before it. Every word has its own braces, its own FORM and its own limit of 3 roots. LINK is the first of these
that fits:
- `FROM`: X is made of Y, or comes from Y.
- `FOR`: X is made for Y, used to do Y.
- `AGAINST`: X protects from Y, stops or fights Y.
- `LIKE`: X looks like Y, or is done like Y.
- `PI`: X is part of Y, or is found in Y.

## Quotes

Nothing is quoted: every concept is built from roots.

## Task

`codes.md` has numbered lines; each is ONE min-co word or phrase (written as the spec above explains) that stands for one
English word — a noun, verb or adjective, as its part of speech shows. For each line give your best English reading (one
word) and 2 alternatives.

Write `answers.md`, exactly one line per code, same numbering, nothing else: `N. best | alt1 | alt2`
