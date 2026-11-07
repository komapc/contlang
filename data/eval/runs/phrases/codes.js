// Коды трёх вариантов для items.json (dec.md), всё — математика сайта (site/math.js, параметры по умолчанию):
// A — пословно: код сайта каждого слова (Reader.encode), порядок min-co — главное первым (у имён второе английское слово);
// B — один код из вектора фразы Numberbatch (vecs.json), часть речи фразы (o имя, i глагол);
// C — один код из среднего векторов двух слов (сложение без словаря фраз).
// SEX запрещён, если его запрещает сайт обоим словам (как Reader.ban).   node data/eval/runs/phrases/codes.js
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const items = JSON.parse(fs.readFileSync(path.join(__dirname, "items.json"))), vecs = JSON.parse(fs.readFileSync(path.join(__dirname, "vecs.json")));
const one = (x, ws, pos) => { const ban = ws.every((w) => rd.ban(w).length) ? rd.ban(ws[0]) : []; const e = co.encode(Float64Array.from(x), 3, ban); return co.format(e.S, e.v, pos === "v" ? "i" : "o"); };
const out = {};
for (const it of items) {
  const ws = it.phrase.split(" ");
  out[it.phrase] = { A: (it.pos === "n" ? [ws[1], ws[0]] : ws).map((w) => rd.encode(w).code).join(" "), B: one(vecs[it.phrase].B, ws, it.pos), C: one(vecs[it.phrase].C, ws, it.pos) };
}
fs.writeFileSync(path.join(__dirname, "codes.json"), JSON.stringify(out, null, 0));
for (const [p, c] of Object.entries(out)) console.log(p.padEnd(18), "|", c.A, "||", c.B, "||", c.C);
