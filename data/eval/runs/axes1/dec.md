# Pre-registration (2026-11-12, before codes): axes1 — whole-range axes and a one-root rule

**Question.** (1) Do anchors over the whole axis range ([v2c roots](../../../../lang/v2c/roots_en.md)) make encoders use
mid values and readers decode better than v2b? (2) Does "one root for a noun / adjective / adverb, up to 3 for a verb" read
better than free 1–3 roots? User's request: use the range more efficiently; single root for non-verbs, body etc. as
secondaries for verbs; any other decisions allowed.

**Arms** (specs built by [run.py](run.py) from v2b2 specs; [specs/](specs/)):
- **B** — v2b as is (control);
- **A** — v2c roots + new [scale paragraph](tasks/scale_v2c.md) ("every value is usable, do not round to ±5");
- **AR** — A + [root rule](tasks/roots_rule.md); examples changed to one-root nouns (house = `{ PLACE(=0) | o } FOR { LIVE | i }`,
  knife = `JOIN(=-4) | o tool`).
All arms get the same [Phrases](tasks/phrases.md) section (up to 3 words, FROM / FOR / AGAINST / LIKE / PI).

**Items.** The 120 words of [size1](../size1/items.json) (4 frequency bands; nouns, verbs, adjectives; one code each) and
the 60 bench1 dev sentences. Not chosen by failures.

**Agents.** Per arm 2 Sonnet encoders (60 words + 30 sentences each, [task](tasks/encode.md)), 2 Haiku word readers (all 120,
best + 2 alternatives) and 2 Haiku sentence readers (all 60). Judges: 2 Sonnet word judges score all 720 first answers
(0/1/2); 3 Sonnet sentence judges score the 360 readings (a third each + 30 overlap with the previous judge + bench1 anchors,
0–3). Total 6 + 12 + 5 = 23.

**Measures** (paired bootstrap over items, 5000, seed 0):
- primary: words — share close (2), A − B and AR − A; sentences — mean 0–3, A − B and AR − A;
- for information: AR − B; by part of speech; close-or-related;
- manipulation check ([check.txt](check.txt), from codes): share of roots with a value, value entropy, share of |v| ≤ 3,
  roots per word by part of speech.

**Decision (in advance):**
- **Anchors (A − B):** words ≥ +5 pp or sentences ≥ +0.15 with the interval above 0, and no significant loss on the other →
  whole-range anchors go into 2.0. Interval includes 0 → keep them only if the manipulation check shows the range is used
  (anchors cost nothing to learn beyond the root), otherwise v2b anchors stay. Significant loss → drop.
- **Root rule (AR − A):** not worse — lower bound above −5 pp (words) and −0.15 (sentences) → adopt (one root per non-verb
  is simpler to learn and parse). Significantly worse on either → drop; nouns then keep 1–3 roots.

**Claude's forecast:** manipulation check — A uses |v| ≤ 3 at least twice as often as B. Words: B 45 %, A 47 %, AR 50 %;
sentences: B 1.05, A 1.10, AR 1.00 (phrases cost something in sentences). Chance A − B is significant: ~25 %.
