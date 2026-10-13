// Перенос кодов модели в математику (пункт 2 из ../twowords3): коды, написанные моделями, считаются верными, а центры C и оси A
// корней подбираются так, чтобы эти коды раскладывали векторы слов: min ‖M·Θ − T‖² + lam‖Θ − Θ0‖², T = |M·Θ0|·x (как scripts/18_sparse_learn.py),
// затем атом нормируется и, если ушёл от исходного дальше cos < tau, возвращается по дуге. Θ0 — нынешний словарь сайта.
// Обучение: site/data/recipes.json и коды Haiku из ../twowords3/write (без 100 тестовых слов ../twowords2 и без кодов с ролями).
// Мера: совпадение кода нового кодера с кодом модели — на отложенных обучающих (5 частей) и на 100 тестовых (код H ../twowords3).
//   node data/eval/runs/distill/fit.js [lam] [tau]       → печать; с --save пишет dict.json (C, A) для make.js
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co0 = new MM.Coder(m.dict, m.has_axis, m.names, m), rd0 = new MM.Reader(co0, V, m.mix);
const args = process.argv.slice(2).filter((a) => !a.startsWith("--")), lam = Number(args[0] ?? 30), tau = Number(args[1] ?? 0.85);
const T2 = path.join(D, "../twowords2"), T3 = path.join(D, "../twowords3");
const test = JSON.parse(fs.readFileSync(path.join(T3, "items.json"))).map((x) => ({ w: x.w, code: x.H }));
const tw = new Set(test.map((x) => x.w)), { cands } = JSON.parse(fs.readFileSync(path.join(T2, "cands.json"))), all = Object.keys(cands);
const train = [];
for (const e of JSON.parse(fs.readFileSync(path.join(REPO, "site/data/recipes.json")))) if (!tw.has(e.en)) train.push({ w: e.en, code: e.code, src: "recipe" });
for (let k = 0; k * 40 < all.length; k++) for (const l of fs.readFileSync(path.join(T3, "write", `ans_${k + 1}.md`), "utf8").split("\n")) {
  const t = l.match(/^\s*(\d+)\.\s*`?([^`]+?)`?\s*$/), w = t && all[k * 40 + Number(t[1]) - 1]; if (w && !tw.has(w)) train.push({ w, code: t[2], src: "haiku" });
}
const ONLY = (process.argv.find((a) => a.startsWith("--only=")) || "").slice(7);
const ok = (e) => (!ONLY || !e.src || e.src === ONLY) && /^[a-z]+$/.test(e.w) && V.index.has(e.w) && !/\b(PI|FROM|FOR|LIKE|agent|tool|result|quality)\b|"/.test(e.code) && co0.parse(e.code).S.length && !co0.parse(e.code).unknown.length;
const tr = train.filter(ok), te = test.filter(ok), R = co0.R, Dm = V.dim, s = m.s, wts = [1, m.head_w, m.head_w];
const th0 = co0.C.concat(co0.A), unit = (a) => { const n = Math.hypot(...a) || 1; return a.map((t) => t / n); };
const row = (code) => { const p = co0.parse(code), r = new Float64Array(2 * R); p.S.forEach((k, i) => { r[k] += wts[i]; r[R + k] += wts[i] * s * p.v[i]; }); return r; };
function solve(A, B) { // A n×n, B n×d (Гаусс)
  const n = A.length, M = A.map((a, i) => [...a, ...B[i]]);
  for (let c = 0; c < n; c++) { let p = c; for (let i = c + 1; i < n; i++) if (Math.abs(M[i][c]) > Math.abs(M[p][c])) p = i; [M[c], M[p]] = [M[p], M[c]];
    for (let i = 0; i < n; i++) if (i !== c) { const f = M[i][c] / M[c][c]; if (f) for (let j = c; j < M[i].length; j++) M[i][j] -= f * M[c][j]; } }
  return M.map((r, i) => r.slice(n).map((t) => t / r[i]));
}
let fit = function (set) {
  const n2 = 2 * R, AtA = Array.from({ length: n2 }, (_, i) => Array.from({ length: n2 }, (_, j) => (i === j ? lam : 0))), AtB = th0.map((a) => a.map((t) => lam * t));
  for (const e of set) { const r = row(e.code), x = V.vec(e.w); const y = new Float64Array(Dm); for (let k = 0; k < n2; k++) if (r[k]) for (let j = 0; j < Dm; j++) y[j] += r[k] * th0[k][j];
    const ny = Math.hypot(...y); for (let a = 0; a < n2; a++) if (r[a]) { for (let b = 0; b < n2; b++) AtA[a][b] += r[a] * r[b]; for (let j = 0; j < Dm; j++) AtB[a][j] += r[a] * ny * x[j]; } }
  const th = solve(AtA, AtB).map((a, i) => { if (i >= R && !m.has_axis[i - R]) return a.map(() => 0); const u = unit(a), o = unit(th0[i]), c = u.reduce((t, x, j) => t + x * o[j], 0);
    if (c >= tau) return u; const p = unit(u.map((x, j) => x - c * o[j])); return o.map((x, j) => tau * x + Math.sqrt(1 - tau * tau) * p[j]); });
  return { C: th.slice(0, R), A: th.slice(R) };
}
const agree = (co, set) => { let head = 0, jac = 0, same = 0;
  for (const e of set) { const g = co0.parse(e.code), c = co.encode(V.vec(e.w), 3, rd0.ban(e.w)), gs = new Set(g.S), cs = new Set(c.S);
    head += g.S[0] === c.S[0]; const inter = [...cs].filter((r) => gs.has(r)).length; jac += inter / new Set([...gs, ...cs]).size; same += inter === gs.size && inter === cs.size; }
  return `главный ${(100 * head / set.length).toFixed(0)}%, Жаккар ${(jac / set.length).toFixed(2)}, тот же набор ${(100 * same / set.length).toFixed(0)}%`; };
const mk = (d) => new MM.Coder(d, m.has_axis, m.names, m);
// --perc=E,eta: после ridge — E эпох пакетного перцептрона: если кодер выбрал не код модели, атомы кода модели тянутся к x,
// атомы выбранного — от x (градиент x·y), затем нормировка и возврат по дуге к исходным (tau)
const PE = (process.argv.find((a) => a.startsWith("--perc=")) || "").slice(7).split(",").map(Number);
const clampU = (a, o) => { const u = unit(a), c = u.reduce((t, x, j) => t + x * o[j], 0); if (c >= tau) return u; const q = unit(u.map((x, j) => x - c * o[j])); return o.map((x, j) => tau * x + Math.sqrt(1 - tau * tau) * q[j]); };
const fitR = fit;
fit = (set) => { let d = fitR(set); if (!PE[0]) return d;
  for (let e = 0; e < PE[0]; e++) { const co = mk(d), th = d.C.concat(d.A).map((a) => Float64Array.from(a));
    for (const x0 of set) { const x = V.vec(x0.w), c = co.encode(x, 3, rd0.ban(x0.w)), rg = row(x0.code), rc = new Float64Array(2 * R);
      c.S.forEach((k, i) => { rc[k] += wts[i]; rc[R + k] += wts[i] * s * c.v[i]; });
      for (let k = 0; k < 2 * R; k++) { const g = rg[k] - rc[k]; if (g) for (let j = 0; j < Dm; j++) th[k][j] += PE[1] * g * x[j]; } }
    const t2 = th.map((a, i) => (i >= R && !m.has_axis[i - R] ? Array.from(a, () => 0) : clampU(Array.from(a), unit(th0[i]))));
    d = { C: t2.slice(0, R), A: t2.slice(R) }; }
  return d; };
console.log(`обучающих ${tr.length} (рецептов ${tr.filter((e) => e.src === "recipe").length}), тестовых ${te.length}; lam ${lam}, tau ${tau}`);
console.log(`  сейчас: отложенные ${agree(co0, tr)} | тест ${agree(co0, te)}`);
const folds = 5, frac = Number((process.argv.find((a) => a.startsWith("--frac=")) || "--frac=1").slice(7));
const cvA = (() => { const parts = []; for (let f = 0; f < folds; f++) { const d = fit(tr.filter((_, i) => i % folds !== f && (i * 7919) % 1000 < frac * 1000)); parts.push(agree(mk(d), tr.filter((_, i) => i % folds === f))); } return parts; })();
const dAll = fit(tr), coN = mk(dAll);
console.log(`  новый:  отложенные (5 частей) ${cvA.join(" / ")}\n          тест ${agree(coN, te)}`);
const drift = dAll.C.map((c, i) => c.reduce((t, x, j) => t + x * unit(th0[i])[j], 0)); console.log(`  cos с прежними центрами: мин ${Math.min(...drift).toFixed(2)}, среднее ${(drift.reduce((a, b) => a + b) / R).toFixed(2)}`);
for (const w of ["person", "pianist", "employee", "bowl", "road", "chapel", "lake", "knight"]) { if (!V.index.has(w)) continue; const a = co0.encode(V.vec(w), 3, rd0.ban(w)), b = coN.encode(V.vec(w), 3, rd0.ban(w)); console.log(`  ${w}: ${co0.format(a.S, a.v)}  →  ${coN.format(b.S, b.v)}`); }
if (process.argv.includes("--save")) fs.writeFileSync(path.join(D, `dict.json`), JSON.stringify({ lam, tau, C: dAll.C.map((a) => a.map((t) => +t.toFixed(5))), A: dAll.A.map((a) => a.map((t) => +t.toFixed(5))) }));
if (process.argv.includes("--insample")) console.log(`  на самих обучающих (все): ${agree(coN, tr)}`);
