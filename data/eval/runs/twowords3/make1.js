// «Два слова» 3, шаг 1: те же 258 слов, что в ../twowords2 (цели и слова пар), — списки для моделей, которые сами пишут код
// по spec (write/task.md; у целей — толкование первого смысла). → write/list_K.md (по 40, тот же порядок, что choose/list_K.md).
//   node data/eval/runs/twowords3/make1.js
const fs = require("fs"), path = require("path"), D = __dirname, T = path.join(D, "../twowords2");
const { words, cands } = JSON.parse(fs.readFileSync(path.join(T, "cands.json"), "utf8"));
const gloss = new Map(words), all = Object.keys(cands);
for (let k = 0; k * 40 < all.length; k++)
  fs.writeFileSync(path.join(D, "write", `list_${k + 1}.md`), all.slice(k * 40, k * 40 + 40).map((w, i) => `${i + 1}. ${w}${gloss.has(w) ? " — " + gloss.get(w) : ""}`).join("\n") + "\n");
console.log(all.length);
