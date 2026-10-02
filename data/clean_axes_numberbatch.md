# Чистка осей (numberbatch, 3000 слов)

Варианты векторов: **raw** — как есть; **freq** — вычтено направление частотности; **abtt** — вычтены среднее и 3 главные компоненты; **both** — оба.

- **|ρ| freq** — средняя / максимальная |корреляция Спирмена| оси с частотностью слова (ранг в GloVe);
- **coherence** — средний косинус (в raw-пространстве) между 10 крайними словами на полюсах; для случайных слов 0.036;
- **wup / pos / top50** — round trip (слово → k осей → ближайшее другое слово): WordNet-сходство, совпадение части речи, попадание в 50 истинных соседей по raw-пространству.

| вариант | k | \|ρ\| freq (сред / макс) | coherence | wup | pos | top50 |
| :-- | --: | :-- | --: | --: | --: | --: |
| raw | 10 | 0.14 / 0.35 | 0.312 | 0.382 | 66% | 48% |
| raw | 30 | 0.11 / 0.32 | 0.276 | 0.444 | 78% | 87% |
| freq | 10 | 0.05 / 0.14 | 0.326 | 0.379 | 64% | 48% |
| freq | 30 | 0.04 / 0.17 | 0.265 | 0.443 | 75% | 89% |
| abtt | 10 | 0.12 / 0.34 | 0.366 | 0.429 | 40% | 41% |
| abtt | 30 | 0.09 / 0.34 | 0.279 | 0.454 | 64% | 81% |
| both | 10 | 0.05 / 0.10 | 0.359 | 0.418 | 42% | 40% |
| both | 30 | 0.04 / 0.08 | 0.269 | 0.449 | 66% | 84% |

## Оси nano-10, вариант raw

1. **−** assign, characterize, classify, specify, describe, portray, declare, interpret  /  **+** late, after, early, years, later, time, day, excitement
2. **−** continue, dwindle, diminish, lessen, anticipate, steadily, persist, accelerate  /  **+** description, representative, official, representation, item, piece, department, agency
3. **−** incredibly, truly, tremendously, absolutely, extremely, perfectly, remarkably, reasonably  /  **+** reappear, notify, refer, interrupt, linger, disturb, precede, occur
4. **−** regard, importance, relevant, specific, relation, pursuant, consideration, requirement  /  **+** hurl, heave, knock, throw, swoop, roar, tear, gasp
5. **−** educate, strive, strengthen, foster, help, uphold, secure, protect  /  **+** though, probably, presumably, nevertheless, apparently, nonetheless, anyway, latter
6. **−** calmly, accordingly, properly, cautiously, gently, somehow, quietly, deliberately  /  **+** tremendous, huge, enormous, great, incredible, formidable, impressive, massive
7. **−** off, finish, run, complete, remove, down, install, set  /  **+** uneasy, admire, profoundly, wonder, vividly, peculiarly, concern, curious
8. **−** congratulate, resign, request, hope, finally, concede, glad, announce  /  **+** proportion, vary, narrow, broad, proportionately, density, vertical, intensity
9. **−** numerous, promptly, prominently, various, several, shortly, brilliantly, frequently  /  **+** guess, believe, belief, assumption, faith, suppose, reckon, think
10. **−** discover, find, happen, exist, create, locate, realize, relate  /  **+** angrily, heartily, reluctantly, solemnly, vigorously, stoutly, stiffly, strongly

## Оси nano-10, вариант both

1. **−** regret, afraid, uneasy, sad, resent, fear, emotion, doubt  /  **+** neatly, effectively, conveniently, accurately, comfortably, roughly, methodically, properly
2. **−** inquire, report, examine, congratulate, description, article, interview, ask  /  **+** diminish, lessen, reduce, weaken, minimal, decrease, dwindle, sustain
3. **−** strengthen, actively, enhance, promote, encourage, help, vitally, educate  /  **+** typical, usual, exact, calculate, odd, suppose, earlier, occurrence
4. **−** quite, pretty, really, especially, nice, awfully, seem, particularly  /  **+** subsequently, thereafter, shortly, after, objective, final, before, later
5. **−** guess, think, suppose, reckon, believe, presume, doubt, surely  /  **+** various, numerous, repeatedly, several, promptly, prominently, frequently, notably
6. **−** likewise, furthermore, moreover, conversely, besides, significantly, considerably, similarly  /  **+** perfect, perfectly, fantastic, accurate, magnificent, brilliant, beautiful, absolutely
7. **−** somehow, indeed, truly, altogether, totally, entirely, actually, completely  /  **+** cautiously, anxiously, nervously, carefully, intently, impatiently, eagerly, thoughtfully
8. **−** learn, realize, discover, understand, find, comprehend, achieve, happen  /  **+** flatly, wholly, reject, unanimously, sanction, authority, endorse, totally
9. **−** strictly, loosely, calm, differently, regulate, behave, define, deliberately  /  **+** tremendous, enormous, considerable, huge, great, formidable, impressive, incredible
10. **−** clearly, characterize, demonstrate, emphasize, distinctly, portray, strongly, depict  /  **+** convenient, pleasant, useful, comfortable, available, helpful, safe, expense
