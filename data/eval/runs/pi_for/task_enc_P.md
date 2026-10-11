# Encoder task

Read spec_enc.md (the min-co spec). Encode each word below as a TWO-WORD code: a head noun (the general kind: tool, cover, seat, strap, house, case, bed…) and a second noun naming the thing it belongs to or works with. Join the two words with `PI` ("HEAD | o PI MOD | o": the second word defines the head, like a compound or "of"). Each word has its own form `| o` and at most 3 roots; every axis value has a sign.

Pick for each word the code most likely to be read as exactly that word by a reader who has only the spec. The second noun must itself be readable (a reader must recognise it as that thing).

- **key** — the small metal object that opens a lock or door
- **lid** — the removable cover of a pot, jar or box
- **saddle** — the seat strapped on a horse's back
- **leash** — the strap for leading a dog
- **pillow** — the soft cushion for the head in bed
- **wallet** — the small flat case for carrying money and cards
- **nest** — the structure a bird builds for its eggs
- **kennel** — the small house for a dog
- **cork** — the stopper of a wine bottle
- **sheath** — the cover for a knife or sword blade
- **collar** — the band around a dog's neck (or the part of a shirt around the neck)
- **hive** — the home of a colony of bees
- **stable** — the building where horses are kept
- **shoelace** — the string for tying a shoe
- **frame** — the border that holds a picture
- **cradle** — the small bed for a baby

Write ONLY the codes to the file given to you, one per line, in this order:
```
key: <code>
lid: <code>
saddle: <code>
leash: <code>
pillow: <code>
wallet: <code>
nest: <code>
kennel: <code>
cork: <code>
sheath: <code>
collar: <code>
hive: <code>
stable: <code>
shoelace: <code>
frame: <code>
cradle: <code>
```
No other text.
