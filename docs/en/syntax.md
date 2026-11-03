# Syntax

## Particles

The connection of words in a sentence is set by particles (three from Toki Pona; `PE`, `AND` and the link words `FROM`, `FOR`, `LIKE` were added). Constructions nest inside each other. The predicate is a word with the form `| i`; there is no separate particle for it: Toki Pona's `LI` was removed (2026-10-14), and the form does its job. An attribute or a noun as predicate is the same root with `| i`: “the house is big” `PLACE INSIDE(=+5) LIVE | o BIG | i`, “a dog is an animal” `THING(=+4) | i` (“to be an animal”). Labels of time, negation and question stand on this verb.

| Particle | Role |
| :-- | :-- |
| `E` | direct object |
| `FROM` | noun link word: X is made of Y |
| `FOR` | link word: X is made for Y |
| `LIKE` | link word: X resembles Y but is not Y |
| `PI` | link word: everything else: X is a part of Y, is located or lives in Y |
| `LA` | condition / context clause |
| `PE` | the agent with the passive voice (by whom): `… V-4 PE X` |
| `AND` | coordination “and, also”: between words, groups and clauses |

## The word: meaning | form

A word is written as **`ROOT(=v) ROOT(=v) … | pos labels`**. Before the `|` is the meaning: the head root and up to two modifier roots, each with the value of its axis `(=v)` if needed. After the `|`: the part of speech and grammatical labels. The roots are English glosses for now ([phonology](phonology.md)).

| Part of speech | Meaning | Example |
| :-- | :-- | :-- |
| `o` | noun (object, concept) | `MOVE \| o`: movement |
| `i` | verb (action, state) | `MOVE \| i`: to move |
| `a` | attribute (modifier) | `MOVE \| a`: mobile |
| `e` | adverbial (manner of action) | `MOVE(=+4) \| e`: quickly |

Any root takes any part of speech (word families, conversion like *work*).

**Noun roles** come after `| o`, one per word, are not roots and are not in the limit (like Esperanto's *-ist, -il, -aĵ, -ec*):

| Role | Meaning | Example |
| :-- | :-- | :-- |
| `agent` | who or what does it, or a person of this field | `ART(=+5) \| o agent`: artist; `TEXT \| o agent`: writer; `HAPPEN \| o agent`: cause |
| `tool` | tool, means | `TEXT \| o tool`: pen; `JOIN(=-4) TOUCH(=+4) \| o tool`: knife |
| `result` | what comes out | `HAPPEN \| o result`: consequence |
| `quality` | the property or state itself | `CAN \| o quality`: ability |

**Form labels** (not roots, not part of the limit of three; omitted = unspecified, as always):

| Label | Meaning | Example |
| :-- | :-- | :-- |
| `T` | time: −5 long ago … 0 now … +5 someday | `T-2` past, `T+2` future |
| `N` | number: 0 none, +1 one, +2 two, +3 several, plural … +5 all; on a verb, the number of the subject: `N+1` singular, `N+2` dual, `N+3` plural (person is not marked) | `N+3` several, `N0` none; `MOVE NEAR(=+4) \| i T-2 N+3`: they came (plural subject) |
| `M` | probability: −5 certainly not … −3 maybe … +4 certainly | `M-5` not |
| `A` | aspect: −5 about to begin … 0 in progress … +5 finished; `A+5` without `T` is a past participle (*known, gone*), `A0` a present participle (*-ing*) | `A-4` began, `A+5` finished |
| `C` | comparison: −3 less, +3 more, +5 most (more or less of what the root names: `GOOD \| a C+3` better, `C-3` worse) | `BIG \| a C+5` biggest |
| `I` | intensity (how strongly a feature or action is expressed): −5 barely … −2 slightly … +2 rather … +5 extremely; do not write `I0` (the decoder loses it), for “moderately” use `I+1…+2`; not comparison (that is `C`) | `GOOD(=+3) \| a I+4` very good; `GOOD \| a I-4` barely good |
| `K` | causation, causative (the subject acts on the object `E` so that it performs or undergoes the verb's action): −5 to prevent, dissuade, forbid … 0 to allow … +5 to force, cause, urge; without an action root, the base is `DO` | `DO \| i K+4 E SOMEONE | o`: forced him; `CONSUME \| i K+4 E SOMEONE | o`: fed; `DO \| i K-4 E SOMEONE | o`: hindered him |
| `D` | definiteness: −3 indefinite (*a*), +3 definite (*the*) | `PLACE LIVE \| o D+3`: this house |
| `R` | the event relative to the reference point (Reichenbach: E↔R; `T` sets R↔now): −3 before the reference point, 0 simultaneously, +3 after | `T-2 R-3`: had already left (before that); `T-2 R+3`: later (in the past); `T+2 R-3`: will have left by then |
| `V` | voice: −4 the subject undergoes (passive), 0 it happens by itself (no actor), +4 the subject acts on purpose | `PART \| i T-2 V-4`: was divided; `PART \| i V0`: divided by itself |
| `!` `?` | command, question (no value) | `CONSUME \| i !`: eat! |

**The reference point R** by default is the nearest named time or event to the left (at the start of a text, the moment of speech); it is set explicitly by a clause `LA [ … ]` (*after…*) or a date in quotes. `R` is not aspect: `A` is about the phase of the event itself (beginning, process, end), `R` about order in time.

`THING(=+4) BIG(=+5) | o N+3` is elephants (three roots are not spent on number). `MOVE NEAR(=+4) | i T-2 M-5` is did not come. Labels are placed once, on the head word of the group.

## Time and negation (accepted)

Time and negation are the form labels `T` and `M` after the `|` (table above), not roots. Omitted = unspecified ([the zero rule](model.md)).

- **`T`** is time from −5 (“very long ago”) through 0 (“now”) to +5 (“someday”): `T-1` just now, `T-3` long ago, `T+1` soon. Without the label, the time is not specified.
- **`M`** is the probability of the statement: a plain statement is the default and has no label; `M+4` certainly, `M-1` probably, `M-3` maybe (50/50), `M-4` unlikely, `M-5` certainly not. “Maybe yes” and “maybe no” differ only in degree. Negation, “maybe” and “certainly” are one label; there is no separate negation particle.

The semantic root `TIME` to the left of the `|` (`TIME(=-2) | e` “yesterday”, `FEEL(=+4) GOOD(=-4) TIME(=+3) | i` “to fear”) and the label `T` to the right do not mix. A root's local axis is written `(=v)`: `LIVE(=-2) | i` is “half alive” (sleeps), `LIVE | i T-2` is “lived”.

*She did not see the message* (hearing is read through SEE and SAY):

```
SOMEONE | o SEE | i T-2 M-5 E THING | o PI SAY | o
```

Pronouns and demonstratives are correlatives built from roots ([lexicon](lexicon.md)).

## The noun group, clauses and questions (accepted)

- **The head first, modifiers after** (as in Toki Pona). Adjectives (`-a`) follow the noun directly, without a particle, as a flat list, and all refer to it: `THING | o MOVE | a BIG(=+3) | a` is a big moving thing.
- **The link words `FROM`, `FOR`, `LIKE`, `PI`** introduce a second noun that narrows the head: `X | o LINK Y | o`. The first word X is always the genus, and the pair as a whole is a special case of it; adjectives go before the link word. The speaker asks the questions in order and takes the first link word that fits, and the listener reads each one in one way:
  1. `FROM`: X is made of Y (material, source): candle = `LONG(=0) HEAT(=+5) | o FROM GRAIN(=+5) TOUCH(=-5) | o` (“light from wax”);
  2. `FOR`: X is made for Y, is used with Y, on Y or as Y: scabbard = `INSIDE(=+5) JOIN(=+5) | o FOR JOIN(=-4) TOUCH(=+4) | o tool` (“a covering for a blade”);
  3. `LIKE`: X resembles Y but is not Y: sunflower = `THING(=0) ABOVE(=+5) | o LIKE ABOVE(=+5) HEAT(=+5) | o` (“a plant resembling the sun”);
  4. `PI`: everything else: X is a part of Y or is located or lives in Y: roof = `ABOVE(=+5) JOIN(=+5) | o PI PLACE LIVE(=+5) | o`; `SOMEONE | o BIG(=+3) | a PI SOMEONE MANY(=+4) | o` is a big person of the people (a ruler).

  Blind test ([result](../../data/eval/runs/links/README.md)): the same codes with link words are read by the first word 46 times out of 80, with a single `PI` instead of all the link words 31 out of 80. Without `LIKE` the set is no better than a single `PI`.
- **`LA`** is condition, context and cause (“if”, “when”, “because”, “although”): `LA [ … ] …`. A clause with `LA` stands before the main one, so “therefore X” is conveyed by reordering: the cause goes in `LA [ … ]`, the consequence after it (`LA [ he was ill ] he stayed home`). If the word order has to change, it is changed.
- **`AND`** is “and, also”: it stands between coordinated words, groups and clauses and connects what is on the left with what is on the right: `LIVE | i AND SAY | i` *lived and spoke*, `[ … ] AND [ … ]`. In a list it goes before the last element. The particle takes axes like a word: `AND SAME(=-5)` but, `AND SAME(=-2)` although, `AND HAPPEN(=+4)` therefore, `AND HAPPEN(=-4)` because, `AND BIG(=+4)` all the more, `AND | M-3` or (a probability label, not a root); the word order is the original one ([encoding](encoding.md)). It is a separate particle, so do not write `JOIN`, `CHANGE`, `SAME` as connectors (they mean attachment, change, identity).
- **`;`** is the boundary between independent clauses of a long sentence: each clause has its own words and particles (`SOMEONE | o SAY | i T-2 ; THING | o LIVE | i`). Brackets `[ … ]` are only for a nested clause or a clause as object. Every word, including the head noun before a link word (`PI`, `FROM`, `FOR`, `LIKE`) and `E`, has its own form `| …` (at least a part of speech); words are not glued together without `|`. The check is `scripts/mincode/validator.py` (the introduction of `;` follows the validator's result: the coders themselves wrote it in 25 of 60 sentences).
- **`{ … }`** is an explicit word boundary in the notation of a sentence: each word `{ ROOTS | FORM }` is in its own curly braces (up to three roots, one form); outside the braces there are only the particles `E PI FROM FOR LIKE LA PE AND`, `[ ]`, `;` and names in quotes (`"Europe"`). Without braces the coders did not put `| form` on every word (validator errors in 73–88% of codes; with braces 28–70%, meaning by the blind judge on the tuning set +0.12 [+0.01, +0.25], on the held-out set +0.01 [−0.20, +0.23], so meaning neither improves nor worsens; [result](../../data/translation_test/clause_rule.md)). Example: `{ SOMEONE | o } { SAY | i T-2 } E { THING | o }`; a modifier after `AND` may have no form: `AND { SAME(=-5) }`. Notation of a single word (`THING(=+4) BIG(=+5) | o N+3`) does not require braces.
- **A content clause** (after *think, say, know, want*) is taken in brackets as an object: `THINK | i E [ … ]`. The spoken marker for brackets is a question for phonology.
- **A question** is a requested value `?`: yes/no is the label `?` on the predicate, “who/what” is `SOMEONE | o ?`, `THING | o ?`. There is no separate question word.
- **Dates and clock time** are in quotes, like numbers: `"5.3"`, `"3:00"`; units of time and parts of the day are by recipes ([encoding](encoding.md), “Time”).

*Who said that the king is dead?*

```
SOMEONE | o ? SAY | i T-2 E [ SOMEONE RULE(=+5) SEX(=+5) | o D+3 LIVE(=-5) | i ]
```

## Omitted values and “doesn't matter”

[The zero rule](model.md) applies: an axis that is not written has an unspecified value (costs nothing in bits); `(=0)` is the explicit middle of the axis. `MOVE | i` is “to move” without specifying speed, `MOVE(=0) | i` is “to walk at an ordinary pace”.

- If a value really **doesn't matter**, the axis is simply not written. A separate marker `?` is needed only for a request (“what value?”).
- The earlier decision “omitted = the middle of the scale” and the option “a feature is the interval `[-5, +5]`” were dropped: the first contradicts the zero rule, the second was not needed.

## Examples

Checked by the validator (`scripts/mincode/validator.py`); not checked by a blind test.

*All humans are born free and equal.*

```
SOMEONE MANY(=+5) | o LIVE BEGIN(=-5) | i T-2 V-4 CAN(=+5) | a SAME(=+5) | a
```

*Some people fear authority.*

```
SOMEONE MANY(=0) | o N+3 FEEL(=+4) GOOD(=-4) TIME(=+3) | i E RULE(=+4) | o
```

*If someone acts freely, society benefits.*

```
LA [ SOMEONE | o DO | i CAN(=+5) | e ] SOMEONE PART(=+5) | o CHANGE GOOD(=+3) | i
```
