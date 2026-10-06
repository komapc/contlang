# Орудие: `DO(=+5)` первым или последним

Вопрос: важен ли порядок `DO(=+5)` в названии орудия — главным корнем (`DO(=+5) TOUCH(=+5) MOVE(=+4) | o`) или последним (`TOUCH(=+5) MOVE(=+4) DO(=+5) | o`). Только декодеры (sonnet, читают tables.md и reading_rules.md, без рецептов): 14 орудий, одни и те же корни, наборы H — `DO(=+5)` первым, T — последним, по 2 декодера; ✓ лучшее слово, ~ среди трёх.

| набор | H1 | H2 | T1 | T2 |
| :-- | --: | --: | --: | --: |
| ✓ / ✓+~ из 14 | 9 / 11 | 11 / 11 | 9 / 10 | 11 / 11 |

- **Порядок не важен**: 20 из 28 в обоих вариантах; разброс между декодерами больше, чем между порядками. Обе записи допустимы.
- *ship* `MOVE GRAIN(=-3)` — 0 из 4 (*fan*): без рецепта воды декодер читает `GRAIN(=-3)` как воздух (как море и река в [roundtrip_lacunae2](roundtrip_lacunae2.md)). В таблице у `GRAIN` нет «жидкости» на −3.
- *camera* `SEE TEXT` — 0 из 4 (*glasses*, *book*): нужна другая основа.
- *saw* `JOIN(=-4) MOVE(=+2)` — 0–1 из 4 (*knife*, *shovel*, *broom*), как и раньше.

| слово | основа | H1 | H2 | T1 | T2 |
| :-- | :-- | :-: | :-: | :-: | :-: |
| knife | `JOIN(=-4) TOUCH(=+4)` | ✗ axe | ✓ | ~ axe | ✓ |
| saw | `JOIN(=-4) MOVE(=+2)` | ~ knife | ✗ brake | ✗ shovel | ✗ broom |
| scissors | `JOIN(=-4) MANY(=+1)` | ✓ | ✓ | ✓ | ✓ |
| hammer | `TOUCH(=+5) MOVE(=+4)` | ✓ | ✓ | ✓ | ✓ |
| brush | `TOUCH(=-3) MOVE` | ✓ | ✓ | ✓ | ✓ |
| pen | `TEXT` | ✓ | ✓ | ✓ | ✓ |
| thermometer | `MEASURE HEAT` | ✓ | ✓ | ✓ | ✓ |
| ladder | `MOVE ABOVE(=+4)` | ~ crane | ✓ | ✗ elevator | ✓ |
| key | `INSIDE(=+4) CAN(=+4)` | ✓ | ✓ | ✓ | ✓ |
| car | `MOVE(=+4)` | ✓ | ✓ | ✓ | ✓ |
| ship | `MOVE GRAIN(=-3)` | ✗ fan | ✗ fan | ✗ fan | ✗ fan |
| weapon | `FIGHT(=+5)` | ✓ | ✓ | ✓ | ✓ |
| gun | `FIGHT(=+5) HEAT(=+5)` | ✓ | ✓ | ✓ | ✓ |
| camera | `SEE TEXT` | ✗ glasses | ✗ glasses | ✗ book | ✗ glasses |
