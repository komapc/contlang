// Самопроверка вместе со штрафом за сродство (absLam 0,5, absTau 1; ../absence): ① dev / 1000 / другие 1000, коды моделей и рецепты.
//   node data/eval/runs/selfcheck/eval2.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math"));
const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code }));
const out = {};
for (const [name, opt, self] of [["штраф", { absLam: 0.5 }, false], ["самопроверка (голова та же) + штраф", { absLam: 0.5 }, true]]) {
  const rd = new MM.Reader(co, V, m.mix, opt), row = {};
  for (const [k, ws] of [["dev", W.dev], ["r1", rand.map((w) => [w, ""])], ["r2", rand2.map((w) => [w, ""])]])
    row[k] = ws.map(([w, f]) => { const e = self ? rd.best(w, f, true) : co.encode(V.vec(w)); return { w, r: self ? e.r : V.rankIn(rd.roots(e.S, e.v, f), w), n: e.S.length, code: co.format(e.S, e.v, f || "o") }; });
  out[name] = row;
  const f = (k) => `${row[k].filter((x) => x.r === 1).length} (корней ${(row[k].reduce((s, x) => s + x.n, 0) / row[k].length).toFixed(2)})`;
  console.log(`${name}: dev ${f("dev")} | 1000 ${f("r1")} | другие 1000 ${f("r2")}`);
}
fs.writeFileSync(path.join(D, "results2.json"), JSON.stringify(out));
