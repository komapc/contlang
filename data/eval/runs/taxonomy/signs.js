// Знак значения: совпадает ли он у математики с моделью. На кодах H (../twowords3), для каждого корня с осью и значением ≠ 0 у модели:
// ① значение из варианта M (подбор по cos при корнях модели), ② «измерение» — z-оценка проекции слова на ось a_r по словарю,
// ③ то же для вектора толкования (../definition/wn.json). → печать: доля совпавших знаков, средний |z|.
//   node data/eval/runs/taxonomy/signs.js
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), items = JSON.parse(fs.readFileSync(path.join(D, "items.json")));
const def = require(path.join(D, "../definition/coder.js"))(), dot = (a, b) => a.reduce((s, x, i) => s + x * b[i], 0);
const st = co.A.map((a, r) => { if (!m.has_axis[r]) return null; const xs = []; for (let i = 0; i < V.words.length; i += 5) xs.push(dot(V.vec(V.words[i]), a)); const mu = xs.reduce((s, x) => s + x) / xs.length; return [mu, Math.sqrt(xs.reduce((s, x) => s + (x - mu) ** 2, 0) / xs.length)]; });
const zOf = (x, r) => (dot(x, co.A[r]) - st[r][0]) / st[r][1];
let n = 0, okM = 0, okZ = 0, okG = 0, nG = 0; const rows = [], byRoot = {};
for (const it of items) { const h = co.parse(it.H || ""), mm = co.parse((it.M || "").split("|")[0]), x = V.vec(it.w), g = def.glossVec(it.w);
  h.S.forEach((r, i) => { if (!m.has_axis[r] || !h.v[i]) return; n++; const sh = Math.sign(h.v[i]);
    const j = mm.S.indexOf(r), vm = j >= 0 ? mm.v[j] : 0; okM += Math.sign(vm) === sh; const z = zOf(x, r); okZ += Math.sign(z) === sh;
    if (g) { nG++; okG += Math.sign(zOf(g, r)) === sh; }
    (byRoot[m.names[r]] ||= [0, 0])[0]++; byRoot[m.names[r]][1] += Math.sign(z) === sh;
    rows.push(`${it.w} ${m.names[r]}: модель ${h.v[i]}, M ${vm}, z ${z.toFixed(1)}`); }); }
console.log(`значений модели ≠ 0: ${n}; знак совпал: M ${Math.round(100 * okM / n)}% (0 у M считается промахом), измерение по слову ${Math.round(100 * okZ / n)}%, по толкованию ${Math.round(100 * okG / nG)}%`);
console.log("по корням (измерение по слову, совпало / всего):", Object.entries(byRoot).sort((a, b) => b[1][0] - a[1][0]).map(([k, [t, o]]) => `${k} ${o}/${t}`).join(", "));
rows.slice(0, 25).forEach((r) => console.log("  " + r));
