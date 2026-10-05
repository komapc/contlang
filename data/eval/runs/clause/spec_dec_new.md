# min-co: how to read a code (spec for the decoder)

A word is a **head root** with a part-of-speech suffix, followed by **modifiers**. Modifiers are further roots
(each also with a suffix when it is a word, or just `ROOT(=v)` when it only sets a value on its own axis).
Order: the head first, each next item refines everything before it (left to right). Up to 3 roots.

Suffixes: `-o` thing/noun, `-i` verb/action, `-a` quality/adjective, `-e` manner/adverb.
`E` marks the object ("E X" = acting on X). `PI` marks a noun used as a modifier. `?` = asked value.

44 roots (NSM-like primitives): GOOD, BIG, NEAR, ABOVE, LIVE, SAME, TIME, INSIDE, PART, SIDE, KNOW, WANT, HEAT, BEGIN, GIVE, TOUCH, MATTER, SEX, HAPPEN, THINK, CAN, MANY, SOMEONE, THING, MOVE, FEEL, RULE (law, rule, govern), CHANGE (change, become different), PARTICULAR (particular, specific, special), ART (skill, craft, discipline), JOIN (join, add, attach, separate), VALUE (price, worth), CARE (care, attention, diligence), TONE (tone, manner toward others), CONSUME (eat, drink), ABSTRACT (concrete vs abstract), MEASURE (measure, amount, ratio, rate), LONG (long object), SAY, BODY, SEE, DO, PLACE, FIGHT (fight, war, quarrel).

Axes: a root with a value `(=v)`, v from -5 to +5; not written = unspecified; `(=0)` = middle.
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

Use ABOVE, INSIDE, BIG only in their literal sense (up, inside, size).
Numbers are digits: `N-a` = ordinal (18-a = eighteenth), `N-o` = the number as a noun. Numbers and proper names (countries, persons, religions, Latin names) are written as they are, in quotes ("Christ").

Task: for each code, give the single English word it most likely stands for (plus 2 alternatives). The code is meant to
stand for ONE common English word. Do not look for any other files.


FORM (new notation): the word is written ROOTS | FORM. Before `|`: meaning roots (head first, up to three, each optionally with its axis value (=v)). After `|`: part of speech (o noun, i verb, a adjective, e adverb) and grammatical marks: T = tense (-2 past, 0 now, +2 future), N = number (0 none, +1 few, +3 several/plural, +5 all), M = probability/negation (-5 not, -3 maybe, +4 certainly). The marks are not roots; a missing mark means unspecified. Output an English word or short phrase that includes tense, number and negation.

More marks after `|`: A = aspect (-5 about to start / beginning ... 0 in progress ... +5 completed); C = degree (-3 less, +3 more = comparative, +5 most = superlative; applies to the root's axis); D = definiteness (-3 indefinite 'a', +3 definite 'the'); `!` = command (imperative); `?` = question.
PHRASES: a sentence is a sequence of words and particles. A word is ROOTS | FORM (see FORM above): it ends where the next uppercase root, quoted item or particle begins. Particles: E = direct object of the preceding verb; PI = a noun that defines the preceding noun (compound / "of"); LA = context or condition clause before a main clause ("although/if/when"); [ ... ] = a clause used as a modifier, complement or content; "..." = a quoted name, number, Latin or technical term kept as is. There is no separate particle for the predicate: a word with part of speech `i` is the verb. Decode each numbered line into ONE fluent English sentence. This is an encyclopedia text.
CLAUSES: `;` separates independent clauses of a long sentence; `[ ... ]` marks a nested or argument clause. Every word has its own `| FORM`.



## Extra form labels V and R
Both go after `|` with the other form labels; scale -5..+5, rule of zero (not written = not specified).
- V (voice): V-4 subject undergoes the action (passive); V0 happens by itself; V+4 subject acts deliberately.
- R (event time relative to a reference point, Reichenbach E vs R). `T` places the reference point R relative to now; `R` places the event relative to R: R-3 earlier than the reference point, R0 same time, R+3 later. Examples: "had left" = `T-2 R-3`; "later" in a past narrative = `T-2 R+3`; "will have finished" = `T+2 R-3`; "was going to" = `T-2 R+3`. The reference point is the nearest time or event named to the left (start of text: now), or is set by a clause `LA [ ... ]` ("after X") or a quoted date. R is not aspect A (A = phase of the event itself). Use R, not `TIME(=+n)`, for later/subsequent/earlier/before/after/then/initially; `TIME(=+1)` reads as "soon". "small" = `BIG(=-3)` alone, no PART.

Task: each line is one code standing for ONE English word or short phrase (a single common word in the intended sense). Give your single best English word or phrase for each.

## Extra form label I (intensity)
- I = how strongly the quality or action named by the head word is present: I-5 barely / hardly, I-2 somewhat, I0 fairly / moderately, I+2 quite, I+4 very, I+5 extremely / utterly. Written once on the head word after `|`, like the other labels (not counted among the 3 roots), e.g. `GOOD(=+3) | a I+4`. I is not the comparison label C (C = more / less than something; I = degree of intensity). Do not use BIG(=+5) as an intensifier.

## Extra form label K (causative / inducement)
- K = the subject acts on someone else (given by E) so that they do or undergo the action of the verb: K-5 prevent / discourage / forbid ... K0 allow / let ... K+5 force / compel / cause. With no action root the base action is DO. Written once on the verb after `|`, like other labels (not counted among the 3 roots). Examples: `DO | i K+4 E SOMEONE(=-3)` = "made them do (it)"; `CONSUME | i K+4 E SOMEONE` = "fed"; `DO | i K-4 E SOMEONE` = "stopped / prevented them".
