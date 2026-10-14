// Шаг 2: цена удаления каждого корня для кодера сайта. Для слова — код и место слова при чтении векторами (rank),
// и для каждого корня его кода — код и место с запретом этого корня.  node remove.js in.json out.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), ban0 = rd.ban.bind(rd); let extra = [];
rd.ban = (w) => [...ban0(w), ...extra];
const out = {};
for (const w of JSON.parse(fs.readFileSync(process.argv[2]))) {
  extra = []; const e = rd.encode(w); if (!e || e.name || !e.S.length) continue;
  const o = { code: e.code, rank: e.rank, ban: {} };
  for (const r of e.S) { extra = [r]; const b = rd.encode(w); o.ban[m.names[r]] = b ? { code: b.code, rank: b.rank } : null; }
  out[w] = o;
}
fs.writeFileSync(process.argv[3], JSON.stringify(out));
