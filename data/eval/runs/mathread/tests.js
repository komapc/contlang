// Бесплатные тесты математики (README, раздел «Тесты»):
//  1 — обратное чтение: математика читает коды моделей (calib.json, рецепты);
//  2 — устойчивость: cos прочтения после малых правок кода (уровень ±1, без неглавного корня, корень → ближайший), и связь с Haiku (calib.json);
//  4 — топология: похожи ли коды близких слов (1000 случайных слов, rand1000.json — коды кодера, кэш);
//  5 — чистота корня: близок ли центр слов, в кодах которых стоит корень, к смыслу корня по спецификации (читатель по глоссам).
//   node data/eval/runs/mathread/tests.js [1245]
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, co, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const { Gloss } = require(path.join(D, "gloss.js"));
const rd = new MM.Reader(co, V, m.mix, {}), DIM = V.dim, N = V.words.length;
const which = process.argv[2] || "1245";
const dot = (a, b) => { let s = 0; for (let j = 0; j < DIM; j++) s += a[j] * b[j]; return s; };
const unit = (y) => { const n = Math.sqrt(dot(y, y)) || 1; return y.map((t) => t / n); };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const mean = (a) => a.reduce((s, x) => s + x, 0) / (a.length || 1);
const sp = (x, y) => { const rk = (a) => { const o = a.map((v, i) => [v, i]).sort((p, q) => p[0] - q[0]), r = []; o.forEach(([, i], k) => (r[i] = k)); return r; }; const a = rk(x), b = rk(y), n = a.length, ma = (n - 1) / 2; let s = 0, sa = 0, sb = 0; for (let i = 0; i < n; i++) { s += (a[i] - ma) * (b[i] - ma); sa += (a[i] - ma) ** 2; sb += (b[i] - ma) ** 2; } return s / Math.sqrt(sa * sb); };
const read1 = (code) => V.top(rd.scores(code), 1)[0].word;
const calib = JSON.parse(fs.readFileSync(path.join(D, "calib.json"))).filter((c) => V.vec(c.w));
const roots = require(path.join(D, "../../../../site/data/roots.json")).roots.map((r) => ({ name: r.name, en_axis: r.axis ? r.en : null, en_gloss: r.axis ? null : r.en }));
const out = [];
const log = (s = "") => { console.log(s); out.push(s); };

if (which.includes("1")) {
  log("## Тест 1. Математика читает коды моделей\n");
  const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code, src: "рецепты" }));
  const sets = { "коды моделей из слепых тестов (links, pi_for)": calib.filter((c) => !c.src.startsWith("math")), "рецепты": rec, "коды математики (dev)": calib.filter((c) => c.src.startsWith("math")) };
  log("| коды | n | cos первого прочтения | близко (≥ 0,5) | место ≤ 10 | Haiku cos (где есть) |\n|---|--:|--:|--:|--:|--:|");
  for (const [name, cs] of Object.entries(sets)) {
    const r = cs.map((c) => { const sc = rd.scores(c.code); return { c1: cosw(V.top(sc, 1)[0].word, c.w), rank: V.rankIn(sc, c.w) }; });
    log(`| ${name} | ${cs.length} | ${mean(r.map((x) => x.c1)).toFixed(2)} | ${r.filter((x) => x.c1 >= 0.5).length} | ${r.filter((x) => x.rank <= 10).length} | ${cs[0].c1 != null ? mean(cs.map((c) => c.c1)).toFixed(2) : "—"} |`);
  }
  log();
}

// правки кода: уровень ±1, без неглавного корня, корень → ближайший по словарю
const G = (() => { const M = co.C.map((c) => unit(c)); return M.map((a) => M.map((b) => dot(a, b))); })();
function perturb(code) {
  const ws = MM.Reader.words(code), head = ws[0].text, [hr, ...rest] = head.split("|"), tail = "|" + rest.join("|"), link = code.slice(head.length);
  const toks = [...hr.matchAll(/\b([A-Z][A-Z]+)\b(?:\(=\s*([+-]?\d+)\s*\))?/g)].filter((t) => co.names.includes(t[1]));
  const fmt = (ts) => ts.map(([n, v]) => (v != null ? `${n}(=${v > 0 ? "+" : ""}${v})` : n)).join(" ") + " " + tail + link;
  const base = toks.map((t) => [t[1], t[2] != null ? Number(t[2]) : null]), out = [];
  base.forEach(([n, v], i) => {
    if (v != null) for (const d of [-1, 1]) if (Math.abs(v + d) <= 5) out.push(fmt(base.map((t, k) => (k === i ? [n, v + d] : t))));
    if (i > 0) out.push(fmt(base.filter((_, k) => k !== i)));
    const r = co.names.indexOf(n), alt = G[r].map((s, j) => [s, j]).filter(([, j]) => j !== r && !base.some((t) => t[0] === co.names[j])).sort((a, b) => b[0] - a[0])[0][1];
    out.push(fmt(base.map((t, k) => (k === i ? [co.names[alt], co.has[alt] ? (v ?? 0) : null] : t))));
  });
  return out;
}
const vecOf = (code) => { const y = new Float64Array(DIM); for (const w of MM.Reader.words(code).slice(0, 1)) { const p = co.parse(w.text); for (const q of co.parts(p.S, p.v)) for (let j = 0; j < DIM; j++) y[j] += q[j]; } return unit(y); };
function robust(code, w) {
  const x = V.vec(w), ps = perturb(code), c0 = dot(vecOf(code), x);
  const cv = ps.map((p) => dot(vecOf(p), x)), cr = ps.map((p) => cosw(read1(p), w));
  return { c0, vec: mean(cv), vecDrop: c0 - mean(cv), read: mean(cr), read0: cosw(read1(code), w), n: ps.length };
}
if (which.includes("2")) {
  log("## Тест 2. Устойчивость кода к малым правкам\n");
  const R = calib.map((c) => ({ ...c, ...robust(c.code, c.w) }));
  const grp = { "коды моделей": R.filter((c) => !c.src.startsWith("math")), "коды математики": R.filter((c) => c.src.startsWith("math")) };
  log("| коды | n | cos вектора кода | после правок | cos прочтения | после правок |\n|---|--:|--:|--:|--:|--:|");
  for (const [g, rs] of Object.entries(grp)) log(`| ${g} | ${rs.length} | ${mean(rs.map((r) => r.c0)).toFixed(2)} | ${mean(rs.map((r) => r.vec)).toFixed(2)} | ${mean(rs.map((r) => r.read0)).toFixed(2)} | ${mean(rs.map((r) => r.read)).toFixed(2)} |`);
  log("\nСвязь с Haiku (Спирмен с cos первого ответа слепого Haiku):\n");
  for (const [k, name] of [["read", "cos прочтения после правок"], ["vec", "cos вектора после правок"], ["vecDrop", "падение cos вектора"]]) {
    log(`- ${name}: все ${sp(R.map((r) => r[k]), R.map((r) => r.c1)).toFixed(2)}, коды моделей ${sp(grp["коды моделей"].map((r) => r[k]), grp["коды моделей"].map((r) => r.c1)).toFixed(2)}, коды математики ${sp(grp["коды математики"].map((r) => r[k]), grp["коды математики"].map((r) => r.c1)).toFixed(2)}`);
  }
  log();
}

// 1000 случайных слов: коды кодера (без пар), кэш
function rand1000() {
  const f = path.join(D, "rand1000.json");
  if (fs.existsSync(f)) return JSON.parse(fs.readFileSync(f));
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const W = JSON.parse(fs.readFileSync(path.join(D, "words.json"))), skip = new Set([...W.dev, ...W.test].map((x) => x[0]));
  const pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]);
  const res = [...pick].map((i) => { const w = V.words[i], e = co.encode(V.vec(w)); return { w, S: e.S, v: e.v, code: co.format(e.S, e.v, "o") }; });
  fs.writeFileSync(f, JSON.stringify(res)); return res;
}
// сходство кодов: общие корни с весом позиции и близостью уровней
function codeSim(a, b) {
  const wa = new Map(a.S.map((r, i) => [r, [i ? 0.6 : 1, a.v[i]]])), wb = new Map(b.S.map((r, i) => [r, [i ? 0.6 : 1, b.v[i]]]));
  let s = 0; for (const [r, [w1, v1]] of wa) if (wb.has(r)) { const [w2, v2] = wb.get(r); s += Math.sqrt(w1 * w2) * (co.has[r] ? 1 - Math.abs(v1 - v2) / 10 : 1); }
  const n = (x) => Math.sqrt([...x.values()].reduce((t, [w]) => t + w, 0)); return s / (n(wa) * n(wb));
}
if (which.includes("4")) {
  log("## Тест 4. Похожи ли коды близких слов\n");
  const C = rand1000(), X = C.map((c) => V.vec(c.w));
  let seed = 9; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const pr = []; for (let k = 0; k < 20000; k++) { const i = Math.floor(rnd() * C.length), j = Math.floor(rnd() * C.length); if (i !== j) pr.push([i, j]); }
  const near = []; C.forEach((_, i) => { const s = X.map((x, j) => [j === i ? -2 : dot(X[i], x), j]).sort((a, b) => b[0] - a[0]).slice(0, 3); for (const [, j] of s) near.push([i, j]); });
  const sh = C.map((_, i) => i).sort(() => rnd() - 0.5);   // случайная перестановка кодов — нижняя граница
  for (const [name, P] of [["случайные пары", pr], ["пары «слово — 3 ближайших в наборе»", near]]) {
    const wc = P.map(([i, j]) => dot(X[i], X[j]));
    log(`- ${name} (${P.length}): Спирмен сходства кодов с cos слов ${sp(P.map(([i, j]) => codeSim(C[i], C[j])), wc).toFixed(2)}; коды переставлены случайно ${sp(P.map(([i, j]) => codeSim(C[sh[i]], C[sh[j]])), wc).toFixed(2)}; среднее сходство кодов ${mean(P.map(([i, j]) => codeSim(C[i], C[j]))).toFixed(2)}`);
  }
  log("\nПримеры: слово, ближайшее в наборе и их коды\n");
  for (const i of [0, 1, 2, 3, 4, 5, 6, 7]) { const [, j] = near[i * 3]; log(`- ${C[i].w} \`${C[i].code}\` — ${C[j].w} \`${C[j].code}\` (cos ${dot(X[i], X[j]).toFixed(2)}, сходство кодов ${codeSim(C[i], C[j]).toFixed(2)})`); }
  log();
}

if (which.includes("5")) {
  log("## Тест 5. Чистота корня\n");
  log("Для каждого корня — слова из 1000 случайных, в коде которых он главный; cos центра этих слов со смыслом корня по спецификации (имя и полюса из roots.yaml, читатель по глоссам) и с вектором корня в словаре математики. Для сравнения — те же числа по кодам моделей из слепых тестов и рецептов (корень в любой позиции).\n");
  const C = rand1000(), g = new Gloss(roots, {}), gl = {}; for (const r of roots) gl[r.name] = g.R[r.name].base;
  const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en));
  const llm = [...calib.filter((c) => !c.src.startsWith("math")).map((c) => [c.w, c.code]), ...rec.map((e) => [e.en, e.code])];
  const byM = {}, byL = {};
  for (const c of C) (byM[co.names[c.S[0]]] = byM[co.names[c.S[0]]] || []).push(c.w);
  for (const [w, code] of llm) for (const r of new Set(co.parse(MM.Reader.words(code)[0].text).S)) (byL[co.names[r]] = byL[co.names[r]] || []).push(w);
  const cen = (ws) => { const y = new Float64Array(DIM); for (const w of ws) { const v = V.vec(w); for (let j = 0; j < DIM; j++) y[j] += v[j]; } return unit(y); };
  const rows = co.names.map((n, r) => { const m = byM[n] || [], l = byL[n] || []; return { n, m: m.length, l: l.length, mg: m.length >= 3 ? dot(cen(m), gl[n]) : null, md: m.length >= 3 ? dot(cen(m), unit(co.C[r])) : null, lg: l.length >= 3 ? dot(cen(l), gl[n]) : null, ex: m.slice(0, 6).join(", ") }; });
  log("| корень | главный у слов (из 1000) | центр ↔ смысл по спецификации | центр ↔ вектор корня у математики | коды моделей: слов | центр ↔ смысл | примеры (математика) |\n|---|--:|--:|--:|--:|--:|---|");
  for (const r of rows.sort((a, b) => (a.mg ?? 9) - (b.mg ?? 9))) log(`| ${r.n} | ${r.m} | ${r.mg?.toFixed(2) ?? "—"} | ${r.md?.toFixed(2) ?? "—"} | ${r.l} | ${r.lg?.toFixed(2) ?? "—"} | ${r.ex} |`);
  const both = rows.filter((r) => r.mg != null && r.lg != null);
  log(`\nСреднее по ${both.length} корням, где есть оба: математика ${mean(both.map((r) => r.mg)).toFixed(2)}, коды моделей ${mean(both.map((r) => r.lg)).toFixed(2)}.`);
  log();
}
fs.writeFileSync(path.join(D, `tests_${which}.md`), out.join("\n") + "\n");
