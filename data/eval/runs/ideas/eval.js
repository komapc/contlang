// Две простые идеи (README):
//  1) корень с осью без значения = «любая степень»: оценка слова — максимум по значениям −5…+5 этого корня (до 2 таких корней), а не значение 0;
//  2) короткие коды математики: из кодов в 1, 2, 3 корня берётся самый короткий, у которого место слова не хуже (или хуже не больше чем на tol).
//   node data/eval/runs/ideas/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix, {});
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const gm = (a) => Math.exp(a.reduce((s, x) => s + Math.log(x), 0) / a.length);
const AX = new Set(m.names.filter((_, r) => m.has_axis[r]));
// ---- 1
const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code }));
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math")).map((c) => ({ w: c.w, code: c.code }));
function anyLevel(code) {
  const head = code.split("|")[0], rest = code.slice(head.length), bare = [];
  head.replace(/\b([A-Z][A-Z]+)\b(?!\(=)/g, (s, n, off) => { if (AX.has(n)) bare.push([n, off]); return s; });
  if (!bare.length || bare.length > 2) return rd.scores(code);
  let best = null;
  const L = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], combos = bare.length === 1 ? L.map((a) => [a]) : L.flatMap((a) => L.map((b) => [a, b]));
  for (const vs of combos) {
    let h = head, shift = 0;
    bare.forEach(([n, off], k) => { const ins = `${n}(=${vs[k]})`, o = off + shift; h = h.slice(0, o) + ins + h.slice(o + n.length); shift += ins.length - n.length; });
    const sc = rd.scores(h + rest); if (!best) best = Float64Array.from(sc); else for (let i = 0; i < sc.length; i++) if (sc[i] > best[i]) best[i] = sc[i];
  }
  return best;
}
for (const [name, cs] of [["рецепты", rec], ["коды моделей", calib]]) {
  const bareCodes = cs.filter((c) => [...c.code.split("|")[0].matchAll(/\b([A-Z][A-Z]+)\b(?!\(=)/g)].some((x) => AX.has(x[1])));
  for (const [lab, f] of [["значение 0 (сейчас)", (c) => rd.scores(c)], ["любая степень", anyLevel]]) {
    const res = bareCodes.map((c) => { const sc = f(c.code); return { r: V.rankIn(sc, c.w), c: cosw(V.top(sc, 1)[0].word, c.w) }; });
    console.log(`1) ${name}, коды с корнем без значения (${bareCodes.length}): ${lab}: место ${gm(res.map((x) => x.r)).toFixed(1)}, первыми ${res.filter((x) => x.r === 1).length}, top10 ${res.filter((x) => x.r <= 10).length}, cos ${(res.reduce((s, x) => s + x.c, 0) / res.length).toFixed(3)}`);
    fs.writeFileSync(path.join(D, `any_${name === "рецепты" ? "rec" : "calib"}_${lab.startsWith("любая") ? "any" : "zero"}.json`), JSON.stringify(res.map((x, i) => ({ w: bareCodes[i].w, code: bareCodes[i].code, ...x }))));
  }
}
// ---- 2
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const rows = rand2.map((w) => { const x = V.vec(w); return [1, 2, 3].map((k) => { const e = co.encode(x, k); return { n: e.S.length, r: V.rankIn(rd.roots(e.S, e.v, ""), w) }; }); });
fs.writeFileSync(path.join(D, "short_r2.json"), JSON.stringify(rand2.map((w, i) => ({ w, opts: rows[i] }))));
for (const tol of [1, 1.5, 2, 3]) {
  const pick = rows.map((o) => { const best = Math.min(...o.map((x) => x.r)); return o.find((x) => x.r <= best * tol); });
  console.log(`2) другие 1000, кратчайший код с местом ≤ ${tol}× лучшего: корней в среднем ${(pick.reduce((s, x) => s + x.n, 0) / 1000).toFixed(2)}, первыми ${pick.filter((x) => x.r === 1).length}, место ${gm(pick.map((x) => x.r)).toFixed(2)}`);
}
const cur = rows.map((o) => o[2]);
console.log(`2) сейчас (до 3 корней): корней в среднем ${(cur.reduce((s, x) => s + x.n, 0) / 1000).toFixed(2)}, первыми ${cur.filter((x) => x.r === 1).length}, место ${gm(cur.map((x) => x.r)).toFixed(2)}`);
