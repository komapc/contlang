// Коды трёх вариантов для items.json (dec.md); всё — математика сайта (site/math.js) и правила грамматики, без LLM.
// A — пословно: код сайта каждого слова (Reader.encode), главное слово первым (у связки — глагол первым: make decision → make, decision).
// F — свёртка в одно слово по классу:
//   deg   — код главного слова + метка интенсивности I (deg.json: very +4, slightly −2 …);
//   light — код родственного глагола (WordNet: decision → decide; из нескольких — ближайший по вектору к имени), иначе вектор имени с `| i`;
//   axis  — код главного слова, значение на общем корне сдвинуто на значение признака (его лучший одиночный корень; run fast: MOVE +2 → +4);
//           если у признака там 0, как indep с лучшим корнем признака не из кода главного слова;
//   indep — два лучших корня главного слова + лучший одиночный корень признака (со значением), форма главного слова.
// B — один код из вектора фразы Numberbatch (vecs.json), форма главного слова (у связки — `| i`).
//   node data/eval/runs/phrases2/codes.js
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const items = JSON.parse(fs.readFileSync(path.join(__dirname, "items.json"))), vecs = JSON.parse(fs.readFileSync(path.join(__dirname, "vecs.json")));
const DEG = JSON.parse(fs.readFileSync(path.join(__dirname, "deg.json"))), cand = JSON.parse(fs.readFileSync(path.join(__dirname, "cand.json")));
const dot = (a, b) => { let s = 0; for (let j = 0; j < a.length; j++) s += a[j] * b[j]; return s; };
const sig = (v) => (v > 0 ? "+" : "") + v;
const formOf = (code) => code.match(/\| ([oiae])/)[1];
const addMark = (code, mk) => code.replace(/^([^|]*\| [oiae]( agent)?)/, `$1 ${mk}`);
const best = (w) => co.singles(V.vec(w)).find((s) => s.has);
const headVec = (w, form) => (V.senseVec ? V.senseVec(w, form) : V.vec(w)) || V.vec(w);
const out = {};
for (const it of items) {
  const h = rd.encode(it.head), d = rd.encode(it.mod), form = it.cls === "light" ? "i" : formOf(h.code);
  const A = it.cls === "light" ? d.code + " " + h.code : h.code + " " + d.code;
  let F;
  if (it.cls === "deg") F = addMark(h.code, "I" + sig(DEG[it.mod]));
  else if (it.cls === "light") {
    const nv = V.vec(it.head), vs = (cand.verb_of[it.head] || []).filter((v) => V.index.has(v)).sort((a, b) => dot(V.vec(b), nv) - dot(V.vec(a), nv));
    if (vs.length) F = rd.encode(vs[0], "i").code; else { const e = co.encode(nv, 3, rd.ban(it.head)); F = co.format(e.S, e.v, "i"); }
    it.verb = vs[0] || null;
  } else if (it.cls === "axis" && best(it.mod).v !== 0) {
    const r = best(it.mod), i = h.S.indexOf(r.r), lv = co.lv[r.r], v = h.v.slice();
    const t = Math.max(-5, Math.min(5, h.v[i] + r.v)); v[i] = lv.reduce((a, b) => (Math.abs(b - t) < Math.abs(a - t) ? b : a));  // сдвиг на значение признака, в допустимых уровнях
    F = co.format(h.S, v, form) + (h.code.includes("| " + form + " agent") ? " agent" : "");
  } else {  // indep (и axis, если у признака на общем корне 0 — сдвигать нечем): лучший корень признака не из кода главного слова
    const e = co.encode(headVec(it.head, form), 2, rd.ban(it.head)), r = co.singles(V.vec(it.mod)).find((s) => s.has && (it.cls !== "axis" || !h.S.includes(s.r)));
    const S = e.S.includes(r.r) ? e.S : e.S.concat([r.r]), v = e.S.includes(r.r) ? e.v : e.v.concat([r.v]);
    F = co.format(S, v, form);
  }
  const b = co.encode(Float64Array.from(vecs[it.phrase]), 3, rd.ban(it.head));
  out[it.phrase] = { A, F, B: co.format(b.S, b.v, form) };
}
fs.writeFileSync(path.join(__dirname, "codes.json"), JSON.stringify(out, null, 0));
fs.writeFileSync(path.join(__dirname, "items.json"), JSON.stringify(items, null, 0));
for (const it of items) { const c = out[it.phrase]; console.log(it.cls.padEnd(6), it.phrase.padEnd(20), "|", c.A, "||", c.F, "||", c.B); }
