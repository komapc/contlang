# Прокси для демо-страницы

Страница на GitHub Pages статическая и не может хранить ключ. Эта функция Cloudflare Workers держит ключ Anthropic, вызывает `claude-haiku-4-5` (самую дешёвую модель), ограничивает ввод 300 символами и 10 запросами в минуту с адреса.

Развёртывание (один раз):

1. `cd worker && npm i -g wrangler && wrangler login`
2. `wrangler secret put ANTHROPIC_API_KEY` (ключ вводится в терминале, в репозиторий не попадает)
3. при другом адресе страницы поправьте `ALLOWED_ORIGINS` в `wrangler.toml`
4. `wrangler deploy` — выведет адрес вида `https://minco-demo.<аккаунт>.workers.dev`
5. вставьте этот адрес в `site/config.js` (`MINCO_API`)

`prompts.js` генерируется: `python3 scripts/site/build.py` (из `roots.yaml` и шаблонов спецификаций). Задайте в панели Anthropic лимит расхода на ключ — это последняя защита от злоупотреблений.
