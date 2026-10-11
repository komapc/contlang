// Проверка чтения кодов векторами (site/math.js Reader) — тот же код, что на сайте.
//   node scripts/site/eval_math.js [--grid] [--graph]   (--graph: связи ConceptNet из data/raw/conceptnet/graph.json (scripts/site/build_graph.py), сетка graphW)
// Рецепты: слова из одного кода (site/data/recipes.json) — top1/10/50, медиана места, место > 1000, cos первого прочтения со словом.
// Пары: коды из нескольких слов из слепых тестов (data/eval/runs/*/key.json, PAIRS ниже) — геометрическое среднее места по словам.
const fs = require("fs"), path = require("path");
const REPO = path.resolve(__dirname, "../.."), SITE = path.join(REPO, "site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
if (process.argv.includes("--graph")) V.setGraph(JSON.parse(fs.readFileSync(path.join(REPO, "data/raw/conceptnet/graph.json"))));

const recipes = JSON.parse(fs.readFileSync(path.join(SITE, "data/recipes.json")))
  .filter((e) => /^[a-z]+$/.test(e.en) && !/\bPI\b|"/.test(e.code) && V.index.has(e.en));
// пары: [слово, код] из слепых тестов
function pairs(only) {
  const out = [], J = (f) => JSON.parse(fs.readFileSync(path.join(REPO, "data/eval/runs", f)));
  const kf = J("key_furniture/key.json"); kf.K.forEach((c) => out.push(["key", c])); kf.F.forEach((c) => out.push(["furniture", c]));
  J("key_door/key.json").G.key.forEach((c) => out.push(["key", c]));
  for (const f of fs.readdirSync(path.join(REPO, "data/eval/runs"))) {   // тесты пар: pairs.json — [{word, code}]
    const p = path.join(REPO, "data/eval/runs", f, "pairs.json");
    if (fs.existsSync(p)) JSON.parse(fs.readFileSync(p)).forEach((e) => out.push([e.word, e.code]));
  }
  return out.filter(([w, c]) => /\b(PI|FROM|FOR|LIKE)\b/.test(c) && V.index.has(w) && (!only || only.test(c)));
}
const cos = (a, b) => { const x = V.vec(a), y = V.vec(b); let s = 0; for (let j = 0; j < x.length; j++) s += x[j] * y[j]; return s; };
const gm = (a) => Math.round(Math.exp(a.reduce((s, x) => s + Math.log(x), 0) / a.length));
const pct = (a, t) => Math.round(100 * a.filter((r) => r <= t).length / a.length) + "%";

function evaluate(opt) {
  const rd = new MM.Reader(co, V, m.mix, opt), rk = [], c1 = [];
  for (const e of recipes) {
    if (!rd.parse(e.code).S.length) continue;
    const sc = rd.scores(e.code); rk.push(V.rankIn(sc, e.en)); c1.push(cos(V.top(sc, 1)[0].word, e.en));
  }
  rk.sort((a, b) => a - b); c1.sort((a, b) => a - b);
  const P = pairs(opt.only), byw = {};
  for (const [w, c] of P) (byw[w] = byw[w] || []).push(V.rankIn(rd.scores(opt.link ? c.replace(/\b(PI|FROM|FOR|LIKE)\b/g, opt.link) : c), w));
  return { n: rk.length, top1: pct(rk, 1), top10: pct(rk, 10), top50: pct(rk, 50), med: rk[rk.length >> 1], over1000: rk.filter((r) => r > 1000).length,
    cos1: c1[c1.length >> 1].toFixed(2), pairs: P.length, pairsGM: gm(Object.values(byw).flat()), pairsTop10: Object.values(byw).flat().filter((r) => r <= 10).length,
    byWord: Object.fromEntries(Object.entries(byw).map(([w, a]) => [w, gm(a)])) };
}
const fmt = (name, r) => `${name.padEnd(28)} рецептов ${r.n}: top1 ${r.top1} top10 ${r.top10} top50 ${r.top50} медиана ${r.med} >1000 ${r.over1000} cos1 ${r.cos1}` +
  ` | пар ${r.pairs}: среднее место ${r.pairsGM}, top10 ${r.pairsTop10}`;
console.log(fmt("сайт", evaluate({})));
if (process.argv.includes("--grid")) {
  for (const posPen of [0, 1, 1.5, 2]) console.log(fmt("posPen " + posPen, evaluate({ posPen })));
  for (const prfMu of [0, 0.3, 0.6]) for (const pairLam of [0.25, 0.4, 0.6]) console.log(fmt(`prfMu ${prfMu} pairLam ${pairLam}`, evaluate({ prfMu, pairLam })));
}
if (process.argv.includes("--graph")) {
  // пары с FOR и с PI отдельно; link — каждую пару читать через одну частицу (те же коды, другие отношения графа)
  for (const graphW of [0, 0.5, 1, 2, 4]) for (const [name, only] of [["все", null], ["PI", /\bPI\b/], ["FOR", /\bFOR\b/]])
    for (const link of only ? ["", "PI", "FOR"] : [""]) console.log(fmt(`graphW ${graphW} ${name}${link ? " как " + link : ""}`, evaluate({ graphW, only, link })));
}
module.exports = { evaluate, pairs, V, co, m, MM };
