# Числа, счёт, математика: слепой круговой тест (12 слов, 2 кодировщика, 2 декодера)

Слова: number, digit, count (verb), sum, zero, half, mathematics, calculate, equal, fraction, three, percent. Протокол как в [roundtrip_grain](roundtrip_grain.md): кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер только таблицы и правила чтения; модель sonnet (субагенты), по одному декодеру на набор. Новых корней не вводилось.

Итог: **точно 15 из 24** (набор 1: 7, набор 2: 8), рядом 9, мимо 0.

| слово | типичный код | прочитано |
| :-- | :-- | :-- |
| zero | `MANY(=0) MEASURE(=-5) \| o` / `MANY(=0) ABSTRACT(=+5) \| o` | zero ×2 |
| number | `MEASURE(=-5) MANY \| o` / `MANY ABSTRACT(=+5) \| o` | quantity (number 3-м), number |
| digit | `MEASURE(=-5) MANY PART(=-2) \| o` / `MANY ABSTRACT(=+5) PART(=-2) \| o` | number, digit |
| count | `MEASURE MANY DO \| i` / `MANY MEASURE(=-5) KNOW \| i` | count ×2 |
| sum | `MANY JOIN(=+4) MEASURE(=-5) \| o` / `JOIN(=+4) MEASURE(=-5) HAPPEN(=+5) \| o` | sum ×2 |
| equal | `SAME(=+5) MEASURE \| a` / `SAME(=+5) MEASURE(=-5) \| a` | equal ×2 |
| calculate | `ART(=-5) THINK MEASURE \| i` / `ART(=-5) MANY THINK \| i` | calculate ×2 |
| three | `"3" \| a` или `\| o` | three ×2 |
| fraction | `PART(=-2) MEASURE(=+5) \| o` / `+ ABSTRACT(=+5)` | fraction, numerator |
| half | `PART(=-2) SAME MEASURE(=+5) \| o` | percentage, proportion |
| percent | `MEASURE(=+5) PART(=-2) \| o` | ratio, fraction |
| mathematics | `ART(=-5) MANY SEE \| o` | statistics ×2 |

Оговорки. *mathematics* (`ART(=-5) MANY SEE`) и *percent* (`MEASURE(=+5) PART(=-2)`) оба кодировщика взяли из `docs/encoding.md`, где эти слова разобраны примерами, поэтому они не независимы; *mathematics* оба раза прочитано как *statistics*. `ABSTRACT(=+5)` рядом с `MANY` хорошо передаёт «отвлечённое число», `MEASURE(=-5)` — «величина, количество». Не проверено: порядковые числительные (*first, second*), кратные (*twice*), ноль как цифра, большие числа словами. Выборка 12 слов, 2 кодировщика, 1 декодер на набор.
