# Encoder task

Read spec_enc.md (the min-co spec). Propose codes, each at most 3 roots per word, every axis value with a sign.

- **door** (noun: the panel you open to go into a room or house): 4 one-word codes `ROOTS | o`.
- **lock** (noun: the device that keeps a door closed until opened with a key): 4 one-word codes.
- **open** (verb: make a door or box open): 3 one-word codes `ROOTS | i`.
- **key** (noun: the small metal object that opens a lock): 6 TWO-WORD codes, head + `PI` + defining word, each word with its own form. The head says "tool" / "small tool" (e.g. `DO(=+5) | o` or `DO(=+5) BIG(=-4) | o`), the second word is your door, lock or open code (as a noun `| o`), so the whole reads "door-tool", "lock-tool", "opening-tool". Example shape: `DO(=+5) BIG(=-4) | o PI <door roots> | o`.

Rank each group: first = most likely to be read as exactly that word by a reader who has only the spec. Avoid codes a reader would read as something else (room, house, wall, box, chain, knife, needle).

Write ONLY the codes to the file given to you:
```
door 1: <code>
...
lock 1: <code>
...
open 1: <code>
...
key 1: <code>
...
key 6: <code>
```
No other text.
