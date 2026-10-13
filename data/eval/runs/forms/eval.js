// Имена в кавычках, множественное = лемма + N+3, часть речи из WordNet (Reader.encode) против «как было» (код с | o, чтение без части речи).
// Один код, без пары PI. Имена (words.json proper) исключены из ① обоих вариантов — у них место 1 даром; считается, сколько их.
// Плюс headAbs: штраф за неупомянутый корень и у главного слова при чтении готового кода (коды моделей, рецепты).
//   node data/eval/runs/forms/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const calib = JSON.parse(fs.readFileSync(path.join(MR, "calib.json"))).filter((c) => V.vec(c.w) && !c.src.startsWith("math"));
const rec = JSON.parse(fs.readFileSync(path.join(D, "../../../../site/data/recipes.json"))).filter((e) => /^[a-z]+$/.test(e.en) && V.index.has(e.en)).map((e) => ({ w: e.en, code: e.code }));
const rd = new MM.Reader(co, V, m.mix), isName = (w) => !!V.proper[V.index.get(w)], isPl = (w) => !!V.plural[V.index.get(w)];
const one = (w, f, neu) => {
  if (!neu) { const e = co.encode(V.vec(w), 3, rd.ban(w)); return { r: V.rankIn(rd.roots(e.S, e.v, f), w), code: co.format(e.S, e.v, f || "o") }; }
  if (!f && isPl(w)) { const l = V.words[V.group[V.index.get(w)]], e = co.encode(V.vec(l), 3, rd.ban(l)); return { r: V.rankIn(rd.roots(e.S, e.v, "o"), w), code: co.format(e.S, e.v, "o N+3") }; }
  const g = f || rd.posOf(w), e = co.encode(V.vec(w), 3, rd.ban(w)); return { r: V.rankIn(rd.roots(e.S, e.v, g), w), code: co.format(e.S, e.v, g) };
};
const out = {};
for (const [name, neu] of [["как было", false], ["имена, N+3, часть речи", true]]) {
  const row = {};
  for (const [k, ws] of [["dev", W.dev], ["r1", rand.map((w) => [w, ""])], ["r2", rand2.map((w) => [w, ""])]])
    row[k] = ws.filter(([w]) => !isName(w)).map(([w, f]) => ({ w, pl: isPl(w), ...one(w, f, neu) }));
  out[name] = row;
  const f = (k) => `${row[k].filter((x) => x.r === 1).length}/${row[k].length} (мн. ${row[k].filter((x) => x.pl && x.r === 1).length}/${row[k].filter((x) => x.pl).length})`;
  console.log(`${name}: dev ${f("dev")} | 1000 ${f("r1")} | другие 1000 ${f("r2")}`);
}
console.log(`имён: 1000 ${rand.filter(isName).length}, другие 1000 ${rand2.filter(isName).length}`);
for (const ha of [false, true]) {
  const r = new MM.Reader(co, V, m.mix, { headAbs: ha }), c = (cs) => (cs.reduce((s, c) => s + cosw(V.top(r.scores(c.code), 1)[0].word, c.w), 0) / cs.length).toFixed(3);
  const t1 = (cs) => cs.filter((c) => V.rankIn(r.scores(c.code), c.w) === 1).length;
  console.log(`headAbs ${ha}: коды моделей cos ${c(calib)} первыми ${t1(calib)}/${calib.length} | рецепты cos ${c(rec)} первыми ${t1(rec)}/${rec.length}`);
}
fs.writeFileSync(path.join(D, "results.json"), JSON.stringify(out));
