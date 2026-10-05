# min-co: how to read a code (spec for the decoder)

A word is a **head root** with a part-of-speech suffix, followed by **modifiers**. Modifiers are further roots
(each also with a suffix when it is a word, or just `ROOT(=v)` when it only sets a value on its own axis).
Order: the head first, each next item refines everything before it (left to right). Up to 3 roots.

Suffixes: `-o` thing/noun, `-i` verb/action, `-a` quality/adjective, `-e` manner/adverb.
`E` marks the object ("E X" = acting on X). `PI` marks a noun used as a modifier. `?` = asked value.

{{ROOTS}}

Axes: a root with a value `(=v)`, v from -5 to +5; not written = unspecified; `(=0)` = middle.
{{AXES}}

Use ABOVE, INSIDE, BIG only in their literal sense (up, inside, size).
Numbers are digits: `N-a` = ordinal (18-a = eighteenth), `N-o` = the number as a noun. Numbers and proper names (countries, persons, religions, Latin names) are written as they are, in quotes ("Christ").

Task: for each code, give the single English word it most likely stands for (plus 2 alternatives). The code is meant to
stand for ONE common English word. Do not look for any other files.


FORM (new notation): the word is written ROOTS | FORM. Before `|`: meaning roots (head first, up to three, each optionally with its axis value (=v)). After `|`: part of speech (o noun, i verb, a adjective, e adverb) and grammatical marks: T = tense (-2 past, 0 now, +2 future), N = number (0 none, +1 few, +3 several/plural, +5 all), M = probability/negation (-5 not, -3 maybe, +4 certainly). The marks are not roots; a missing mark means unspecified. Output an English word or short phrase that includes tense, number and negation.

More marks after `|`: A = aspect (-5 about to start / beginning ... 0 in progress ... +5 completed); C = degree (-3 less, +3 more = comparative, +5 most = superlative; applies to the root's axis); D = definiteness (-3 indefinite 'a', +3 definite 'the'); `!` = command (imperative); `?` = question.
PHRASES: a sentence is a sequence of words and particles. A word is ROOTS | FORM (see FORM above): it ends where the next uppercase root, quoted item or particle begins. Particles: E = direct object of the preceding verb; PI = a noun that defines the preceding noun (compound / "of"); LA = context or condition clause before a main clause ("although/if/when"); [ ... ] = a clause used as a modifier, complement or content; "..." = a quoted name, number, Latin or technical term kept as is. There is no separate particle for the predicate: a word with part of speech `i` is the verb. Decode each numbered line into ONE fluent English sentence. This is an encyclopedia text.
{{CLAUSE_RULE}}



## Extra form labels V and R
Both go after `|` with the other form labels; scale -5..+5, rule of zero (not written = not specified).
- V (voice): V-4 subject undergoes the action (passive); V0 happens by itself; V+4 subject acts deliberately.
- R (event time relative to a reference point, Reichenbach E vs R). `T` places the reference point R relative to now; `R` places the event relative to R: R-3 earlier than the reference point, R0 same time, R+3 later. Examples: "had left" = `T-2 R-3`; "later" in a past narrative = `T-2 R+3`; "will have finished" = `T+2 R-3`; "was going to" = `T-2 R+3`. The reference point is the nearest time or event named to the left (start of text: now), or is set by a clause `LA [ ... ]` ("after X") or a quoted date. R is not aspect A (A = phase of the event itself). Use R, not `TIME(=+n)`, for later/subsequent/earlier/before/after/then/initially; `TIME(=+1)` reads as "soon". "small" = `BIG(=-3)` alone, no PART.

Task: each line is one code standing for ONE English word or short phrase (a single common word in the intended sense). Give your single best English word or phrase for each.

## Extra form label I (intensity)
- I = how strongly the quality or action named by the head word is present: I-5 barely / hardly, I-2 somewhat, I0 fairly / moderately, I+2 quite, I+4 very, I+5 extremely / utterly. Written once on the head word after `|`, like the other labels (not counted among the 3 roots), e.g. `GOOD(=+3) | a I+4`. I is not the comparison label C (C = more / less than something; I = degree of intensity). Do not use BIG(=+5) as an intensifier.

## Extra form label K (causative / inducement)
- K = the subject acts on someone else (given by E) so that they do or undergo the action of the verb: K-5 prevent / discourage / forbid ... K0 allow / let ... K+5 force / compel / cause. With no action root the base action is DO. Written once on the verb after `|`, like other labels (not counted among the 3 roots). Examples: `DO | i K+4 E SOMEONE(=-3)` = "made them do (it)"; `CONSUME | i K+4 E SOMEONE` = "fed"; `DO | i K-4 E SOMEONE` = "stopped / prevented them".
