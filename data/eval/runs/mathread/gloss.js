// Читатель по глоссам — бесплатная замена слепого Haiku: корень = вектор его имени (и глоссы), уровень сдвигает к полюсу оси
// (en_axis: «-5 tiny ... +5 huge»), слово кода = сумма корней (главный 1, прочие hw), пара — второе слово с весом mw. Чтение — ближайшие слова словаря сайта.
const fs = require("fs"), path = require("path");
const { V } = require(path.join(__dirname, "../../../../scripts/site/eval_math.js"));
const D = V.dim, N = V.words.length;
function mean(words) { const y = new Float64Array(D); let k = 0; for (const w of words) { const v = V.vec(w); if (v) { k++; for (let j = 0; j < D; j++) y[j] += v[j]; } } return k ? unit(y) : null; }
function unit(y) { let n = 0; for (const t of y) n += t * t; n = Math.sqrt(n) || 1; return y.map((t) => t / n); }
const words = (s) => (s || "").toLowerCase().replace(/\([^)]*\)|`[^`]*`/g, " ").split(/[^a-z]+/).filter((w) => w.length > 2 && !["and", "the", "not", "with", "for", "one"].includes(w));
class Gloss {
  constructor(roots, opt = {}) {
    this.o = Object.assign({ hw: 0.7, mw: 0.5, pole: 1 }, opt); this.R = {};
    for (const r of roots) {
      const base = mean([r.name.toLowerCase(), ...words(r.en_gloss).slice(0, 3)]) || new Float64Array(D);
      const ax = r.en_axis || "", neg = (ax.match(/-5\s+([^.+]+?)\s*\.\.\./) || [])[1], pos = (ax.match(/\+5\s+([^.(`]+)/) || [])[1];
      const n = neg && mean(words(neg).slice(0, 2)), p = pos && mean(words(pos).slice(0, 2));
      this.R[r.name] = { base, n, p };
    }
  }
  rootVec(name, v) {
    const r = this.R[name]; if (!r) return null; const y = Float64Array.from(r.base);
    if (v != null && r.n && r.p) { const t = v / 5 * this.o.pole; for (let j = 0; j < D; j++) y[j] += t > 0 ? t * r.p[j] : -t * r.n[j]; }
    return unit(y);
  }
  wordVec(text) {
    const y = new Float64Array(D); let i = 0;
    for (const m of text.split("|")[0].matchAll(/\b([A-Z][A-Z]+)\b(?:\(=\s*([+-]?\d+)\s*\))?/g)) { const v = this.rootVec(m[1], m[2] != null ? Number(m[2]) : null); if (!v) continue; const w = i++ ? this.o.hw : 1; for (let j = 0; j < D; j++) y[j] += w * v[j]; }
    const q = (text.match(/"([^"]+)"/) || [])[1]; if (q && V.vec(q.toLowerCase())) { const v = V.vec(q.toLowerCase()); for (let j = 0; j < D; j++) y[j] += v[j]; i++; }
    return i ? unit(y) : null;
  }
  codeVec(code) {
    const parts = code.split(/\b(?:FROM|FOR|LIKE|PI)\b/), y = new Float64Array(D);
    parts.forEach((p, k) => { const v = this.wordVec(p); if (v) for (let j = 0; j < D; j++) y[j] += (k ? this.o.mw : 1) * v[j]; });
    return unit(y);
  }
  // оценки слов: cos с вектором кода; служебные убраны
  scores(code) { const y = this.codeVec(code), o = new Float64Array(N); for (let i = 0; i < N; i++) { if (V.stop[i]) { o[i] = -Infinity; continue; } let s = 0; for (let j = 0; j < D; j++) s += V.X[i * D + j] * y[j]; o[i] = s / V.norm[i]; } return o; }
}
module.exports = { Gloss, V };
