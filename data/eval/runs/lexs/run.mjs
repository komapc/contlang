// lexs: вызовы gpt-5-mini (dec.md). Код воркера main скопирован в w/ (в конец index.js добавлен только export).
//   OPENROUTER_KEY_FILE=... node run.mjs gen      → cand_G.json   (G1, G2: режим encode воркера, «lemma (pos: gloss)»)
//   OPENROUTER_KEY_FILE=... node run.mjs read     → reads.json    (3 слепых чтения каждого кода-кандидата, пачки по 20)
//   OPENROUTER_KEY_FILE=... node run.mjs judge    → judged.json   (судья 2/1/0 по каждой паре слово — прочтение)
//   OPENROUTER_KEY_FILE=... node run.mjs sent     → sent_codes.json (M0, MG, ML: предложение одним проходом, без словаря / со словарём G1 / с выбранным)
import fs from "node:fs";
import { ask, ENCODE_TASK_EN } from "./w/index.js";
import { ENC_SPEC, DEC_SPEC } from "./w/prompts.js";
import { ENC_SENTS } from "./w/prompts_sent.js";  // спецификация предложений из PR #19

const D = new URL(".", import.meta.url).pathname;
const keyFile = process.env.OPENROUTER_KEY_FILE;
const env = { OPENROUTER_API_KEY: keyFile ? fs.readFileSync(keyFile, "utf8").trim() : process.env.OPENROUTER_API_KEY, MODEL: "openai/gpt-5-mini" };
const J = (f) => JSON.parse(fs.readFileSync(`${D}/${f}`)); const W = (f, x) => fs.writeFileSync(`${D}/${f}`, JSON.stringify(x, null, 1));
const tryAsk = (ms) => ask(env, ms).catch(() => ({ error: "network" }));
async function pool(items, n, fn) {
  const out = new Array(items.length); let k = 0, done = 0;
  await Promise.all(Array.from({ length: n }, async () => { while (k < items.length) { const i = k++; out[i] = await fn(items[i], i); if (++done % 50 === 0) process.stdout.write(`${done} `); } }));
  return out;
}
async function retry(fn, ok) { let r; for (let t = 0; t < 3; t++) { r = await fn(); if (ok(r)) return r; } return r; }
const probe = await tryAsk([{ role: "user", content: "Reply with {\"ok\": 1}" }]);
if (probe.error) { console.error("OpenRouter:", probe.error); process.exit(1); }
const shuffle = (a, seed) => { let s = seed; const r = () => (s = (s * 16807) % 2147483647) / 2147483647; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(r() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const item = (x) => `${x.lemma} (${x.pos}: ${x.gloss})`;

const READ = `
TASK: the user message has numbered lines; each line is ONE min-co word that stands for one common English word. You have NOT seen the words. For each line give your best English reading (one word).
Reply with ONLY a JSON object: {"answers": ["<reading of line 1>", "<reading of line 2>", ...]} with exactly as many answers as lines.`;
const JUDGE = `Each numbered line is "N. TARGET — ANSWER": TARGET is an English word with its part of speech and sense, ANSWER is a guess made by someone who did not see it.
Score how close the ANSWER is in meaning to TARGET:
2 — close: the same meaning or a near synonym (same semantic field, could stand in for it in most contexts; another part of speech of the same word counts);
1 — related: clearly connected (same topic, part/whole, a broader or narrower notion), but not the same thing;
0 — off: unrelated or only loosely associated.
Judge meaning only, not spelling or form.
Reply with ONLY a JSON object: {"scores": [<score of line 1>, <score of line 2>, ...]} with exactly as many scores as lines.`;
const SENT_ENCODE = `
TASK: the user message is ONE English sentence. Translate it into min-co as one line, following the Sentences section: every word inside its own braces \`{ ROOTS | FORM marks }\`, particles (E, AND, LA, [ ], ;) between words, proper names in quotes. A different person will decode it WITHOUT seeing the English: choose roots, roles and marks so that each word reads back as meant. Small grammar words become marks (not → M-5, very → I+4, more → C+3, past → T-2, will → T+2, plural → N+3, the → D+3, passive → V-4). Every axis value has a sign.
Reply with ONLY a JSON object: {"code": "<the code>"}`;  // как SENT_ENCODE в PR #19 (../mini/w/index.js)
const GLOSS = (g) => `
GLOSSARY: verified min-co words for some words of this sentence (base forms). Use them for these words, adding the marks the sentence needs (tense, number, negation, ...):
${g}`;

async function batched(lines, size, sys, field, seed) {  // пачки по size строк → массив ответов той же длины
  const out = []; const chunks = [];
  for (let i = 0; i < lines.length; i += size) chunks.push(lines.slice(i, i + size));
  const res = await pool(chunks, 8, (ch) => retry(() => tryAsk([{ role: "system", content: sys }, { role: "user", content: ch.map((x, k) => `${k + 1}. ${x}`).join("\n") }]),
    (a) => a.obj && Array.isArray(a.obj[field]) && a.obj[field].length === ch.length));
  res.forEach((a, k) => { const arr = a.obj && Array.isArray(a.obj[field]) && a.obj[field].length === chunks[k].length ? a.obj[field] : chunks[k].map(() => null); out.push(...arr); });
  return out;
}

const cmd = process.argv[2];
if (cmd === "gen") {
  const L = J("lemmas.json"); const jobs = L.flatMap((x, i) => ["G1", "G2"].map((v) => ({ i, v })));
  const res = await pool(jobs, 8, (j) => retry(() => tryAsk([{ role: "system", content: ENC_SPEC + ENCODE_TASK_EN }, { role: "user", content: item(L[j.i]) }]), (a) => a.obj && a.obj.code));
  const out = { G1: [], G2: [] }; jobs.forEach((j, k) => { out[j.v][j.i] = res[k].obj ? String(res[k].obj.code || "") : ""; });
  W("cand_G.json", out); console.log("\nпустых:", jobs.filter((j, k) => !res[k].obj).length);
} else if (cmd === "read") {
  const C = J("cands.json"); const out = {};
  for (const [v, codes] of Object.entries(C)) for (const rep of [1, 2, 3]) {
    const order = shuffle([...codes.keys()], 1000 * rep + v.charCodeAt(0) + v.charCodeAt(1));
    const ans = await batched(order.map((i) => codes[i]), 20, DEC_SPEC + READ, "answers", rep);
    out[`${v}/${rep}`] = []; order.forEach((i, k) => { out[`${v}/${rep}`][i] = ans[k] == null ? "" : String(ans[k]); });
    console.log(v, rep, "пустых:", ans.filter((a) => a == null).length);
  }
  W("reads.json", out);
} else if (cmd === "judge") {
  const L = J("lemmas.json"), R = J("reads.json"); const keys = new Map();
  for (const ans of Object.values(R)) ans.forEach((a, i) => keys.set(`${i}\t${a.toLowerCase().trim()}`, [i, a.toLowerCase().trim()]));
  const P = shuffle([...keys.values()], 7);
  const sc = await batched(P.map(([i, a]) => `${item(L[i])} — ${a || "—"}`), 40, JUDGE, "scores", 7);
  const out = {}; P.forEach(([i, a], k) => { out[`${i}\t${a}`] = sc[k]; }); W("judged.json", out);
  console.log("пар:", P.length, "без оценки:", sc.filter((x) => x == null).length);
} else if (cmd === "sent") {
  const S = J("sents.json"), L = J("lemmas.json"), C = J("cands.json"), pick = J("pick.json");
  const gl = (n, v) => L.map((x, i) => [x, i]).filter(([x]) => x.sents.includes(n)).map(([x, i]) => `${x.lemma} (${x.pos}) = ${v === "G" ? C.G1[i] : C[pick[i]][i]}`).join("\n");
  const jobs = S.flatMap((s, n) => [["M0", ""], ["MG", GLOSS(gl(n, "G"))], ["ML", GLOSS(gl(n, "L"))]].map(([v, g]) => ({ n, v, sys: ENC_SENTS + SENT_ENCODE + g, s: s.s })));
  const res = await pool(jobs, 8, (j) => retry(() => tryAsk([{ role: "system", content: j.sys }, { role: "user", content: j.s }]), (a) => a.obj && typeof a.obj.code === "string"));
  const out = { M0: [], MG: [], ML: [] }; jobs.forEach((j, k) => { out[j.v][j.n] = res[k].obj ? String(res[k].obj.code) : ""; });
  W("sent_codes.json", out); console.log("\nсбоев:", jobs.filter((j, k) => !res[k].obj).length);
}
