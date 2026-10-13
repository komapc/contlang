// Кодер «коротко и резко»: значения только из LV (0 печатается голым корнем — центр корня и есть его простой смысл), и из кодов,
// чей cos не хуже лучшего больше чем на δ, берётся код с наименьшим числом корней (при равенстве — с большим cos).
// На 100 словах ../twowords2: число корней, доля голых и ±5, потеря cos, круг математики (Reader), примеры. → codes.json
//   node data/eval/runs/bold/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co0 = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co0, V, m.mix);
const words = JSON.parse(fs.readFileSync(path.join(D, "../twowords2/items.json"))).map((x) => x.w);
const fmt = (co, S, v) => S.map((r, i) => (co.has[r] && v[i] !== 0 ? `${co.names[r]}(=${v[i] > 0 ? "+" : ""}${v[i]})` : co.names[r])).join(" ") + " | o";
const mkCo = (LV) => { if (!LV) return co0; const lv = {}; m.names.forEach((n, r) => { if (!m.has_axis[r]) return; const base = (m.levels && m.levels[n]) || [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]; const t = LV.filter((x) => base.includes(x)); lv[n] = t.length ? t : base; });
  return new MM.Coder(m.dict, m.has_axis, m.names, Object.assign({}, m, { levels: lv })); };
const VARS = { A: [null, 0], "035 δ0": [[-5, -3, 0, 3, 5], 0], "035 δ.03": [[-5, -3, 0, 3, 5], 0.03], "035 δ.06": [[-5, -3, 0, 3, 5], 0.06], "035 δ.1": [[-5, -3, 0, 3, 5], 0.1], "05 δ.03": [[-5, 0, 5], 0.03], "05 δ.06": [[-5, 0, 5], 0.06] };
const out = {};
for (const [name, [LV, dl]] of Object.entries(VARS)) {
  const co = mkCo(LV), res = {}; let nr = 0, bare = 0, five = 0, weak = 0, tot = 0, loss = 0, lr = 0;
  for (const w of words) { const x = V.vec(w), ban = rd.ban(w);
    if (V.proper[V.index.get(w)]) continue;
    const list = co.top(x, 400, 3, ban), best = co0.encode(x, 3, ban).cos, c1 = list[0].cos;
    const e = name === "A" ? co0.encode(x, 3, ban) : list.filter((e) => e.cos >= c1 - dl).sort((a, b) => a.S.length - b.S.length || b.cos - a.cos)[0];
    const code = name === "A" ? co0.format(e.S, e.v) : fmt(co, e.S, e.v);
    res[w] = code; nr += e.S.length; loss += best - e.cos; lr += Math.log(V.rankIn(rd.scores(code), w));
    e.S.forEach((r, i) => { tot++; if (!co.has[r] || e.v[i] === 0) bare++; else if (Math.abs(e.v[i]) === 5) five++; else if (Math.abs(e.v[i]) <= 2) weak++; }); }
  const n = Object.keys(res).length; out[name] = res;
  console.log(`${name.padEnd(9)} корней ${(nr / n).toFixed(1)}, голых ${Math.round(100 * bare / tot)}%, ±5 ${Math.round(100 * five / tot)}%, 0…±2 ${Math.round(100 * weak / tot)}%, потеря cos ${(loss / n).toFixed(3)}, круг ${Math.round(Math.exp(lr / n))}`);
}
fs.writeFileSync(path.join(D, "codes.json"), JSON.stringify(out, null, 1));
for (const w of ["employee", "pianist", "chapel", "malaria", "bowl", "lake", "road", "dose", "bubble", "outlet", "grief", "list"]) console.log(`${w}: ` + ["A", "035 δ.03", "035 δ.06", "05 δ.06"].map((k) => `${k}: ${out[k][w].replace(" | o", "")}`).join(" | "));
