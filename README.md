# contlang

**Сайт:** [minco.lipu.dev](https://minco.lipu.dev/)

**min-co** — минимальный непрерывный конструируемый язык (*minimal + continuous*). Слово = **до трёх корней** (главный первым, у корня может быть значение на его оси −5…+5) **`|` часть речи и грамматические метки**; связь слов — частицы, как в Toki Pona. Схема подбирается экспериментами на данных (эмбеддинги, WordNet), см. `data/` и `scripts/`.

## Версии языка

В репозитории несколько версий min-co рядом ([lang/README.md](lang/README.md)): **v1** (min-co 1.0, тег `minco-1.0`) — файлы ниже, сайт и воркер;
**v2** (min-co 2.0, в разработке) — [`lang/v2/`](lang/v2/charter.md). Инструменты без `--lang` работают с v1.

## Документация (v1)

**Источник правды о языке — [`roots.yaml`](roots.yaml)** (корни, оси, допустимые значения осей, метки, частицы); из него генерируются [таблицы](docs/tables.md) и блоки в словаре (`.venv/bin/python scripts/mincode/gen.py`).

- [Как читать min-co](docs/reading.md) — короткая памятка для знающих Toki Pona и эсперанто
- [Модель: корень и структура](docs/model.md)
- [Философия и принципы](docs/philosophy.md)
- [Синтаксис](docs/syntax.md)
- [Сводные таблицы: корни, оси, метки](docs/tables.md) (генерируются)
- [Рецепты кодирования](docs/encoding.md)
- [Словарь: корни, суффиксы, признаки](docs/lexicon.md)
- [Фонология и структура слова](docs/phonology.md)
- [Пересмотр языка: эталон Токипоны, предложения, открытые вопросы](docs/rethink.md)
- [Математическое кодирование](docs/math.md)
- English translation of these documents: [docs/en/](docs/en/) (проверка согласованности — `tests/test_docs_en.py`)
- Прежние планы — [docs/history/](docs/history/)

## Инструменты

- Скилл `mincode` (`.claude/skills/mincode/SKILL.md`): закодировать слово или раскодировать код.
- `scripts/mincode/`: `gen.py` (генерация документов из `roots.yaml`, `--check`), `validator.py` (проверка кодов: корни, оси и их допустимые значения, метки, лимит корней; те же правила у воркера — `worker/check.js`, согласие проверяет `tests/test_check_parity.py`).
- `scripts/eval/`: слепой тест кодирования (спецификации, лист судьи, подсчёт с интервалом; нынешняя мера — доля ответов «близко» по слепому судье), протокол — [scripts/eval/README.md](scripts/eval/README.md); данные и прогоны — `data/eval/`.
- Окружение: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`; все команды ниже — через `.venv/bin/python` (системному `python3` обычно не хватает `pyyaml` и `markdown`). Для теста воркера нужен `node`.
- Проверка: `.venv/bin/python -m pytest tests` (согласованность файлов, валидатор и воркер, сборка спецификаций).
- Сайт: статические страницы `site/` (GitHub Pages, обновляются сами при push): английская `/` и русская `/ru/` собираются из одного источника `data/site/index.html`, документы `docs/*.md` публикуются как `/docs/<имя>/`, вместе с `sitemap.xml` (`.venv/bin/python scripts/site/build.py`, внутри — `scripts/site/pages.py`) и прокси-воркер `worker/` для модели (выкладывается вручную); что генерируется и порядок обновления — [worker/README.md](worker/README.md). На GitHub при каждом push проверяется, что сгенерированные файлы не устарели и тесты проходят (`.github/workflows/check.yml`).

