# min-co vs Toki Pona: two minimal conlangs compared

Toki Pona and min-co are both minimal constructed languages: a small set of words, no inflection, and longer meanings built by putting words together, head first. min-co borrowed much of that from Toki Pona. They differ in what they are for. Toki Pona is a language people speak, built around simplicity, where context fills in the details. min-co is an experiment: can a few dozen roots, each with a numeric scale, pin a meaning down more precisely, and can a computer encode and decode it?

## Toki Pona in brief

Toki Pona was created by the linguist Sonja Lang and first published online in 2001. It has about 120–140 words, depending on how the rarer ones are counted, and 14 sounds. A word covers a broad area of meaning (`pona` is good, simple, to fix), and phrases are built head first: `jan pona` is “person + good”, a friend. A handful of particles (`li`, `e`, `la`, `pi`, `o`) mark the parts of the sentence. The vagueness is deliberate: the language invites you to say what matters and leave the rest to context. Toki Pona has an active community of speakers, books, music and its own writing systems, such as sitelen pona.

## min-co in brief

min-co (a working name, from *minimal + continuous*) has 45 meaning roots, mostly general concepts such as GOOD, BIG, PLACE, KNOW, SAY. 39 of them have a value axis from −5 to +5, so a number says where on the scale you mean: `SAY(=-4) | i` is to whisper, `SAY(=+5) | i` to scream. A word is up to three roots, the main one first: `PLACE LIVE | o` is a house. After the bar come the part of speech (`o i a e`, as in Esperanto's *-o -i -a -e*) and optional labels for tense, number or negation. See [how to read min-co](../../docs/en/reading.md).

A min-co code can be written by a person or a language model, or computed: a word's meaning vector (ConceptNet Numberbatch) is approximated by a sum of at most three roots with integer axis values. Decoding works the same way in reverse, so codes can be tested blind: one reader gets only the code and names the word. The goal is the right semantic field (*house, dwelling, hut* all count), not the exact word. The details are in [the math](../../docs/en/math.md).

## Side by side

| | Toki Pona | min-co |
|---|---|---|
| Status | Published in 2001, with a community of speakers | An experiment in progress, with no speakers |
| Vocabulary | About 120–140 words | 45 meaning roots, 39 with an axis from −5 to +5 |
| A word | One word, or a head-first phrase: `jan pona` | Up to three roots, head first, and a form after the bar: `SOMEONE FRIEND(=+5) \| o` |
| Shades of meaning | Context and more words | A number on the root's axis |
| Parts of speech | Set by position in the sentence | Written after the bar: `o` noun, `i` verb, `a` attribute, `e` adverb |
| Tense, number | Usually left to context | Optional labels: `T-2` past, `N+3` plural |
| Particles | `li`, `e`, `la`, `pi`, `o` | `E`, `PI`, `LA`, link words `FROM`, `FOR`, `LIKE`; no `LI` |
| Sounds and writing | 14 sounds, Latin letters, sitelen pona | Not settled; the draft uses Toki Pona words for roots |
| Who encodes | People | People, language models, or vector math |

## Different goals

Toki Pona simplifies on purpose. Its small vocabulary is meant to make you think about what you really want to say, and a listener is expected to fill in the rest from the situation. That is a strength in conversation, and it is why the language has a culture of its own.

min-co asks a narrower, measurable question: how much meaning a very small vocabulary can carry when each root is a scale rather than a single point. It is tested the way a code is tested, with blind readers and numbers, and its notation is still changing with the results.

## What the tests showed

min-co uses Toki Pona as its benchmark. In a blind test on 100 single words, with a language model writing the codes and two blind readers, also models, decoding them, min-co codes led readers closer to the target word than Toki Pona phrases, by a factor of about 2.4. In whole sentences the difference disappeared: context helps Toki Pona readers, and min-co is not ahead there. One caveat favours min-co: the models know Toki Pona from training and min-co only from a short specification. The data and method are in [rethinking the language](../../docs/en/rethink.md).

## Which one to learn

To speak a minimal language with other people, learn Toki Pona: it has the community, the courses and the literature. min-co is for those curious about how meaning can be encoded with a handful of scales, and how far a computer can follow. You can try encoding and decoding words on the [min-co home page](/).
