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

## Roots (44)

- GOOD: -5 terrible … +5 excellent
- BIG: -5 tiny … +5 huge (size only)
- NEAR: -5 far … +5 here
- ABOVE: -5 below, down … +5 above, up
- LIVE: -5 dead … -2 asleep … +5 alive
- SAME: -5 opposite, different … -4 special … +3 ordinary … +5 identical
- TIME: -5 long ago … 0 now … +5 far future (-1 just now, +1 soon)
- INSIDE: -5 outside … 0 on the border, at the edge, the surface … +5 inside
- PART: -5 particle, crumb … -2 a part, member … +2 the whole … +5 a group of many
- SIDE: -5 back … +5 front
- KNOW: -5 ignorant … +5 sure
- WANT: -5 hate, refuse … +5 love, crave
- HEAT: -5 ice cold … +5 fire hot
- BEGIN: -5 start … 0 ongoing … +5 end
- GIVE: -5 take … 0 exchange … +5 give
- TOUCH: -5 soft … +5 hard, sharp
- SEX: -5 female … +5 male (only for words of explicit sex)
- HAPPEN: event, happen (no axis)
- THINK: -5 doubt … 0 think … +5 decide
- CAN: -5 impossible … -3 hard … +5 easy
- MANY: -5 none, never … -1 few … 0 some … +3 many … +5 all, always
- SOMEONE: -5 they, others … 0 someone … +3 you … +5 I
- THING: -5 stone, inanimate … 0 plant … +4 animal
- MOVE: -5 stand still … 0 walk … +5 rush
- FEEL: -5 calm … +5 excited, intense (pleasant or not is GOOD)
- RULE: -5 private, informal … +4 authority, institution … +5 law, official
- CHANGE: -5 stay the same … 0 change … +5 transform (the direction comes from the next root: `CHANGE GOOD(=+3)` improve)
- ART: -5 technology, exact science … +5 arts, humanities (the plain root means skill, craft)
- JOIN: -5 separate, remove … +5 join, add, attach
- VALUE: -5 worthless … +5 precious (price, worth)
- CARE: -5 careless, lazy … +5 careful, thorough, diligent (attitude to a task)
- FRIEND: -5 enemy, hostile, cruel … +5 friend, friendly, kind (attitude toward people)
- MOOD: -5 tragic … -3 sad … 0 serious … +3 glad … +5 funny
- CONSUME: -5 give out (emit, speak, write) … +5 take in (eat, drink, read, listen)
- MEASURE: -5 an amount (size, length, weight) … 0 a level, degree … +5 a ratio, rate
- LONG: -5 thread, rope … 0 stick … +5 pole, beam (long objects)
- SAY: -5 whisper … 0 speak … +5 shout (also noises)
- GRAIN: -5 gas … -3 liquid … 0 powder, grain … +5 one solid piece
- FIGHT: -5 game, sport … 0 quarrel … +5 war
- BODY: body (no axis)
- SEE: see, look (no axis)
- DO: do, make, act (no axis)
- PLACE: place (no axis)
- TEXT: written language, document (no axis)

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

Write the letter and the value together, without `(=`: `MOVE | i T-2` = moved, `SOMEONE | o N+3 D+3` = the people.

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

## Task

Each line is one code standing for ONE common English word in some sense. Give your best English word and 2 alternatives.
