# roots2 — the v2c curve: 1 root 0 %, 10 → 16 %, 30 → 40 %, 51 → 54 %, 300 → 77 %

Pre-registered: [dec.md](dec.md) (commit `f60c5e8`, before codes). Script: [run.py](run.py); numbers [result.txt](result.txt),
chart points [points.json](points.json), word roots [word_roots.json](word_roots.json), leakage [leak.txt](leak.txt),
codes [codes.json](codes.json), all answers and judge scores [answers/](answers/). Chart: [size1/axes.svg](../size1/axes.svg)
(made by [plot.py](plot.py)).

## Result (120 size1 words, one code ≤ 3 words, 2 readers × 2 judges; judges agree exactly on 93 %)

| roots X | close | token-weighted U [95 %] | targets that are roots | close, target not a root | forecast U |
|---|---|---|---|---|---|
| 1 | 0 % | 0 % | 0 | 0 % | 3 % |
| 3 | 4 % | 4 % [1 … 8] | 0 | 4 % | 6 % |
| 10 | 15 % | 16 % [11 … 22] | 0 | 15 % | 14 % |
| 20 | 27 % | 28 % [21 … 36] | 2 | 26 % | 22 % |
| 30 | 39 % | 40 % [33 … 48] | 2 | 38 % | 32 % |
| 51 (all v2c) | 52 % | 54 % [47 … 62] | 3 | 51 % | 48 % |
| 100 (+ 49 word roots) | 54 % | 57 % [49 … 64] | 8 | 51 % | 56 % |
| 200 (+ 149) | 71 % | 74 % [67 … 80] | 18 | 66 % | 64 % |
| 300 (+ 249) | 74 % | 77 % [70 … 83] | 29 | 66 % | 70 % |

Codes stay short at every X: 1.0–1.1 words and 1.5–2.1 roots per code.

## What it means

1. **Up to 51 roots the curve is steep and nearly straight on a log scale**: each doubling of the root set adds ~12–14 pp.
   The v2c roots at 51 (54 %) agree with roots1's V2C arm (51 %, other protocol and judges).
2. **51 → 100 adds almost nothing** (54 → 57 %, non-root targets 51 → 51 %): the first 49 word roots are very general
   verbs and adjectives (*make, go, new, take, come, get, use* …) that overlap what the v2c roots already say.
3. **100 → 200 adds a lot** (57 → 74 %), and not only through identity: on targets that are *not* roots, 51 → 66 %. The roots
   added between 100 and 200 are everyday concrete nouns (*city, war, country, hand, water, church, family, room, car*), and with them
   encoders build far clearer codes (*CAR CONTROL* → *drive*). This is the gap found in words1 ("everyday concrete roots").
4. **200 → 300 adds little** for non-root targets (66 → 66 %); the extra 3 pp come from targets that became roots.
5. Compared with the computer line (3 numbers per word on X automatic axes) min-co stays above at every X ≥ 3 (at 51: 54 vs 34 %).

For the design: ~50 abstract roots + ~150 everyday concrete words is where most of the gain is; beyond that the curve
is a lexicon (identity), not composition.

## Caveats

- Leakage above 51: up to 29 of the 120 targets are themselves roots (all from Brown rank ≤ 300); "close, target not a root"
  is the cleaner measure there. The token-weighted U gives band 1 (rank ≤ 300) a third of the weight, so it is the most
  affected.
- 2 encoders and 2 readers per X; one encoder's choices move a point by several pp (see the intervals).
- Word roots are the most frequent Brown lemmas, not a chosen set; a designed set of ~150 concrete roots may do better.
- X = 1 (MOVE only) is degenerate: no word was read close.
