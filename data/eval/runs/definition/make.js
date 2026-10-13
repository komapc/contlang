// Коды 100 слов ../twowords2 для слепого теста из eval.json: s — только толкование (β 1), gts — род + правда (τ 0,5) + толкование (β 1).
// Слова без кода (имена) — код A. → s/codes_K.md, gts/codes_K.md, items.json
//   node data/eval/runs/definition/make.js
const fs = require("fs"), path = require("path"), D = __dirname;
const ev = JSON.parse(fs.readFileSync(path.join(D, "eval.json"))), prev = JSON.parse(fs.readFileSync(path.join(D, "../twowords2/items.json")));
const items = prev.map((it) => ({ w: it.w, A: it.A, S: ev.S[it.w]?.code || it.A, GTS: ev.GTS[it.w]?.code || it.A }));
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of ["S", "GTS"]) { fs.mkdirSync(path.join(D, v.toLowerCase()), { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(D, v.toLowerCase(), `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it[v]}`).join("\n") + "\n"); }
console.log(`S ≠ A: ${items.filter((x) => x.S !== x.A).length}, GTS ≠ A: ${items.filter((x) => x.GTS !== x.A).length}, без кода: ${prev.filter((it) => !ev.S[it.w]).map((it) => it.w)}`);
