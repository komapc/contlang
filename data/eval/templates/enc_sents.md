# Encoder instructions (sentences)

You will translate English sentences into min-co, one independent line per sentence.
A different person will decode your codes WITHOUT seeing the English, using only the spec below. Write each code so that its meaning can be recovered.

- Use ONLY the {{N_ROOTS}} roots below; never invent roots or use English words as roots. At most 3 roots per word.
- Do not quote common words. Give exactly one code per input item, with the same numbering, as `N. CODE`. No other text.

{{CORE}}
## Sentences

A sentence is a sequence of words and particles. Every word has its own `| FORM`; a word ends at its form.
- `E`: the next word is the direct object of the verb before it.
- `LA [ … ]`: a context or condition clause before the main clause (if, when, although).
- `[ … ]`: a clause used inside another, as its object or modifier.
- `;`: separates independent clauses.
- `AND`: joins two words of the same kind.
- A word with part of speech `i` is the verb; there is no separate predicate particle.
{{CLAUSE_RULE}}
