// Род по таксономии (anchors.py → heads.json) и проверка диагноза.
// T — главный корень и его значение из таблицы (значение None — голый корень), остальные (до 2) математика подбирает
//     векторами (Coder.top с обязательным главным); у слова без рода — код A. v = 0 у уточнений печатается голым корнем
//     (центр корня — его простой смысл), (=0) остаётся только там, где таблица имеет в виду середину оси (THING(=0) plant).
// M — диагноз: корни и их порядок из кода модели H (../twowords3), значения подбирает математика; форма — как у H.
// → items.json, t/codes_K.md, mr/codes_K.md
//   node data/eval/runs/taxonomy/make.js
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const HD = JSON.parse(fs.readFileSync(path.join(D, "heads.json"))), prev = JSON.parse(fs.readFileSync(path.join(D, "../twowords2/items.json")));
const H = Object.fromEntries(JSON.parse(fs.readFileSync(path.join(D, "../twowords3/items.json"))).map((x) => [x.w, x.H]));
const cache = {}, coFor = (lv) => { const k = JSON.stringify(lv); return cache[k] || (cache[k] = new MM.Coder(m.dict, m.has_axis, m.names, Object.assign({}, m, { levels: Object.assign({}, m.levels, lv) }))); };
const fmt = (S, v, mid) => S.map((r, i) => (!co.has[r] ? co.names[r] : v[i] === 0 ? (i === 0 && mid ? `${co.names[r]}(=0)` : co.names[r]) : `${co.names[r]}(=${v[i] > 0 ? "+" : ""}${v[i]})`)).join(" ");
const items = prev.map((it) => {
  const w = it.w, x = V.vec(w), ban = rd.ban(w), h = HD[w];
  let T = it.A;
  if (h) { const r = m.names.indexOf(h.root), c = coFor(co.has[r] ? { [h.root]: [h.v ?? 0] } : {}), e = c.encode(x, 3, (ban || []).filter((b) => b !== r), r); T = fmt(e.S, e.v, h.v === 0) + " | o"; }
  // M: корни H в их порядке, значения — лучшие по cos
  const hp = co.parse(H[w] || ""), form = (H[w] || "").includes("|") ? H[w].slice(H[w].indexOf("|")) : "| o";
  let M = H[w];
  if (hp.S.length) { const cand = co.top(x, 2000, hp.S.length, co.names.map((_, r) => r).filter((r) => !hp.S.includes(r)), hp.S[0]).find((e) => e.S.length === hp.S.length && e.S.every((r, i) => r === hp.S[i]))
      || co.top(x, 2000, hp.S.length, co.names.map((_, r) => r).filter((r) => !hp.S.includes(r)), hp.S[0]).find((e) => e.S.length === hp.S.length);
    if (cand) M = fmt(cand.S, cand.v, false) + " " + form; }
  return { w, A: it.A, H: H[w], T, M, head: h };
});
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of ["T", "M"]) { const d = path.join(D, v === "T" ? "t" : "mr"); fs.mkdirSync(d, { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(d, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it[v]}`).join("\n") + "\n"); }
items.slice(0, 100).filter((_, i) => i % 6 === 0).forEach((x) => console.log(`${x.w}: A ${x.A} | T ${x.T} | H ${x.H} | M ${x.M}`));
