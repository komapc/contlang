# Encoder instructions (sentence test, Toki-Pona style notation)

You will encode English sentences (encyclopedia text) into min-co, one independent code per numbered sentence. A different person will decode your codes WITHOUT seeing the sentence, using only the spec below, so keep the meaning recoverable.

Rules:
- Use ONLY the {{N_ROOTS}} roots in the spec. Never invent roots, never use English words as roots. Quote ONLY proper names (countries, persons, places, religions), numbers, dates and Latin or chemical names that have no root. NEVER put ordinary English words in quotes (not even nouns like bell, sea, books, websites): express every ordinary word with roots, even if the result is long or approximate. Technical terms with no root may be quoted only if they are scientific names (Latin, chemical).
- One code per input sentence, same numbering ("1. code"), no other text.

{{ROOTS}}

Axes: a root takes a value on its own axis, not written = unspecified.
{{AXES}}

NOTATION (Toki-Pona style, no part-of-speech suffixes):
- A word is one root, optionally with its axis value glued on: `GOOD+3`, `TIME-2`, `MANY+5`, `GOOD0` (explicit middle). Axis value -5..+5 (MANY 0..+5). Roots without an axis (BODY SEE DO PLACE FIGHT) never take one.
- A phrase is a head word followed by modifier words separated by spaces; each modifier refines everything before it, exactly like an English compound: `THING+4 BIG+5` = a big animal, `PLACE LIVE` = dwelling. One English word may need several min-co words; there is no limit of three roots, but stay short.
- Parts of speech come from position, as in Toki Pona: the first phrase of a clause is the subject (a noun phrase); `LI` introduces the predicate (a verb phrase: head = action, later words = how); `E` introduces the direct object (noun phrase); a modifier after a noun head is an adjective, after a verb head an adverb. A root can be any part of speech by position.
- Particles: `LI` predicate; `E` object; `PI` a noun phrase that defines the preceding noun (compound / 'of'); `LA` context or condition clause before a main clause (although / if / when); `AND` and / also; `PE` agent after a passive (V-4); `[ ... ]` a clause used as a modifier or content; `;` separates independent clauses of a long sentence; `"..."` quoted names, numbers, Latin or technical terms kept as is, written as a word of its own.
- Example: `SOMEONE LI SAY.T-2 E THING PI SAY` ; `LA [ SOMEONE LI LIVE ] THING+4 LI MOVE+4.T0`.

Grammatical marks (NOT roots) are glued to the head word of a phrase with `.`, scale -5..+5, not written = unspecified: `T` tense: time of reference point relative to now (T-2 past, T0 now, T+2 future); `R` event time relative to the reference point (R-3 earlier, R0 same time, R+3 later; "had left" = T-2 R-3); `N` number (N0 none, N+1 few, N+3 several/plural, N+5 all); `M` negation/probability (M-5 not, M-3 maybe, M+4 certainly); `A` aspect (A-5 about to begin, A0 in progress, A+5 completed); `C` comparison (C-3 less, C+3 more, C+5 most); `I` intensity (I-4 hardly, I-2 somewhat, I+2 quite, I+4 very, I+5 extremely; I0 is never written); `D` definiteness (D-3 'a', D+3 'the'); `V` voice (V-4 passive: the subject undergoes the action; V0 happens by itself; V+4 acts deliberately); `K` causative (K-5 prevent ... K0 allow ... K+5 force/cause; base action DO); `!` command; `?` question. Example: `SAY.T-2.M-5` = did not say; `THING+4.N+3` = several animals. At most one of each mark per phrase.
