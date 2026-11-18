## Task

`items.md` has numbered items. Each has an ENGLISH sentence, its CODE in min-co (a constructed language), and the list of
the code's WORDS — each word is one `{ ROOTS | FORM }` in braces, numbered [1], [2], …

For every word, write what the writer of the code meant by that word: its English meaning in base form (lemma), 1 to 3
English words. Examples: `{ PLACE LIVE | o }` → house; `{ SAY | i T-2 }` → say; `{ SOMEONE(=-5) | o }` → she (if it stands
for "she" in the English); `{ ABOVE(=+5) LONG | o }` → umbrella (if it stands for "umbrella").

Rules:
- One gloss per word, in the same order; exactly as many glosses as the item lists words.
- Gloss only that word's own meaning. Use the English sentence only to see which English word the writer was aiming at.
- Never add anything the code does not contain: no words the writer dropped, no names that are not in the code, no extra
  details. If a word cannot be matched to anything in the English, gloss what its roots most plausibly mean.
- Base form only: no tense, plural, articles or negation (the code's marks carry those): "walked" → walk, "the dogs" → dog.
- No "|" inside a gloss.

Write `glosses.md`: one line per item, same numbering, `N. gloss1 | gloss2 | … | glossK`. No other text.
