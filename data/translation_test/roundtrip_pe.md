# Частица PE (деятель при пассиве): слепой тест

Раньше (`roundtrip_voice.md`, №9) деятель при `V-4` через `E` читался как дополнение. Введена частица `PE` («кем»). Декодер видел только спецификацию, коды писал я.

| # | код | декодировано | верно |
| --: | :-- | :-- | :-: |
| 1 | `PLACE LIVE \| o D+3 LI DO \| i T-2 V-4 PE SOMEONE(=-3) \| o` | The house was built by others. | да |
| 2 | `SOMEONE SEX(=+5) \| o D+3 LI LIVE(=-5) \| i T-2 V-4 PE SOMEONE SEX(=+5) RULE(=+5) \| o D+3` | The man was killed by the king. | да |
| 3 | `THING SAY \| o D+3 LI SAY \| i T-2 V-4 PE SOMEONE RULE(=+4) \| o D+3` | The word was spoken by the authorities. | да |
| 4 | `SOMEONE MANY(=+5) \| o LI GIVE KNOW \| i T-2 V-4 PE SOMEONE SEX(=+5) TIME(=-4) \| o` | Everyone was taught by the forefathers. | да (старик → предки) |
| 5 | `PLACE SOMEONE MANY \| o D+3 LI LIVE(=-5) \| i T-2 V-4 PE SOMEONE FIGHT PART(=+5) \| o D+3` | The city was destroyed by the army. | да |
| 6 | `CONSUME \| o D+3 LI CONSUME \| i T-2 V-4 PE SOMEONE BIG(=-3) \| o D+3` | The food was eaten by the small child. | да |

Роли «кто / над кем» верны в 6 из 6. Один декодер, один кодировщик (я): проверка предварительная.
