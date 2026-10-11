// Прокси для демо min-co: держит ключ OpenRouter, вызывает дешёвую модель, ограничивает ввод.
// Развёртывание: см. worker/README.md
import { ENC_SPEC, DEC_SPEC, CHECK } from "./prompts.js";

const DEFAULT_MODEL = "openai/gpt-4o-mini"; // можно сменить переменной MODEL в wrangler.toml
const MAX_INPUT = 300;

const ENCODE_TASK_RU = `
TASK: the user message is ONE English word (possibly with a sense hint in brackets) or a short phrase.
Encode it into min-co using the spec and the encoding tips above, as a single code in the form \`ROOTS | form\` (e.g. \`GRAIN(=0) THING(=-5) PART(=-5) | o\`). Use quotes only as the quote rule in the tips says (names, numbers, Latin/international names of specific species, substances, organs, celestial bodies, games, narrow terms); everything else is built from roots. At most 3 roots (compass words: 4). Every axis value has a sign: \`(=+5)\`, \`(=-2)\`, \`(=0)\`.

How to work (silently, then answer):
1. Paraphrase the meaning and name what separates it from its nearest synonyms.
2. Build the concept from 1-3 roots whose meanings COMBINE into that paraphrase (head root first). Do not pick a root only because the English word feels related to it; read each root by its axis table. Follow the encoding tips for the word's kind (numbers, materials, abstract nouns, ...).
3. Check by decoding: would someone who has only the spec most naturally read your code as a different, more common word? If so, rework it.
4. Confidence: "высокая" only if the decoder would plainly recover this very word; "средняя" if a close synonym; "низкая" if only part of the meaning is kept.
Write axis values as in the spec: \`(=+3)\`, \`(=-2)\`, \`(=0)\`, never \`+0\`.
Reply with ONLY a JSON object, no other text, no markdown fences:
{"idea": "<one-line paraphrase, English>", "code": "<the code>", "tokens": [{"t": "<one root with value, or the form part>", "note": "<короткое пояснение по-русски: какой корень, какое значение оси, какая роль>"}], "confidence": "высокая|средняя|низкая", "confusable": ["<1-2 English words the code could be confused with>"]}`;
const DECODE_TASK_RU = `
TASK: the user message is a min-co code. You have NOT seen the original text.
Decode it into the English word, phrase or sentence it most likely stands for.
Reply with ONLY a JSON object, no other text:
{"best": "<best reading>", "alternatives": ["<alt 1>", "<alt 2>"], "why": "<одна короткая фраза по-русски, как прочитан код>"}`;
// по умолчанию пояснения и уверенность по-английски; lang: "ru" — по-русски
const ENCODE_TASK_EN = ENCODE_TASK_RU.replace('"высокая" only', '"high" only').replace('"средняя" if', '"medium" if').replace('"низкая" if', '"low" if')
  .replace("<короткое пояснение по-русски: какой корень, какое значение оси, какая роль>", "<a short note in English: which root, which axis value, what role>").replace('"высокая|средняя|низкая"', '"high|medium|low"');
const DECODE_TASK_EN = DECODE_TASK_RU.replace("<одна короткая фраза по-русски, как прочитан код>", "<one short sentence in English: how the code was read>");
// второе слово: код уже есть, но слепое прочтение (или векторы) нашли его ближе к другим словам
const SECOND_TASK = (prev, confused) => `
SECOND WORD: your first code for this word was \`${prev}\`, but a reader who has only the spec takes it for: ${confused}.
Rewrite it as a two-word compound \`HEAD | o LINK MODIFIER | o\`: the head is the general kind (keep the first code or fix it), the modifier is ONE more min-co word of 1-3 roots for ANOTHER thing that narrows it, chosen so that the pair cannot be read as ${confused}. LINK is chosen by the LINKS rule of the spec: FROM (made of it), else FOR (made for it), else LIKE (looks like it), else PI (part of it, found or living in it). Do not just repeat or shift the head's roots in the modifier. Each of the two words has its own root limit.
Verified compounds: key = small tool FOR doorway \`DO(=+5) BIG(=-4) | o FOR PART(=-2) PLACE SIDE(=+5) | o\`; sheath = covering FOR blade \`INSIDE(=+5) JOIN(=+5) | o FOR JOIN(=-4) TOUCH(=+4) DO(=+5) | o\`; candle = light FROM wax \`LONG(=0) HEAT(=+5) | o FROM GRAIN(=+5) TOUCH(=-5) | o\`; sunflower = plant LIKE sun \`THING(=0) ABOVE(=+5) | o LIKE ABOVE(=+5) HEAT(=+5) | o\`; furniture = collection of inanimate things PI house \`PART(=+5) THING(=-5) | o PI PLACE INSIDE(=+5) LIVE | o\`.
In "tokens" explain both words; in "confusable" name what the new code could still be confused with.`;
const MSG = {
  en: { busy: "too many requests, wait a minute", need: "mode and text are required", long: (n) => `at most ${n} characters`, down: "the model is unavailable", notJson: "the model did not return JSON" },
  ru: { busy: "слишком много запросов, подождите минуту", need: "mode и text обязательны", long: (n) => `не длиннее ${n} символов`, down: "модель недоступна", notJson: "модель вернула не JSON" },
};

// Проверка кода по правилам языка (как scripts/mincode/validator.py, только главное): корни, лимит, знак значения.
// В паре через связку (FROM, FOR, LIKE, PI) каждое слово проверяется отдельно.
const LINKS = /\b(?:FROM|FOR|LIKE|PI)\b/;
function codeProblems(code) {
  return String(code || "").split(LINKS).flatMap(wordProblems);
}
function wordProblems(word) {
  const body = word.split("|")[0].replace(/"[^"]*"/g, " ").trim();
  if (!body) return [];
  const roots = [], bad = [];
  for (const t of body.split(/\s+/)) {
    const m = t.match(/^([A-Z]+)(?:\(=([+-]?)(\d)\))?$/);
    if (!m) { bad.push(`malformed token ${t}`); continue; }
    if (["PI", "FROM", "FOR", "LIKE", "E", "AND", "LA", "PE", "LI"].includes(m[1])) continue;
    if (!CHECK.roots.includes(m[1])) bad.push(`unknown root ${m[1]}`);
    else roots.push(m[1]);
    if (m[3] && m[3] !== "0" && !m[2]) bad.push(`value without sign in ${t} (write (=+${m[3]}))`);
  }
  const counted = roots.filter((r) => r !== CHECK.extra_root);
  const compass = counted.length === CHECK.compass.length && CHECK.compass.every((r) => counted.includes(r));
  if (counted.length > CHECK.max_roots && !compass) bad.push(`${counted.length} roots, the limit is ${CHECK.max_roots}`);
  return bad;
}

async function ask(env, messages) {
  const r = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: { "authorization": "Bearer " + env.OPENROUTER_API_KEY, "content-type": "application/json", "X-Title": "min-co demo" },
    body: JSON.stringify({ model: env.MODEL || DEFAULT_MODEL, max_tokens: 700, temperature: 0, messages }),
  });
  if (!r.ok) return { error: r.status };
  const data = await r.json();
  const raw = (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || "";
  const m = raw.match(/\{[\s\S]*\}/);
  try { return { raw, obj: JSON.parse(m[0]) }; } catch { return { raw }; }
}

function cors(origin, env) {
  const allowed = (env.ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
  const ok = !allowed.length || allowed.includes(origin) || /^http:\/\/localhost(:\d+)?$/.test(origin || "");
  return {
    "Access-Control-Allow-Origin": ok ? origin || "*" : "null",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "content-type",
    "Vary": "Origin",
  };
}

function json(body, status, headers) {
  return new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json", ...headers } });
}

export default {
  async fetch(req, env) {
    const origin = req.headers.get("Origin");
    const h = cors(origin, env);
    if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: h });
    if (req.method !== "POST") return json({ error: "POST only" }, 405, h);
    if (h["Access-Control-Allow-Origin"] === "null") return json({ error: "origin not allowed" }, 403, h);

    if (env.LIMITER) {
      const ip = req.headers.get("CF-Connecting-IP") || "anon";
      const { success } = await env.LIMITER.limit({ key: ip });
      if (!success) return json({ error: "too many requests, wait a minute / слишком много запросов" }, 429, h);
    }

    let body;
    try { body = await req.json(); } catch { return json({ error: "bad json" }, 400, h); }
    const lang = body.lang === "ru" ? "ru" : "en", t = MSG[lang];
    const mode = body.mode;
    const text = String(body.text || "").trim();
    if (!["encode", "decode"].includes(mode) || !text) return json({ error: t.need }, 400, h);
    if (text.length > MAX_INPUT) return json({ error: t.long(MAX_INPUT) }, 400, h);

    // encode с prev и confused — повторное кодирование со вторым словом
    const prev = mode === "encode" && typeof body.prev === "string" ? body.prev.trim().slice(0, MAX_INPUT) : "";
    const confused = Array.isArray(body.confused) ? body.confused.filter((x) => typeof x === "string").map((x) => x.trim().slice(0, 40)).filter(Boolean).slice(0, 5) : [];
    const system = (mode === "encode" ? ENC_SPEC + (lang === "ru" ? ENCODE_TASK_RU : ENCODE_TASK_EN) + (prev && confused.length ? SECOND_TASK(prev, confused.join(", ")) : "")
      : DEC_SPEC + (lang === "ru" ? DECODE_TASK_RU : DECODE_TASK_EN));
    const messages = [{ role: "system", content: system }, { role: "user", content: text }];
    let a = await ask(env, messages);
    if (a.error) return json({ error: t.down, status: a.error }, 502, h);
    if (mode === "encode" && a.obj) {
      const bad = codeProblems(a.obj.code);
      if (bad.length) {  // одна попытка исправить
        messages.push({ role: "assistant", content: a.raw }, { role: "user", content: `Your code breaks the rules: ${bad.join("; ")}. Fix it and reply with the JSON object only.` });
        const b = await ask(env, messages);
        if (b.obj) a = b;
        const left = codeProblems(a.obj.code);
        if (left.length) a.obj.warnings = left;
      }
    }
    if (!a.obj) return json({ error: t.notJson, raw: a.raw }, 502, h);
    return json(a.obj, 200, h);
  },
};
