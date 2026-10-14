// Код смысла кодером сайта: вектор смысла = норм(слово) + норм(среднее опорных слов), дальше как Reader.encodeWith
// (3 корня; у имени — второе слово через PI, если оно поднимает слово или его опорные слова в прочтении).  node senses.js
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), co = rd.co;
const site = JSON.parse(fs.readFileSync(path.join(__dirname, "../big1000/site_codes.json"))), out = {};
const norm = (x) => { const n = Math.hypot(...x); return x.map((t) => t / n); };
for (const it of JSON.parse(fs.readFileSync(path.join(__dirname, "items.json")))) {
  const w = it.w, sc0 = site[w], form = /\|\s*i/.test(sc0) ? "i" : "o", pl = /\| o N\+3/.test(sc0);
  out[w] = it.senses.map((s) => {
    const A = [...new Set(s.anchors)].filter((a) => { const i = V.index.get(a); return i !== undefined && !(V.stop && V.stop[i]); });
    const xw = V.vec(w), mean = new Float64Array(V.dim);
    for (const a of A) { const v = V.vec(a); for (let j = 0; j < V.dim; j++) mean[j] += v[j]; }
    const x = A.length ? Float64Array.from(norm(Array.from(xw).map((t, j) => t + norm(Array.from(mean))[j]))) : xw;
    const T = [w, ...A.slice(0, 3)], rk = (sc) => Math.min(...T.map((t) => V.rankIn(sc, t)));
    const b = co.encode(x, 3, rd.ban(w)), base = co.format(b.S, b.v, form), sc = rd.prf(rd.roots(b.S, b.v, form));
    let code = base, r = rk(sc);
    if (form === "o" && r > 1) for (const n of V.near(x, rd.opt.pairN, w)) {
      if (T.includes(n)) continue;
      const e = co.encode(V.vec(n), 2, rd.ban(n));
      if (e.S.some((q) => b.S.includes(q))) continue;
      const mc = co.format(e.S, e.v, "o"), r2 = rk(V.pair(sc, rd.readings(mc), rd.opt.pairLam));
      if (r2 < r) { r = r2; code = `${base} PI ${mc}`; }
    }
    if (pl) code = code.replace(/^([^|]*\| o)/, "$1 N+3");
    return { code, anchors: A.slice(0, 8) };
  });
}
fs.writeFileSync(path.join(__dirname, "codes.json"), JSON.stringify(out, null, 0));
