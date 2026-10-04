# Слепой тест трёх новых осей: CHANGE, RULE (официальное), PARTICULAR

18 слов, три независимых кодировщика (видели только спецификацию на 38 корней), три декодера (видели только спецификацию и коды). Попадание — слово или близкий синоним в лучшем ответе или альтернативах. Оценки мои.

| # | слово | A | B | C | попаданий |
| --: | :-- | :-- | :-- | :-- | --: |
| 1 | change | `CHANGE(=0)` → change | `CHANGE` → change | `CHANGE` → change | 3/3 |
| 2 | alter | `DO CHANGE SAME(=-2)` → modify, alter | `CHANGE(=1) DO V+4` → modify, alter | `DO CHANGE(=+1)` → modify, alter | 3/3 |
| 3 | transform | `CHANGE(=+5)` | `CHANGE(=5)` | `CHANGE(=+5)` | 3/3 |
| 4 | remain | `CHANGE(=-5)` → stay, remain | то же | то же | 3/3 |
| 5 | increase | `CHANGE BIG(=+3)` → grow, increase | то же | то же | 3/3 |
| 6 | improve | `CHANGE GOOD(=+3)` | то же | то же | 3/3 |
| 7 | committee | `SOMEONE PART(=+5) BIG(=-3)` → family | `SOMEONE PART(=5) RULE(=1)` → family | `SOMEONE PART(=+5) BIG(=-3)` → committee (small group) | 0–1/3 |
| 8 | commission | `SOMEONE PART(=+5) RULE(=+4)` → government | RULE(=3) → government | RULE(=+4) → government | 0/3 (рядом) |
| 9 | agency | `RULE(=+4) PART(=-2)` → official | → law | → official | 0/3 (рядом) |
| 10 | government | `RULE(=+4) SOMEONE PART(=+5)` → nation | → state | → state | 0/3 (рядом: state) |
| 11 | authority | `RULE(=+4)` | `RULE(=4)` | `RULE(=+4)` | 3/3 |
| 12 | private | `RULE(=-5) \| a` → informal, private | то же | informal, private | 3/3 |
| 13 | official | `RULE(=+5) \| a` | то же | то же | 3/3 |
| 14 | specific | `PARTICULAR(=+4)` → special, specific | `(=3)` → particular, specific | `(=3)` → special, specific | 3/3 |
| 15 | particular | `(=+3)` → specific | `(=4)` → specific | `(=+4)` → specialized, peculiar | 2/3 |
| 16 | unique | `PARTICULAR(=+5) SAME(=-5)` → unique | то же → unique | `PARTICULAR(=+5) PART(=+2)` → whole-specific | 2/3 |
| 17 | special | `(=+2)` → certain | `(=2)` → special | `(=+2)` → certain | 1/3 |
| 18 | general | `PARTICULAR(=-5)` | то же | то же | 3/3 |

Итого строго: **38 из 54** (70 %).

## Выводы

- **CHANGE принят**: все шесть слов (change, alter, transform, remain, increase, improve) прочитаны верно всеми тремя парами. Схема «направление через BIG и GOOD» работает.
- **Ось RULE принята частично**: authority, private, official читаются 9/9. Но типы организаций (committee, commission, agency, government) по-прежнему не различаются: всё сливается в «правительство / государство / официальное лицо». Это тот же вывод, что и раньше: организационные типы не передаются корнями, нужен словарь `@NN` или принять потерю.
- **PARTICULAR принят с оговоркой**: полюса (general −5, specific +3…+4, unique через `SAME(-5)`) работают. Оттенки specific / particular / special / certain не различаются: кодировщики выбирают +2…+5 почти случайно. Ось даёт кластер, а не точное слово; делить его на градации не надо.
- Замечено в кодах: `V+4` как метка залога на `DO` (B) без необходимости; `RULE(=1)` для committee (B) читается как «семья» — слабые значения RULE около 0 ничего не несут.
