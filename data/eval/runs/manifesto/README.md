# Манифест на min-co и обратно (2026-10-14)

Проба по просьбе пользователя: 12 фраз манифеста (по [philosophy.md](../../../../docs/philosophy.md)) — [text_en.md](text_en.md).
Кодировал Claude (Opus) по спецификации предложений ([enc_spec.md](enc_spec.md)) — [codes.md](codes.md), валидатор без ошибок.
Обратно переводил слепой Haiku: видел только [dec_spec.md](dec_spec.md) и коды — [back_en.md](back_en.md). Один прогон; оценка — моя, не судьи.

| # | исходник | обратный перевод | смысл |
|--:|---|---|---|
| 1 | min-co is a small language for careful and flexible thought | min-co is written briefly, for careful thought and for change | почти |
| 2 | Its rules are few, and its words are few | Rules are few, and short texts are few too | наполовину |
| 3 | A meaning is a place in a field, not a box | A conclusion is found in a short text and placed there; it is not placed inside a physical thing | нет |
| 4 | A word is a root plus small changes on its axes | A short text begins, and small changes come | нет |
| 5 | The language has 45 roots, and most roots have one axis | Text is inside section 45; many beginning parts contain length | нет |
| 6 | The short mark at the end of a word tells what kind of word it is | A letter at the back teaches the same thing that appears in a short text | наполовину |
| 7 | If you do not write a value, the value is unknown | If you do not write any quantity, the quantity is not known | да |
| 8 | The main word comes first | A precious short saying comes forward | наполовину |
| 9 | You do not learn a dictionary; you build words from roots | You do not take in complete speech; you make short texts from their beginnings | наполовину |
| 10 | A code is good if the reader names a word of the same field | When a reader speaks a short text in the same place, the text is good | наполовину |
| 11 | Math writes the codes; a thinking machine does not | Exact measurement makes texts; a technical thinking tool does not | почти |
| 12 | When we think about simplicity, we look at Toki Pona | If we think of ease, we see Toki Pona | да |

Итог: 2 да, 2 почти, 6 наполовину, 3 нет (из 12). Грамматика (`LA [ ]`, `;`, `M-5`, `E`, роли) читается; ломаются понятия о самом языке:
- «слово» `SAY TEXT PART(=-2)` читается как «короткий текст», «корень» `PART(=-2) BEGIN(=-5)` — как «начало», «ось» `MEASURE(=0) LONG(=0)` — как «длина»;
- «значение слова» `THINK | o result PI …` — «вывод»;
- `"45"` без слова-счётчика прочитано как номер раздела.
Метаязыка (слово, корень, ось, значение) в 45 корнях нет — его приходится описывать, и описания неоднозначны.
