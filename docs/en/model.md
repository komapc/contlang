# The model: root and structure

Everything in the language comes down to two things: the root and the structure. An axis is not a separate entity but a root in a modifier position with a value (just as in Esperanto a root and a suffix are roughly the same thing). This was decided in discussion; the earlier “root, axis, structure” model has been replaced.

## 1. The root

A discrete anchor: what kind of object, action or concept this is. About 45, mostly NSM primitives (*someone, thing, move, think, want, see, place, …*); the current list is in the [lexicon](lexicon.md). A root does not know its part of speech.

**Every root has its own axis or none.** An axis is a continuous scale from −5 to +5, defined by poles in the spirit of NSM: for GOOD “bad … good”, for INSIDE “outside … inside”, for LIVE “dead … alive”. The value is relative to the root (a *big mouse* is smaller than a *small elephant*). All axes are two-sided: −5 is the opposite pole, 0 the middle, +5 the full pole (for MANY: −5 none … 0 some amount … +5 all).

**The zero rule.** An axis that is not written has an unspecified value, which costs nothing in bits. `(=0)` is an explicit value: the middle of the axis. Exact quantities (`1`, `17`) are numbers from the exemptions.

There are no shared “universal axes” (M1–M9): if a fine shade is needed, one more root is used.

## 2. Compound words

A word is one, two or three roots, as in Esperanto. The head comes first; each following root refines everything before it, without brackets (left to right); more than three roots are not allowed. The second root works sometimes as a root and sometimes as a suffix. A root in a modifier position with an axis value is the “axis” of the earlier model:

| word | notation |
| :-- | :-- |
| house | `PLACE LIVE \| o` |
| bedroom | `PLACE LIVE(=-2) \| o` |
| morgue | `PLACE LIVE(=-5) \| o` |
| a good thing | `THING GOOD(=+3) \| o` |

An axis without a thing (*good*) is a root in the head position: `GOOD(=+5)`. Ambiguous grouping is written with brackets `[ … ]`. Two words (`X | o LINK Y | o`) are built by the same logic: the first is the genus, the second narrows it ([syntax](syntax.md)).

The cost in bits: dense (9 shared axes) ≈ 31 bits for the values; sparse (axes in roots) ≈ 8.4 bits for each axis needed (root number + value). The sparse way is cheaper as long as a word needs no more than three or four axes. This has not yet been checked on data.

## 3. Structure

- **Two layers in a word, separated by `|`.** On the left is the meaning: roots (head first, up to three) with axis values. On the right is the form: the part of speech (`o` noun, `i` verb, `a` attribute, `e` adverbial; 2 bits, as with the Esperanto suffixes earlier), for a noun a role (`agent`, `tool`, `result`, `quality`, like Esperanto's *-ist, -il, -aĵ, -ec*), and grammatical labels. Labels are a closed set, are not roots and do not count toward the limit of three: `T` time (the reference moment relative to “now”), `R` the time of the event relative to that reference (Reichenbach's S, R, E), `N` number, `M` negation and probability, `A` aspect, `C` comparison, `I` intensity, `D` definiteness, `V` voice, `K` causation, `!` command, `?` question; values are on the −5…+5 scale under the zero rule. Example: `FEEL(=+4) GOOD(=-4) TIME(=+3) | i T+2 N+4` is “they will be frightened” (fear: a feeling, bad, in the future; form: verb, future, many). The semantic `TIME(=+3)` on the left and the grammatical `T+2` on the right do not mix. Grammatical labels are placed once, on the head word of the group.
- **Order:** the head first, modifiers after.
- **Particles:** `E` object, `PI` a noun as modifier, `LA` condition, brackets `[ … ]` for a clause, `?` for a requested value. The predicate is the word with `| i`; `LI` was removed (2026-10-14, [syntax](syntax.md)).
- **Time and negation** are the labels `T` and `M` after the `|`; the semantic `TIME` stays a root on the left; there is no root `MAYBE`, probability is the label `M`.

## What to take from other languages (accepted for further work)

- Esperanto's table of correlatives: questions, demonstratives, “all / nobody” are assembled from the roots SOMEONE, THING, PLACE, TIME, NEAR, MANY and the particle `?` (see the lexicon).
- Evidentiality (“saw”, “heard”): the roots SEE, THINK, KNOW (HEAR was removed) as a particle modifying the sentence.
- Number: the root MANY (`THING MANY(=+3)` is “several”); the axis is two-sided (−5 none … 0 some amount … +5 all); without a value, the number is not specified.
- Argument places on a root (Lojban) instead of cases.
- Form length by frequency (Huffman coding).
- A marker for names and loanwords (Lojban, *cmevla*) for the exemptions.
- A formal grammar checked by a parser.

## What remains open

- Abstractions (*responsibility, category, probability, career…*) have no roots so far; roots are added as failures come up. The root KIND (“kind, variety”) was tested and not accepted, including as a head only ([kind](../../data/eval/runs/kind/README.md), [side_kind](../../data/eval/runs/side_kind/README.md); decision of 2026-10-14).
- To check on data: sparse encoding (a root + up to 3 modifier roots) against 9 shared axes at the same number of bits.
- Verbs of change of state via a head root with a value (*grow* = `BIG(=+3) | i` instead of `CHANGE BIG(=+3) | i`) were tested and not accepted: there is no difference ([verbs](../../data/eval/runs/verbs/README.md)).
