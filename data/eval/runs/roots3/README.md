# roots3 — 4 and 5 roots per word: min-co +3 pp (n.s.), PCA +18…+29 pp

Pre-registered: [dec.md](dec.md) (commit `18cfc82`, before codes). Script: [run.py](run.py); numbers [result.txt](result.txt),
chart points [points.json](points.json), codes [codes.json](codes.json), all answers and judge scores [answers/](answers/).
Chart: [size1/axes.svg](../size1/axes.svg) (made by [roots2/plot.py](../roots2/plot.py)).

## Result — min-co v2c (120 size1 words, 2 readers × 2 judges per arm; judges agree exactly on 93 %;
X = 200 added later by the [dec.md](dec.md) amendment, judged in its own batch of 2)

N3 = roots2's codes (free number of roots, in practice 1.5–2.1), re-judged in this batch; N4 / N5 = encoder told to use
**exactly** 4 / 5 roots in one code of ≤ 3 words (they complied: 1439 of 1440 codes exact).

| roots X | N3 (free) | N4 | N5 | N4 − N3, pp [95 %] | N5 − N3, pp [95 %] |
|---|---|---|---|---|---|
| 10 | 17 % | 20 % | 19 % | +4.0 [−2.5 … +10.2] | +3.3 [−2.1 … +8.8] |
| 30 | 40 % | 46 % | 47 % | +6.2 [−1.9 … +13.8] | +7.1 [−0.2 … +14.8] |
| 51 | 54 % | 59 % | 53 % | +5.2 [−3.1 … +13.8] | −0.4 [−8.1 … +7.1] |
| 100 | 58 % | 61 % | 63 % | +5.8 [−2.3 … +14.0] | +7.1 [−1.2 … +15.4] |
| 200 | 74 % | 67 % | 74 % | −4.4 [−12.5 … +3.8] | +2.3 [−5.2 … +9.8] |
| 300 | 76 % | 76 % | 73 % | +1.7 [−5.6 … +9.0] | −0.2 [−7.1 … +7.1] |
| **pooled over X** | | | | **+3.1 [−1.1 … +7.2]** | **+3.2 [−1.0 … +7.4]** |

(cells: token-weighted U; differences: unweighted close, paired over words; pooled = mean over the 6 X, bootstrap over words)

## PCA axes (size1/machine_axes.py, no agents) — U

| axes X | 3 values | 4 values | 5 values |
|---|---|---|---|
| 10 | 9 % | 12 % | 14 % |
| 30 | 24 % | 35 % | 44 % |
| 51 | 34 % | 52 % | 63 % |
| 120 | 52 % | 73 % | 87 % |
| 300 | 59 % | 80 % | 92 % |

## What it means

1. **More roots per word barely help min-co**: forcing 4 or 5 roots gives +3 pp on average, not significant (without
   X = 200 the 4-root gain was +4.6 [+0.3 … +8.7]; X = 200 went −4.4); no single X is significant. The forecast (−3 pp at X ≤ 30) was wrong in sign: even with 10
   roots the extra roots did not add noise.
2. **PCA gains much more** from extra values (+18 pp at X = 51 for 4, +29 for 5 — more than forecast +10 / +20). With 4
   values PCA ≈ min-co at X ≈ 51–100; with 5 values it is above min-co from X ≈ 51.
3. Why: a PCA value is a precise coordinate read by a reader who knows the exact position of all 21,514 words; each extra
   value multiplies the distinguishable cells. A min-co root is a coarse human concept, and the Haiku reader decodes words
   from meaning, so after 2 roots the next ones mostly repeat what is already said. The PCA reader is an idealised machine
   (exact word vectors, nearest-neighbour search) — no human could read it; min-co is meant to be learned and read by people.

## Caveats

- N3 readings come from roots2's readers (another batch); N4 / N5 readers are new. Judging is one batch for all.
- 2 encoders and 2 readers per arm; intervals per X are ±7–8 pp.
- Above 51 up to 29 targets are themselves roots (roots2/leak.txt), same for all N.
