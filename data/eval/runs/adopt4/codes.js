// Кодер сайта (site/math.js Reader.encode, как на странице «Проба») со словарём сайта и с добавленным LAND (../adopt3/dict45.npz → land.json).
//   node codes.js pool.json → codes.json {word: [old, new]}
const fs = require("fs"), path = require("path"), REPO = path.resolve(__dirname, "../../../.."), SITE = path.join(REPO, "site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const L = JSON.parse(fs.readFileSync(path.join(__dirname, "land.json")));
const m2 = { ...m, names: [...m.names, "LAND"], has_axis: [...m.has_axis, true], dict: { C: [...m.dict.C, L.C], A: [...m.dict.A, L.A] } };
const mk = (mm) => new MM.Reader(new MM.Coder(mm.dict, mm.has_axis, mm.names, mm), V, mm.mix);
const r1 = mk(m), r2 = mk(m2), out = {};
for (const w of JSON.parse(fs.readFileSync(process.argv[2]))) if (V.index.has(w)) out[w] = [r1.encode(w), r2.encode(w)].map((e) => (typeof e === "string" ? e : e.code));
fs.writeFileSync(process.argv[3] || path.join(__dirname, "codes.json"), JSON.stringify(out, null, 0));
const ch = Object.values(out).filter(([a, b]) => a !== b); console.log("слов", Object.keys(out).length, "изменилось", ch.length, "с LAND", ch.filter(([, b]) => /LAND/.test(b)).length);
