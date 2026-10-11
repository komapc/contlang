// Слепая проверка эхо-уровней: коды кодера сайта (A, THING и SEX уже ограничены) и с запретом слабых уровней у эхо-корней (B)
// на словах own8k.json (не dev/test/rand1000), берутся только слова, у которых код изменился; листы по 20, A и B в разном порядке.
//   node data/eval/runs/echo/make.js [папка для листов]
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, co, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const R5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], strong = (k) => R5.filter((v) => Math.abs(v) >= 3 || (k && v === 0));
const ECHO = { SAY: strong(1), CARE: strong(1), TONE: strong(1), GRAIN: strong(1), FEEL: strong(0), GOOD: strong(0), KNOW: strong(0) };
const coB = new MM.Coder(m.dict, m.has_axis, m.names, { ...m, levels: { ...m.levels, ...ECHO } });
const rdA = new MM.Reader(co, V, m.mix, {}), rdB = new MM.Reader(coB, V, m.mix, {});
const own = JSON.parse(fs.readFileSync(path.join(D, "../anchor/own8k.json"))), out = process.argv[2], res = [];
for (const [w, c] of own) {
  if (res.length >= 60) break;
  if (!/\b(SAY|CARE|TONE|GRAIN|FEEL|GOOD|KNOW)\(=[+-]?[12]\)/.test(c) && !/\b(FEEL|GOOD|KNOW)\(=0\)/.test(c)) continue;   // B отличается только там, где A брал запрещённый уровень
  const form = c.split("|").pop().trim().split(/\s+/)[0], a = rdA.encode(w, form), b = rdB.encode(w, form);
  if (a.code !== b.code && !/\b(FROM|FOR|LIKE|PI)\b/.test(a.code + b.code)) res.push({ w, form, A: a.code, B: b.code, rA: V.rankIn(rdA.scores(a.code), w), rB: V.rankIn(rdB.scores(b.code), w) });
}
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const key = {};
for (const v of ["A", "B"]) {
  const ids = res.map((_, i) => i).sort(() => rnd() - 0.5);
  for (let s = 0; s < 3; s++) {
    const name = `echo_${v}_${s + 1}`, part = ids.slice(20 * s, 20 * s + 20);
    key[name] = part.map((i) => res[i].w);
    const txt = part.map((i, k) => `${k + 1}. ${res[i][v]}`).join("\n") + "\n";
    fs.writeFileSync(path.join(D, `sheet_${name}.md`), txt); if (out) { fs.mkdirSync(out, { recursive: true }); fs.writeFileSync(path.join(out, `list_${name}.md`), txt); }
  }
}
fs.writeFileSync(path.join(D, "codes.json"), JSON.stringify(res, null, 1)); fs.writeFileSync(path.join(D, "key.json"), JSON.stringify(key, null, 1));
const lo = (r) => r.filter((x) => x === 1).length;
console.log(`слов ${res.length}; математика первыми: A ${lo(res.map((x) => x.rA))}, B ${lo(res.map((x) => x.rB))}`);
for (const x of res.slice(0, 12)) console.log(x.w.padEnd(14), x.A.padEnd(46), "→", x.B);
