// Коды 100 слов ../twowords2 кодером с перенесённым словарём (dict.json от fit.js) — так же, как вариант A там
// (Coder.encode, запрет SEX у слов без пола, имена в кавычках). → n/codes_K.md (по 50), items.json.
//   node data/eval/runs/distill/make.js
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const d = JSON.parse(fs.readFileSync(path.join(D, "dict.json"))), co0 = new MM.Coder(m.dict, m.has_axis, m.names, m), rd0 = new MM.Reader(co0, V, m.mix);
const co = new MM.Coder(d, m.has_axis, m.names, m);
const prev = JSON.parse(fs.readFileSync(path.join(D, "../twowords2/items.json")));
const items = prev.map((it) => { const w = it.w, e = co.encode(V.vec(w), 3, rd0.ban(w)); return { w, A: it.A, N: V.proper[V.index.get(w)] ? it.A : co.format(e.S, e.v, "o") }; });
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1)); fs.mkdirSync(path.join(D, "n"), { recursive: true });
for (const k of [1, 2]) fs.writeFileSync(path.join(D, "n", `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it.N}`).join("\n") + "\n");
console.log(`изменилось ${items.filter((x) => x.N !== x.A).length}/100`); items.slice(0, 8).forEach((x) => console.log(`${x.w}: ${x.A} → ${x.N}`));
