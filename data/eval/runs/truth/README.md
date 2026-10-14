# Корень TRUE: вымысел … заявлено … доказано (2026-10-15)

Пороги — [dec.md](dec.md) (закоммичен до листов). 46 слов, где код с TRUE отличается от кода сайта: 9 из худших (всегда мимо)
и 37 свежих слов поля TRUE (без слов-полюсов оси и слов строки спецификации). **M** — сайт, **T** — 46 корней, строка TRUE
в спецификации (`root.json`, `codes.js`). Каждый вариант — 2 слепых Haiku (все 46 кодов), судья Haiku 2/1/0, все строки оценены.

Лестница, которую кодер сам строит по словам словаря (ось × 0,5): −5 fantasy, suspicion · −4 lie, fiction, fraud · −3 false, rumors,
speculation · −2 wrong, doubts, allegations · −1 doubt, belief, theory · 0 claim, alleged, believe, supposed · +1 truth, facts,
confirmed · +2 true, fact, prove, evidence · +3 real, proof, sure, accurate · +4 actual, truly, certainly, reliable · +5 certain, exact, absolute.

## Итог ([result.txt](result.txt), [table.md](table.md))

| | M | T | разница (95 %) | n |
|---|--:|--:|---|--:|
| **T − M** | 4 % | 27 % | **+22,8 % [+12,0 … +34,8]** | 46 |
| — поле TRUE | 4 % | 31 % | +27,0 % [+14,9 … +40,5] | 37 |
| — худшие | 6 % | 11 % | +5,6 % [−16,7 … +33,3] | 9 |

«Рядом»: M 28 %, T 35 %. **Порог пройден.** Примеры: reality `TRUE(=+2)` → fact, truth; invented → fabricated; artificial,
significant, valid, existence, absolute — прочитаны точно; believe → suppose; testify → declare. Не помогло: right/rights
(читаются как место — SIDE PLACE), princess, discovery, tale (→ forgery), truly.

Оговорки: слова поля выбраны там, где TRUE близок по вектору, — это проверка корня на его поле; по всему словарю TRUE входит
в 2–3 лучших корня примерно у 150 из 7700 частых слов. На 120 хорошо читаемых словах (обратное чтение математикой) он почти
не появляется и ничего не портит. Ввод корня — решение пользователя.
