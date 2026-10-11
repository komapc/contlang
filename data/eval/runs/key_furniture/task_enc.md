# Encoder task

Read spec_enc.md (the min-co spec). Propose codes for two English nouns: **key** (the small metal object that opens a lock) and **furniture** (chairs, tables, beds, cupboards as a class).

For each noun give:
- 4 different ONE-WORD codes: `ROOTS | o`, at most 3 roots, every axis value with a sign, e.g. `GRAIN(=0) THING(=-5) PART(=-5) | o`.
- 4 different TWO-WORD codes: a head noun + `PI` + a defining noun, each word with its own form, e.g. `DO(=+5) TEXT | o PI THING(=-3) | o`. The head is the general kind, the second word is what tells it apart (like "door-tool", "house-things").

Rank them: first = the one a reader who has only the spec would most likely read as exactly this word. Think about what a reader would read instead (tool? box? lock? room? house?) and avoid that.

Write ONLY the codes to the file given to you, format:
```
key 1: <code>
...
key 8: <code>
furniture 1: <code>
...
furniture 8: <code>
```
(1–4 one-word, 5–8 two-word.) No other text.
