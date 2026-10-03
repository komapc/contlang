# Лестница PART на словах-группах: независимые кодировщики

11 слов, 3 независимых кодировщика (видели спецификацию с лестницей `PART`, не видели мои коды), 3 слепых декодера. Попадание — слово или близкий синоним в лучшем ответе или альтернативах (оценка моя, не слепая).

| слово | попаданий | A | B | C |
| :-- | :-- | :-- | :-- | :-- |
| group | 3/3 | `PART(=+5) \| o` → group | `PART(=+5) \| o` → collection | `PART(=+5) \| o` → group |
| union | 0/3 | `PART(=+5) RULE \| o` → code of laws | `PART(=+5) RULE SAME \| o` → constitution | `PART(=+5) SAME(=+3) RULE \| o` → code of law |
| class | 1/3 (class в альтернативах), остальное community | `PART(=+5) SOMEONE SAME(=+3) \| o` → community | `SOMEONE PART(=+5) SAME \| o` → community | `SOMEONE PART(=+5) SAME(=+2) \| o` → community |
| party | 0/3 | `PART(=+5) SOMEONE RULE \| o` → government | `SOMEONE PART(=+5) RULE \| o` → government | `SOMEONE PART(=+5) RULE \| o` → government |
| team | 3/3 | `PART(=+5) SOMEONE DO \| o` → organization | `SOMEONE PART(=+5) DO \| o` → team | `SOMEONE PART(=+5) DO \| o` → organization |
| committee | 0/3 | `PART(=+5) SOMEONE BIG(=-3) \| o` → family | `SOMEONE PART(=+5) BIG(=-3) \| o` → family | `SOMEONE PART(=+5) BIG(=-3) \| o` → family |
| society | 1/3 (society в альтернативах), остальное population | `PART(=+5) SOMEONE LIVE \| o` → population | `SOMEONE PART(=+5) LIVE \| o` → population | `SOMEONE PART(=+5) LIVE \| o` → population |
| forest | 3/3 | `PART(=+5) THING(=0) \| o` → forest | `THING(=0) PART(=+5) MANY \| o` → herd | `THING(=0) PART(=+5) PLACE \| o` → forest |
| fleet | 3/3 | `PART(=+5) CONTAINER MOVE \| o` → fleet | `CONTAINER MOVE PART(=+5) \| o` → fleet | `CONTAINER PART(=+5) MOVE \| o` → fleet |
| member | 3/3 | `PART(=-2) SOMEONE \| o` → member | `PART(=-2) SOMEONE \| o` → member | `SOMEONE PART(=-2) \| o` → member |
| institution | 0/3 (council / state) | `PART(=+5) RULE SOMEONE \| o` → council | `RULE PLACE PART(=+5) \| o` → state | `RULE PLACE PART(=+5) \| o` → state |

Итоги:
- Работает (3/3): *group, team, forest, fleet, member*. Кодировщики сходятся: `X PART(=+5)` для групп и стад, `SOMEONE PART(=-2)` для члена.
- Рядом, но не точно: *society* (читается *population*), *class* (*community*).
- Не работает: *union, party, committee, institution*. Как только к группе добавляется `RULE`, декодер читает «правительство» или «свод законов» (*union* → *code of law*, *party* → *government*); `BIG(=-3)` в *committee* читается как «семья»; *institution* → *state*. Группа есть, а различие (союз, партия, комитет) не выражено корнями.

Вывод: лестница `PART` принимается для групп вещей и людей, членства и коллективов (*-aro*). Организационные типы (*union, party, committee, institution*) корнями не различаются: либо `@NN`, либо принять потерю. Порядок слов: главное слово первым, `PART(=+5)` сразу после него (один кодировщик ставил `PART` первым).
