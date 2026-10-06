# Прокси для демо-страницы

Страница на GitHub Pages статическая и не может хранить ключ. Эта функция Cloudflare Workers держит ключ OpenRouter, вызывает дешёвую модель (по умолчанию `openai/gpt-4o-mini`, меняется переменной `MODEL` в `wrangler.toml`), ограничивает ввод 300 символами и 10 запросами в минуту с адреса.

Развёртывание (один раз):

1. `cd worker && npm i -g wrangler && wrangler login`
2. `wrangler secret put OPENROUTER_API_KEY` (ключ вводится в терминале, в репозиторий не попадает)
3. при другом адресе страницы поправьте `ALLOWED_ORIGINS` в `wrangler.toml`
4. `wrangler deploy` — выведет адрес вида `https://minco-demo.<аккаунт>.workers.dev`
5. вставьте этот адрес в `site/config.js` (`MINCO_API`)

`prompts.js` генерируется: `python3 scripts/site/build.py` (из `roots.yaml` и шаблонов спецификаций). Задайте на ключе OpenRouter лимит расхода (https://openrouter.ai/settings/keys) — это последняя защита от злоупотреблений.

## Обновление после правок языка

Что откуда берётся и как попадает на сайт:

| файл | откуда | как попадает на сайт |
| :-- | :-- | :-- |
| `docs/tables.md`, блоки `docs/lexicon.md` | `roots.yaml` → `python3 scripts/mincode/gen.py` | только документация |
| `site/data/roots.json`, `site/data/examples.json` | `roots.yaml`, отчёты слепых тестов → `python3 scripts/site/build.py` | **сами** после push в `main` (GitHub Pages, `.github/workflows/pages.yml`) |
| `site/data/math.json`, `site/data/vocab.bin` (математика на странице: словари корней, 10 000 частых слов и весь список 3000) | `roots.yaml`, `data/sparse_dict_learned.npz`, векторы Numberbatch → `.venv/bin/python scripts/site/build_math.py` (локально: нужны numpy и `data/raw`) | сами после push; `build.py --check` и проверка на GitHub сообщат, если корни или полюса изменились, а файл не пересобран |
| `worker/prompts.js` (подсказки модели) | `roots.yaml`, шаблоны спецификаций, `data/site/tips_short.md` → `python3 scripts/site/build.py` | **вручную**: `cd worker && npx wrangler deploy` |

Порядок после изменения `roots.yaml` или рецептов:

1. `python3 scripts/mincode/gen.py && python3 scripts/site/build.py`; если менялись корни или полюса — ещё `.venv/bin/python scripts/18_sparse_learn.py` (обученный словарь) и `.venv/bin/python scripts/site/build_math.py`
2. `.venv/bin/python -m pytest -q tests`
3. коммит и `git push` — сайт обновится сам, а на GitHub при каждом push запускается проверка (`.github/workflows/check.yml`: `gen.py --check`, `build.py --check`, тесты); красная проверка значит, что сгенерированные файлы устарели или в документации есть неверный код
4. если менялся `worker/prompts.js` (почти всегда при правке корней или `tips_short.md`): `cd worker && npx wrangler deploy`

Краткие приёмы кодирования для модели на сайте правятся вручную в `data/site/tips_short.md` (это сокращение `docs/encoding.md`, держите их согласованными).

