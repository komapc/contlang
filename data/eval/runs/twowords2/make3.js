// «Два слова» 2, шаг 3: выбор модели (choose/ans_K.md: «N. буква» к choose/list_K.md) → коды вариантов и списки для слепых читателей.
// A — один код математики (первый кандидат, как сейчас); B — один код, выбранный моделью;
// C — код_A(X) | o LINK код_A(Y) | o; D — то же с кодами, выбранными моделью; E — пара словами.
// Пара со словом не из словаря — код A (в C) и B (в D). → items.json, a/ … e/codes_K.md (по 50).
//   node data/eval/runs/twowords2/make3.js
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const { words, pairs, cands } = JSON.parse(fs.readFileSync(path.join(D, "cands.json"), "utf8"));
const all = Object.keys(cands), pick = {};
for (let k = 0; k * 40 < all.length; k++) for (const l of fs.readFileSync(path.join(D, "choose", `ans_${k + 1}.md`), "utf8").split("\n")) {
  const t = l.match(/^\s*(\d+)\.\s*\(?([a-h])\b/i); if (t) { const w = all[k * 40 + Number(t[1]) - 1]; if (w) pick[w] = "abcdefgh".indexOf(t[2].toLowerCase()); }
}
const one = (w, ch) => (V.index.has(w) && V.proper[V.index.get(w)] ? `"${w[0].toUpperCase()}${w.slice(1)}"` : cands[w] ? cands[w][ch ? pick[w] ?? 0 : 0] : null);
const items = words.map(([w, g], i) => {
  const p = pairs[i], A = one(w, false), B = one(w, true);
  const pc = (ch) => { const x = p && one(p[0], ch), y = p && one(p[2], ch); return x && y ? `${x} ${p[1]} ${y}` : null; };
  const C = pc(false) || A, Dd = pc(true) || B, r = (c) => V.rankIn(rd.scores(c), w);
  return { w, g, pair: p ? p.join(" ") : null, A, B, C, D: Dd, E: p ? p.join(" ") : w, rA: r(A), rB: r(B), rC: r(C), rD: r(Dd) };
});
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of "ABCDE") { const d = path.join(D, v.toLowerCase()); fs.mkdirSync(d, { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(d, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${v === "E" ? it.E.replace(/ (FROM|FOR|LIKE|PI) /, " $1 ") : it[v]}`).join("\n") + "\n"); }
const first = (k) => items.filter((x) => x[k] === 1).length, gm = (k) => Math.round(Math.exp(items.reduce((s, x) => s + Math.log(x[k]), 0) / items.length));
console.log(`выбрано ${Object.keys(pick).length}/${all.length}, не первый кандидат ${Object.values(pick).filter((x) => x > 0).length}; пар нет: ${items.filter((x) => !x.pair).length}`);
for (const k of ["rA", "rB", "rC", "rD"]) console.log(`${k}: первыми ${first(k)}, место (геом.) ${gm(k)}`);
items.slice(0, 12).forEach((x) => console.log(`${x.w}: A ${x.A} | B ${x.B} | D ${x.D}`));
