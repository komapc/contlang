# The philosophy of min-co

**min-co** (*minimal + continuous*) is a minimal philosophical language (artlang) for precise and flexible thought.

- A minimum of grammar and vocabulary (inspired by Toki Pona and Esperanto).
- A maximum of expressiveness through a small set of universal continuous features.
- Concepts are not categories but positions in a conceptual space.
- Nuance instead of a label: the meaning of a word is a root plus continuous adjustments.

## Principles

1. **A small set of general roots.** About 45 general concepts not tied to a part of speech (*move, think, want, good, big, …*), mostly NSM primitives; most have their own axis. The list and the rules for adding to it are in [`roots.yaml`](../../roots.yaml) and the [lexicon](lexicon.md).
2. **The part of speech works like Esperanto suffixes, in the form after the `|`.** `o` noun, `i` verb, `a` attribute, `e` adverbial; a noun may have the role `agent`, `tool`, `result`, `quality` (*-ist, -il, -aĵ, -ec*). Any root takes any part of speech: `MOVE | o` (movement), `MOVE | i` (to move), `MOVE | a` (mobile), `MOVE | e` (movingly). The form is separate from the meaning: a root does not know what part of speech it is.
3. **Axes are the only continuous mechanism.** The semantic adjustments of a word are axes with a value from -5 to +5 and a scope: each root has its own axis or none (GOOD, BIG, TIME, …); there are no shared unnamed axes. There are no separate “gradient roots” or local axes: they are the same axes ([model](model.md)).
4. **Features are optional.** An axis that is not written has an unspecified value (the zero rule: it costs nothing in bits); `(=0)` is the explicit middle. The marker `?` requests a value (see [syntax](syntax.md), [model](model.md)).
5. **Minimal grammar.** The head first, the particles `E`, `PI`, `LA`, the link words `FROM`, `FOR`, `LIKE`, brackets and `?`; the predicate is the word with `| i`, without `LI` ([syntax](syntax.md)).
6. **A not-quite-infinite vocabulary.** Words are generated as roots + axis values + form; compounds (two words joined by a link word) are built by the same logic. Stable recipes are fixed by testing, but there is no need to memorize a vocabulary.
7. **The goal is the semantic field.** A code has succeeded if the reader names a word from the same field (*house, dwelling, hut*), not necessarily the same word.
8. **Math does the encoding.** The code of a word on the site is built by math (word and root vectors), not by a language model; the model serves only as reader and judge in blind tests ([math](math.md)). The model of simplicity is Toki Pona.

## Where this came from

The scheme was not invented entirely by hand but selected through experiments on data (English, ConceptNet Numberbatch embeddings, 3000 words): global axes, roots with local axes, roots with universal axes, and a continuous form against a suffix were compared. Details and metrics: [work plan (historical, in Russian)](../history/plan.md), the `data/` directory.

The overall design: [model](model.md). More: [syntax](syntax.md), [lexicon](lexicon.md), [phonology](phonology.md).
