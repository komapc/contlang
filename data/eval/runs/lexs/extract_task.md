## Task

sents.md has 120 numbered English sentences. For every sentence, list its CONTENT words: nouns, main verbs, adjectives and
adverbs. Skip pronouns, determiners, prepositions, conjunctions, auxiliary and modal verbs (be, have, do, will, can, ...
when used as auxiliaries), numbers, and proper names. Keep "not"-like words out too.

For each content word give its base form (lemma: `ran` → run, `officers` → officer, `fastest` → fast), its part of speech
(noun / verb / adjective / adverb) and a short gloss of the sense it has IN THIS SENTENCE (3–8 words, plain English, do not
use the word itself). A phrasal verb (`give up`) or fixed compound (`data processing`) is one item.

Write lemmas.md: one line per item, in sentence order, exactly
`N | lemma | pos | gloss`
where N is the sentence number. Nothing else.
