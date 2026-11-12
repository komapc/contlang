# size1 — phrase limit barely matters for min-co (43 / 41 / 45 %), Toki Pona needs phrases (9 / 27 / 33 %)

Pre-registration: [dec.md](dec.md) (commit `a620173`, before codes). Script [run.py](run.py), results [result.txt](result.txt)
(including every word with its codes), curve [curve.json](curve.json), chart [plot.py](plot.py), codes
[codes.json](codes.json), readings and scores [answers/](answers/).

![share of text understood vs units to learn, by phrase limit](size.svg)

## Result (120 words, first answer, 2 readers × 2 judges per word and variant; judges agree exactly on 91 %)

| close | 1 word | up to 2 | up to 3 | words per code (k1 / k2 / k3) |
|---|---|---|---|---|
| **min-co** (82 units) | 43 % | 41 % | 45 % | 1.00 / 1.61 / 2.29 |
| **Toki Pona, cipher** (120 units) | 9 % | 27 % | 33 % | 1.00 / 2.00 / 2.98 |

| paired difference, pp [95 %] | min-co | Toki Pona |
|---|---|---|
| up to 2 − 1 word | −1.7 [−7.7 … +4.6] | **+17.9 [+10.8 … +25.2]** |
| up to 3 − 1 word | +2.1 [−6.5 … +10.6] | **+23.8 [+14.6 … +32.7]** |
| up to 3 − up to 2 | +3.8 [−4.6 … +12.1] | +5.8 [−2.3 … +13.8] |
| Toki Pona − min-co | 1 word −33.3; up to 2 −13.8; up to 3 −11.7 (all intervals below 0) | |

**Rule from dec.md: all min-co intervals include 0 → for reading single words the phrase limit does not matter; choose
it by learnability (shorter).** A min-co word already holds up to 3 roots, so a second and third word add little; given
the freedom, the encoder kept one word in 39 % (k2) and 23 % (k3) of codes. Toki Pona words are one root each, so it
needs phrases: going from 1 to 2 words triples its accuracy, the third word adds a little more.

By frequency band (close): min-co k1 53 / 40 / 42 / 35 % from the most to the least frequent band; Toki Pona k3
32 / 32 / 37 / 32 % — flat, because its phrases are equally vague for common and rare words.

## The curve

U(N) — share of Brown content-word tokens read close, with a lexicon of the N most frequent lemmas (entries read right
90 % of the time) and the measured band accuracy for the rest; L = 82 + N (min-co) or 120 + N (Toki Pona).

| N entries | min-co 1 / ≤2 / ≤3 | Toki Pona 1 / ≤2 / ≤3 |
|---|---|---|
| 0 | 44 / 42 / 47 % | 11 / 28 / 33 % |
| 300 | 56 / 55 / 58 % | 34 / 48 / 53 % |
| 1000 | 68 / 68 / 69 % | 55 / 64 / 66 % |
| 3000 | 79 / 78 / 78 % | 73 / 76 / 78 % |

The three min-co lines nearly coincide. Toki Pona starts far lower but the gap closes as the lexicon grows: from about
3000 entries the language under the lexicon hardly matters, because the lexicon covers 80 % of the text.

Claude's forecast (min-co 50 / 56 / 58, Toki Pona 25 / 38 / 43) was wrong for min-co (no gain from phrases) and too high
for Toki Pona.

## Caveats

- **Word level only.** In sentences Toki Pona reads better than min-co ([tpx1](../tpx1/README.md): tpx 1.54 vs mc 1.04):
  context resolves its broad words. This run says nothing about sentences.
- Absolute levels drift between runs (min-co without lexicon: 44 % here, 55 % in [size0](../size0/README.md) with a Haiku
  encoder and judge); compare only within this run.
- The dec.md count was wrong: 1440 readings (720 per language), not 720; each judge got 960 lines, as designed (2/3 each).
- The Toki Pona encoders first counted `pi` as free: 16 phrases over the limit were rewritten by the same encoders before
  any reading.
- One Toki Pona reader (tp2a) deliberately gave different answers to identical phrases; this mostly affects k1, where
  many words share one Toki Pona word.
- The curve is a model: a_lex = 0.9 assumed; ranks above 10 000 use the 3001–10000 band.
