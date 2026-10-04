# MEASURE: слепой тест (16 слов × 2 кодировщика, 2 декодера)

Ось: −5 единица, измерение … 0 количество, размер … +5 отношение величин. Оценка: слово названо лучшим или среди двух альтернатив.

| слово | код A | код B | A | B |
| :-- | :-- | :-- | :-- | :-- |
| measurement | `MEASURE(=-5) \| o` | то же | meter | unit |
| ratio | `MEASURE(=+5) \| o` | то же | ✓ | ✓ |
| proportion | `+5 PART(=+2)` / `+5 SAME(=+3)` | | percentage, alt ✓ | ✓ |
| amount | `MEASURE(=0)` | то же | ✓ | ✓ |
| rate | `+5 TIME` | то же | ✓ | ✓ |
| percentage | `+5 PART(=-2) 100` / `+5 PART(=-2)` | | percent ✓ | ✓ |
| meter | `-5 PLACE` / `-5 BIG(=+3)` | | alt ✓ | scale ✗ |
| size | `0 BIG` | то же | ✓ | ✓ |
| to measure | `MEASURE(=-5) \| i` | то же | ✓ | ✓ |
| degree | `+5 BIG` | то же | ✓ | ✓ |
| scale | `-5 PART(=+5)` | то же | ✓ | alt ✓ |
| average | `0 SAME(=0)` / `0 SAME(=+2)` | | equality ✗ | alt ✓ |
| quantity | `0 MANY` | то же | alt ✓ | alt ✓ |
| dimension | `0 PLACE` / `0 SIDE` | | area ✗ | alt ✓ |
| unit | `-5 PART(=+2)` | то же | ✓ | measurement ✗ |
| proportional | `+5 SAME` / `+5 \| a` | | ✓ | ✓ |

Итого 26 из 32 (81%); лучшим названо 19 из 32 (59%). Промахи — соседи (*meter / mile*, *unit / measurement*). Ось читается без перепутанного знака.

## Версия 2 (ось «сама по себе … относительно другой»)

Первая версия оси (−5 единица … 0 количество … +5 отношение) смешивала три понятия и была переписана: −5 величина как есть (*size, amount, length, number*), 0 уровень, степень, +5 величина относительно другой (*ratio, rate, percentage, average*); единица `MEASURE SAME`, измерение `MEASURE DO` / `MEASURE | i`. Ось независима: SemAxis, косинус с BIG −0,18, с остальными не выше 0,14.

Слепой тест на тех же 16 словах (новые кодировщики и декодеры): **26 из 32** (то же, что v1), лучшим названо около 18. Исправлено: *measurement* (оба), *unit*, *average*, *scale*, *to measure*, *degree/level*. Потеряно: *meter*, *dimension* (читаются *distance / length*), *proportional*. Знак оси перепутан не был: *amount / size / number* на −5, *ratio / rate / percentage* на +4…+5.
