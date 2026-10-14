// Слова у полюсов атома (atoms/NAME.json) при v = −5, 0, +5.  node poles.js NAME…
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
for (const N of process.argv.slice(2)) { const K = JSON.parse(fs.readFileSync(path.join(__dirname, "atoms", N + ".json")));
  for (const v of [-5, 0, 5]) { const x = K.C.map((c, j) => c + m.s * v * K.A[j]); console.log(`${N}(=${v}):`, V.near(x, 60).filter((w) => V.index.get(w) < 20000 && !V.proper[V.index.get(w)]).slice(0, 16).join(", ")); } }
