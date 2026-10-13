# Корень SEX только у слов, где пол — часть смысла (2026-10-13)

Векторы Numberbatch несут уклон корпуса: teacher, nurse ближе к «женскому», president, doctor, engineer — к «мужскому».
Кодер математики ставил SEX в 77 кодах из «других 1000» (president `RULE(=+3) SEX(=+3) TIME(=-1)`, teacher `ART(=+1) SEX(=-3) KNOW(=+3)`),
хотя спецификация говорит «only for words of explicit sex». Имена (michael, rebecca) тоже получали SEX.

Правило (scripts/site/build_words.py → words.json `sexed`, 81 слово): пол — часть смысла, если слово — male, female, masculine, feminine
или первый нарицательный синсет WordNet начинается с «a woman / a male / a young man…» (не «a father or mother»), либо лежит под man, woman, male, female.
Остальным словам кодер (`Reader.ban`) не даёт SEX, а штраф за неупомянутый корень не считает SEX (иначе код без SEX отталкивал бы nurse).
SEX(=0) не нужен: отсутствие корня уже значит «человек вообще», а SEX(=0) тратит один из трёх корней и читается как «средний пол».

`node eval.js` → eval.out, results.json:

| | dev | 1000 | другие 1000 | кодов с SEX (1000 / другие) | коды моделей cos | рецепты cos |
|---|--:|--:|--:|--:|--:|--:|
| как было | 71 | 466 | 449 | 61 / 77 | 0,227 | 0,321 |
| SEX только с полом | 70 | 457 | 433 | 10 / 8 | 0,227 | 0,321 |

Цена — 9–16 слов первыми на 1000: векторы узнавали слово как раз по уклону. Оставшиеся коды с SEX — husband, wife, sister, widow, monk, princess…
Примеры: president → `RULE(=+4) TIME(=-2) PART(=+3)`, teacher → `ART(=+1) KNOW(=+3) RULE(=0)`, soldier → `FIGHT(=+3)`, king и mother без изменений.
