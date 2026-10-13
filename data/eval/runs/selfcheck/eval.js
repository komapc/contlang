// Самопроверка кодера на сайте (site/math.js Reader.best): ① dev / 1000 / другие 1000, без самопроверки, с ней и с keepHead (головной корень не меняется);
// плюс negW 0,4 поверх. Пишет results.json (место и код каждого слова).
//   node data/eval/runs/selfcheck/eval.js
const fs = require("fs"), path = require("path"), D = __dirname, MR = path.join(D, "../mathread");
const { V, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const co = new MM.Coder(m.dict, m.has_axis, m.names, m);
const W = JSON.parse(fs.readFileSync(path.join(MR, "words.json"))), rand = JSON.parse(fs.readFileSync(path.join(MR, "rand1000.json"))).map((c) => c.w);
const rand2 = (() => { let seed = 11; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const skip = new Set([...W.dev, ...W.test].map((x) => x[0]).concat(rand)), pool = V.words.map((_, i) => i).filter((i) => !V.stop[i] && V.group[i] === i && /^[a-z]{3,}$/.test(V.words[i]) && !skip.has(V.words[i]));
  const pick = new Set(); while (pick.size < 1000) pick.add(pool[Math.floor(rnd() * pool.length)]); return [...pick].map((i) => V.words[i]); })();
const sets = { dev: W.dev, r1: rand.map((w) => [w, ""]), r2: rand2.map((w) => [w, ""]) };
const variants = process.argv[2] === "head" ? { "самопроверка, голова та же": [{}, true] } : { "сейчас": [{}, null], "самопроверка": [{}, false], "самопроверка, голова та же": [{}, true], "самопроверка, голова та же, negW 0,4": [{ negW: 0.4 }, true], "negW 0,4": [{ negW: 0.4 }, null] };
const out = {};
for (const [name, [opt, keep]] of Object.entries(variants)) {
  const rd = new MM.Reader(co, V, m.mix, opt); out[name] = {};
  const line = [];
  for (const [k, ws] of Object.entries(sets)) {
    out[name][k] = ws.map(([w, f]) => {
      const e = keep === null ? co.encode(V.vec(w)) : rd.best(w, f, keep);
      return { w, r: keep === null ? V.rankIn(rd.roots(e.S, e.v, f), w) : e.r, n: e.S.length, code: co.format(e.S, e.v, f || "o") };
    });
    const a = out[name][k]; line.push(`${k} первыми ${a.filter((x) => x.r === 1).length} (корней ${(a.reduce((s, x) => s + x.n, 0) / a.length).toFixed(2)})`);
  }
  console.log(`${name}: ${line.join(" | ")}`);
}
fs.writeFileSync(path.join(D, process.argv[2] === "head" ? "results_head.json" : "results.json"), JSON.stringify(out));
