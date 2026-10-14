// Кодер сайта (Reader.encode) без KIND и с KIND (kind.json).  node codes.js in.json out.json → {word: [old, new]};  node codes.js --pool → pool.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const K = JSON.parse(fs.readFileSync(path.join(__dirname, "kind.json")));
if (process.argv[2] === "--pool") {  // 300 знаменательных слов из первых 10 000, ближайших к атому KIND при −5, 0 или +5, + слова ../big1000
  const big = JSON.parse(fs.readFileSync(path.join(__dirname, "../big1000/words.json"))), bad = new Set([...meta.stop, ...meta.proper]), near = new Set();
  for (const v of [-5, 0, 5]) { const x = K.C.map((c, j) => c + m.s * v * K.A[j]); V.near(x, 400).filter((w) => V.index.get(w) < 10000 && !bad.has(V.index.get(w)) && /^[a-z]{3,}$/.test(w)).slice(0, 100).forEach((w) => near.add(w)); }
  const pool = [...near].filter((w) => !big.includes(w)); fs.writeFileSync(path.join(__dirname, "pool.json"), JSON.stringify({ near: pool, big })); console.log(pool.length); process.exit();
}
const m2 = { ...m, names: [...m.names, "KIND"], has_axis: [...m.has_axis, true], dict: { C: [...m.dict.C, K.C], A: [...m.dict.A, K.A] } };
const mk = (mm) => new MM.Reader(new MM.Coder(mm.dict, mm.has_axis, mm.names, mm), V, mm.mix), r1 = mk(m), r2 = mk(m2), out = {};
for (const w of JSON.parse(fs.readFileSync(process.argv[2]))) out[w] = [r1.encode(w), r2.encode(w)].map((e) => (e ? (typeof e === "string" ? e : e.code) : null));
fs.writeFileSync(process.argv[3], JSON.stringify(out));
