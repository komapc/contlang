// V2: кодер сайта с уровнями −5, 0, +5 (0 — голый корень), 2 корня, третий при приросте cos > δ (70-й перцентиль); пара PI как на сайте.
// V3: то же + роль из items.json.  node enc.js → codes.json {w: {A, V2, V3}}
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const levels = {}; m.names.forEach((n, r) => { if (m.has_axis[r]) levels[n] = n === "THING" ? [-5, 0, 4] : n === "SEX" ? [-5, 5] : [-5, 0, 5]; });
const co = new MM.Coder(m.dict, m.has_axis, m.names, Object.assign({}, m, { levels })), rd = new MM.Reader(co, V, m.mix);
const fmt = (S, v, form) => S.map((r, i) => (co.has[r] && v[i] ? `${co.names[r]}(=${v[i] > 0 ? "+" : ""}${v[i]})` : co.names[r])).join(" ") + ` | ${form}`;
const site = JSON.parse(fs.readFileSync(path.join(__dirname, "../big1000/site_codes.json"))), its = JSON.parse(fs.readFileSync(path.join(__dirname, "items.json")));
const rows = its.map((it) => {
  const w = it.w, A = site[w], form = (A.match(/\|\s*([oiae])/) || [, "o"])[1], pl = /^[^|]*\| o N\+3/.test(A), i = V.index.get(w);
  const wl = pl && V.group[i] !== i ? V.words[V.group[i]] : w, x = V.vec(wl), ban = rd.ban(wl);
  const e2 = co.encode(x, 2, ban), e3 = co.encode(x, 3, ban);
  return { it, w, wl, A, form, pl, x, ban, e2, e3, gain: e3.cos - e2.cos };
});
const g = rows.map((r) => r.gain).sort((a, b) => a - b), delta = g[Math.floor(0.7 * g.length)], out = {};
for (const r of rows) {
  const b = r.gain > delta && r.e3.S.length === 3 ? r.e3 : r.e2, base = fmt(b.S, b.v, r.form), sc = rd.roots(b.S, b.v, r.form);
  let mod = "", rank = V.rankIn(sc, r.wl);
  if (r.form === "o" && rank > 1) for (const n of V.near(r.x, rd.opt.pairN, r.wl)) {
    const e = co.encode(V.vec(n), 2, rd.ban(n));
    if (e.S.some((q) => b.S.includes(q))) continue;
    const mc = fmt(e.S, e.v, "o"), r2 = V.rankIn(V.pair(sc, rd.readings(mc), rd.opt.pairLam), r.wl);
    if (r2 < rank) { rank = r2; mod = ` PI ${mc}`; }
  }
  const mk = (role) => base + (role ? ` ${role}` : "") + (r.pl ? " N+3" : "") + mod;
  out[r.w] = { A: r.A, V2: mk(""), V3: r.it.role ? mk(r.it.role) : null };
}
fs.writeFileSync(path.join(__dirname, "codes.json"), JSON.stringify(out, null, 1));
console.log("δ", delta.toFixed(4), "3 корня:", Object.values(out).filter((o) => o.V2.split("|")[0].trim().split(" ").length === 3).length);
