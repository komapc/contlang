# min-co: how a word is written

A word is `ROOTS | FORM`.

- ROOTS: 1 to 3 roots. The first is the head: what kind of thing, action or quality it is. Each next root narrows everything before it.
- FORM: the part of speech, then optional marks.
  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb.
  - Example: `PLACE LIVE | o` = a place where one lives = house.

A root may carry a value on its axis, `ROOT(=v)`, with v from -5 to +5.
The anchors listed with each root name some points of its axis. **Every value from -5 to +5 is usable**: a value between
two anchors means something between them (`GOOD(=+1)` = okay, `GOOD(=+4)` = very good, `BIG(=-3)` = quite small).
Pick the value that fits best; do not round to ±5. With no value, the root is meant plainly (`GOOD` = good).
HAPPEN never takes a value.

## Roots (30)

- GOOD: -5 terrible … -2 poor … 0 so-so … +2 fine … +5 excellent
- BIG: -5 tiny … -2 small … 0 medium … +2 large … +5 huge (size only)
- ABOVE: -5 bottom, down … -2 low … 0 level, middle height … +2 high … +5 top, up, sky
- LIVE: -5 dead … -3 dying, ill … -2 asleep … 0 living … +3 healthy … +5 lively, full of life
- SAME: -5 opposite … -3 different, other, special … 0 similar, like … +3 usual, ordinary … +5 identical, the same
- TIME: -5 long ago … -2 recently … -1 just now … 0 now … +1 soon … +2 later … +5 far future
- INSIDE: -5 outside, outdoors … -2 near the outside … 0 surface, edge, border … +2 within … +5 deep inside, core
- PART: -5 particle, crumb … -2 a part, piece, member … 0 one unit, a single whole … +2 a pair, a few together … +5 a group, set, collection
- KNOW: -5 not know, ignorant, absurd … -2 guess … 0 notice, be aware … +3 understand … +5 know well, expert (teach = GIVE KNOW)
- WANT: -5 hate, refuse … -2 dislike … 0 indifferent … +2 like, wish … +5 love, crave
- BEGIN: -5 start, origin … -2 early stage … 0 ongoing, middle … +2 late stage … +5 end, finish
- GIVE: -5 grab, seize, steal … -2 take, get … 0 exchange, trade … +2 offer, lend … +5 give, donate, grant
- THINK: -5 doubt … -2 wonder … 0 think … +3 plan, intend … +5 decide
- MANY: -5 none, never … -3 rarely, very few … -1 few … 0 some … +3 many, often … +5 all, always
- SOMEONE: -5 they, others … -3 he, she … 0 someone … +3 you … +5 I
- THING: -5 stone, inanimate … -2 material, stuff … 0 plant … +2 small creature, insect … +4 animal
- MOVE: -5 stand still … -2 creep, slow … 0 walk, go … +2 run … +5 rush, fly
- RULE: -5 private, personal … -2 habit, custom … 0 rule, norm … +3 authority, institution … +5 law, official
- CHANGE: -5 keep, stay the same … -2 adjust, adapt … 0 change … +3 turn into, become … +5 transform completely
- ART: -5 technology, exact science … -2 engineering, trade … 0 skill, craft … +2 design … +5 arts, humanities
- JOIN: -5 separate, remove … -2 loosen, detach … 0 touch, meet … +3 connect, attach, add … +5 merge, unite
- VALUE: -5 worthless … -2 cheap … 0 price, worth, buying and selling … +2 expensive … +5 precious, vital, important
- MEASURE: -5 an amount (size, length, weight) … -2 a count, number … 0 a level, degree … +2 a rate, speed … +5 a ratio, percentage, statistics
- SAY: -5 ask, question … -2 answer, reply … 0 say, tell … +3 claim, promise … +5 order, command (loudness is the I mark: `SAY | i I+5` = shout)
- GRAIN: -5 gas … -3 liquid … -1 mud, paste … 0 powder, grain … +2 lump, chunk … +5 one solid piece
- FIGHT: -5 game, sport … -2 contest … 0 quarrel … +2 fight, struggle … +5 war
- SEE: -5 hidden, unseen … -2 glimpse … 0 see, look … +3 watch, observe … +5 visible, obvious
- DO: -5 rest, idle … -2 try … 0 do, act … +3 make, work … +5 labour, toil
- PLACE: -5 spot, point … -3 room … 0 building … +3 town, city … +5 country, world (plain PLACE = a place)
- TEXT: -5 letter, sign, symbol … -2 word, name … 0 sentence, message … +3 article, document … +5 book

Only these 30 roots exist. Examples elsewhere in this spec may use other roots — those are not available; build every meaning from the 30 roots above, roles and phrases.

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
