# big1000: два кодера на 1000 случайных слов

1000 случайных знаменательных слов из первых 10 000 слов словаря сайта (sample.py, seed 20261021).
Сравниваются два кодера:

- **math** — кодер сайта (`site/math.js` Reader.encode, `site.js`) → site_codes.json;
- **llm** — Haiku со спецификацией сайта ENC_SPEC (`worker/prompts.js`) → llm_codes.json. Haiku получает слово, часть речи (по форме кода math) и первое значение WordNet.

Читают слепые читатели Haiku с DEC_SPEC, по 50 кодов, у каждого коды только одного кодера (lists.json, answers/).
Первый ответ оценивает слепой судья Haiku: 2 близко / 1 рядом / 0 мимо (judge/, ../reader/labels.json).

    python run.py writers|readers|pairs|merge|score SCRATCH

Итог — result.txt. Худшие слова — worst.md: сумма двух оценок, при равенстве выше то, что чаще встречается.
