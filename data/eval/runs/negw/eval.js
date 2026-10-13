// Способ 2 «не упомянут — значит, мал»: Reader opt negW (site/math.js mixFor) — из суммы корней вычитается negW·|y|·(центры НЕупомянутых корней).
// Кодер не меняется (коды те же), меняется только чтение. Словарь и смесь — как на сайте (site/data/math.json).
// ① dev (100 слов, с частью речи), ① 1000 (rand1000), ① другие 1000 (seed 11, как в ../anchor/eval.js) — место слова, первыми, cos первого прочтения;
// тест 1 — математика читает коды моделей (../mathread/calib.json) и рецепты: cos первого прочтения со словом.
//   node data/eval/runs/negw/eval.js 0 0.2 0.4 0.6 learned_10:2 mean:2   (имя:κ — веса по корням из weights.json, fit.py, умноженные на κ)
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), dev = W.dev;
const rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math"));
const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code }));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const enc = (ws) => ws.map(([w, f]) => ({ w, f, ...co.encode(V.vec(w)) }));
const E = { dev: enc(dev), r1: enc(rand.map((w) => [w, ""])), r2: enc(rand2.map((w) => [w, ""])) };
const out = {};
const WT = fs.existsSync(path.join(D, "weights.json")) ? JSON.parse(fs.readFileSync(path.join(D, "weights.json"))) : {};
const OUT = process.env.OUT || "results.json";
for (const negW of process.argv.slice(2)) {
  const [wn, k] = negW.split(":"), opt = k ? { negVec: WT[wn].map((t) => t * Number(k)) } : { negW: Number(negW) };
  const rd = new MM.Reader(co, V, m.mix, opt), row = {};
  for (const [k, es] of Object.entries(E)) {
    const res = es.map((e) => { const sc = rd.roots(e.S, e.v, e.f); return { r: V.rankIn(sc, e.w), c: cosw(V.top(sc, 1)[0].word, e.w) }; });
    row[k] = { ranks: res.map((x) => x.r), c1: res.map((x) => x.c) };
  }
  for (const [k, cs] of [["calib", calib], ["rec", rec]]) row[k] = { c1: cs.map((c) => cosw(V.top(rd.scores(c.code), 1)[0].word, c.w)) };
  out[negW] = row;
  const f = (k) => `${row[k].ranks.filter((r) => r === 1).length} (cos ${(row[k].c1.reduce((s, x) => s + x, 0) / row[k].c1.length).toFixed(3)})`;
  const g = (k) => `${(row[k].c1.reduce((s, x) => s + x, 0) / row[k].c1.length).toFixed(3)} (близко ${row[k].c1.filter((x) => x >= 0.5).length})`;
  console.log(`negW ${negW}: dev ${f("dev")} | 1000 ${f("r1")} | другие 1000 ${f("r2")} | коды моделей ${g("calib")} | рецепты ${g("rec")}`);
}
fs.writeFileSync(path.join(D, OUT), JSON.stringify(out));
