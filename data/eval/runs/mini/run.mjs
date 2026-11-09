// mini: конвейер PR #19 (режим sentence) на модели воркера (gpt-5-mini) — dec.md.
// Код воркера из ветки worker-sent скопирован в w/ без изменений (в конец index.js добавлен только export).
//   OPENROUTER_API_KEY=... node run.mjs encode   → enc.json  (first = один проход M0, code = после чтения и правки MV)
//   OPENROUTER_API_KEY=... node run.mjs decode   → dec_gpt.json (gpt-5-mini читает M0 и MV, как режим decode воркера)
import fs from "node:fs";
import { encodeSentence, ask, DECODE_TASK_EN } from "./w/index.js";
import { DEC_SENTS } from "./w/prompts.js";

const D = new URL(".", import.meta.url).pathname;
// ключ: переменная OPENROUTER_API_KEY или файл вне репозитория из OPENROUTER_KEY_FILE
const keyFile = process.env.OPENROUTER_KEY_FILE;
const env = { OPENROUTER_API_KEY: process.env.OPENROUTER_API_KEY || (keyFile ? fs.readFileSync(keyFile, "utf8").trim() : ""), MODEL: "openai/gpt-5-mini" };
if (!env.OPENROUTER_API_KEY) { console.error("нужен OPENROUTER_API_KEY"); process.exit(1); }
const SN = JSON.parse(fs.readFileSync(`${D}/../pipe/sents.json`)).holdout.map((x) => x.s);
const tryAsk = (ms) => ask(env, ms).catch(() => ({ error: "network" }));

async function pool(items, n, fn) {  // n запросов одновременно
  const out = new Array(items.length); let k = 0;
  await Promise.all(Array.from({ length: n }, async () => { while (k < items.length) { const i = k++; out[i] = await fn(items[i], i); } }));
  return out;
}
async function retry(fn, bad) {  // до 3 попыток на сбой сети / не JSON
  let r; for (let t = 0; t < 3; t++) { r = await fn(); if (!bad(r)) return r; } return r;
}

const probe = await tryAsk([{ role: "user", content: "Reply with {\"ok\": 1}" }]);
if (probe.error) { console.error("OpenRouter отвечает ошибкой", probe.error, probe.error === 401 ? "— неверный ключ" : ""); process.exit(1); }
const cmd = process.argv[2];
if (cmd === "encode") {
  const out = await pool(SN, 4, async (s, i) => {
    const r = await retry(() => encodeSentence(tryAsk, s, false), (r) => r.error);
    process.stdout.write(`${i + 1}${r.error ? "!" : ""} `); return { i, ...r };
  });
  fs.writeFileSync(`${D}/enc.json`, JSON.stringify(out, null, 1)); console.log("\nошибок:", out.filter((r) => r.error).length);
} else if (cmd === "decode") {
  const E = JSON.parse(fs.readFileSync(`${D}/enc.json`)); const jobs = [];
  for (const e of E) for (const [v, c] of [["M0", e.first], ["MV", e.code]]) jobs.push({ i: e.i, v, c });
  const out = await pool(jobs, 4, async (j) => {
    const a = await retry(() => tryAsk([{ role: "system", content: DEC_SENTS + DECODE_TASK_EN }, { role: "user", content: j.c || "" }]), (a) => a.error || !a.obj);
    return { i: j.i, v: j.v, best: a.obj ? String(a.obj.best || "") : "" };
  });
  fs.writeFileSync(`${D}/dec_gpt.json`, JSON.stringify(out, null, 1)); console.log("пустых:", out.filter((o) => !o.best).length);
}
