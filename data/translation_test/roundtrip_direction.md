# Направление движения: слепой тест

Вопрос: нужна ли в языке запись «откуда / куда» (лакуна *extract*: сайт дал `CONSUME(=+5) THING(=0) | i` → *eat*). Слова (24): *enter, exit, insert, extract, emerge, pour, arrive, depart, approach, escape, return, rise, descend, bring, send, push, pull, throw, import, export, swallow, remove, fill, empty*.

Протокол как в [roundtrip_time](roundtrip_time.md): sonnet, по 2 кодировщика и по 1 декодеру на кодировщика; ✓ лучшее слово = оригинал (синонимы засчитаны: *leave* = *exit/depart*, *fall* = *descend*, *flee* = *escape*), ~ среди трёх.

- **A** — нынешняя спецификация.
- **B** — рецепт на существующих корнях: у глагола движения (`MOVE`, `GIVE`, `DO`) значение `INSIDE` / `NEAR` / `ABOVE` — **где движение кончается**: войти `MOVE INSIDE(=+5) | i`, выйти `MOVE INSIDE(=-5) | i`, прибыть `MOVE NEAR(=+5) | i`, уйти `MOVE NEAR(=-5) | i`, подняться `MOVE ABOVE(=+5) | i`, приближаться `MOVE NEAR(=+5) | i A0`; двигать другое — `K+3`: вставить `MOVE INSIDE(=+5) | i K+3`, принести `MOVE NEAR(=+5) | i K+3`; вернуться `MOVE SAME(=+5) | i`.
- **C** — новая метка формы `W` (`W+4` к, в; `W-4` от, из), корень места без значения: войти `MOVE INSIDE | i W+4`.

| набор | A1 | A2 | B1 | B2 | C1 | C2 |
| :-- | --: | --: | --: | --: | --: | --: |
| ✓ / ✓+~ из 24 | 17 / 19 | 19 / 20 | 18 / 22 | 18 / 22 | 18 / 20 | 18 / 21 |

Что видно:

- **Лакуны почти нет.** Кодировщики A без всякого рецепта сами пишут `MOVE INSIDE(=±5)`, `MOVE NEAR(=±5)`, `MOVE ABOVE(=±4)` — и декодер это читает: войти, выйти, вставить, прибыть, уйти, подняться, спуститься, принести, отправить — 6 из 6 во всех наборах. Ошибка сайта на *extract* — кодировщик не взял `MOVE`, а не нехватка записи.
- **Метка `W` ничего не даёт** (C ≈ B ≈ A) — новая грамматика не нужна.
- **Рецепт B снимает разнобой**: *return* (A: `MOVE PLACE SAME` → *gather*, *arrive*; B: `MOVE SAME(=+5)` → 2 из 2), *fill / empty* (`MOVE INSIDE(=±5) MANY(=+5) | i K+3`). *extract* = `MOVE INSIDE(=-5) | i K+3` читается как *remove* (~): вынуть и убрать — один код, потеря принята.
- **Остались промахи**: *pull* — 0 из 6 (`TOUCH MOVE NEAR(=+3)` читается как *hit*, *press*: «к себе» не выражено); *import / export* — читаются как *invest / spend / withdraw* (`VALUE` уводит в деньги, страны нет). Это отдельные лакуны, не направление.

## По словам

| слово | A1 | A2 | B1 | B2 | C1 | C2 |
| :-- | :-: | :-: | :-: | :-: | :-: | :-: |
| enter | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| exit | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| insert | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| extract | ✗ remove | ✗ exclude | ~ remove | ~ remove | ✓ | ~ remove |
| emerge | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| pour | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| arrive | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| depart | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| approach | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| escape | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| return | ✗ gather | ~ arrive | ✓ | ✓ | ✓ | ✓ |
| rise | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| descend | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| bring | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| send | ✓ | ✓ | ✓ | ✓ | ~ remove | ✓ |
| push | ~ kick | ✓ | ✓ | ✓ | ✓ | ✗ recoil |
| pull | ✗ hit | ✗ hit | ✗ put | ✗ press | ✗ press | ✗ hit |
| throw | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| import | ✗ earn | ✓ | ✗ invest | ✗ buy | ✗ invest | ~ invest |
| export | ✗ spend | ✓ | ~ spend | ~ sell | ✗ withdraw | ~ withdraw |
| swallow | ✓ | ✓ | ✓ | ~ eat | ~ inject | ✓ |
| remove | ~ separate | ✓ | ~ separate | ~ separate | ✗ separate | ✗ separate |
| fill | ✓ | ✗ absorb | ~ pack | ✓ | ✓ | ✓ |
| empty | ✓ | ✗ extract | ✓ | ✓ | ✓ | ✓ |

## Коды трудных слов

| набор | слово | код |
| :-- | :-- | :-- |
| A1 | extract | `MOVE INSIDE(=-5) \| i K+4` |
| A1 | pull | `TOUCH(=+4) MOVE NEAR(=+3) \| i` |
| A1 | import | `GIVE(=-3) VALUE INSIDE(=+5) \| i` |
| A1 | return | `MOVE PLACE SAME(=+5) \| i` |
| A1 | remove | `JOIN(=-4) \| i` |
| B1 | extract | `MOVE INSIDE(=-5) \| i K+3` |
| B1 | pull | `MOVE TOUCH NEAR(=+3) \| i K+3` |
| B1 | import | `MOVE INSIDE(=+5) VALUE \| i K+3` |
| B1 | return | `MOVE SAME(=+5) \| i` |
| B1 | remove | `JOIN(=-4) \| i` |
| C1 | extract | `MOVE INSIDE \| i K+3 W-4` |
| C1 | pull | `TOUCH(=+3) MOVE NEAR \| i K+3 W+4` |
| C1 | import | `MOVE INSIDE VALUE \| i K+3 W+4` |
| C1 | return | `MOVE NEAR SAME(=+5) \| i W+4` |
| C1 | remove | `JOIN(=-4) \| i` |
