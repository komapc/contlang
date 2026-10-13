// «Два слова», шаг 1: 100 случайных существительных из «других 1000» (не имена, часть речи o по WordNet) → words.txt, gen/words_K.md (по 50).
//   node data/eval/runs/twowords/make1.js
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
const pick = nouns.slice(0, 100);
fs.writeFileSync(path.join(D, "words.txt"), pick.join("\n") + "\n"); fs.mkdirSync(path.join(D, "gen"), { recursive: true });
for (const k of [1, 2]) fs.writeFileSync(path.join(D, "gen", `words_${k}.md`), pick.slice((k - 1) * 50, k * 50).map((w, i) => `${i + 1}. ${w}`).join("\n") + "\n");
console.log(`существительных ${nouns.length}; взято 100:`, pick.join(", "));
