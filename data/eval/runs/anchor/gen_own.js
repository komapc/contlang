// Коды нынешнего кодера (без пар) для всех слов словаря сайта вне dev/test, rand1000 и отложенных 1000 из eval.js (rand2) (≈4760; всего подходящих слов 6962) → own8k.json [[слово, код]]
//   node data/eval/runs/anchor/gen_own.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, co } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const ok = (i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]);
let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;   // как rand2 в eval.js
const skip0 = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool0 = V.words.map((_, i) => i).filter((i) => ok(i) && !skip0.has(V.words[i]));
const r2 = new Set(); while (r2.size < 1000) r2.add(pool0[Math.floor(rnd() * pool0.length)]);
const pick = pool0.filter((i) => !r2.has(i));
const out = pick.map((i) => { const w = V.words[i], e = co.encode(V.vec(w)); return [w, co.format(e.S, e.v, "o")]; });
fs.writeFileSync(path.join(D, "own8k.json"), JSON.stringify(out));
console.log(`own8k: ${out.length}, из отложенных ${out.filter(([w]) => [...r2].some((i) => V.words[i] === w)).length}`);
