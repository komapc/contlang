// Кодер сайта (site/math.js Reader.encode, как на странице «Проба») для списка слов.  node site.js in.json out.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), out = {};
for (const w of JSON.parse(fs.readFileSync(process.argv[2]))) { const e = rd.encode(w); out[w] = e ? (typeof e === "string" ? e : e.code) : null; }
fs.writeFileSync(process.argv[3], JSON.stringify(out));
