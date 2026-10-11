// Коды математики для слов набора (words.json) и их чтение математикой (круг ①); листы для слепого чтения Haiku (②).
//   node data/eval/runs/mathread/make_codes.js dev [вариант] [папка декодеров]
// codes_<набор>_<вариант>.json: [{w, form, code, pair, rank, top, cos1, roots: [{name, single}], ...}]; sheet_NN.md — 20 кодов в случайном порядке, key.json — слова листов.
const fs = require("fs"), path = require("path");
const D = __dirname, { V, co, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const [set = "dev", variant = "base", out] = process.argv.slice(2);
const words = JSON.parse(fs.readFileSync(path.join(D, "words.json")))[set];
const rd = new MM.Reader(co, V, m.mix, {});
const cos = (a, b) => { const x = V.vec(a), y = V.vec(b); if (!x || !y) return 0; let s = 0; for (let j = 0; j < x.length; j++) s += x[j] * y[j]; return s; };
const res = words.map(([w, form]) => {
  const e = rd.encode(w, form), sc = rd.scores(e.code), top = V.top(sc, 5).map((t) => t.word), x = V.vec(w), sg = co.singles(x);
  const p = rd.parse(e.code);
  return { w, form, code: e.code, pair: e.mod, rank: V.rankIn(sc, w), rank0: e.rank0, top, cos1: cos(top[0], w),
    roots: p.S.map((r, i) => ({ name: co.names[r], v: p.v[i], single: sg.find((t) => t.r === r).cos, place: sg.findIndex((t) => t.r === r) + 1 })) };
});
fs.writeFileSync(path.join(D, `codes_${set}_${variant}.json`), JSON.stringify(res, null, 1));
let seed = 3; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const order = res.map((_, i) => i).sort(() => rnd() - 0.5), key = {};
for (let s = 0; s * 20 < order.length; s++) {
  const ids = order.slice(s * 20, s * 20 + 20), name = `${set}_${variant}_${String(s + 1).padStart(2, "0")}`;
  key[name] = ids.map((i) => res[i].w);
  fs.writeFileSync(path.join(D, `sheet_${name}.md`), ids.map((i, k) => `${k + 1}. ${res[i].code}`).join("\n") + "\n");
  if (out) { fs.mkdirSync(out, { recursive: true }); fs.copyFileSync(path.join(D, `sheet_${name}.md`), path.join(out, `list_${name}.md`)); }
}
fs.writeFileSync(path.join(D, `key_${set}_${variant}.json`), JSON.stringify(key, null, 1));
const r = res.map((x) => x.rank).sort((a, b) => a - b);
console.log(`${set}/${variant}: слов ${res.length}, первыми ${r.filter((x) => x === 1).length}, top10 ${r.filter((x) => x <= 10).length}, медиана ${r[r.length >> 1]}, cos первого ${(res.reduce((s, x) => s + x.cos1, 0) / res.length).toFixed(2)}, пар ${res.filter((x) => x.pair).length}`);
