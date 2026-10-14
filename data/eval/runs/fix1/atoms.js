// Что значат атомы корней в векторах: ближайшие слова к c_r + s·v·a_r при v = −5, 0, +5 (и для корня без оси — к c_r).  node atoms.js ROOT…
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), N = Math.min(V.words.length, 20000);
for (const R of process.argv.slice(2)) {
  const r = co.names.indexOf(R);
  for (const v of co.has[r] ? [-5, 0, 5] : [0]) {
    const x = co.C[r].map((c, j) => c + co.s * v * co.A[r][j]);
    console.log(`${R}(=${v}):`, V.near(x, 4 * 15).filter((w) => V.index.get(w) < N && !(V.proper && V.proper[V.index.get(w)])).slice(0, 15).join(", "));
  }
}
