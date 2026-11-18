# min-co v2c (draft) — whole-range axes, one root per non-verb

Draft built on v2b; not adopted. Tested in [axes1](../../data/eval/runs/axes1/).

**Why.** In 1792 v2b codes, encoders wrote axis values almost only at the poles (±5, ±4): value entropy was low for KNOW
(1.25 bits), THINK (1.31), RULE (1.12), JOIN (0.88), CONSUME (0.74), MEASURE (0.79); SAY took no value in 86 % of uses, and
DO, PLACE, SEE, BODY, TEXT, HAPPEN had no axis at all. A root with 11 values that uses 3 of them wastes most of its range.
Separately, one-root codes read best (big1000: 87 % close for one-root adjectives, 76 % verbs, vs ~40–55 % with 2–3 roots;
observational).

**Changes.**
1. [roots_en.md](roots_en.md): every axis has named anchors across the whole range (−5, about −2, 0, about +2/+3, +5).
   - New axes: BODY (head … trunk … arm/hand … leg/foot), SEE (hidden … glimpse … see … watch … visible), DO (rest … try …
     do … make/work … labour), PLACE (spot … room … building … town … country/world), TEXT (letter/sign … word … sentence …
     document … book). HAPPEN keeps no axis.
   - SAY becomes a speech-act axis (ask … answer … say … claim/promise … order); loudness moves to the I mark.
   - KNOW, THINK, RULE, SAME, CHANGE, JOIN, MEASURE, CONSUME get intermediate anchors.
2. Scale paragraph: every value −5…+5 is usable; between two anchors means between them; do not round to ±5.
3. Root rule (arm AR in axes1): a noun, adjective or adverb has exactly one root; a verb has 1–3 (action, then body part,
   manner or object kind). Otherwise use a role or a phrase of up to 3 words. Tense stays the T mark (grammatical axes —
   T R A N M C I D V K — are marks, not roots).
