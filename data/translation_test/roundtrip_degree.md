# Метка I (интенсивность): слепой тест

12 фраз «наречие степени + прилагательное», два независимых кодировщика (видели только спецификацию), два декодера (видели только спецификацию и коды). Оценки мои: верно = и степень, и признак совпали или близкий синоним.

| # | фраза | код A | → A | код B | → B |
| --: | :-- | :-- | :-- | :-- | :-- |
| 1 | very good | `GOOD(=+3) \| a I+4` | very good | то же | very good |
| 2 | extremely big | `BIG(=+3) \| a I+5` | extremely big | то же | extremely big |
| 3 | slightly warm | `HEAT(=+2) \| a I-2` | slightly warm | `HEAT(=+1) \| a I-2` | slightly warm |
| 4 | hardly possible | `CAN(=+1) \| a I-5` | barely able (alt. barely possible) | то же | barely able (alt. scarcely possible) |
| 5 | quite near | `NEAR(=+3) \| a I+2` | quite near | то же | quite near |
| 6 | rather difficult | `CAN(=-3) \| a I0` | difficult (степень потеряна) | `CAN(=-3) \| a I+1` | quite difficult |
| 7 | somewhat bad | `GOOD(=-3) \| a I-2` | somewhat bad | `GOOD(=-2) \| a I-2` | somewhat bad |
| 8 | barely alive | `LIVE(=+1) \| a I-5` | barely alive | `LIVE(=-2) \| a I-5` | barely alive |
| 9 | highly important | `GOOD(=+3) PARTICULAR(=+3) \| a I+4` | very special | `PARTICULAR(=+4) \| a I+4` | very specific |
| 10 | completely different | `SAME(=-5) \| a I+5` | utterly different | то же | utterly different |
| 11 | almost certain | `MAYBE(=+3) \| a I-2` | perhaps | `MAYBE(=+3) \| a I+2` | quite likely |
| 12 | moderately big | `BIG(=+3) \| a I0` | big (степень потеряна) | `BIG(=+2) \| a I0` | fairly large |

Из 24 прочтений: верно 18, частично 2 (№6 и №12 у A: признак верен, степень потеряна при `I0`), мимо 4 (№9 обе, №11 обе).

- Степень `I` в целом читается: очень, чрезвычайно, слегка, едва, весьма, совсем (`I±2`, `I±4`, `I±5`) — верно в каждом случае, где признак был закодирован верно.
- `I0` («довольно, умеренно») декодер может проигнорировать (2 из 4 случаев): для слабой степени лучше писать `I+1…+2` или `I-1…-2`.
- Мимо ушли не из-за `I`: у *important* нет корня (кодировщики брали `PARTICULAR`, читается как *special / specific*); *almost* («почти») метка `I` не выражает (читается как «возможно / вероятно»).
