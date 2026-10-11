// Сравнение вариантов словаря (dicts.py) по бесплатным мерам:
//  ① круг математики: dev (100 слов, часть речи известна) и 1000 случайных слов (rand1000, без пар) — первыми, cos первого прочтения;
//  тест 1 — математика читает коды моделей (слепые тесты links/pi_for и рецепты): cos первого прочтения, близко (≥ 0,5);
//  тест 2 — прочтение своих кодов (dev) после малых правок; тест 4 — сходство кодов близких слов (Спирмен).
//   node data/eval/runs/anchor/eval.js learned poles name spec ...
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const DIM = V.dim, dot = (a, b) => { let s = 0; for (let j = 0; j < DIM; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const mean = (a) => a.reduce((s, x) => s + x, 0) / (a.length || 1);
const sp = (x, y) => { const rk = (a) => { const o = a.map((v, i) => [v, i]).sort((p, q) => p[0] - q[0]), r = []; o.forEach(([, i], k) => (r[i] = k)); return r; }; const a = rk(x), b = rk(y), n = a.length, ma = (n - 1) / 2; let s = 0, sa = 0, sb = 0; for (let i = 0; i < n; i++) { s += (a[i] - ma) * (b[i] - ma); sa += (a[i] - ma) ** 2; sb += (b[i] - ma) ** 2; } return s / Math.sqrt(sa * sb); };
const dev = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))).dev;
const rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
// ещё 1000 случайных слов, не из rand1000 (его коды — «свои коды» в fit.py, поэтому там ① не отложенный)
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647, W = JSON.parse(fs.readFileSync(path.join(MR, "words.json")));
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math"));
const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code }));
function perturb(co, S, v, form) {
  const out = [], G = co.G;
  S.forEach((r, i) => {
    if (co.has[r]) for (const d of [-1, 1]) if (Math.abs(v[i] + d) <= 5) out.push([S, v.map((x, k) => (k === i ? x + d : x))]);
    if (i > 0) out.push([S.filter((_, k) => k !== i), v.filter((_, k) => k !== i)]);
    const alt = G[r].slice(0, co.R).map((s, j) => [s, j]).filter(([, j]) => j !== r && !S.includes(j)).sort((a, b) => b[0] - a[0])[0][1];
    out.push([S.map((x, k) => (k === i ? alt : x)), v.map((x, k) => (k === i ? (co.has[alt] ? x : 0) : x))]);
  });
  return out;
}
function codeSim(a, b) {
  const wa = new Map(a.S.map((r, i) => [r, [i ? 0.6 : 1, a.v[i]]])), wb = new Map(b.S.map((r, i) => [r, [i ? 0.6 : 1, b.v[i]]]));
  let s = 0; for (const [r, [w1, v1]] of wa) if (wb.has(r)) { const [w2, v2] = wb.get(r); s += Math.sqrt(w1 * w2) * (1 - Math.abs(v1 - v2) / 10); }
  const n = (x) => Math.sqrt([...x.values()].reduce((t, [w]) => t + w, 0)); return s / (n(wa) * n(wb));
}
const rows = [];
for (const name of process.argv.slice(2)) {
  const t0 = Date.now(), dd = JSON.parse(fs.readFileSync(path.join(D, `dict_${name}.json`)));
  const co = new MM.Coder({ C: dd.C, A: dd.A }, m.has_axis, m.names, m), rd = new MM.Reader(co, V, { ...m.mix, hub: dd.hub }, {});
  const read = (S, v, f) => rd.roots(S, v, f);
  // ① dev (с частью речи, без пар — пары меряются отдельно) и 1000 случайных
  const dv = dev.map(([w, f]) => { const e = co.encode(V.vec(w)), sc = read(e.S, e.v, f); return { w, f, S: e.S, v: e.v, r: V.rankIn(sc, w), c1: cosw(V.top(sc, 1)[0].word, w) }; });
  const rn = rand.map((w) => { const e = co.encode(V.vec(w)), sc = read(e.S, e.v, ""); return { w, S: e.S, v: e.v, r: V.rankIn(sc, w), c1: cosw(V.top(sc, 1)[0].word, w) }; });
  const r2 = rand2.map((w) => { const e = co.encode(V.vec(w)), sc = read(e.S, e.v, ""); return { w, S: e.S, v: e.v, r: V.rankIn(sc, w), c1: cosw(V.top(sc, 1)[0].word, w) }; });
  // тест 1
  const t1 = (cs) => cs.map((c) => cosw(V.top(rd.scores(c.code), 1)[0].word, c.w));
  const a1 = t1(calib), a2 = t1(rec);
  // тест 2 (dev)
  const t2 = mean(dv.map((c) => mean(perturb(co, c.S, c.v).map(([S, v]) => cosw(V.top(read(S, v, c.f), 1)[0].word, c.w)))));
  // тест 4 (отложенные 1000: слово и 3 ближайших; на rand1000 — t4in, там подгонка видела коды)
  const T4 = (rs) => { const X = rs.map((c) => V.vec(c.w)), P = []; rs.forEach((_, i) => X.map((x, j) => [j === i ? -2 : dot(X[i], x), j]).sort((a, b) => b[0] - a[0]).slice(0, 3).forEach(([, j]) => P.push([i, j])));
    return sp(P.map(([i, j]) => codeSim(rs[i], rs[j])), P.map(([i, j]) => dot(X[i], X[j]))); };
  const t4 = T4(r2), t4in = T4(rn);
  const r = { name, dev1: dv.filter((c) => c.r === 1).length, devc: mean(dv.map((c) => c.c1)), rnd1: rn.filter((c) => c.r === 1).length, rndc: mean(rn.map((c) => c.c1)), rnd2: r2.filter((c) => c.r === 1).length, rnd2c: mean(r2.map((c) => c.c1)),
    t1b: mean(a1), t1bn: a1.filter((c) => c >= 0.5).length, t1r: mean(a2), t1rn: a2.filter((c) => c >= 0.5).length, t2, t4, t4in, sec: (Date.now() - t0) / 1000 };
  rows.push(r);
  console.log(JSON.stringify(r));
  fs.writeFileSync(path.join(D, `codes_dev_${name}.json`), JSON.stringify(dv.map((c) => ({ w: c.w, form: c.f, code: co.format(c.S, c.v, c.f), rank: c.r, c1: c.c1 })), null, 0));
}
console.log("\n| словарь | ① dev первыми | ① dev cos | ① 1000 первыми | ① 1000 cos | ① другие 1000 первыми | cos | тест 1: коды моделей cos (близко из " + calib.length + ") | тест 1: рецепты cos (близко из " + rec.length + ") | тест 2 | тест 4 |\n|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|");
for (const r of rows) console.log(`| ${r.name} | ${r.dev1} | ${r.devc.toFixed(2)} | ${r.rnd1} | ${r.rndc.toFixed(2)} | ${r.rnd2} | ${r.rnd2c.toFixed(2)} | ${r.t1b.toFixed(2)} (${r.t1bn}) | ${r.t1r.toFixed(2)} (${r.t1rn}) | ${r.t2.toFixed(2)} | ${r.t4.toFixed(2)} |`);
