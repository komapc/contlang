
### key

для сравнения: lock 0.48, door 0.35, keys 0.77, doorknob 0.32, latch 0.35, staple 0.20, stapler 0.10, clamp 0.11, nail 0.18, fastener 0.21, coin 0.11

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 3 | `DO(=+5) BIG(=-4) \| o PI PART(=-2) PLACE SIDE(=+5) \| o` | 0.57 | 1.00 | door key (0.82), doorknob (0.32) |
| 14 | `DO(=+5) \| o PI PART(=-2) PLACE SIDE(=+5) \| o` | 0.26 | 0.30 | door (0.35), entrance (0.17) |
| 9 | `DO(=+5) BIG(=-4) GRAIN(=+5) \| o PI DO(=+5) JOIN(=+5) MOVE(=-5) \| o` | 0.21 | 0.24 | nail (0.18), pin (0.24) |
| 12 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=+5) CHANGE(=-5) \| o` | 0.19 | 0.21 | nail (0.18), staple (0.20) |
| 1 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=+5) \| o` | 0.15 | 0.15 | staple (0.20), stapler (0.10) |
| 13 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=+5) CAN(=-3) \| o` | 0.15 | 0.17 | stapler (0.10), staple (0.20) |
| 5 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=+5) PART(=-2) \| o` | 0.14 | 0.22 | staple (0.20), paper clip (0.09) |
| 7 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=+5) MOVE(=-5) \| o` | 0.14 | 0.24 | clip (0.09), staple (0.20) |
| 10 | `DO(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=-5) \| o` | 0.13 | 0.13 | knife (0.11), scissors (0.14) |
| 2 | `DO(=+5) BIG(=-4) \| o PI PART(=-2) JOIN(=-5) PLACE \| o` | 0.11 | 0.19 | pocketknife (0.12), divider (0.11) |
| 8 | `DO(=+5) BIG(=-4) \| o PI PART(=-2) DO(=+5) INSIDE(=+4) \| o` | 0.09 | 0.19 | microchip (0.09), microchip (0.09) |
| 11 | `DO(=+5) BIG(=-4) GRAIN(=+5) \| o PI PART(=-2) DO(=+5) INSIDE(=+4) \| o` | 0.09 | 0.09 | microchip (0.09), microchip (0.09) |
| 4 | `DO(=+5) BIG(=-4) \| o PI CHANGE(=+3) JOIN(=-5) \| o` | 0.08 | 0.14 | decrement (0.05), coin (0.11) |
| 6 | `DO(=+5) BIG(=-4) \| o PI DO(=+3) INSIDE(=+5) \| o` | 0.06 | 0.15 | pocketknife (0.12), probe (-0.01) |

### door

для сравнения: entrance 0.55, front 0.41, gate 0.67, room 0.37, facade 0.23

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 2 | `PART(=-2) PLACE SIDE(=+5) \| o` | 0.50 | 0.50 | entrance (0.55), entrance (0.55), entrance (0.55), entrance (0.55), front (0.41), front (0.41) |
| 4 | `PART(=-2) PLACE INSIDE(=+5) \| o` | 0.37 | 0.37 | room (0.37), room (0.37), room (0.37), room (0.37) |
| 1 | `PART(=-2) JOIN(=-5) PLACE \| o` | 0.06 | 0.12 | island (0.01), island (0.01), gap (0.22), island (0.01) |
| 7 | `PART(=-2) JOIN(=-5) INSIDE(=+5) \| o` | 0.03 | 0.08 | core (0.03), extract (-0.05), kernel (0.03), organ (0.04), splinter (0.06), insert (0.08) |
| 8 | `PART(=-2) GRAIN(=+5) INSIDE(=+4) \| o` | 0.03 | 0.08 | core (0.03), core (0.03), kernel (0.03), kernel (0.03), core (0.03), core (0.03), kernel (0.03), kernel (0.03) |

### lock

для сравнения: clamp 0.35, bolt 0.48, glue 0.18, latch 0.69, padlock 0.77

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 1 | `DO(=+5) JOIN(=+5) CAN(=-3) \| o` | 0.84 | 0.87 | clamp (0.35), lock (1.00), lock (1.00), lock (1.00) |
| 8 | `DO(=+5) JOIN(=+5) TOUCH(=+5) \| o` | 0.37 | 0.44 | clamp (0.35), fastener (0.47), nail (0.18), fastener (0.47) |
| 4 | `DO(=+5) JOIN(=+5) GRAIN(=+5) \| o` | 0.33 | 0.48 | bolt (0.48), nail (0.18), nail (0.18), bolt (0.48) |
| 3 | `DO(=+5) JOIN(=+5) PART(=-2) \| o` | 0.32 | 0.47 | clip (0.17), fastener (0.47) |
| 6 | `DO(=+5) JOIN(=+5) MOVE(=-5) \| o` | 0.31 | 0.37 | glue (0.18), clamp (0.35), clamp (0.35), clamp (0.35) |
| 5 | `DO(=+5) JOIN(=+5) CHANGE(=-5) \| o` | 0.25 | 0.33 | glue (0.18), fastener (0.47), glue (0.18), glue (0.18) |
| 2 | `DO(=+5) JOIN(=+5) PLACE \| o` | 0.06 | 0.09 | bridge (0.06), bridge (0.06), bridge (0.06), bridge (0.06), bridge (0.06), bridge (0.06) |

### open

для сравнения: extract -0.00, insert 0.05, cut 0.15, remove 0.09, detach 0.14, unlock 0.47

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 1 | `DO(=+3) JOIN(=-5) \| i` | 0.12 | 0.18 | cut (0.15), cut (0.15), remove (0.09), cut (0.15), detach (0.14), detach (0.14), cut (0.15), separate (0.17), subtract (-0.09), cut (0.15), cut (0.15), cut (0.15) |
| 3 | `DO(=+3) INSIDE(=+5) \| i` | 0.05 | 0.23 | insert (0.05), insert (0.05), insert (0.05), insert (0.05) |
| 4 | `JOIN(=-5) INSIDE(=+5) \| i` | -0.00 | 0.10 | extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00), extract (-0.00) |

### key: насколько ответы близки к lock / door (лучший из трёх)

| # | key | lock | door |
|--:|--:|--:|--:|
| 1 | 0.15 | 0.18 | 0.11 |
| 2 | 0.19 | 0.23 | 0.17 |
| 3 | 1.00 | 0.64 | 0.74 |
| 4 | 0.14 | 0.11 | 0.04 |
| 5 | 0.22 | 0.26 | 0.07 |
| 6 | 0.15 | 0.12 | 0.04 |
| 7 | 0.24 | 0.31 | 0.07 |
| 8 | 0.19 | 0.08 | 0.04 |
| 9 | 0.24 | 0.31 | 0.12 |
| 10 | 0.13 | 0.10 | 0.09 |
| 11 | 0.09 | 0.04 | 0.03 |
| 12 | 0.21 | 0.30 | 0.10 |
| 13 | 0.17 | 0.33 | 0.09 |
| 14 | 0.30 | 0.45 | 0.83 |
