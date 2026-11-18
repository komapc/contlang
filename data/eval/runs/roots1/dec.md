# Pre-registration (2026-11-12, before codes): roots1 — learn X roots, how surely is a word guessed?

**Question** (user): min-co with fewer roots, and v2c, on the "X axes → accuracy" chart next to PCA axes
([size1 axes.svg](../size1/axes.svg)). Measurement for the chart, not a design decision.

**Arms** (specs: [specs/](specs/), built by [run.py](run.py)):
- **R10, R20, R30** — the size1 min-co (v2b) spec with only the 10 / 20 / 30 most used roots ([rank.json](rank.json): use in
  the 1000 big1000 v1 codes; the 6 roots new in v2b ranked by their rate in v2b2 codes). Marks, roles, phrases unchanged.
  Examples that use removed roots stay, with a note that those roots are not available.
- **V2C** — v2c roots and scale paragraph (as axes1 arm A), otherwise the size1 spec.
- **V2B** — size1's own min-co readings (readers mc1a, mc2a, mc3a), re-judged here.

**Items, protocol** — as size1: the same 120 words; encoders (Sonnet, 2 per arm) write 1 word / ≤ 2 / ≤ 3 words per word;
3 Haiku readers per arm on Latin-square lists; 5 Sonnet judges, each answer scored by 2 (0 / 1 / 2). Agents: 8 + 12 + 5 = 25.

**Measures:** share close per arm × phrase limit; token-weighted with Brown band shares ([band_shares.json](band_shares.json)),
as size1's U at N = 0; for information: R10/R20/R30/V2C − V2B at ≤ 3 words (paired bootstrap).

**Claude's forecast** (≤ 3 words): R10 ≈ 25 %, R20 ≈ 35 %, R30 ≈ 42 %, V2B ≈ 46 %, V2C ≈ 47 %; i.e. min-co stays above
the PCA 3-value line at every X, and the curve flattens after ~30 roots.
