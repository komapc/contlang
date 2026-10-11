// Эхо-уровни: корень нужен коду ради центра, а уровень на прочтение не влияет. На своих кодах (own8k.json, первые N) для каждого корня с осью:
//   место слова у математики с кодом как есть, с уровнем −v (знак перевёрнут) и без корня. Чувствительность уровня — log2(место(−v) / место),
//   важность корня — log2(место без корня / место). Эхо — корень важен, уровень нет.   node data/eval/runs/anchor/echo.js [N] → echo.out
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, co, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const rd = new MM.Reader(co, V, m.mix, {}), N = +(process.argv[2] || 1500);
const own = JSON.parse(fs.readFileSync(path.join(D, "own8k.json"))).filter(([, c]) => !/\b(FROM|FOR|LIKE|PI)\b/.test(c)).slice(0, N);
const has = Object.fromEntries(m.names.map((n, r) => [n, m.has_axis[r]]));
const rank = (code, w) => V.rankIn(rd.scores(code), w) + 1;
const st = {};   // корень → [[v, sens, imp, слово]]
for (const [w, code] of own) {
  const [head, form] = code.split("|"), toks = head.trim().split(/\s+/), r0 = rank(code, w);
  toks.forEach((t, j) => {
    const mm = t.match(/^([A-Z]+)(?:\(=([+-]?\d+)\))?$/); if (!mm || !has[mm[1]]) return;
    const v = +(mm[2] || 0); if (!v) return;
    const flip = toks.map((u, k) => (k === j ? `${mm[1]}(=${v > 0 ? "-" : "+"}${Math.abs(v)})` : u)).join(" ");
    const drop = toks.filter((_, k) => k !== j).join(" ");
    const sens = Math.log2(rank(`${flip} |${form}`, w) / r0), imp = drop ? Math.log2(rank(`${drop} |${form}`, w) / r0) : NaN;
    (st[mm[1]] = st[mm[1]] || []).push([v, sens, imp, w, j]);
  });
}
const med = (a) => { const b = a.filter((x) => !isNaN(x)).sort((x, y) => x - y); return b.length ? b[b.length >> 1] : NaN; };
const out = ["| корень | слабых (|v| ≤ 2) | чувств. слабого | важность слабого | эхо (важен, уровень нет) | сильных | чувств. сильного | примеры эха |", "|---|--:|--:|--:|--:|--:|--:|---|"];
const rows = Object.entries(st).map(([n, a]) => {
  const wk = a.filter((x) => Math.abs(x[0]) <= 2), sg = a.filter((x) => Math.abs(x[0]) >= 3);
  const echo = wk.filter((x) => x[2] >= 1 && x[1] < 0.5);
  return [echo.length / Math.max(1, wk.length), `| ${n} | ${wk.length} | ${med(wk.map((x) => x[1])).toFixed(2)} | ${med(wk.map((x) => x[2])).toFixed(2)} | ${echo.length} (${Math.round(100 * echo.length / Math.max(1, wk.length))} %) | ${sg.length} | ${med(sg.map((x) => x[1])).toFixed(2)} | ${echo.slice(0, 6).map((x) => `${x[3]} ${x[0] > 0 ? "+" : ""}${x[0]}`).join(", ")} |`];
}).sort((a, b) => b[0] - a[0]);
fs.writeFileSync(path.join(D, "echo.out"), out.concat(rows.map((r) => r[1])).join("\n") + "\n"); console.log(out.concat(rows.map((r) => r[1])).join("\n"));
