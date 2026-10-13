// Самопроверка кодера: кандидаты — лучшие коды в 1, 2, 3 корня (Coder.encode) и их соседи (значение ±1, без одного корня);
// берётся код с лучшим местом при чтении (Reader.roots), при равенстве — короче. ① dev / 1000 / другие 1000.
//   node data/eval/runs/ideas/selfcheck.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix, {});
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const lv = (r) => (m.levels && m.levels[m.names[r]]) || [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5];
function variants(S, v) {
  const out = [[S, v]];
  S.forEach((r, i) => {
    if (m.has_axis[r]) for (const d of [-1, 1]) { const nv = v[i] + d; if (lv(r).includes(nv)) out.push([S, v.map((x, k) => (k === i ? nv : x))]); }
    if (S.length > 1) out.push([S.filter((_, k) => k !== i), v.filter((_, k) => k !== i)]);
  });
  return out;
}
const res = {};
for (const [name, ws] of [["dev", W.dev], ["r1", rand.map((w) => [w, ""])], ["r2", rand2.map((w) => [w, ""])]]) {
  res[name] = ws.map(([w, f]) => {
    const x = V.vec(w), base = co.encode(x, 3), cand = [];
    for (const k of [1, 2, 3]) { const e = co.encode(x, k); for (const c of variants(e.S, e.v)) cand.push(c); }
    const sc = (S, v) => V.rankIn(rd.roots(S, v, f), w);
    const r0 = sc(base.S, base.v), short = [1, 2, 3].map((k) => co.encode(x, k)).map((e) => ({ n: e.S.length, r: sc(e.S, e.v), code: co.format(e.S, e.v, f || "o") }));
    let best = null; for (const [S, v] of cand) { const r = sc(S, v); if (!best || r < best.r || (r === best.r && S.length < best.n)) best = { r, n: S.length, code: co.format(S, v, f || "o") }; }
    const sb = short.reduce((a, b) => (b.r < a.r || (b.r === a.r && b.n < a.n) ? b : a));
    return { w, base: { r: r0, n: base.S.length, code: co.format(base.S, base.v, f || "o") }, short: sb, self: best };
  });
  const s = (k) => `первыми ${res[name].filter((x) => x[k].r === 1).length}, корней ${(res[name].reduce((a, x) => a + x[k].n, 0) / res[name].length).toFixed(2)}`;
  console.log(`${name} (${res[name].length}): сейчас ${s("base")} | кратчайший из 1–3 ${s("short")} | самопроверка с соседями ${s("self")}`);
}
fs.writeFileSync(path.join(D, "selfcheck.json"), JSON.stringify(res));
