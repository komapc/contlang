# INSIDE(=0) — «на границе»: подпись середины оси

spec_new: `INSIDE: -5 outside … 0 on the border, at the edge, the surface … +5 inside` против нынешней (spec_old, без середины).
100 слов поля «граница / край / поверхность / покров» (words.json). Haiku пишет коды по spec_old, другая Haiku со spec_new
переписывает, где подпись помогает (make.py); изменено 22. 4 слепых читателя Haiku на код, судья ../reader. Пороги — dec.md.

| | без подписи | с подписью | разница (95 %) | n |
|---|--:|--:|---|--:|
| изменённые коды | 32 % | 53 % | **+22 % (+5 … +38)** | 22 |

По порогу подпись **принимается**. Лучше всего: boundary (island → border ×3), verge, suburb, horizon, crossing, surface.
Хуже: border `INSIDE(=0) LONG(=-5)` читается как hem (кайма) — для государственной границы лучше `LAND RULE LONG(=-5)` (../border);
corner, ceiling, frontier `… PLACE LIVE(=-2)` (bed).
