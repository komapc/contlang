# roots1 — fewer roots cost a lot: 10 roots 13 %, 20 → 19 %, 30 → 34 %, 51 → 43 % (v2b) / 52 % (v2c)

Pre-registered: [dec.md](dec.md) (commit `dae081d`, before codes). Script: [run.py](run.py); numbers [result.txt](result.txt),
chart points [points.json](points.json), codes [codes.json](codes.json), all answers and judge scores [answers/](answers/).
Chart: [size1/axes.svg](../size1/axes.svg).

## Result (120 size1 words, first reader answer, 3 readers × 2 judges per cell; judges agree exactly on 90 %)

| roots | 1 word | ≤ 2 words | ≤ 3 words | ≤ 3 words − V2B, pp [95 %] |
|---|---|---|---|---|
| R10 (10 most used) | 10 % | 10 % | 13 % | −29.6 [−39.2 … −19.2] |
| R20 | 23 % | 22 % | 19 % | −24.2 [−32.9 … −14.6] |
| R30 | 27 % | 32 % | 34 % | −8.8 [−19.2 … +2.1] |
| V2B (51, size1 answers re-judged) | 38 % | 40 % | 43 % | — |
| V2C (51, whole-range anchors) | 41 % | 44 % | 52 % | **+8.8 [0.0 … +17.5]** |

Token-weighted (as size1's U, used on the chart): R10 14 %, R20 20 %, R30 34 %, V2B 46 %, V2C 51 % (≤ 3 words).

**Forecast vs result** (≤ 3 words): R10 25 → 13, R20 35 → 19, R30 42 → 34, V2B 46 → 43, V2C 47 → 52. The curve is
steeper than forecast and does **not** flatten after 30 roots: every added root still pays.

## What it means

1. **Root count matters more than phrase length.** Going from 1 word to 3 words adds 0–9 pp; going from 30 to 51 roots
   adds ~10–20 pp. With 10–20 roots, longer phrases do not help at all (R20: 23 → 19 %): encoders write 2.5–2.7 roots per
   code, but so few, so general roots do not pin the word down.
2. **Min-co stays above the PCA 3-value line at every X** (token-weighted, ≤ 3 words vs 3 values: 10 roots 14 vs 9 %,
   20 → 20 vs 18 %, 30 → 34 vs 24 %, 51 → 46 vs 34 %), using 1.7–2.9 roots per code.
3. **v2c (whole-range anchors) vs v2b**: +8.8 pp at ≤ 3 words, interval touching 0. axes1 measured the same change at
   +2.5 pp n.s. Together: likely a small real gain, not proven.
4. **For the design**: no sign of a plateau at 51 → a bigger root set (or a lexicon) is still the main lever; cutting roots
   for learnability costs heavily below ~30.

## Caveats

- 2 encoders per arm, 120 words; per-word variation of encoders is large.
- R10/R20/R30 keep spec examples that use removed roots (with a note "not available"); no code used a removed root.
  One R10 code (reader R10_3, line 98) has 4 words, over the limit; kept.
- V2B readings are size1's (another day, same spec and model); only judging is shared. V2C and R-arms are new.
- Roots ranked by v1 use in big1000 codes (6 new v2b roots by their v2b2 rate) — "most used", not optimally chosen subsets.
