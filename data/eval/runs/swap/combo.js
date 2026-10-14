// Шаг 2: кодер сайта с набором новых корней (atoms/*.json) и запретом удаляемых.  node combo.js ADD1,ADD2 DEL1,DEL2 in.json out.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const [add, del, inp, outp] = process.argv.slice(2), A = add ? add.split(",") : [], Dl = del ? del.split(",") : [];
const at = A.map((n) => JSON.parse(fs.readFileSync(path.join(__dirname, "atoms", n + ".json"))));
const m2 = { ...m, names: [...m.names, ...A], has_axis: [...m.has_axis, ...A.map(() => true)], dict: { C: [...m.dict.C, ...at.map((a) => a.C)], A: [...m.dict.A, ...at.map((a) => a.A)] } };
const rd = new MM.Reader(new MM.Coder(m2.dict, m2.has_axis, m2.names, m2), V, m2.mix), ban0 = rd.ban.bind(rd), bi = Dl.map((n) => m2.names.indexOf(n));
rd.ban = (w) => [...ban0(w), ...bi]; const out = {};
for (const w of JSON.parse(fs.readFileSync(inp))) { const e = rd.encode(w); if (e && !e.name) out[w] = { code: e.code, rank: e.rank }; }
fs.writeFileSync(outp, JSON.stringify(out));
