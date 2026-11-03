# Phonology and word structure

In the notation, roots are denoted by English glosses (`MOVE`, `THINK`). The site has a **draft of the sound** (below, “Draft of the sound”): it has not been tested by ear; it is a page option, not a decision of the language.

## Accepted

- **The part of speech** is marked by the Esperanto vowels: `o` noun, `i` verb, `a` attribute, `e` adverbial. In the notation they stand in the form after the `|` (`MOVE | i`); in sound they are intended as the suffixes `-o -i -a -e` ([syntax](syntax.md)).
- A reasonable restriction follows from this: a root must not end in a vowel, or it could not be told apart from a word with a suffix (as in Esperanto). This restriction is preliminary and will need checking when the sounds of the roots are chosen.

## Early prototype (not accepted, open)

The idea of the original document: to encode features in the sound of the word.

- Repeating a vowel = the intensity of the value: `DOM-T-a`, `DOM-T-aa`, `DOM-T-aaa` is a house of increasing size.
- The pair T/D sets the direction of the feature (T = +, D = -): `GO-T-aa` is to go into the future, `GO-D-aa` into the past.

Problems: 11 levels per feature fit vowel repetition poorly, and the vowels are now taken by the part-of-speech suffixes. Most likely, features will have to be written separately from the root (as special words or affixes), as in Toki Pona, not inside the root's sound.

## Open

- The inventory of sounds and the syllable structure of a root.
- How feature values (-5..+5) are pronounced and written.
- Whether the suffixes `-o/-i/-a/-e` conflict with the particles `E`, `PI`, `LA` (for example, `E` as a separate word).

## Draft of the sound (the site's “Phonetics” option)

The source is [`phonetics.yaml`](../../phonetics.yaml), from which `site/data/phonetics.json` is built; on the page it is turned on by a switch under the input field. It has only been checked by machine (a syllable uniqueness test), not by ear or on people.

- **A root is a whole Toki Pona word**, where one fits the meaning (`pona` is `GOOD`, `suli` is `BIG`, `sona` is `KNOW`, `moku` is `CONSUME`, `toki` is `SAY`). The word **does not change**: the head of a word is always an ordinary Toki Pona word (decision of 2026-10-14: “the head is Toki Pona”). The other roots have words with Toki Pona phonotactics.
- **An axis value is a suffix** made of syllables that do not exist in Toki Pona (`ti`, `wu`, `ji`, `wo` are forbidden by its phonotactics), so it cannot be mistaken for a word: `ti` is positive, `wu` negative, repeated |v| times; an explicit `(=0)` is a short `y` (Russian `ы`); “unspecified” has no suffix. Examples: `GOOD` is `pona`, `GOOD(=+3)` is `ponatititi`, `GOOD(=-2)` is `ponawuwu`, `GOOD(=0)` is `ponay`. The zero rule from [model.md](model.md) is preserved. In the codes of the math encoder the axis is always named (`(=0)` is 12%), in the model's codes it is not named in 22% of cases ([big1000](../../data/eval/runs/big1000/README.md)).
- **Why not the voicing of the first consonant** (the previous variant: `pona` / `bona` / `lona`): it changed the word, and only one of the three forms stayed Toki Pona (a bare `SAY` sounded `moki`, `insa` → `iksa`). A suffix keeps the word whole. The price: the sign stands at the end of the word, not on the root itself; this has not been tested by ear.
- **Counting repetitions:** a repetition can be counted, while the ear does not measure vowel length (5 and 6 morae cannot be told apart); the suffix `ti`/`wu` is shorter than repeating the whole word (`GOOD(=+5)` is `pona` and five `ti`, not five `pona`).
- **Roots without an axis** (`SEE` is `lukin`, `PLACE` is `tomo`, `TEXT` is `lipu`, `DO` is `pali`, `BODY` is `sijelo`, `HAPPEN` is `kama`) take no suffix.
- **A word** = root blocks joined by `-`, then `'` (a glottal stop) and the part-of-speech vowel `o i a e`, then the role (`ul il aj ec`) and the labels joined by `·`. A label is a vowel + a consonant: `at` is `T+`, `ad` is `T−`, `an` is `T0`; the number is given by the same repetition (`T-2` → `adad`).
- **Particles** begin with `h`, and `h` occurs nowhere else: `he` E, `hi` PI, `ha` LA, `ho` PE, `hu` AND, `hen` FROM, `hon` FOR, `hin` LIKE, `hem … hom` are the brackets, `hum` is `;`.

Why `y` rather than `ain` or a nasal vowel: the syllable `ain` is heavy at the end, and a nasal vowel merges with `n` and `m` inside words. Open: a listening test of counting 2–6 repetitions and of the pairs `p/b`, `t/d`, `s/z`, `f/v`; checking syllables for resemblance to real words (`ma-ma`, `pa-pa` do not occur in the neutral form, but the repetitions `ta-ta`, `ka-ka`, `ba-ba` do); word length at the values the model chooses; the pronunciation of quotes and brackets; Toki Pona words without an exact match (`LIVE` is `moli`, which actually means “to die”, `SEX` is `mije`, `THINK` is `kon`, `THING` is `ijo`) must be replaced or kept with a caveat; word length.
