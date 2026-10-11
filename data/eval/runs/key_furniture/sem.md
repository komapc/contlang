
### key

для сравнения: lock 0.48, door 0.35, keys 0.77, keyhole 0.34, tool 0.25, needle 0.05, scissors 0.14, container 0.03, pliers 0.21, chip 0.09

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 12 | `DO(=+5) JOIN(=-5) \| o PI DO(=+5) JOIN(=+5) \| o` | 0.18 | 0.18 | staple remover (0.14), pliers (0.21) |
| 3 | `DO(=+5) JOIN(=-5) TOUCH(=+4) \| o` | 0.14 | 0.14 | scissors (0.14), scissors (0.14) |
| 5 | `DO(=+5) JOIN(=-5) BIG(=-5) \| o` | 0.14 | 0.14 | scissors (0.14), scissors (0.14) |
| 11 | `GRAIN(=+5) BIG(=-4) \| o PI DO(=+5) RULE(=+4) \| o` | 0.13 | 0.19 | seal (0.16), coin (0.11) |
| 1 | `GRAIN(=+5) BIG(=-5) DO(=+5) \| o` | 0.13 | 0.17 | pill (0.08), nail (0.18) |
| 13 | `DO(=+5) JOIN(=-5) \| o PI "iron" \| o` | 0.13 | 0.13 | hacksaw (0.13), hacksaw (0.13) |
| 14 | `DO(=+5) BIG(=-4) \| o PI INSIDE(=+5) JOIN(=+5) \| o` | 0.07 | 0.17 | chip (0.09), needle (0.05) |
| 2 | `DO(=+5) JOIN(=-5) GRAIN(=+5) \| o` | 0.07 | 0.16 | axe (0.10), saw (0.04) |
| 9 | `GRAIN(=+5) BIG(=-4) \| o PI DO(=+5) JOIN(=-5) \| o` | 0.07 | 0.09 | grinder (0.04), chip (0.09) |
| 6 | `INSIDE(=+4) CAN(=+4) DO(=+5) \| o` | 0.06 | 0.12 | container (0.03), engine (0.09) |
| 7 | `INSIDE(=+4) LONG(=+1) DO(=+5) \| o` | 0.05 | 0.24 | needle (0.05), needle (0.05) |
| 10 | `DO(=+5) JOIN(=-5) \| o PI GRAIN(=+5) BIG(=-5) \| o` | 0.04 | 0.06 | shredder (0.04), grinder (0.04) |
| 4 | `DO(=+5) RULE(=+4) JOIN(=-5) \| o` | 0.03 | 0.07 | sanction (-0.07), gavel (0.14) |
| 8 | `INSIDE(=+4) BIG(=-4) DO(=+5) \| o` | 0.03 | 0.14 | needle (0.05), filter (0.01) |

### furniture

для сравнения: chair 0.47, table 0.39, equipment 0.33, contents 0.12, container 0.16, skeleton 0.07, stones 0.14, timber 0.38

| # | код | cos первого ответа | лучший из трёх | прочитано первым |
|--:|---|--:|--:|---|
| 14 | `DO(=+5) PART(=+5) \| o PI PLACE INSIDE(=+5) LIVE \| o` | 1.00 | 1.00 | furniture (1.00), furniture (1.00) |
| 8 | `PART(=+5) THING(=-5) \| o PI INSIDE(=+5) PLACE \| o` | 1.00 | 1.00 | furniture (1.00), furniture (1.00) |
| 13 | `PART(=+5) THING(=-5) \| o PI PLACE INSIDE(=+5) LIVE \| o` | 1.00 | 1.00 | furniture (1.00), furniture (1.00) |
| 2 | `PART(=+5) THING(=-5) MOVE(=-5) \| o` | 1.00 | 1.00 | furniture (1.00), furniture (1.00) |
| 10 | `PART(=+5) THING(=-5) \| o PI MOVE(=-5) \| o` | 0.59 | 0.59 | still life (0.18), furniture (1.00) |
| 12 | `PART(=+5) THING(=-5) \| o PI LONG(=+5) \| o` | 0.39 | 0.39 | timber (0.38), lumber (0.40) |
| 4 | `PART(=+5) THING(=-5) DO(=+5) \| o` | 0.33 | 0.33 | equipment (0.33), equipment (0.33) |
| 5 | `PART(=+5) THING(=-5) PLACE \| o` | 0.26 | 0.26 | landscape (0.16), storeroom (0.37) |
| 3 | `PART(=+5) THING(=-5) BIG(=+3) \| o` | 0.19 | 0.19 | pile (0.12), buildings (0.26) |
| 7 | `DO(=+5) PART(=+5) INSIDE(=+5) \| o` | 0.16 | 0.16 | container (0.16), container (0.16) |
| 1 | `PART(=+5) THING(=-5) INSIDE(=+5) \| o` | 0.12 | 0.49 | contents (0.12), contents (0.12) |
| 11 | `PART(=+5) THING(=-5) \| o PI GRAIN(=+5) \| o` | 0.12 | 0.18 | stones (0.14), rocks (0.10) |
| 9 | `PART(=+5) THING(=-5) \| o PI BODY \| o` | 0.07 | 0.17 | skeleton (0.07), skeleton (0.07) |
| 6 | `PART(=+5) THING(=-5) BODY \| o` | 0.07 | 0.13 | skeleton (0.07), skeleton (0.07) |
