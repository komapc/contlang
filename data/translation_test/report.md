# Слепой тест перевода: английский → min-co → английский

Схема: корни NSM (27) + градиентные корни + суффиксы + частицы LI/E/PI/LA; универсальные оси не использовались (они неназванные, вручную их не закодировать). Кодировал я, декодировал отдельный агент без доступа к оригиналам (`spec.md`, `encoded.md`, `sentences.md`).

| # | оригинал | декодирование (кратко) | оценка |
| :-- | :-- | :-- | :-- |
| 1 | The dog sleeps in the house. | animal is dying in the house | частично (животное, дом; «спит» → «умирает») |
| 2 | I want to see my friend tomorrow. | I want to see a good person soon | хорошо |
| 3 | She did not hear the noise. | someone did not hear a loud noise a while ago | хорошо (пол потерян) |
| 4 | Many people died in the war. | everyone died long ago, everyone did great evil to everyone | частично |
| 5 | If it rains, we stay inside. | when a fast thing moves far below, most of us stay inside | частично («остаёмся внутри» есть, дождь потерян) |
| 6 | The big red car moved quickly to Paris. | a big red bus quickly arrived at Paris recently | хорошо |
| 7 | Who said that the king is dead? | someone asked whether a person from a foreign people died | частично («кто-то сказал/спросил», «мёртв»; король, «кто» потеряны) |
| 8 | He thinks that the water is cold. | someone thinks about a living person and something unpleasant | провал |
| 9 | Children learn language by listening. | a weak person understands the kind of word when hearing it | провал |
| 10 | The meeting is on March 5 at 3 o'clock. | a compatriot appears now: 3 5 3 | провал |
| 11 | I love you. | I really want you to be good | частично |
| 12 | Maybe the book is very good. | maybe the word for the thing is very good | хорошо |

Итого: 4 хорошо, 5 частично, 3 провала (оценки мои, одна проба, 12 предложений).

## Что ломается

1. **Конкретные существительные** (dog, water, rain, king, car, book, children, language): собираются перифразой из корней, и она неоднозначна. Это ожидаемо: в тесте нет универсальных осей, которые и должны различать *dog* и *cat*. Ручная кодировка тут не показательна; настоящий путь — автоматическая (слово → корень + суффикс + оси → ближайшее слово), как в метриках.
2. **Слой 2 не определён.** Нет времени глагола (пришлось через `TIME-e`), отрицания (`ALA` временный), вопроса, числа, местоимений (`MI`, `SINA` временные), «что» (`LA` читается как «если/когда/потому что/что»), роли `PI` (определение, «из», «который»).
3. **Градиенты читаются неоднозначно:** ABOVE(-4) путают с направлением, GOOD(-5) читается и как «зло», и как «вред», BIG(2) — как «громкий». Нужна ясная конвенция полюсов и значений.
4. **Числа и даты:** формат (месяц-день-час) не определён, строка 10 нечитаема.
5. **Логические связки** (и, но, или, потому что) не определены.
6. **Роль слов после WORD-o** (`KIND`, `THING`): «тип слова», «язык», «добрые слова».

## Что работает

Простые события и признаки («хочу увидеть хорошего человека скоро», «большая красная машина быстро поехала в "Paris"», «может быть, слово хорошее») восстанавливаются верно. Именно собственные имена, цвета и числа, вынесенные послаблениями, держатся лучше всего.
