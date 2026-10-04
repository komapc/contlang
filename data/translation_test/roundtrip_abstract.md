# Слепой тест оси ABSTRACT (конкретное … абстрактное)

16 слов, два независимых кодировщика (видели только спецификацию на 44 корня), два декодера (видели только спецификацию и коды). Попадание — слово или близкий синоним в лучшем ответе или альтернативах. Оценки мои.

| # | слово | A | B | попаданий |
| --: | :-- | :-- | :-- | --: |
| 1 | idea | `THINK(=0) ABSTRACT(=+5) \| o` → thought, idea | `THINK ABSTRACT(=+5) \| o` → idea | 2/2 |
| 2 | theory | `KNOW(=+1) THINK ABSTRACT(=+5)` → concept | `THINK ABSTRACT(=+5) PART(=+5)` → philosophy, theory | 1/2 |
| 3 | principle | `RULE(=+1) THINK ABSTRACT(=+5)` → principle | `RULE(=0) ABSTRACT(=+5)` → principle | 2/2 |
| 4 | belief | `KNOW(=+2) THINK` → knowledge | `THINK KNOW(=+3)` → belief | 1/2 |
| 5 | assume | `THINK(=+2) MAYBE(=-1) ABSTRACT(=+5) \| i` → assume | `THINK(=+3) MAYBE(=-1) \| i` → suppose | 2/2 |
| 6 | imply | `SAY(=-3) ABSTRACT(=+5)` → imply | `SAY ABSTRACT(=+5) MAYBE(=-1)` → imply | 2/2 |
| 7 | presume | `THINK(=+4) MAYBE(=-1) KNOW(=-1)` → infer, presume | `THINK(=+3) MAYBE(=-1) TIME(=-2)` → remember | 1/2 |
| 8 | suppose | `THINK(=+1) MAYBE(=-3)` → wonder, suppose | `THINK ABSTRACT(=+5) MAYBE(=-3)` → assume | 2/2 |
| 9 | kick | `TOUCH(=+4) MOVE(=+4) BODY` → kick | `TOUCH(=+4) MOVE(=+4) ABSTRACT(=-5)` → hit | 1/2 |
| 10 | shake | `MOVE(=+2) PART(=-2) ABSTRACT(=-5)` → shake | `MOVE(=+2) MANY(=+3) ABSTRACT(=-5)` → shake | 2/2 |
| 11 | tumble | `MOVE(=-1) ABOVE(=-4) CARE(=-5)` → fall, tumble | `MOVE(=+2) ABOVE(=-4) CARE(=-4)` → fall, tumble | 2/2 |
| 12 | rattle | `MOVE(=+3) TOUCH(=+3) SAY(=-3)` → poke | `SAY THING(=-5) MOVE(=+3)` → rumble | 0/2 (рядом) |
| 13 | concrete | `ABSTRACT(=-5) \| a` | то же | 2/2 |
| 14 | abstract | `ABSTRACT(=+5) \| a` | то же | 2/2 |
| 15 | tangible | `TOUCH CAN ABSTRACT(=-5) \| a` | то же | 2/2 |
| 16 | theoretical | `KNOW(=+1) THINK ABSTRACT(=+5) \| a` → intellectual | `KNOW ABSTRACT(=+5) MAYBE(=-3)` → speculative | 1/2 |

Итого строго: **25 из 32** (78 %). Знак оси не перепутан ни разу; все промахи — соседи по значению (*concept* вместо *theory*, *knowledge* вместо *belief*, *hit* вместо *kick*, *rumble* вместо *rattle*).

## Выводы

- **Ось принята.** Полюса читаются: `ABSTRACT(=-5)` даёт физическое (*kick, shake, tumble, concrete, tangible*), `ABSTRACT(=+5)` — умственное (*idea, principle, imply, assume, abstract*).
- Чаще всего кодировщики сочетают её с `THINK` (мысль, предположение), `SAY` (*imply* = `SAY ABSTRACT(=+5)`), `TOUCH` + `MOVE` (физические действия).
- Кластер *assume / suppose / presume* слит (разница во второстепенных оттенках), как раньше с *specific / particular*.
- Без `ABSTRACT` у кодировщика *kick* и *hit* неразличимы; ось сама их не различает.
