// Коды rand1000 для подгонки весов negVec (fit.py): слово, корни кода, единичный вектор суммы корней t, вектор слова x.
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const out = rand.map((w) => { const x = V.vec(w), e = co.encode(x), y = new Float64Array(x.length);
  for (const p of co.parts(e.S, e.v)) for (let j = 0; j < y.length; j++) y[j] += p[j];
  const n = Math.hypot(...y); return { w, S: e.S, t: Array.from(y, (u) => +(u / n).toFixed(5)), x: Array.from(x, (u) => +u.toFixed(5)) }; });
fs.writeFileSync(path.join(D, "dump_r1.json"), JSON.stringify({ C: m.dict.C, names: m.names, rows: out }));
