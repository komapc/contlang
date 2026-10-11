// Тест 1 честно: математика читает отложенные коды моделей словарём, подогнанным без них (fit.py, 5 частей).
//   node data/eval/runs/anchor/eval_cv.js 3_0.2 3_0 ...
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); let s = 0; for (let j = 0; j < x.length; j++) s += x[j] * y[j]; return s; };
const base = JSON.parse(fs.readFileSync(path.join(D, "dict_learned.json")));
for (const tag of process.argv.slice(2)) {
  const a = [], b = [];
  for (let k = 0; k < 5; k++) {
    const dd = JSON.parse(fs.readFileSync(path.join(D, `cv_${tag}_${k}.json`)));
    for (const [dict, out] of [[dd, a], [base, b]]) {
      const co = new MM.Coder({ C: dict.C, A: dict.A }, m.has_axis, m.names, m), rd = new MM.Reader(co, V, { ...m.mix, hub: dict.hub }, {});
      for (const [w, code] of dd.test) out.push(cosw(V.top(rd.scores(code), 1)[0].word, w));
    }
  }
  const mean = (x) => x.reduce((s, t) => s + t, 0) / x.length;
  console.log(`${tag}: отложенные коды моделей (${a.length}) — cos первого прочтения ${mean(a).toFixed(2)}, близко ${a.filter((x) => x >= 0.5).length}; нынешний словарь на тех же ${mean(b).toFixed(2)}, близко ${b.filter((x) => x >= 0.5).length}`);
}
