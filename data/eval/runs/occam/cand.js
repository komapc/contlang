// Все наборы корней (1–3 из topr 12) для слов: та же база, форма, метки, роль и вектор смысла, что у Reader.encode, с cos.
//   node cand.js words.json → cand.json {w: {site, cands: [{code, cos, S, v}]}}
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const rd = new MM.Reader(new MM.Coder(m.dict, m.has_axis, m.names, m), V, m.mix), co = new MM.Coder(m.dict, m.has_axis, m.names, { ...m, topr: 12 });
const words = JSON.parse(fs.readFileSync(process.argv[2])), out = {};
for (const w of words) {
  const e = rd.encode(w); if (!e || e.name) continue;
  const b = e.lemma || w, fo = e.form || "o", x = V.senseVec(b, fo), tail = e.code.slice(e.code.indexOf("|") + 1).trim();
  const cands = co.top(x, 5000, 3, rd.ban(b)).map((t) => ({ code: co.format(t.S, t.v, fo).replace(/\|.*$/, "| " + tail), cos: t.cos, k: t.S.length,
    zh: t.S.filter((r, i) => i > 0 && m.has_axis[r] && t.v[i] === 0).length, z: t.S.filter((r, i) => m.has_axis[r] && t.v[i] === 0).length }));
  out[w] = { site: e.code, base: b, form: fo, cands };
}
fs.writeFileSync(path.join(__dirname, "cand.json"), JSON.stringify(out));
console.log(Object.keys(out).length, "слов");
