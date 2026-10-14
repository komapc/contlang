// Кандидаты кодов кодера сайта для слов: та же база, форма, метки, роль и вектор смысла, что у Reader.encode,
// но K лучших по cos наборов корней (Coder.top, topr 12).   node cand.js words.json K → cand.json {w: {site, cands: [...]}}
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), co = new MM.Coder(m.dict, m.has_axis, m.names, { ...m, topr: 12 });
const words = JSON.parse(fs.readFileSync(process.argv[2])), K = +process.argv[3] || 60, out = {};
for (const w of words) {
  const e = rd.encode(w); if (!e || e.name) continue;
  const b = e.lemma || w, fo = e.form || "o", x = V.senseVec(b, fo), tail = e.code.slice(e.code.indexOf("|") + 1).trim();
  const cands = co.top(x, K, 3, rd.ban(b)).map((t) => co.format(t.S, t.v, fo).replace(/\|.*$/, "| " + tail));
  out[w] = { site: e.code, base: b, form: fo, cands: [...new Set([e.code, ...cands])] };
}
fs.writeFileSync(process.argv[4] || path.join(__dirname, "cand.json"), JSON.stringify(out));
console.log(Object.keys(out).length, "слов");
