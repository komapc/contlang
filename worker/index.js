// Прокси для демо min-co: держит ключ OpenRouter, вызывает дешёвую модель, ограничивает ввод.
// Развёртывание: см. worker/README.md
import { ENC_SPEC, DEC_SPEC } from "./prompts.js";

const DEFAULT_MODEL = "openai/gpt-4o-mini"; // можно сменить переменной MODEL в wrangler.toml
const MAX_INPUT = 300;

const ENCODE_TASK = `
TASK: the user message is ONE English word (possibly with a sense hint in brackets) or one short sentence.
Encode it into min-co using the spec above, as a single code (use ';' only for several clauses). Remember: ordinary English words are never quoted; express them with roots.

How to work (follow in order, silently, then answer):
1. Paraphrase the meaning in plain words and name what separates it from its nearest synonyms (the shade of meaning to keep).
2. Build the concept from 1-3 roots whose meanings COMBINE into that paraphrase: the head root carries the core, modifiers and axis values narrow it down. Do not pick a root only because the English word sounds or feels related to it. Read each root by its axis table, not by its name: e.g. a root that names a domain (TIME, PLACE, THING) is right only if the word is about that thing itself, not merely about something that lasts, happens or exists somewhere.
3. Check by decoding: read your code the way someone who has only the spec would. If it would most naturally come back as a different, more common word, change the code.
4. Confidence: "высокая" only if the decoder would plainly recover this very word; "средняя" if it recovers a close synonym; "низкая" if the concept needs a guess or only part of the meaning is kept. A single bare root for an abstract word is rarely "высокая". List in "confusable" the words the code is most likely to be read as.
Reply with ONLY a JSON object, no other text, no markdown fences:
{"idea": "<one-line paraphrase of the meaning, English>", "code": "<the code>", "tokens": [{"t": "<one token or phrase of the code>", "note": "<короткое пояснение по-русски: какой корень, какое значение оси, какая роль>"}], "confidence": "высокая|средняя|низкая", "confusable": ["<1-2 English words the code could be confused with>"]}`;
const DECODE_TASK = `
TASK: the user message is a min-co code. You have NOT seen the original text.
Decode it into the English word, phrase or sentence it most likely stands for.
Reply with ONLY a JSON object, no other text:
{"best": "<best reading>", "alternatives": ["<alt 1>", "<alt 2>"], "why": "<одна короткая фраза по-русски, как прочитан код>"}`;

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
      if (!success) return json({ error: "слишком много запросов, подождите минуту" }, 429, h);
    }

    let body;
    try { body = await req.json(); } catch { return json({ error: "bad json" }, 400, h); }
    const mode = body.mode;
    const text = String(body.text || "").trim();
    if (!["encode", "decode"].includes(mode) || !text) return json({ error: "mode и text обязательны" }, 400, h);
    if (text.length > MAX_INPUT) return json({ error: `не длиннее ${MAX_INPUT} символов` }, 400, h);

    const system = (mode === "encode" ? ENC_SPEC + ENCODE_TASK : DEC_SPEC + DECODE_TASK);
    const r = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: { "authorization": "Bearer " + env.OPENROUTER_API_KEY, "content-type": "application/json", "X-Title": "min-co demo" },
      body: JSON.stringify({ model: env.MODEL || DEFAULT_MODEL, max_tokens: 700, temperature: 0, messages: [{ role: "system", content: system }, { role: "user", content: text }] }),
    });
    if (!r.ok) return json({ error: "модель недоступна", status: r.status }, 502, h);
    const data = await r.json();
    const raw = (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || "";
    const m = raw.match(/\{[\s\S]*\}/);
    if (!m) return json({ error: "модель вернула не JSON", raw }, 502, h);
    try { return json(JSON.parse(m[0]), 200, h); } catch { return json({ error: "не удалось разобрать ответ", raw }, 502, h); }
  },
};
