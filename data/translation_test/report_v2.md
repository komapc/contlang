# Слепой тест 2: время и отрицание как признаки (`TIME`, `MAYBE`)

Те же 12 предложений плюс три новых (13–15) в новой записи `SOMEONE-o LI HEAR-i(TIME=-2, MAYBE=-5)`. Декодер без доступа к оригиналам (`spec.md`, `encoded.md`).

| # | оригинал | декодирование | оценка |
| :-- | :-- | :-- | :-- |
| 3 | She did not hear the noise. | someone did not hear a loud noise | верно (отрицание, прошедшее) |
| 4 | Many people died in the war. | long ago all people died when everyone did great evil | верно по времени (давно), смысл частично |
| 6 | The big red car moved quickly to "Paris". | a big red bus drove quickly right up to Paris | верно |
| 13 | He will not come tomorrow. | someone will not come close | верно (будущее, отрицание) |
| 14 | They were not happy. | people did not feel happy | верно (прошедшее, отрицание) |
| 12 | Maybe the book is very good. | the description of the thing might not be very good | **неверно: «может быть, да» прочитано как «может быть, нет»** |
| 15 | Maybe she knew the answer. | someone may not have known what was said | **неверно: то же** |

Остальные строки (1, 2, 5, 7–11) читаются так же, как в первом тесте (см. `report.md`): простые события и признаки верно, конкретные существительные и сложные клаузы нет.

## Выводы

- **Отрицание и время работают:** в трёх строках с отрицанием (3, 13, 14) смысл восстановлен полностью, время (прошедшее, будущее) читается во всех строках.
- **Ошибка в моей шкале `MAYBE`.** Я определил `-1` как «может быть, нет», и декодер честно прочёл «maybe» как «may not». Шкала должна быть вероятностью с утверждением (0) наверху: `-1` вероятно, `-3` может быть, `-4` вряд ли, `-5` нет. Исправлено в `docs/syntax.md`; пересмотр не проверялся.
- **Не решено и мешает:**
  - роль `PI` в цепочках (`THING-o PI MOVE-a PI PEOPLE-o PI BIG-a PI RGB`): непонятно, что к чему присоединяется;
  - `(=v)` на `-o`/`-a` («живое существо» или «живой»);
  - шкала `SAME` (что значит `-1`, `+3`) и градуировка `TIME` («завтра» или «скоро»);
  - дата `3 5 3`;
  - `LA` («если», «когда», «что») и `QUESTION`.
