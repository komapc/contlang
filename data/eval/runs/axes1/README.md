# axes1 — whole-range anchors are used but don't read better; the one-root rule hurts sentences (−0.15)

Pre-registered: [dec.md](dec.md) (commit `cf63bb4`, before codes). Script: [run.py](run.py); totals and every word with its
codes and readings — [result.txt](result.txt); code statistics [check.txt](check.txt); codes [codes.json](codes.json),
specs [specs/](specs/), raw answers [answers/](answers/).

## Result

Arms: **B** = v2b; **A** = [v2c roots](../../../../lang/v2c/roots_en.md) (anchors over the whole range, new axes for
BODY / SEE / DO / PLACE / TEXT, SAY = speech act) + "every value is usable"; **AR** = A + one root for a noun / adjective /
adverb, up to 3 for a verb. Same Phrases section in all arms.

| | B (v2b) | A (whole-range) | AR (A + one root) |
|---|---|---|---|
| **words, close** (120 words, 2 judges, 96 % exact agreement) | 44 % | 47 % | 46 % |
| **sentences, meaning 0–3** (60, 3 judges) | 1.40 | 1.31 | 1.16 |
| roots per word (nouns) | 1.70 (1.83) | 1.51 (1.62) | 1.11 (1.00) |
| roots written with a value | 53 % | 78 % | 93 % |
| values with \|v\| ≤ 3 | 21 % | 51 % | 57 % |
| words per word-code | 1.07 | 1.05 | 1.39 |

| contrast | words | sentences |
|---|---|---|
| A − B | +2.5 pp [−4.8 … +9.6] | −0.09 [−0.28 … +0.11] |
| AR − A | −1.2 pp [−8.1 … +5.8] | **−0.15 [−0.29 … −0.01]** |
| AR − B | +1.2 pp [−6.7 … +9.2] | **−0.24 [−0.42 … −0.06]** |

**By the rules in dec.md:**
- **Anchors (A − B):** both intervals include 0; the manipulation check shows the range is used (mid values 21 % → 51 %)
  → whole-range anchors may stay; they neither help nor hurt measurably.
- **Root rule (AR − A):** significantly worse in sentences → **dropped**; nouns keep 1–3 roots.

Claude's forecast: words B 45 / A 47 / AR 50 %, sentences B 1.05 / A 1.10 / AR 1.00; mid values at least doubled — words
and manipulation right, sentences wrong in direction for A (forecast +0.05, got −0.09, n.s.).

## What it means

1. **Encoders follow the scale paragraph.** Told "every value is usable", they write mid values 2½× as often. But readers
   don't gain from it: a mid value is a finer point on an axis the reader still has to guess the word from.
2. **One root is too few for many words.** With one root an adjective has nothing to narrow it: *beautiful* `GOOD(=+4)
   SEE` (read right) became `GOOD(=+4)` → *excellent*; *sovereign* `RULE(=+4) JOIN(=-5)` (→ *independent*) became
   `RULE(=+5)` → *legal*. Adjectives: B 52 %, A 45 %, AR 36 % (21 words, for information). Nouns move the other way
   (45 / 47 / 51 %) because the one-root rule pushes them into phrases (`X FOR Y`), which read well for objects (as in
   func1). In sentences the extra phrases and lost narrowing cost −0.15.
3. **Anchors are vocabulary.** Moving a word between anchors changes what is read: v2b had `SAME(=-4)` = *special* (read
   right), v2c lists *special* together with *different* at −3, and both A and AR were read as *different*.

## Caveats

- One encoder per half of the items per arm: encoder differences are confounded with arm (encoder AR1 wrote its last 10
  sentences quickly — but not shorter than A1's).
- Sentence scores are within this run only (B = 1.40 here, while earlier runs scored min-co on the same sentences around 1.0–1.1 — judge drift between runs).
- Words: one code per word, first answer only.
