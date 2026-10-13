// Значение как измерение (после ../taxonomy): z — z-оценка проекции слова на ось a_r по словарю сайта; значение = голый корень,
// если |z| < Z0, иначе ±5 со знаком z. Корни без оси — голые. Выраженность корня без оси — z-оценка cos(слово, центр).
// MZ — корни и порядок из кода модели H, значения — измерение (диагноз; форма как у H).
// TZ — корни варианта T ../taxonomy (род по таксономии + уточнения математики), значения уточнений — измерение (род — из таблицы).
// SZ — без подгонки суммы: род по таксономии (без рода — самый выраженный корень), уточнения — самые выраженные корни по |z|
//      (первое — всегда, второе — если |z| ≥ Z2), значение по измерению. → items.json, mz/ tz/ sz/ codes_K.md
//   node data/eval/runs/measure/make.js [Z0] [Z2]
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix), R = co.R;
const Z0 = Number(process.argv[2] ?? 0.5), Z2 = Number(process.argv[3] ?? 2);
const TX = JSON.parse(fs.readFileSync(path.join(D, "../taxonomy/items.json"))), HD = JSON.parse(fs.readFileSync(path.join(D, "../taxonomy/heads.json")));
const dot = (a, b) => { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; };
const stat = (vecs) => vecs.map((a) => { const xs = []; for (let i = 0; i < V.words.length; i += 5) xs.push(dot(V.vec(V.words[i]), a)); const mu = xs.reduce((s, x) => s + x) / xs.length; return [mu, Math.sqrt(xs.reduce((s, x) => s + (x - mu) ** 2, 0) / xs.length)]; });
const SA = stat(co.A), SC = stat(co.C);
const zA = (x, r) => (dot(x, co.A[r]) - SA[r][0]) / SA[r][1], zC = (x, r) => (dot(x, co.C[r]) - SC[r][0]) / SC[r][1];
const val = (x, r) => { if (!m.has_axis[r]) return null; const z = zA(x, r), lv = co.lv[r]; if (Math.abs(z) < Z0) return 0; const t = Math.sign(z) * 5; return lv.includes(t) ? t : (t > 0 ? Math.max(...lv) : Math.min(...lv)); };
const sal = (x, r) => (m.has_axis[r] ? Math.max(Math.abs(zA(x, r)), zC(x, r)) : zC(x, r));
const one = (r, v) => (!m.has_axis[r] || !v ? m.names[r] : `${m.names[r]}(=${v > 0 ? "+" : ""}${v})`);
const items = TX.map((it) => {
  const w = it.w, x = V.vec(w), ban = new Set(rd.ban(w) || []), h = HD[w];
  // MZ
  const hp = co.parse(it.H || ""), form = (it.H || "").includes("|") ? it.H.slice(it.H.indexOf("|")) : "| o";
  const MZ = hp.S.length ? hp.S.map((r) => one(r, val(x, r))).join(" ") + " " + form : it.H;
  // TZ: корни T, род со значением из таблицы
  const tp = co.parse(it.T), headR = h ? m.names.indexOf(h.root) : null;
  const TZ = tp.S.map((r, i) => (i === 0 && r === headR ? (h.v === 0 ? `${m.names[r]}(=0)` : one(r, h.v)) : one(r, val(x, r)))).join(" ") + " | o";
  // SZ
  let head = headR, hv = h ? h.v : null;
  const rank = [...Array(R).keys()].filter((r) => !ban.has(r)).sort((a, b) => sal(x, b) - sal(x, a));
  if (head == null) { head = rank[0]; hv = val(x, head); }
  const rest = rank.filter((r) => r !== head), S = [rest[0]]; if (sal(x, rest[1]) >= Z2) S.push(rest[1]);
  const SZ = [h && hv === 0 ? `${m.names[head]}(=0)` : one(head, hv), ...S.map((r) => one(r, val(x, r)))].join(" ") + " | o";
  return { w, A: it.A, H: it.H, T: it.T, MZ, TZ, SZ };
});
fs.writeFileSync(path.join(D, "items.json"), JSON.stringify(items, null, 1));
for (const v of ["MZ", "TZ", "SZ"]) { const d = path.join(D, v.toLowerCase()); fs.mkdirSync(d, { recursive: true });
  for (const k of [1, 2]) fs.writeFileSync(path.join(d, `codes_${k}.md`), items.slice((k - 1) * 50, k * 50).map((it, i) => `${i + 1}. ${it[v]}`).join("\n") + "\n"); }
const jac = (a, b) => { const A = new Set(co.parse(a).S), B = new Set(co.parse(b || "").S); return [...A].filter((r) => B.has(r)).length / (new Set([...A, ...B]).size || 1); };
for (const v of ["A", "T", "TZ", "SZ"]) console.log(`${v}: совпадение набора корней с H ${(items.reduce((s, it) => s + jac(it[v], it.H), 0) / items.length).toFixed(2)}, корней ${(items.reduce((s, it) => s + co.parse(it[v]).S.length, 0) / items.length).toFixed(1)}`);
items.filter((_, i) => i % 7 === 0).forEach((x) => console.log(`${x.w}: H ${x.H} | MZ ${x.MZ} | TZ ${x.TZ} | SZ ${x.SZ}`));
