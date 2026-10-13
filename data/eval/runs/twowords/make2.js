// «Два слова», шаг 2: пары от Haiku (gen/pairs_K.md: «N. X | LINK | Y») кодируются математикой.
// A — один код слова; B — код(X) | o LINK код(Y) | o (пара от модели); C — что сейчас делает сайт (Reader.encode: код или код PI сосед).
// Место слова при чтении векторами (Reader.scores) и списки кодов для слепых читателей a/, b/, c/ (codes_K.md по 50). → items.json
//   node data/eval/runs/twowords/make2.js
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const words = fs.readFileSync(path.join(D, "words.txt"), "utf8").trim().split("\n");
const pairs = [];
for (const k of [1, 2]) for (const l of fs.readFileSync(path.join(D, "gen", `pairs_${k}.md`), "utf8").split("\n")) {
  const t = l.match(/^\s*(\d+)\.\s*([^|]+)\|\s*(FROM|FOR|LIKE|PI)\s*\|\s*(.+)$/i); if (t) pairs[(k - 1) * 50 + Number(t[1]) - 1] = [t[2].trim().toLowerCase(), t[3].toUpperCase(), t[4].trim().toLowerCase()];
}
const single = (w) => {
  const i = V.index.get(w); if (i === undefined) return null;
  if (V.proper[i]) return `"${w[0].toUpperCase()}${w.slice(1)}"`;
  const e = co.encode(V.vec(w), 3, rd.ban(w)); return co.format(e.S, e.v, "o");
};
const items = words.map((w, i) => {
  const p = pairs[i], A = single(w), cx = p && single(p[0]), cy = p && single(p[2]);
  const B = cx && cy ? `${cx} ${p[1]} ${cy}` : null, C = rd.encode(w, "o").code;
  const r = (c) => (c ? V.rankIn(rd.scores(c), w) : null);
  return { w, pair: p ? p.join(" ") : null, A, B, C, rA: r(A), rB: r(B), rC: r(C) };
});
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of ["A", "B", "C"]) { const d = path.join(D, v.toLowerCase()); fs.mkdirSync(d, { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(d, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it[v] || it.A}`).join("\n") + "\n"); }
const ok = items.filter((x) => x.B), first = (k) => ok.filter((x) => x[k] === 1).length, gm = (k) => Math.round(Math.exp(ok.reduce((s, x) => s + Math.log(x[k]), 0) / ok.length));
console.log(`пар закодировано ${ok.length}/100 (нет в словаре: ${items.filter((x) => !x.B).map((x) => x.pair).join("; ")})`);
for (const k of ["rA", "rB", "rC"]) console.log(`${k}: первыми ${first(k)}, место (геом.) ${gm(k)}`);
items.slice(0, 15).forEach((x) => console.log(`${x.w}: ${x.pair} | B ${x.B} (${x.rB}) | A ${x.rA} C ${x.rC}`));
