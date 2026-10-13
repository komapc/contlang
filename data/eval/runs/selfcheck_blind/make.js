// Слепой тест читаемости: коды математики без самопроверки (A) и с самопроверкой (B, голова та же, штраф 0,5).
// Слова — 100 случайных из «других 1000» (../selfcheck/results2.json), у которых коды различаются. Пара не добавляется.
// Часть речи — преобладающая по WordNet (site/data/words.json). Пишет items.json и списки кодов a/codes_K.md, b/codes_K.md (по 50).
//   node data/eval/runs/selfcheck_blind/make.js
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const sc = JSON.parse(fs.readFileSync(path.join(D, "../selfcheck/results2.json")))["самопроверка (голова та же) + штраф"].r2;
const posOf = (w) => { const i = V.index.get(w), p = [0, 1, 2, 3].map((j) => V.pos[i * 4 + j]); return p[0] < 0 ? "o" : "oiae"[p.indexOf(Math.max(...p))]; };
const strip = (c) => c.replace(/ \| .*$/, "");
const diff = sc.filter((x) => { const b = co.encode(V.vec(x.w)); return strip(co.format(b.S, b.v)) !== strip(x.code); });
let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const pick = [...diff]; for (let i = pick.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [pick[i], pick[j]] = [pick[j], pick[i]]; }
const items = pick.slice(0, 100).map((x) => { const f = posOf(x.w), b = co.encode(V.vec(x.w));
  return { w: x.w, pos: f, A: `${strip(co.format(b.S, b.v))} | ${f}`, B: `${strip(x.code)} | ${f}`, rA: V.rankIn(new MM.Reader(co, V, m.mix, { absLam: 0.5 }).roots(b.S, b.v, ""), x.w), rB: x.r }; });
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of ["a", "b"]) { fs.mkdirSync(path.join(D, v), { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(D, v, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${v === "a" ? it.A : it.B}`).join("\n") + "\n"); }
console.log(`различаются ${diff.length} из ${sc.length}; взято ${items.length}`); items.slice(0, 12).forEach((it) => console.log(it.w, "|", it.A, "|", it.B));
