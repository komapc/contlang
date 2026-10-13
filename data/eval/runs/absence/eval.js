// Отсутствие корня в оценке слова, а не в сумме векторов (README):
//  (а) штраф за сродство: score −= λ·max(0, max_{r ∉ код} Z[w][r] − τ), Z — z-оценка cos(слово, центр r) по словарю;
//  (б) обратная таблица: у каждого слова сайта свой код кодера; score += μ·z(сходство данного кода с кодом слова).
// Подбор λ, τ, μ на ① 1000 (rand1000), проверка на ① других 1000 и dev; коды моделей (calib) и рецепты — cos первого прочтения.
//   node data/eval/runs/absence/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix, {});
const N = V.words.length, R = co.R, DIM = V.dim, dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
// Z[i*R + r]
const Cu = co.C.map((c) => { const n = Math.sqrt(dot(c, c)); return c.map((t) => t / n); });
const Z = new Float32Array(N * R);
for (let r = 0; r < R; r++) { const a = new Float64Array(N); let mu = 0, sd = 0;
  for (let i = 0; i < N; i++) { let s = 0; const o = i * DIM; for (let j = 0; j < DIM; j++) s += V.X[o + j] * Cu[r][j]; a[i] = s / V.norm[i]; mu += a[i]; }
  mu /= N; for (let i = 0; i < N; i++) sd += (a[i] - mu) ** 2; sd = Math.sqrt(sd / N); for (let i = 0; i < N; i++) Z[i * R + r] = (a[i] - mu) / sd; }
// обратная таблица: код кодера для каждого слова (кэш)
const TP = path.join(D, "table.json");
let T; if (fs.existsSync(TP)) T = JSON.parse(fs.readFileSync(TP)); else { T = V.words.map((w) => { const e = co.encode(V.vec(w)); return [e.S, e.v]; }); fs.writeFileSync(TP, JSON.stringify(T)); }
function codeSim(S1, v1, S2, v2) {
  const wa = new Map(S1.map((r, i) => [r, [i ? 0.6 : 1, v1[i]]])), wb = new Map(S2.map((r, i) => [r, [i ? 0.6 : 1, v2[i]]]));
  let s = 0; for (const [r, [w1, x1]] of wa) if (wb.has(r)) { const [w2, x2] = wb.get(r); s += Math.sqrt(w1 * w2) * (1 - Math.abs(x1 - x2) / 10); }
  const n = (x) => Math.sqrt([...x.values()].reduce((t, [w]) => t + w, 0)); return s / (n(wa) * n(wb));
}
const z = (a) => { let mu = 0, s = 0; for (const t of a) mu += t; mu /= a.length; for (const t of a) s += (t - mu) ** 2; s = Math.sqrt(s / a.length) || 1; return a.map((t) => (t - mu) / s); };
function extras(S, v) {
  const inS = new Uint8Array(R); S.forEach((r) => (inS[r] = 1));
  const pen = new Float32Array(N), sim = new Float64Array(N);
  for (let i = 0; i < N; i++) { let mx = -9; for (let r = 0; r < R; r++) if (!inS[r] && Z[i * R + r] > mx) mx = Z[i * R + r]; pen[i] = mx; sim[i] = codeSim(S, v, T[i][0], T[i][1]); }
  return { pen, sim: z(sim) };
}
const combine = (base, ex, p) => { const out = Float64Array.from(base); for (let i = 0; i < N; i++) out[i] += -p.lam * Math.max(0, ex.pen[i] - p.tau) + p.mu * ex.sim[i]; return out; };
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
function prep(ws) { return ws.map(([w, f]) => { const e = co.encode(V.vec(w)); return { w, base: rd.roots(e.S, e.v, f), ex: extras(e.S, e.v) }; }); }
const P = { dev: prep(W.dev), r1: prep(rand.map((w) => [w, ""])), r2: prep(rand2.map((w) => [w, ""])) };
// чужие коды: только главное слово (без пар), как Reader.roots
const prepC = (cs) => cs.map((c) => { const h = c.code.split(/\b(?:PI|FROM|FOR|LIKE)\b/)[0], p = co.parse(h); return p.S.length ? { w: c.w, base: rd.roots(p.S, p.v, MM.Reader.form(h)), ex: extras(p.S, p.v) } : null; }).filter(Boolean);
const calib = prepC(JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math")));
const rec = prepC(JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code })));
const first = (set, p) => set.filter((x) => V.rankIn(combine(x.base, x.ex, p), x.w) === 1).length;
const ranks = (set, p) => set.map((x) => V.rankIn(combine(x.base, x.ex, p), x.w));
const c1 = (set, p) => set.reduce((s, x) => s + cosw(V.top(combine(x.base, x.ex, p), 1)[0].word, x.w), 0) / set.length;
const grid = [{ lam: 0, tau: 0, mu: 0 }];
for (const lam of [0.25, 0.5, 1]) for (const tau of [1, 2, 3]) grid.push({ lam, tau, mu: 0 });
for (const mu of [0.25, 0.5, 1, 2]) grid.push({ lam: 0, tau: 0, mu });
const tuned = grid.map((p) => ({ p, f: first(P.r1, p) })).sort((a, b) => b.f - a.f);
console.log("подбор на 1000:", tuned.slice(0, 6).map((t) => `${JSON.stringify(t.p)} ${t.f}`).join(" | "), "| без поправок", tuned.find((t) => !t.p.lam && !t.p.mu).f);
const bestA = tuned.find((t) => t.p.lam && !t.p.mu).p, bestB = tuned.find((t) => t.p.mu && !t.p.lam).p;
const both = [0.25, 0.5, 1].map((s) => ({ ...bestA, lam: bestA.lam * s, mu: bestB.mu })).map((p) => ({ p, f: first(P.r1, p) })).sort((a, b) => b.f - a.f)[0].p;
const out = {};
for (const [name, p] of [["сейчас", grid[0]], ["(а) сродство", bestA], ["(б) таблица", bestB], ["(а)+(б)", both]]) {
  out[name] = { p, dev: ranks(P.dev, p), r1: ranks(P.r1, p), r2: ranks(P.r2, p), calib: c1(calib, p), rec: c1(rec, p) };
  const f = (a) => a.filter((r) => r === 1).length;
  console.log(`${name} ${JSON.stringify(p)}: dev ${f(out[name].dev)} | 1000 ${f(out[name].r1)} | другие 1000 ${f(out[name].r2)} | коды моделей cos ${out[name].calib.toFixed(3)} | рецепты cos ${out[name].rec.toFixed(3)}`);
}
fs.writeFileSync(path.join(D, "results.json"), JSON.stringify(out));
