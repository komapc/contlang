// Ближайшие слова к атому SIDE сайта (site/data/math.json) при v = −5 … +5, и сколько кодов кодера сайта на 1000 словах ../big1000 содержат SIDE.  node atoms.js
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const r = m.names.indexOf("SIDE"), C = m.dict.C[r], A = m.dict.A[r];
for (const v of [-5, -3, 0, 3, 5]) { const x = C.map((c, j) => c + m.s * v * A[j]); console.log(`SIDE(=${v}):`, V.near(x, 40).filter((w) => V.index.get(w) < 20000 && !V.proper[V.index.get(w)]).slice(0, 18).join(", ")); }
const site = JSON.parse(fs.readFileSync(path.join(__dirname, "../big1000/site_codes.json"))), ws = Object.keys(site).filter((w) => /\bSIDE\b/.test(site[w] || ""));
console.log("big1000: SIDE в", ws.length, "кодах; головой", ws.filter((w) => /^SIDE\b/.test(site[w])).length);
console.log(ws.slice(0, 60).map((w) => `${w}: ${site[w]}`).join("\n"));
