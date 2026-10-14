// W2 / W3: к нынешнему коду цели добавляются 1–2 опорных слова через LIKE; берутся те, при которых цель выше всего при чтении
// векторами (Reader.scores, как читает сайт). W3 — жадно: лучшее первое слово (W2) + лучшее второе.  node search.js pool.json codes.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix);
const P = JSON.parse(fs.readFileSync(process.argv[2])), out = {};
const rank = (code, w) => V.rankIn(rd.scores(code), w);
for (const [w, o] of Object.entries(P)) {
  const r1 = rank(o.code, w); let b2 = null;
  for (const [a, ac] of o.anchors) { const c = `${o.code} LIKE ${ac}`, r = rank(c, w); if (!b2 || r < b2.r) b2 = { r, c, a: [a] }; }
  let b3 = null;
  for (const [a, ac] of o.anchors) { if (a === b2.a[0]) continue; const c = `${b2.c} LIKE ${ac}`, r = rank(c, w); if (!b3 || r < b3.r) b3 = { r, c, a: [...b2.a, a] }; }
  out[w] = { A: o.code, rA: r1, W2: b2.c, r2: b2.r, a2: b2.a, W3: b3.c, r3: b3.r, a3: b3.a };
}
fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 0));
const med = (k) => { const v = Object.values(out).map((x) => x[k]).sort((a, b) => a - b); return v[v.length >> 1]; };
const t1 = (k) => Object.values(out).filter((x) => x[k] === 1).length;
console.log("медиана места A/W2/W3:", med("rA"), med("r2"), med("r3"), " первым:", t1("rA"), t1("r2"), t1("r3"));
