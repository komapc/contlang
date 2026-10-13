// «Два слова» 3, шаг 2: коды, написанные моделью (write/ans_K.md: «N. код»), и разбор пары по частям.
// F — X словом, Y кодом, выбранным моделью (вариант D ../twowords2); G — X кодом, выбранным моделью, Y словом;
// H — один код, написанный моделью; I — пара кодами, написанными моделью. → items.json, f/ … i/codes_K.md (по 50).
//   node data/eval/runs/twowords3/make2.js
const fs = require("fs"), path = require("path"), D = __dirname, T = path.join(D, "../twowords2");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const { cands } = JSON.parse(fs.readFileSync(path.join(T, "cands.json"), "utf8")), all = Object.keys(cands);
const prev = JSON.parse(fs.readFileSync(path.join(T, "items.json"), "utf8")), wrote = {};
for (let k = 0; k * 40 < all.length; k++) for (const l of fs.readFileSync(path.join(D, "write", `ans_${k + 1}.md`), "utf8").split("\n")) {
  const t = l.match(/^\s*(\d+)\.\s*`?([^`]+?)`?\s*$/); if (t && all[k * 40 + Number(t[1]) - 1]) wrote[all[k * 40 + Number(t[1]) - 1]] = t[2].trim();
}
// код слова пары в D: часть строки D до / после LINK
const split = (c, link) => { const j = c.indexOf(` ${link} `); return j < 0 ? null : [c.slice(0, j), c.slice(j + link.length + 2)]; };
const r = (c) => { try { return V.rankIn(rd.scores(c), w0); } catch { return null; } }; let w0;
const items = prev.map((it) => {
  w0 = it.w; const p = it.pair.split(" "), [x, link, y] = [p[0], p[1], p[2]], d = split(it.D, link);
  const F = d ? `${x} ${link} ${d[1]}` : it.D, G = d ? `${d[0]} ${link} ${y}` : it.D;
  const H = wrote[it.w] || it.A, I = wrote[x] && wrote[y] ? `${wrote[x]} ${link} ${wrote[y]}` : H;
  return { w: it.w, pair: it.pair, D: it.D, F, G, H, I, rH: r(H), rI: r(I), rA: it.rA };
});
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of "FGHI") { const d = path.join(D, v.toLowerCase()); fs.mkdirSync(d, { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(d, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it[v]}`).join("\n") + "\n"); }
const vals = Object.values(wrote), cnt = (re) => vals.filter((c) => re.test(c)).length;
console.log(`написано ${vals.length}/${all.length}; с agent ${cnt(/\bagent\b/)}, tool ${cnt(/\btool\b/)}, result ${cnt(/\bresult\b/)}, quality ${cnt(/\bquality\b/)}, в кавычках ${cnt(/"/)}`);
const ok = items.filter((x) => x.rH), gm = (k) => Math.round(Math.exp(ok.reduce((s, x) => s + Math.log(x[k] || 5000), 0) / ok.length));
console.log(`векторами: A ${gm("rA")}, H ${gm("rH")}, I ${gm("rI")}`);
items.slice(0, 10).forEach((x) => console.log(`${x.w}: H ${x.H} | I ${x.I}`));
