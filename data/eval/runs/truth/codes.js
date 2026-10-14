// Коды M (сайт) и T (сайт + корень TRUE из root.json: центр = норм(среднее полюсов), ось = норм(+ − −) × axis_scale)
// для слов из файла; field — частые слова (ранг 300–8000), у которых TRUE среди 3 лучших одиночных корней при cos > 0,3.
//   node codes.js words.json out.json   |   node codes.js --field out.json
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const c = JSON.parse(fs.readFileSync(path.join(__dirname, "root.json")));
const norm = (a) => { const n = Math.hypot(...a); return a.map((x) => x / n); }, mean = (ws) => { const o = new Array(m.dim).fill(0); let k = 0; for (const w of ws) { const x = V.vec(w); if (!x) continue; k++; for (let j = 0; j < m.dim; j++) o[j] += x[j]; } return [o.map((x) => x / k), k]; };
const [p, kp] = mean(c.pos), [n, kn] = mean(c.neg);
const d = { C: m.dict.C.concat([norm(p.map((x, j) => (x * kp + n[j] * kn) / (kp + kn)))]), A: m.dict.A.concat([norm(p.map((x, j) => x - n[j])).map((x) => x * c.axis_scale)]) };
const coT = new MM.Coder(d, m.has_axis.concat([true]), m.names.concat([c.name]), m), R = m.names.length;
const rdM = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), rdT = new MM.Reader(coT, V, m.mix);
if (process.argv[2] === "--field") {
  const stop = new Set(meta.stop), pr = new Set(meta.proper || []), out = [];
  for (let i = 300; i < 8000; i++) {
    if (stop.has(i) || pr.has(i)) continue;
    const x = V.vec(m.words[i]); if (!x) continue;
    const s = coT.singles(x), k = s.findIndex((t) => t.r === R);
    if (k >= 0 && k < 3 && s[k].cos > 0.3) out.push(m.words[i]);
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(out.length, "слов поля");
} else {
  const out = {};
  for (const w of JSON.parse(fs.readFileSync(process.argv[2]))) {
    const a = rdM.encode(w), b = rdT.encode(w); if (!a || a.name || !b) continue;
    out[w] = { M: a.code, T: b.code, base: a.lemma || w, rankM: a.rank, rankT: b.rank };
  }
  fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 0)); console.log(Object.keys(out).length, "слов");
}
