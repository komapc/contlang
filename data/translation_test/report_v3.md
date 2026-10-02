# Слепой тест 3: структура клауз (`PI`, `LA`, скобки, вопрос `?`, даты)

18 предложений (`sentences.md`, `encoded.md`, `spec.md`), декодер без оригиналов.

| # | оригинал | декодирование | оценка |
| :-- | :-- | :-- | :-- |
| 1 | The dog sleeps in the house. | a living body is almost dead in the people's place | частично |
| 2 | I want to see my friend tomorrow. | I want to see a very good person tomorrow/soon | хорошо |
| 3 | She did not hear the noise. | someone did not hear a fairly loud sound recently | хорошо |
| 4 | Many people died in the war. | all the people died long ago; all the people did terrible things | частично |
| 5 | If it rains, we stay inside. | a thing moves high above if I don't move inside | **провал (условие перепутано)** |
| 6 | The big red car moved quickly to "Paris". | the big red public vehicle went near Paris | частично/хорошо |
| 7 | Who said that the king is dead? | who said that a big person/leader of the people is dead? | хорошо |
| 8 | He thinks that the water is cold. | someone thinks a fully alive thing feels bad | провал |
| 9 | Children learn language by listening. | a small group of people will know the people's word when they hear it | провал |
| 10 | The meeting is on March 5 at 3 o'clock. | similar people met on March 5 at 3:00 | хорошо |
| 11 | I love you. | I really want you | частично |
| 12 | Maybe the book is very good. | the word of the thing is maybe very good | хорошо (шкала MAYBE исправлена) |
| 13 | He will not come tomorrow. | someone will not come close | хорошо |
| 14 | They were not happy. | people did not feel good a short time ago | хорошо |
| 15 | Maybe she knew the answer. | someone perhaps didn't know the word that was said | частично (степень верна, полярность нет) |
| 16 | Did he come? | did someone come close (recently)? | хорошо |
| 17 | What do you want? | what do you want? | хорошо |
| 18 | I think that he is good. | I think someone is good | хорошо |

Итого: 10 хорошо, 5 частично, 3 провала. На первых 12 предложениях: тест 1 дал 4 / 5 / 3, тест 3 — 5 / 4 / 3. Оценки мои, один декодер, малая выборка.

## Что подтвердилось

Структура работает: отрицание, время, вопрос (`MAYBE=?`, `SOMEONE-o(?)`, `THING-o(?)`), клауза в скобках после *думать/сказать*, даты (`DATE(...)`, `CLOCK(...)`) и шкала `MAYBE` читаются верно.

## Что не работает

1. **Конкретные существительные** (water, child, dog, king, book, car): через перифразы корней неоднозначно. Это главное узкое место, а не грамматика.
2. **`LA` (условие):** в строке 5 условие и следствие перепутаны.
3. **Градиент на корнях без явных полюсов** (`LIVE-i(=-2)`, `SAME-a(=3)`): читается произвольно; нужно либо определить полюса всех градиентных корней, либо ограничить `(=v)` определёнными корнями.
4. **Мелочи формы:** как сочетаются `(=v)` и `(TIME=v)` в одной скобке; на что действует `MAYBE` (сказуемое или вся клауза); смысл `-a/-e/-o` у глагольных корней без правил (`MOVE-a`, `SAY-a`).
