# Encoder instructions (sentence test, Toki-Pona style notation)

You will encode English sentences (encyclopedia text) into min-co, one independent code per numbered sentence. A different person will decode your codes WITHOUT seeing the sentence, using only the spec below, so keep the meaning recoverable.

Rules:
- Use ONLY the 44 roots in the spec. Never invent roots, never use English words as roots. Quote ONLY proper names (countries, persons, places, religions), numbers, dates and Latin or chemical names that have no root. NEVER put ordinary English words in quotes (not even nouns like bell, sea, books, websites): express every ordinary word with roots, even if the result is long or approximate. Technical terms with no root may be quoted only if they are scientific names (Latin, chemical).
- One code per input sentence, same numbering ("1. code"), no other text.

44 roots (NSM-like primitives): GOOD, BIG, NEAR, ABOVE, LIVE, SAME, TIME, INSIDE, PART, SIDE, KNOW, WANT, HEAT, BEGIN, GIVE, TOUCH, MATTER, SEX, HAPPEN, THINK, CAN, MANY, SOMEONE, THING, MOVE, FEEL, RULE (law, rule, govern), CHANGE (change, become different), PARTICULAR (particular, specific, special), ART (skill, craft, discipline), JOIN (join, add, attach, separate), VALUE (price, worth), CARE (care, attention, diligence), TONE (tone, manner toward others), CONSUME (eat, drink), ABSTRACT (concrete vs abstract), MEASURE (measure, amount, ratio, rate), LONG (long object), SAY, BODY, SEE, DO, PLACE, FIGHT (fight, war, quarrel).

Axes: a root takes a value on its own axis, not written = unspecified.
- GOOD: -5 terrible ... +5 excellent
- BIG: -5 tiny ... +5 huge (size, degree, intensity)
- NEAR: -5 far ... +5 near/here
- ABOVE: -5 below/down ... +5 above/up
- LIVE: -5 dead ... +5 alive (-2 = asleep/barely alive)
- SAME: -5 different/opposite ... +5 identical/exactly
- TIME: -5 long ago ... 0 now ... +5 someday (-1 just now, +1 soon)
- INSIDE: -5 outside ... +5 inside/innermost
- PART: -5 particle/crumb ... -2 a part/piece/member-of ... +2 the whole/complete (also 'entirely') ... +5 a group/collection made of many wholes (a set, union); after a head noun, PART(=+5) means a collection of those things
- SIDE: -5 back ... +5 front
- KNOW: -5 ignorant ... +5 sure/knowing
- WANT: -5 hate/refuse ... +5 love/crave
- HEAT: -5 ice cold ... 0 lukewarm ... +5 fire hot
- BEGIN: -5 start/begin ... 0 ongoing/middle ... +5 finish/end (-4 first, +4 last)
- GIVE: -5 take/steal ... 0 exchange ... +5 give/donate
- TOUCH: -5 soft/gentle ... 0 ordinary ... +5 hard/sharp
- MATTER: -5 solid ... 0 liquid ... +5 gas
- SEX: -5 female ... +5 male
- HAPPEN: -5 cause/origin ... 0 plain event ... +5 consequence/result (position in a chain of events)
- THINK: -5 doubt/hesitate ... 0 think ... +5 decide/conclude
- CAN: -5 impossible ... +5 can/easily (-3 hard)
- MANY: one-sided 0 none ... +5 all (+4 most, +3 many, +1 few)
- SOMEONE: -5 they/other ... 0 someone ... +3 you ... +5 I/me
- THING: -5 inanimate/stone ... 0 plant ... +4 animal
- MOVE: -5 stand still ... 0 walk ... +5 sprint/very fast
- FEEL: -5 calm/low-energy ... +5 excited/intense (pleasant or not is GOOD)
- RULE: -5 personal/private/informal ... 0 ordinary ... +5 official/institutional/law (RULE(=+4) = authority, an institution)
- CHANGE: -5 stay/remain/not change ... 0 change ... +5 transform completely (direction of change comes from other roots: CHANGE BIG(=+3) = grow, CHANGE GOOD(=+3) = improve)
- PARTICULAR: -5 general/universal ... 0 ordinary ... +5 particular/unique/specific
- ART: -5 calculation/technology/devices/exact science ... 0 mixed ... +5 creativity/culture/humanities/arts. The bare root means skill, craft, discipline.
- JOIN: -5 separate/remove/subtract ... 0 composition unchanged ... +5 join/add/attach/unite.
- VALUE: -5 cheap/worthless ... 0 ordinary price ... +5 expensive/valuable/precious.
- CARE: -5 careless/hasty ... 0 ordinary ... +5 careful/thorough/meticulous.
- TONE: -5 rude/cold/hostile/harsh ... 0 neutral ... +5 polite/warm/friendly/sincere.
- CONSUME: -5 emit/output (excrete, write, speak, spit, exhale) ... 0 exchange ... +5 take in/intake (eat, drink, read, listen, inhale). The channel or object is given by a second root, e.g. SEE, SAY, BODY.
- ABSTRACT: -5 concrete/physical/tangible (house, kick, shake) ... 0 mixed ... +5 abstract/mental/intangible (theory, principle, assume, imply). A noun or verb is on the physical or the mental side; as an adjective: concrete / abstract.
- MEASURE: -5 a magnitude in itself (size, amount, length, weight, number) ... 0 level, degree, extent ... +5 a magnitude relative to another (ratio, rate, proportion, percentage, average). Measuring as an action: `MEASURE | i` (to measure); a unit is a magnitude used as a standard (`MEASURE SAME`). As an adjective: measurable / proportional.
- LONG: -5 thin flexible (thread, rope, hair, wire) ... 0 stick, rod, twig ... +5 thick rigid (pole, log, beam, pillar). The root for long objects; as an adjective: long, tall (`LONG | a`).
- SAY: -5 whisper, murmur, mumble (quiet) ... 0 ordinary speech ... +5 shout, scream, roar (loud). Also for noises: SAY(=+3) THING | o = noise, SAY(=-3) | o = whisper.

NOTATION (Toki-Pona style, no part-of-speech suffixes):
- A word is one root, optionally with its axis value glued on: `GOOD+3`, `TIME-2`, `MANY+5`, `GOOD0` (explicit middle). Axis value -5..+5 (MANY 0..+5). Roots without an axis (BODY SEE DO PLACE FIGHT) never take one.
- A phrase is a head word followed by modifier words separated by spaces; each modifier refines everything before it, exactly like an English compound: `THING+4 BIG+5` = a big animal, `PLACE LIVE` = dwelling. One English word may need several min-co words; there is no limit of three roots, but stay short.
- Parts of speech come from position, as in Toki Pona: the first phrase of a clause is the subject (a noun phrase); `LI` introduces the predicate (a verb phrase: head = action, later words = how); `E` introduces the direct object (noun phrase); a modifier after a noun head is an adjective, after a verb head an adverb. A root can be any part of speech by position.
- Particles: `LI` predicate; `E` object; `PI` a noun phrase that defines the preceding noun (compound / 'of'); `LA` context or condition clause before a main clause (although / if / when); `AND` and / also; `PE` agent after a passive (V-4); `[ ... ]` a clause used as a modifier or content; `;` separates independent clauses of a long sentence; `"..."` quoted names, numbers, Latin or technical terms kept as is, written as a word of its own.
- Example: `SOMEONE LI SAY.T-2 E THING PI SAY` ; `LA [ SOMEONE LI LIVE ] THING+4 LI MOVE+4.T0`.

Grammatical marks (NOT roots) are glued to the head word of a phrase with `.`, scale -5..+5, not written = unspecified: `T` tense: time of reference point relative to now (T-2 past, T0 now, T+2 future); `R` event time relative to the reference point (R-3 earlier, R0 same time, R+3 later; "had left" = T-2 R-3); `N` number (N0 none, N+1 few, N+3 several/plural, N+5 all); `M` negation/probability (M-5 not, M-3 maybe, M+4 certainly); `A` aspect (A-5 about to begin, A0 in progress, A+5 completed); `C` comparison (C-3 less, C+3 more, C+5 most); `I` intensity (I-4 hardly, I-2 somewhat, I+2 quite, I+4 very, I+5 extremely; I0 is never written); `D` definiteness (D-3 'a', D+3 'the'); `V` voice (V-4 passive: the subject undergoes the action; V0 happens by itself; V+4 acts deliberately); `K` causative (K-5 prevent ... K0 allow ... K+5 force/cause; base action DO); `!` command; `?` question. Example: `SAY.T-2.M-5` = did not say; `THING+4.N+3` = several animals. At most one of each mark per phrase.
