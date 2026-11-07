# Encoder instructions (adjectives and degree adverbs)

You will encode English words into min-co, one independent code per line, using the spec below. A different person will
decode your codes WITHOUT seeing the English, using only the spec. Write each code so that the reader recovers the word.
- Use ONLY the 45 roots below; at most 3 roots per word; do not quote common words.
- Adjectives (lines marked ADJ): one word with part of speech `a`, no marks. Its FIRST root must carry an axis value of
  magnitude 3 (`(=+3)` or `(=-3)`) that expresses the quality, so the word means the plain adjective (not "very ...").
- Degree adverbs (lines marked ADV): one word with part of speech `e`, roots only (do not use the I mark).
Reply in exactly this format, one line per input line, nothing else: `N. CODE`.
