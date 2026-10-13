// Кодер-«определение»: сравнение вариантов без читателей. На 100 словах ../twowords2 и 300 существительных «других 1000»:
// доля «паролей» (в коде есть корень, чья часть c_r + s·v·a_r для самого слова не правда: z < 0,5), круг математики
// (место слова, когда Reader читает код: геом. среднее и первыми), совпадение набора корней с кодом модели H (../twowords3, только 100).
//   node data/eval/runs/definition/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, mk = require("./coder.js");
const base = mk(), { V, rd, co, WN, zPart } = base;
const H = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(D, "../twowords3/items.json"))).map((x) => [x.w, x.H]));
const words = Object.keys(WN).filter((w) => V.index.has(w) && !V.proper[V.index.get(w)]), test = words.filter((w) => WN[w].test), other = words.filter((w) => !WN[w].test);
const ONLY = process.argv[2]; const VARS0 = { A: {}, G: { genus: true }, T: { truth: 0.5 }, S: { beta: 1 }, GT: { genus: true, truth: 0.5 }, GTS: { genus: true, truth: 0.5, beta: 1 }, "GTS β0,5": { genus: true, truth: 0.5, beta: 0.5 }, "GTS τ1": { genus: true, truth: 1, beta: 1 },
  "GTg": { genus: true, truth: 0.5, on: "gloss" }, "GTgS": { genus: true, truth: 0.5, on: "gloss", beta: 0.5 }, "GTg τ1": { genus: true, truth: 1, on: "gloss" }, "GTgS τ1": { genus: true, truth: 1, on: "gloss", beta: 0.5 } };
const VARS = ONLY ? Object.fromEntries(Object.entries(VARS0).filter(([k]) => k === "A" || ONLY.split(",").includes(k))) : VARS0;
const out = {};
for (const [name, opt] of Object.entries(VARS)) {
  const def = mk(opt), res = {};
  for (const w of words) { const e = def.encode(w); res[w] = { code: e.code, pw: e.S.some((r, i) => zPart(V.vec(w), r, e.v[i]) < 0.5), rank: V.rankIn(rd.scores(e.code), w) }; }
  const st = (ws) => { const gm = Math.round(Math.exp(ws.reduce((s, w) => s + Math.log(res[w].rank), 0) / ws.length));
    return `пароли ${Math.round(100 * ws.filter((w) => res[w].pw).length / ws.length)}%, круг ${gm} (первыми ${ws.filter((w) => res[w].rank === 1).length})`; };
  let jac = 0, n = 0; for (const w of test) { const h = co.parse(H[w] || ""); if (!h.S.length) continue; const a = new Set(h.S), b = new Set(co.parse(res[w].code).S); jac += [...b].filter((r) => a.has(r)).length / new Set([...a, ...b]).size; n++; }
  console.log(`${name.padEnd(9)} 100: ${st(test)}, с H ${(jac / n).toFixed(2)} | 300: ${st(other)}`); out[name] = res;
}
fs.writeFileSync(path.join(D, ONLY ? "eval_part.json" : "eval.json"), JSON.stringify(out));
for (const w of ["employee", "pianist", "chapel", "malaria", "bowl", "lake", "road", "knight", "coca", "integration", "religion", "profit"]) if (out.A[w]) console.log(`${w} [${WN[w].genus}]: ` + Object.keys(out).map((k) => `${k} ${out[k][w].code.replace(' | o', '')}`).join(' | '));
