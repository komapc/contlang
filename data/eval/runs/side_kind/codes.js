// Коды кодера сайта (Reader.encode, текущий site/math.js): как есть, без корня SIDE (запрет корня всем словам) и с KIND (../kind/kind.json).
//   node codes.js side|kind in.json out.json → {word: {cur, noside}} (noside — только у кодов с SIDE) или {word: {cur, kind}}
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const K = JSON.parse(fs.readFileSync(path.join(__dirname, "../kind/kind.json")));
const m2 = { ...m, names: [...m.names, "KIND"], has_axis: [...m.has_axis, true], dict: { C: [...m.dict.C, K.C], A: [...m.dict.A, K.A] } };
const mk = (mm) => new MM.Reader(new MM.Coder(mm.dict, mm.has_axis, mm.names, mm), V, mm.mix);
const cur = mk(m), kind = mk(m2), noside = mk(m), si = m.names.indexOf("SIDE"), ban0 = noside.ban.bind(noside);
noside.ban = (w) => [...ban0(w), si];
const code = (r, w) => { const e = r.encode(w); return e ? e.code : null; }, out = {};
const [mode, inp, outp] = process.argv.slice(2);
for (const w of JSON.parse(fs.readFileSync(inp))) {
  const c = code(cur, w); out[w] = { cur: c };
  if (mode === "side" && c && /\bSIDE\b/.test(c)) out[w].noside = code(noside, w);
  if (mode === "kind") out[w].kind = code(kind, w);
}
fs.writeFileSync(outp, JSON.stringify(out));
