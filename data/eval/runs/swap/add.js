// Шаг 1: кодер сайта с одним новым корнем (atoms/NAME.json) на словах in.json: код и место слова при чтении векторами.  node add.js NAME in.json out.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const [N, inp, outp] = process.argv.slice(2), K = JSON.parse(fs.readFileSync(path.join(__dirname, "atoms", N + ".json")));
const m2 = { ...m, names: [...m.names, N], has_axis: [...m.has_axis, true], dict: { C: [...m.dict.C, K.C], A: [...m.dict.A, K.A] } };
const rd = new MM.Reader(new MM.Coder(m2.dict, m2.has_axis, m2.names, m2), V, m2.mix), out = {};
for (const w of JSON.parse(fs.readFileSync(inp))) { const e = rd.encode(w); if (e && !e.name) out[w] = { code: e.code, rank: e.rank }; }
fs.writeFileSync(outp, JSON.stringify(out));
