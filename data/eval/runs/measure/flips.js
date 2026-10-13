// Где знак измерения расходится со значением модели (|v| ≥ 3), по корням
const fs = require("fs"), path = require("path"), D = __dirname, REPO = path.join(D, "../../../..");
const { V, m, MM } = require(path.join(REPO, "scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const items = JSON.parse(fs.readFileSync(path.join(D, "items.json")));
const dot = (a, b) => { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; };
const st = {}; const zs = (r) => st[r] ??= (() => { const xs = []; for (let i = 0; i < V.words.length; i += 5) xs.push(dot(V.vec(V.words[i]), co.A[r])); const mu = xs.reduce((s, x) => s + x) / xs.length; return [mu, Math.sqrt(xs.reduce((s, x) => s + (x - mu) ** 2, 0) / xs.length)]; })();
const by = {};
for (const it of items) { const p = co.parse(it.H || ""), x = V.vec(it.w);
  p.S.forEach((r, i) => { const v = p.v[i]; if (!m.has_axis[r] || !v || Math.abs(v) < 3) return; const [mu, sd] = zs(r), z = (dot(x, co.A[r]) - mu) / sd;
    const b = by[m.names[r]] ??= { n: 0, bad: 0, ex: [] }; b.n++; if (Math.sign(z) !== Math.sign(v)) { b.bad++; b.ex.push(`${it.w} ${v > 0 ? "+" : ""}${v}/z${z.toFixed(1)}`); } }); }
const rows = Object.entries(by).sort((a, b) => b[1].bad - a[1].bad); let N = 0, B = 0;
for (const [r, b] of rows) { N += b.n; B += b.bad; console.log(`${r}\t${b.bad}/${b.n}\t${b.ex.join(", ")}`); }
console.log(`всего ${B}/${N}`);
