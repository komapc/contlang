# Encoder instructions (words)

You will encode single English words into min-co.
A different person will decode your codes WITHOUT seeing the English, using only the spec below. Write each code so that its meaning can be recovered.

- Use ONLY the 10 roots below; never invent roots or use English words as roots. At most 3 roots per word.
- Do not quote common words. Give exactly one code per input item, with the same numbering, as `N. CODE`. No other text.

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

## Roots (10)

- GOOD: -5 terrible … -2 poor … 0 so-so … +2 fine … +5 excellent
- PART: -5 particle, crumb … -2 a part, piece, member … 0 one unit, a single whole … +2 a pair, a few together … +5 a group, set, collection
- KNOW: -5 not know, ignorant, absurd … -2 guess … 0 notice, be aware … +3 understand … +5 know well, expert (teach = GIVE KNOW)
- GIVE: -5 grab, seize, steal … -2 take, get … 0 exchange, trade … +2 offer, lend … +5 give, donate, grant
- THINK: -5 doubt … -2 wonder … 0 think … +3 plan, intend … +5 decide
- SOMEONE: -5 they, others … -3 he, she … 0 someone … +3 you … +5 I
- MOVE: -5 stand still … -2 creep, slow … 0 walk, go … +2 run … +5 rush, fly
- RULE: -5 private, personal … -2 habit, custom … 0 rule, norm … +3 authority, institution … +5 law, official
- SAY: -5 ask, question … -2 answer, reply … 0 say, tell … +3 claim, promise … +5 order, command (loudness is the I mark: `SAY | i I+5` = shout)
- DO: -5 rest, idle … -2 try … 0 do, act … +3 make, work … +5 labour, toil

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

`list.md` gives numbered English words (noun, verb or adjective) with their intended sense. For each, write ONE code — one
word, or a phrase of at most 3 words — that lets a reader who knows only the spec above guess the English word (or a word
of the same meaning) most surely. Every word in its own braces `{ ROOTS | FORM }`.

Write `answers.md` with exactly one line per item, same numbering: `N. code`. No other text.
