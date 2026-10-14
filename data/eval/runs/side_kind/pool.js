// Пулы: kind — знаменательные слова (ранг < 20000), ближайшие к атому KIND при v = −5, −3, 0, +3, +5 (по 500), все слова ../kind рядом с атомом и слова ../big1000, у которых в ../kind KIND был головой;
// side — 1000 слов ../big1000 и 1500 случайных частых слов (ранг < 10000), не из пула kind.  node pool.js → pool.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const K = JSON.parse(fs.readFileSync(path.join(__dirname, "../kind/kind.json"))), old = JSON.parse(fs.readFileSync(path.join(__dirname, "../kind/pool.json")));
const bad = new Set([...meta.stop, ...meta.proper]), ok = (w, n) => V.index.get(w) < n && !bad.has(V.index.get(w)) && /^[a-z]{3,}$/.test(w), oc = JSON.parse(fs.readFileSync(path.join(__dirname, "../kind/codes.json"))), kind = new Set([...old.near, ...old.big.filter((w) => /^KIND\b/.test(oc[w][1] || ""))]);
const kind0 = new Set(kind), near = (v) => V.near(K.C.map((c, j) => c + m.s * v * K.A[j]), 2000).filter((w) => ok(w, 20000));
for (const v of [-5, -3, 0, 3, 5]) { near(v).slice(0, 250).forEach((w) => kind0.add(w)); near(v).slice(0, 500).forEach((w) => kind.add(w)); }
// пул side собран при пуле kind по 250 и не меняется; слова пула kind по 500, попавшие в пул side, из kind убраны
const big = old.big.filter((w) => !kind0.has(w)), rest = m.words.filter((w) => ok(w, 10000) && !kind0.has(w) && !big.includes(w));
let s = 20261014; const rnd = () => ((s = (s * 1103515245 + 12345) % 2147483648) / 2147483648);
for (let i = rest.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [rest[i], rest[j]] = [rest[j], rest[i]]; }
const side = [...big, ...rest.slice(0, 1500)], ss = new Set(side), out = { kind: [...kind].filter((w) => !ss.has(w)), side }; fs.writeFileSync(path.join(__dirname, "pool.json"), JSON.stringify(out));
console.log("kind", out.kind.length, "side", out.side.length);
