// Коды кодера сайта (Reader.encode) для списка слов → {слово: код}; с флагом heads — ещё 8 лучших кодов головы (Coder.top) в той же форме.
//   node enc.js in.json out.json [heads]
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), co = rd.co, out = {};
const [inp, outp, heads] = process.argv.slice(2);
for (const w of JSON.parse(fs.readFileSync(inp))) {
  const e = rd.encode(w); if (!e || e.name) continue;
  if (!heads) { out[w] = e.code; continue; }
  const form = (e.code.match(/\|\s*([oiae])\b/) || [0, "o"])[1], tail = e.code.slice(e.code.indexOf("|") + 1).trim().slice(1);
  out[w] = { code: e.code, top: co.top(V.vec(w), 8, 3, rd.ban(w)).map((b) => co.format(b.S, b.v, form) + tail) };
}
fs.writeFileSync(outp, JSON.stringify(out));
