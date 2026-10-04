# «Важный»: два варианта кода, слепой тест

5 слов × 2 варианта = 10 кодов, два декодера (порядок кодов перемешан, спецификация без ответов). Коды писал я. Читалось одно прилагательное и два запасных.

**Вариант а** — `BIG` + `HAPPEN` («большие последствия»); **вариант б** — `GOOD` + `BIG` («большое и хорошее»).

| слово | вариант а: код | A | B | вариант б: код | A | B |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| important | `BIG(=+4) HAPPEN(=+3)` | significant | major | `GOOD(=+3) BIG(=+3)` | fine | great |
| significant | `BIG(=+3) HAPPEN(=+3)` | considerable | significant | `GOOD(=+2) BIG(=+2)` | decent | considerable |
| major | `BIG(=+4) HAPPEN(=+4)` | important | important | `GOOD(=+2) BIG(=+4)` | great | grand |
| crucial | `BIG(=+5) HAPPEN(=+5)` | momentous (alt. decisive) | momentous | `GOOD(=+4) BIG(=+5)` | wonderful | magnificent |
| vital | `BIG(=+5) HAPPEN(=+4) LIVE(=+3)` | dramatic (alt. vital) | dramatic | `GOOD(=+4) BIG(=+4) LIVE(=+3)` | splendid | thriving |

- **Вариант а**: 8–9 из 10 (синонимы по смыслу «важный»: significant, major, important, momentous, decisive). Единственная слабая точка — *vital* (`LIVE(=+3)` читается как «драматичный»).
- **Вариант б**: 0 из 10. `GOOD` вместе с `BIG` читается как похвала (*great, wonderful, splendid*), а не как важность.
- Градация работает грубо: `BIG(=+3) HAPPEN(=+3)` — *significant / considerable*, `+4 / +4` — *important / major*, `+5 / +5` — *momentous / decisive*.
