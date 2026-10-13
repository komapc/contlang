// Словарь, переученный при весе не главных 0,4 (MATH_HW=0.4 scripts/18_sparse_learn.py + scripts/site/build_math.py), против 0,6.
// Берёт текущий site/data/math.json (подменить на math_hw04.json или оставить 0,6) — TAG имя строки, WTS вес, SELF 1 = самопроверка (голова та же) + штраф 0,5.
//   TAG=dict04 WTS=0.4 SELF=0 node data/eval/runs/relearn/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const hw = Number(process.env.WTS), self = process.env.SELF === "1", tag = process.env.TAG;
const co = new MM.Coder(m.dict, m.has_axis, m.names, { ...m, wts: [1, hw, hw] }), rd = new MM.Reader(co, V, m.mix, self ? { absLam: 0.5 } : {});
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math"));
const row = {};
for (const [k, ws] of [["dev", W.dev], ["r1", rand.map((w) => [w, ""])], ["r2", rand2.map((w) => [w, ""])]])
  row[k] = ws.map(([w, f]) => { const e = self ? rd.best(w, f, true) : co.encode(V.vec(w)); return { r: self ? e.r : V.rankIn(rd.roots(e.S, e.v, f), w), n: e.S.length }; });
row.calib = calib.map((c) => cosw(V.top(rd.scores(c.code), 1)[0].word, c.w));
const f = (k) => row[k].filter((x) => x.r === 1).length;
console.log(`${tag} (вес ${hw}${self ? ", самопроверка + штраф" : ""}): dev ${f("dev")} | 1000 ${f("r1")} | другие 1000 ${f("r2")} | корней ${(row.r2.reduce((s, x) => s + x.n, 0) / 1000).toFixed(2)} | коды моделей ${(row.calib.reduce((s, x) => s + x, 0) / row.calib.length).toFixed(3)}`);
fs.writeFileSync(path.join(D, `results_${tag}.json`), JSON.stringify(row));
