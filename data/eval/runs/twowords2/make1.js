// «Два слова» 2, шаг 1: все существительные из «других 1000» (не имена, не множественное, часть речи o) в случайном порядке → nouns.txt; отбор и толкования — make1.py.
//   node data/eval/runs/twowords2/make1.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const nouns = rand2.filter((w) => !V.proper[V.index.get(w)] && !V.plural[V.index.get(w)] && rd.posOf(w) === "o");
let seed = 5; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
for (let i = nouns.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [nouns[i], nouns[j]] = [nouns[j], nouns[i]]; }
fs.writeFileSync(path.join(D, "nouns.txt"), nouns.join("\n") + "\n"); console.log(`существительных ${nouns.length}`);
