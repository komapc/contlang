# Pre-registration (2026-11-12, before codes): roots2 — the v2c curve, learn X roots from 1 to 300

**Question** (user): roots1 had too few v2c points; measure v2c from 1 to 300 roots, at least 5 points in the middle.
Measurement for the chart ([size1 axes.svg](../size1/axes.svg)), not a design decision.

**Arms** X = 1, 3, 10, 20, 30, 51, 100, 200, 300 (specs: [specs/](specs/), built by [run.py](run.py)):
- X ≤ 51 — the v2c spec (as roots1 arm V2C) with only its X most used roots ([roots1/rank.json](../roots1/rank.json)).
- X > 51 — all 51 v2c roots + (X − 51) **word roots**: the most frequent Brown content lemmas in size1's rank order, skipping
  root names, link words, adverbs and inflected forms ([word_roots.json](word_roots.json), rule fixed without looking at the
  items). A word root means just that English word, with a WordNet gloss, and takes no value. This is where roots turn into a
  lexicon — the upper part of the curve measures "roots + basic vocabulary".
- X = 51 is re-run in this protocol (not spliced from roots1).

**Leakage** ([leak.txt](leak.txt), computed before codes): target words that are themselves a root — 3 at X 51, 8 at 100,
18 at 200, 29 at 300, almost all from band 1 (Brown rank ≤ 300). Reported separately: close on targets that are not roots.

**Protocol** — size1's 120 words. 2 Sonnet encoders per arm (60 words each) write ONE code, ≤ 3 words ([tasks/write.md](tasks/write.md));
2 Haiku readers per arm read all 120 codes (own shuffle); 6 Sonnet judges, each answer scored by 2 (0 / 1 / 2, close = 2).
Agents: 18 + 18 + 6 = 42.

**Measures:** share close per X; token-weighted U with Brown band shares (as size1, roots1) with a 95 % bootstrap over words
(within bands); close on non-root targets.

**Claude's forecast** (U): X 1 ≈ 3 %, 3 ≈ 6 %, 10 ≈ 14 %, 20 ≈ 22 %, 30 ≈ 32 %, 51 ≈ 48 %, 100 ≈ 56 %, 200 ≈ 64 %, 300 ≈ 70 %;
on non-root targets the curve flattens above 51 (≈ 50 → 55 %).
