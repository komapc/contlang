// Кодер-«определение»: ③ главный корень — род слова, ① каждый корень (со своим значением) — правда о слове, ④ кодируется
// слово вместе с толкованием. Правда корня = z-оценка cos(x, c_r + s·v·a_r) по словарю сайта (для каждого корня и значения).
//   const def = require("./coder.js")(opt)  → def.encode(w) → { S, v, code, head, cos };  opt: { genus, truth (порог z), beta (вес толкования), on: «x» | «gloss» — по чему мерить правду и род }
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../..", "..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix), R = co.R, Dm = V.dim;
const WN = JSON.parse(fs.readFileSync(path.join(D, "wn.json")));
const dot = (a, b) => { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; };
const unit = (a) => { const n = Math.sqrt(dot(a, a)) || 1; return Float64Array.from(a, (t) => t / n); };
// части корней: P[r][k] — единичный вектор c_r + s·v·a_r для k-го уровня; статистика cos по 2000 словам словаря
const P = co.C.map((c, r) => co.lv[r].map((v) => unit(c.map((t, j) => t + co.s * v * co.A[r][j]))));
const sample = []; for (let i = 0; i < V.words.length && sample.length < 2000; i += 5) sample.push(V.vec(V.words[i]));
const ST = P.map((ps) => ps.map((p) => { const xs = sample.map((x) => dot(x, p)), mu = xs.reduce((a, b) => a + b) / xs.length; return [mu, Math.sqrt(xs.reduce((a, b) => a + (b - mu) ** 2, 0) / xs.length)]; }));
const zPart = (x, r, v) => { const k = co.lv[r].indexOf(v), [mu, sd] = ST[r][k]; return (dot(x, P[r][k]) - mu) / sd; };
const zRoot = (x, r) => Math.max(...co.lv[r].map((v) => zPart(x, r, v)));
const STOP = new Set("a an the of or and to in on for by with from that which who as at be is are was its it their this into used use any one some especially usually".split(" "));
const glossVec = (w) => { const e = WN[w]; if (!e) return null; const ts = e.gloss.toLowerCase().match(/[a-z]+/g).filter((t) => !STOP.has(t) && t !== w && V.index.has(t));
  if (!ts.length) return null; const g = new Float64Array(Dm); for (const t of ts) { const x = V.vec(t); for (let j = 0; j < Dm; j++) g[j] += x[j]; } return unit(g); };
module.exports = (opt = {}) => {
  const o = Object.assign({ genus: false, truth: null, beta: 0, on: "x" }, opt);
  const vecOf = (w) => { const x = V.vec(w), g = o.beta ? glossVec(w) : null; return g ? unit(Float64Array.from(x, (t, j) => t + o.beta * g[j])) : Float64Array.from(x); };
  function encode(w) {
    const x = vecOf(w), ban = new Set(rd.ban(w) || []), g = o.on === "gloss" ? glossVec(w) : null, t = g || x;  // t — по чему мерится правда
    let head = null;
    if (o.genus && WN[w] && WN[w].genus && V.index.has(WN[w].genus)) { const gx = V.vec(WN[w].genus);  // род: корень, правдивый и о роде, и о слове
      let b = -1e9; for (let r = 0; r < R; r++) if (!ban.has(r)) { const q = zRoot(gx, r) + zRoot(t, r); if (q > b) { b = q; head = r; } } }
    if (o.truth != null) for (let r = 0; r < R; r++) if (r !== head && zRoot(t, r) < o.truth) ban.add(r);
    const list = co.top(x, o.truth != null ? 200 : 1, 3, [...ban], head);
    const ok = (e) => o.truth == null || e.S.every((r, i) => r === head || zPart(t, r, e.v[i]) >= o.truth);
    const e = list.find(ok) || list[0];
    return { S: e.S, v: e.v, cos: e.cos, head, code: co.format(e.S, e.v, "o") };
  }
  return { encode, zPart, co, rd, V, m, WN, vecOf, glossVec };
};
