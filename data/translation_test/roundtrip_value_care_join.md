# Корни VALUE, CARE (тщательность), JOIN: слепой тест

18 слов, два независимых кодировщика (видели только спецификацию), два декодера. Оценки мои. Коды кодировщиков A и B почти совпали, ниже отличия указаны там, где они есть.

**Ось тщательности** кодировщики писали как ось у корня `DO` (вариант до решения завести отдельный корень `CARE`). Шесть слов затем переписаны механической заменой `DO(` → `CARE(` и прочитаны ещё одним декодером.

| слово | код (A) | → A | → B |
| :-- | :-- | :-- | :-- |
| expensive | `VALUE(=+4) \| a` | expensive | expensive |
| cheap | `VALUE(=-4) \| a` | cheap | cheap |
| valuable | `VALUE(=+5) GOOD(=+3) \| a` | precious (запасным valuable) | precious (запасным valuable) |
| worthless | `VALUE(=-5) \| a` | worthless | worthless |
| price | `VALUE \| o` | price | price |
| buy | `GIVE(=-3) VALUE \| i` | buy | **sell** |
| sell | `GIVE(=+3) VALUE \| i` | sell | **buy** |
| carefully | `DO(=+3) \| e` → `CARE(=+3) \| e` | carefully | carefully; CARE-прогон: carefully |
| carelessly | `CARE(=-3) \| e` | carelessly | carelessly; carelessly |
| thoroughly | `CARE(=+5) PART(=+2) \| e` | thoroughly | thoroughly; thoroughly |
| hastily | `CARE(=-5) MOVE(=+4) \| e` | hastily | hastily; hastily |
| meticulous | `CARE(=+5) PART(=-4) \| a I+4` | meticulous | meticulous; meticulous |
| sloppy | `CARE(=-4) \| a` | careless (запасным sloppy) | careless (запасным sloppy); careless |
| join | `JOIN(=+3) \| i` | join | add (запасным join) |
| add | `JOIN(=+5) THING \| i` | unite | attach |
| remove | `JOIN(=-4) \| i` | separate (запасным detach) | separate (запасным remove) |
| attach | `JOIN(=+5) TOUCH(=+3) \| i` | weld | connect |
| separate | `JOIN(=-3) PART \| i` | detach | subtract (запасным detach) |

- **VALUE**: 10 из 10 на прилагательных и «цене». *Buy / sell* через `GIVE(=∓3) VALUE`: один декодер читает верно, другой меняет их местами; направление `GIVE` читается неоднозначно (слабое значение ±3 легко спутать).
- **CARE**: 6 из 6 в подтверждающем прогоне (12 из 12 с осью на `DO`). Все слова тщательности читаются верно, включая *thoroughly* (`PART(=+2)` «полностью») и *hastily* (`MOVE(=+4)` «быстро»).
- **JOIN**: примерно 8 из 10. Верно или близко: *join, remove, attach, separate*; *add* не читается ни у одного декодера (*unite, attach*). Внутри кластера слова сливаются.
