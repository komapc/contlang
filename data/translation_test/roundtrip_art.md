# Корень ART (−5 техника … +5 культура): слепой тест

16 слов, два независимых кодировщика (видели только спецификацию), два декодера (видели только спецификацию и коды). Оценки мои: верно = слово или близкий синоним первым ответом, «запасным» = в двух альтернативах.

| слово | код A | → A | код B | → B |
| :-- | :-- | :-- | :-- | :-- |
| poetry | `ART(=+5) SAY \| o` | language (запасным: poetry) | то же | poetry |
| painting | `ART(=+5) SEE MATTER(=0) \| o` | painting | то же | painting |
| philosophy | `ART(=+3) THINK KNOW \| o` | philosophy | `ART(=+4) THINK KNOW` | philosophy |
| history | `ART(=+4) KNOW TIME(=-3) \| o` | history | `ART KNOW TIME(=-5)` | history |
| music | `ART(=+5) FEEL SAY \| o` | music | `ART(=+5) SAY FEEL` | song (запасным: music) |
| literature | `ART(=+5) SAY PART(=+5) \| o` | literature | `ART(=+5) THING SAY` | literature |
| physics | `ART(=-4) MATTER MOVE \| o` | physics | `ART(=-4) MATTER HEAT` | physics |
| chemistry | `ART(=-4) MATTER CHANGE \| o` | chemistry | `ART(=-3) MATTER CHANGE` | chemistry |
| mathematics | `ART(=-5) MANY SEE \| o` | mathematics | `ART(=-5) MANY` | mathematics |
| engineering | `ART(=-4) DO THING \| o` | technology (запасным: engineering) | то же | engineering |
| machine | `THING(=-5) MOVE DO \| o` | machine | то же | machine |
| computer | `THING(=-5) THINK ART(=-5) \| o` | computer | то же | computer |
| engineer | `SOMEONE ART(=-4) DO \| o` | engineer | `SOMEONE ART(=-4) DO THING` | engineer |
| scientist | `SOMEONE ART(=-4) KNOW \| o` | scientist | `SOMEONE ART(=-3) KNOW` | scientist |
| artist | `SOMEONE ART(=+5) DO \| o` | artist | то же | artist |
| architecture | `ART(=0) DO PLACE \| o` | workshop | то же | workshop |

Итого из 32 прочтений: первым ответом верно или близким синонимом 29, запасным 1, мимо 2 (оба — *architecture*).

- Имя `ART` не вызвало перекоса в «искусство»: на `ART(=-4)` декодеры читают физику, химию, технику; опасение «всегда живопись» не подтвердилось.
- Кодировщики независимо выбрали практически одинаковые коды: ось применяют единообразно (физика −4, математика −5, поэзия +5).
- Мимо только *architecture* (`ART(=0) DO PLACE` читается как «мастерская»): смесь искусства и техники на нуле плюс `PLACE` не даёт «проектирование зданий».
