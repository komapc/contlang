# Summary tables: roots, axes, labels

> English translation of [docs/tables.md](../tables.md), which is generated from [`roots.yaml`](../../roots.yaml) (`python3 scripts/mincode/gen.py`).

A brief overview of the current state. Sources of truth: `roots.yaml` (roots and axes), [syntax.md](syntax.md) (labels and particles), [model.md](model.md) (the model). This is only a summary; in case of disagreement they are right.

## Roots with an axis (39)

An axis is a −5 … +5 scale; an axis that is not written has an unspecified value, `(=0)` is the explicit middle.

| root | −5 | 0 | +5 |
| :-- | :-- | :-- | :-- |
| GOOD | bad | | good |
| BIG | little | | much |
| NEAR | far, abroad, on the way | | close, nearby, in the center (this / that) |
| ABOVE | lower | | higher |
| LIVE | dead | | alive |
| SAME | different, special | | the same, common |
| TIME | long ago | now | someday |
| INSIDE | outside | on the boundary | inside |
| PART | crumb (−2 part, member) | +2 whole, “completely” | +5 group, set (after a word: a collection of such things, *-aro*) |
| SIDE | back, backward; to return | | front, forward; upcoming |
| KNOW | foolish, absurd, I don't know | informed | I know, to inform, to teach |
| WANT | hatred | | love |
| HEAT | ice | warmth | fire |
| BEGIN | to begin | in progress | to finish |
| GIVE | to seize, to take away | exchange, to receive | to give away, to present, to donate |
| TOUCH | soft, smooth, tender | ordinary | hard, stiff, harsh |
| SEX | female | | male |
| THINK | to doubt | to think | to decide |
| CAN | impossible (−3 difficult) | | easy |
| MANY | −5 none, not at all (−3 almost none, shortage) | 0 some amount | +5 all (+3 many) |
| SOMEONE | they / another | someone | I (+3 you) |
| THING | stone | plant | animal (+4) |
| MOVE | to stand | to walk | to rush |
| FEEL | lethargy | | strong feeling |
| RULE | personal, informal | ordinary | official, institution, law |
| CHANGE | to stay | to change | to transform, to change completely |
| ART | calculation, technology, exact sciences | mixed | creativity, culture, humanities |
| JOIN | to separate, to remove | composition unchanged | to attach, to add, to unite |
| VALUE | cheap, sale, buying and selling | ordinary price | expensive, valuable, important |
| CARE | careless, mistake, fault | ordinary | diligent, thorough |
| FRIEND | enemy, hostile | neutral | friend, friendly, kind |
| MOOD | grief, despair, tragic (−3 sadness) | serious, calm | funny, laughter (+3 merry, joyful) |
| CONSUME | to emit (write, speak, excrete) | exchange | to absorb (eat, read, listen) |
| MEASURE | a quantity in itself (size, amount) | level, degree | a quantity relative to another (ratio, share, percent, statistics) |
| LONG | thread, cloth, rope (thin, flexible) | wire, rod, fastener | beam, board, log, wooden furniture |
| SAY | whisper, mumbling | ordinary speech | shout, roar |
| GRAIN | gas, steam (−3 liquid, water) | granular, loose | solid, in one piece |
| FIGHT | game, sport, competition | brawl, dispute | war to the death |
| LAND | sea, water | shore | land, solid ground |

## Roots without an axis (6)

| root | meaning |
| :-- | :-- |
| HAPPEN | event, to happen |
| BODY | body |
| SEE | to see |
| DO | to do |
| PLACE | place |
| TEXT | written language, text, record |

## The word's form: after the `|`

Part of speech (2 bits): `o` noun, `i` verb, `a` attribute, `e` adverbial.

Labels (not roots, they do not count toward the limit of three roots; labels are placed once, on the head word of the group):

| label | what | scale |
| :-- | :-- | :-- |
| `T` | time: the reference point relative to “now” | −5 long ago … 0 now … +5 someday (`T-2` past, `T+2` future) |
| `R` | the time of the event relative to the reference point | −3 earlier … 0 simultaneously … +3 later |
| `N` | number | 0 none … +5 all (`N+3` several) |
| `M` | negation, probability | −5 not … −3 maybe … +4 certainly |
| `A` | aspect | −5 about to begin … 0 in progress … +5 finished |
| `C` | comparison | −3 less, +3 more, +5 most |
| `I` | intensity | −5 barely … −2 slightly … +2 rather … +5 extremely (`I+4` very; do not write `I0`) |
| `D` | definiteness | −3 *a*, +3 *the* |
| `V` | voice | −4 undergoes, 0 by itself, +4 on purpose |
| `K` | causation (causative) | −5 to prevent, to dissuade … 0 to allow … +5 to force, to cause |
| `!` | command | no value |
| `?` | question | no value |

## Noun roles

After `| o`, at most one, no value; they do not count toward the root limit.

| role | what it means |
| :-- | :-- |
| `agent` | the one who does this, or a person of this field (a person or a thing): `TEXT | o agent` writer, `HAPPEN | o agent` cause, `ART(=+5) | o agent` artist |
| `tool` | tool, means: `TEXT | o tool` pen, `JOIN(=-4) TOUCH(=+4) | o tool` knife |
| `result` | what comes out: `HAPPEN | o result` consequence |
| `quality` | the quality or state itself: `GOOD | o quality` goodness, `CAN | o quality` ability |

## Phrase particles

| particle | role |
| :-- | :-- |
| `E` | object |
| `FROM` | noun link word: X FROM Y means X is made of Y (material, source); checked first |
| `FOR` | link word: X FOR Y means X is made for Y (used with Y, on Y or as Y); second |
| `LIKE` | link word: X LIKE Y means X resembles Y but is not Y; third |
| `PI` | link word: X PI Y is everything else: X is a part of Y or is located or lives in Y; last |
| `LA` | condition, context, reference point for `R` |
| `PE` | the agent with `V-4` (“by whom”) |
| `AND` | coordination: and, also |
| `[ ]` | clause |
| `;` | boundary between independent clauses of a long sentence (each word has its own form `| …`) |
| `"…"` | names, numbers, dates, Latin |

## Counts

45 roots (39 with an axis, 6 without); 12 form labels; 4 noun roles; 11 particles and signs (+ quotes); 4 parts of speech. Limit: up to 3 roots in a word, without exceptions.
