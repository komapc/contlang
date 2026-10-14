// Новые коды кодера сайта (база + метки, один смысл) для целей ../three2, у которых есть база (words.json infl). node enc.js → codes.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix);
const T = JSON.parse(fs.readFileSync(path.join(__dirname, "../three2/codes.json"))), out = {};
for (const w of Object.keys(T).sort()) {
  const i = V.index.get(w); if (!V.infl[i]) continue;
  const e = rd.encode(w); out[w] = { old: T[w].A, new: e.code, base: e.lemma, marks: e.marks };
}
fs.writeFileSync(path.join(__dirname, "codes.json"), JSON.stringify(out, null, 0));
console.log(Object.keys(out).length, "слов; код изменился у", Object.values(out).filter((o) => o.old !== o.new).length);
