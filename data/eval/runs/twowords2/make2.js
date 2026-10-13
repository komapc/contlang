// «Два слова» 2, шаг 2: пары от Haiku (gen/pairs_K.md: «N. X | LINK | Y») и кандидаты кодов для выбора моделью.
// Для каждого слова (цели и слова пар) — 8 разных кодов математики: лучшие по cos (Coder.top), каждый следующий делит
// с каждым уже взятым не больше одного корня. Первый — код A (как сейчас). → cands.json, choose/list_K.md (по 40 слов).
//   node data/eval/runs/twowords2/make2.js
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const words = fs.readFileSync(path.join(D, "words.tsv"), "utf8").trim().split("\n").map((l) => l.split("\t"));
const pairs = [];
for (const k of [1, 2]) for (const l of fs.readFileSync(path.join(D, "gen", `pairs_${k}.md`), "utf8").split("\n")) {
  const t = l.match(/^\s*(\d+)\.\s*([^|]+)\|\s*(FROM|FOR|LIKE|PI)\s*\|\s*(.+)$/i); if (t) pairs[(k - 1) * 50 + Number(t[1]) - 1] = [t[2].trim().toLowerCase(), t[3].toUpperCase(), t[4].trim().toLowerCase()];
}
const div = (w, K = 8) => { const out = [];
  for (const e of co.top(V.vec(w), 300, 3, rd.ban(w))) { if (out.every((o) => e.S.filter((r) => o.S.includes(r)).length <= 1)) out.push(e); if (out.length >= K) break; }
  return out.map((e) => co.format(e.S, e.v, "o")); };
const gloss = new Map(words);
const all = [...new Set([...words.map(([w]) => w), ...pairs.flatMap((p) => (p ? [p[0], p[2]] : []))])].filter((w) => V.index.has(w) && !V.proper[V.index.get(w)]);
const cands = Object.fromEntries(all.map((w) => [w, div(w)]));
fs.writeFileSync(path.join(D, "cands.json"), JSON.stringify({ words, pairs, cands }, null, 1));
const L = "abcdefgh";
for (let k = 0; k * 40 < all.length; k++)
  fs.writeFileSync(path.join(D, "choose", `list_${k + 1}.md`), all.slice(k * 40, k * 40 + 40).map((w, i) =>
    `${i + 1}. ${w}${gloss.has(w) ? " — " + gloss.get(w) : ""}\n` + cands[w].map((c, j) => `   ${L[j]}) ${c}\n`).join("")).join("\n"));
console.log(`слов ${all.length}, списков ${Math.ceil(all.length / 40)}; нет в словаре: ${pairs.flatMap((p) => (p ? [p[0], p[2]] : [])).filter((w) => !V.index.has(w)).join(", ")}`);
