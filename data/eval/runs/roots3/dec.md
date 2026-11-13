# Pre-registration (2026-11-13, before codes): roots3 — 4 and 5 roots per word, v2c and PCA

**Question** (user): add 4 and 5 (values / roots per word) to the v2c curve and to the PCA line
([size1 axes.svg](../size1/axes.svg)). Measurement for the chart, not a design decision.

**Arms** — roots2's specs (v2c roots; above 51 the same word roots), X = 10, 30, 51, 100, 300:
- **N4, N5** — the encoder writes ONE code (≤ 3 words) with **exactly 4 / 5 roots in total** ([tasks/write.md](tasks/write.md));
  each word still ≤ 3 roots. Exact, not "up to": in roots2 encoders used only 1.5–2.1 roots although 3 per word were
  allowed, so "up to" would measure nothing; PCA also always gets exactly r values.
- **N3** — roots2's codes and readings for the same X (free number of roots, ≤ 3 words), re-judged in this batch.
Readers get roots2's decoder spec unchanged (they are not told N).

**Protocol** — size1's 120 words; 2 Sonnet encoders (60 words each) and 2 Haiku readers (all 120) per new arm; 10 Sonnet
judges, every answer (2400 new + 1200 roots2) scored by 2. Agents: 20 + 20 + 10 = 50.

**PCA** — [size1/machine_axes.py](../size1/machine_axes.py) with r = 4 and 5 values per word (no agents).

**Measures:** token-weighted U per X × N with 95 % bootstrap; N4 − N3 and N5 − N3 (paired over words, unweighted close).

**Claude's forecast:** at X ≤ 30 N4/N5 a little worse than N3 (−3 pp: forced roots add noise when few roots exist); at 51–300
about equal or +3 pp. PCA: 4 values ≈ +10 pp over 3 at X = 51, 5 values ≈ +20 pp — the machine gains much more from extra
values than min-co does from extra roots.

## Amendment (2026-11-13, after the first result, before X = 200 codes)

User asked for X = 200 too. Same protocol: arms X200N4, X200N5 (2 encoders, 2 readers each) + roots2's X200 readings as N3.
They are judged in a separate small batch (2 Sonnet judges, each scores all 720 X = 200 answers), so every answer is still
scored by 2. Forecast: N4 / N5 within ±5 pp of N3 (74 %), as at the other X.
