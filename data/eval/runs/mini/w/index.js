// Прокси для демо min-co: держит ключ OpenRouter, вызывает дешёвую модель, ограничивает ввод.
// Развёртывание: см. worker/README.md
import { ENC_SPEC, DEC_SPEC, ENC_SENTS, DEC_SENTS } from "./prompts.js";
import { codeProblems, sentenceProblems } from "./check.js";

const DEFAULT_MODEL = "openai/gpt-5-mini"; // можно сменить переменной MODEL в wrangler.toml
const MAX_INPUT = 300;
const MAX_CODE = 1500;  // код предложения длиннее самого предложения

// Режим sentence — кодировщик предложений по data/eval/runs/pipe (слепой тест, holdout +0,44 из 3 к одному проходу):
// [упростить] → закодировать → прочитать вслепую (без исходного предложения) → исправить то, что прочитано не так.
const SENT_SIMPLIFY = `
TASK (pass 1: simplify): the user message is ONE English sentence. It will be translated into min-co (spec above, for reference only — do NOT write min-co now). Rewrite it in plain, simple English that keeps its full meaning: keep who does what to whom, negation, tense, quantity, degree and names; replace idioms and metaphors by their literal meaning; prefer common basic words; split a long sentence into short clauses; make subjects and objects explicit; drop words that add nothing.
Reply with ONLY a JSON object: {"simple": "<the simplified sentence>"}`;
const SENT_ENCODE = `
TASK: the user message is ONE English sentence. Translate it into min-co as one line, following the Sentences section: every word inside its own braces \`{ ROOTS | FORM marks }\`, particles (E, AND, LA, [ ], ;) between words, proper names in quotes. A different person will decode it WITHOUT seeing the English: choose roots, roles and marks so that each word reads back as meant. Small grammar words become marks (not → M-5, very → I+4, more → C+3, past → T-2, will → T+2, plural → N+3, the → D+3, passive → V-4). Every axis value has a sign.
Reply with ONLY a JSON object: {"code": "<the code>"}`;
const SENT_READ = `
TASK: the user message is one English sentence written in min-co. You have NOT seen the original. First give the meaning of every braced word on its own, in order (a word or two each), then ONE fluent English sentence that combines them.
Reply with ONLY a JSON object: {"words": ["<meaning of word 1>", "..."], "sentence": "<the sentence>"}`;
const SENT_REVISE = `
TASK (revision): the user message has the INTENDED English sentence, the min-co CODE written for it, and how a reader who saw only the CODE and the spec read it (each word, then the whole sentence). Revise the code so that it would be read as intended: keep every word that was read right; change the roots, values or marks of a misread word, or split it into two words, or merge two words; fix the particles if the roles were misread.
Reply with ONLY a JSON object: {"code": "<the revised code>"}`;

const ENCODE_TASK_RU = `
TASK: the user message is ONE English word (possibly with a sense hint in brackets) or a short phrase.
Encode it into min-co using the spec and the encoding tips above, as a single code in the form \`ROOTS | form\` (e.g. \`GRAIN(=0) THING(=-5) PART(=-5) | o\`). Quotes only for proper names, digits and scientific names of particular species or substances; everything else is built from roots. At most 3 roots. For a doer, tool, result or quality write the role after \`| o\` (\`TEXT | o tool\` = pen). Every axis value has a sign: \`(=+5)\`, \`(=-2)\`, \`(=0)\`.

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
Verified compounds: key = small tool FOR doorway \`BIG(=-4) | o tool FOR PART(=-2) PLACE SIDE(=+5) | o\`; sheath = covering FOR blade \`INSIDE(=+5) JOIN(=+5) | o FOR JOIN(=-4) TOUCH(=+4) | o tool\`; candle = light FROM wax \`LONG(=0) HEAT(=+5) | o FROM GRAIN(=+5) TOUCH(=-5) | o\`; sunflower = plant LIKE sun \`THING(=0) ABOVE(=+5) | o LIKE ABOVE(=+5) HEAT(=+5) | o\`; furniture = collection of inanimate things PI house \`PART(=+5) THING(=-5) | o PI PLACE INSIDE(=+5) LIVE | o\`.
In "tokens" explain both words; in "confusable" name what the new code could still be confused with.`;
// Ключ лимита на адрес. Клиенту IPv6 выдают целую сеть /64, поэтому считается сеть,
// а не адрес: иначе смена адреса обходит лимит.
function limitKey(ip) {
  if (!ip) return "anon";
  if (!ip.includes(":")) return ip;
  const [head, tail] = ip.split("::");
  const left = head ? head.split(":") : [];
  const right = tail ? tail.split(":") : [];
  const zeros = ip.includes("::") ? Array(Math.max(0, 8 - left.length - right.length)).fill("0") : [];
  return [...left, ...zeros, ...right].slice(0, 4).map((part) => part.toLowerCase().replace(/^0+(?=.)/, "")).join(":");
}

// Поля ответа, которые читает страница: остальное не отдаём, чтобы это не был открытый доступ к модели.
const REPLY_FIELDS = ["idea", "code", "tokens", "confidence", "confusable", "warnings", "best", "alternatives", "why", "simple", "first", "readback"];
const replyOf = (obj) => Object.fromEntries(REPLY_FIELDS.filter((key) => key in obj).map((key) => [key, obj[key]]));

const MSG = {
  en: { busy: "too many requests, wait a minute", need: "mode and text are required", long: (n) => `at most ${n} characters`, down: "the model is unavailable", notJson: "the model did not return JSON" },
  ru: { busy: "слишком много запросов, подождите минуту", need: "mode и text обязательны", long: (n) => `не длиннее ${n} символов`, down: "модель недоступна", notJson: "модель вернула не JSON" },
};

async function ask(env, messages) {
  const r = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: { "authorization": "Bearer " + env.OPENROUTER_API_KEY, "content-type": "application/json", "X-Title": "min-co demo" },
    body: JSON.stringify({ model: env.MODEL || DEFAULT_MODEL, max_tokens: 2000, reasoning: { effort: "low" }, messages }),
  });
  if (!r.ok) return { error: r.status };
  const data = await r.json().catch(() => ({}));
  const raw = (data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || "";
  const m = raw.match(/\{[\s\S]*\}/);
  try { return { raw, obj: JSON.parse(m[0]) }; } catch { return { raw }; }
}

// Код предложения с одной попыткой исправить нарушения правил; null — модель не ответила JSON с кодом.
async function sentenceCode(tryAsk, messages) {
  let a = await tryAsk(messages);
  if (a.error) return { error: a.error };
  if (!a.obj || typeof a.obj.code !== "string") return { error: "json" };
  const bad = sentenceProblems(a.obj.code);
  if (bad.length) {
    messages.push({ role: "assistant", content: a.raw }, { role: "user", content: `Your code breaks the rules: ${bad.slice(0, 8).join("; ")}. Fix it and reply with the JSON object only.` });
    const b = await tryAsk(messages);
    if (b.obj && typeof b.obj.code === "string") a = b;
  }
  return { code: a.obj.code, problems: sentenceProblems(a.obj.code) };
}

async function encodeSentence(tryAsk, text, simplify) {
  let intended = text, simple;
  if (simplify) {
    const s = await tryAsk([{ role: "system", content: ENC_SENTS + SENT_SIMPLIFY }, { role: "user", content: text }]);
    if (s.obj && typeof s.obj.simple === "string" && s.obj.simple.trim()) intended = simple = s.obj.simple.trim().slice(0, 600);
  }
  const first = await sentenceCode(tryAsk, [{ role: "system", content: ENC_SENTS + SENT_ENCODE }, { role: "user", content: intended }]);
  if (first.error) return first;
  // слепое чтение: читатель видит только спецификацию и код
  const rd = await tryAsk([{ role: "system", content: DEC_SENTS + SENT_READ }, { role: "user", content: first.code }]);
  const ok = rd.obj && typeof rd.obj.sentence === "string";
  const readback = ok ? { words: (Array.isArray(rd.obj.words) ? rd.obj.words : []).map(String).slice(0, 40), sentence: rd.obj.sentence } : null;
  let code = first.code, problems = first.problems;
  if (readback) {
    const msg = `INTENDED: ${intended}\nCODE: ${first.code}\nREAD AS: ${readback.words.join(" / ")} => ${readback.sentence}`;
    const rev = await sentenceCode(tryAsk, [{ role: "system", content: ENC_SENTS + SENT_REVISE }, { role: "user", content: msg }]);
    // правка не хуже по правилам — берём её; иначе остаётся первый код
    if (!rev.error && rev.problems.length <= first.problems.length) ({ code, problems } = rev);
  }
  const out = { code, first: first.code, readback };
  if (simple) out.simple = simple;
  if (problems.length) out.warnings = problems;
  return out;
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

    // Без лимитов ключ оплачивает кто угодно, поэтому без них запросы не принимаются.
    if (!env.LIMITER || !env.GLOBAL_LIMITER) return json({ error: "limits are not configured" }, 503, h);
    for (const [limiter, key] of [[env.LIMITER, limitKey(req.headers.get("CF-Connecting-IP"))], [env.GLOBAL_LIMITER, "all"]]) {
      const { success } = await limiter.limit({ key });
      if (!success) return json({ error: "too many requests, wait a minute / слишком много запросов" }, 429, h);
    }

    if (Number(req.headers.get("content-length") || 0) > 4096) return json({ error: "body too large" }, 413, h);
    let body;
    try { body = await req.json(); } catch { return json({ error: "bad json" }, 400, h); }
    if (!body || typeof body !== "object" || Array.isArray(body)) return json({ error: "bad json" }, 400, h);
    const lang = body.lang === "ru" ? "ru" : "en", t = MSG[lang];
    const mode = body.mode;
    const text = String(body.text || "").trim();
    if (!["encode", "decode", "sentence"].includes(mode) || !text) return json({ error: t.need }, 400, h);
    const max = mode === "decode" && text.includes("{") ? MAX_CODE : MAX_INPUT;
    if (text.length > max) return json({ error: t.long(max) }, 400, h);
    const tryAsk = (ms) => ask(env, ms).catch(() => ({ error: "network" }));

    if (mode === "sentence") {
      const r = await encodeSentence(tryAsk, text, body.simplify === true);
      if (r.error) return json({ error: r.error === "json" ? t.notJson : t.down, status: r.error }, 502, h);
      return json(replyOf(r), 200, h);
    }
    if (mode === "decode" && text.includes("{")) {  // код предложения: слова в { }
      const a = await tryAsk([{ role: "system", content: DEC_SENTS + (lang === "ru" ? DECODE_TASK_RU : DECODE_TASK_EN) }, { role: "user", content: text }]);
      if (a.error) return json({ error: t.down, status: a.error }, 502, h);
      if (!a.obj) return json({ error: t.notJson }, 502, h);
      return json(replyOf(a.obj), 200, h);
    }

    // encode с prev и confused — повторное кодирование со вторым словом
    // prev и confused идут в системный промпт: только код по правилам и английские слова
    let prev = mode === "encode" && typeof body.prev === "string" ? body.prev.trim().slice(0, MAX_INPUT) : "";
    if (!/^[A-Za-z0-9 ()=+|"'-]*$/.test(prev) || codeProblems(prev).length) prev = "";
    const confused = Array.isArray(body.confused) ? body.confused.filter((x) => typeof x === "string").map((x) => x.trim().slice(0, 40)).filter((x) => /^[A-Za-z' -]+$/.test(x)).slice(0, 5) : [];
    const system = (mode === "encode" ? ENC_SPEC + (lang === "ru" ? ENCODE_TASK_RU : ENCODE_TASK_EN) + (prev && confused.length ? SECOND_TASK(prev, confused.join(", ")) : "")
      : DEC_SPEC + (lang === "ru" ? DECODE_TASK_RU : DECODE_TASK_EN));
    const messages = [{ role: "system", content: system }, { role: "user", content: text }];
    // сбой сети или ответ не JSON — 502 с заголовками CORS, а не 500 без них
    let a = await tryAsk(messages);
    if (a.error) return json({ error: t.down, status: a.error }, 502, h);
    if (mode === "encode" && a.obj) {
      const bad = codeProblems(a.obj.code);
      if (bad.length) {  // одна попытка исправить
        messages.push({ role: "assistant", content: a.raw }, { role: "user", content: `Your code breaks the rules: ${bad.join("; ")}. Fix it and reply with the JSON object only.` });
        const b = await tryAsk(messages);
        if (b.obj) a = b;
        const left = codeProblems(a.obj.code);
        if (left.length) a.obj.warnings = left;
      }
    }
    if (!a.obj) return json({ error: t.notJson }, 502, h);
    return json(replyOf(a.obj), 200, h);
  },
};

// для eval: те же функции, что в PR #19
export { encodeSentence, ask, DECODE_TASK_EN };
