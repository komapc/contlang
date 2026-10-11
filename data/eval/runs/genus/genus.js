// Идея 5, шаг 2: код «род + отличие» по senses.json → codes_<набор>_genus.json и листы для слепого чтения (как ../mathread/make_codes.js).
//   голова — код рода (гиперонима) до 3 корней; отличие — слово толкования (≤ 2 корня, без корней головы), из 8 лучших по близости к «значение − голова»
//   берётся то, с которым математика ставит слово выше (отличие есть всегда, если есть кандидат); связка — FOR / FROM / LIKE, если слово стоит после «used for / made of / resembling», иначе PI.
//   Прилагательные и наречия (рода в WordNet нет) — код кодера сайта, как раньше.
//   node data/eval/runs/genus/genus.js dev [папка для листов]
const fs = require("fs"), path = require("path"), D = __dirname;
const { V, co, m, MM } = require(path.join(D, "../../../../scripts/site/eval_math.js"));
const [set = "dev", out] = process.argv.slice(2);
const S = JSON.parse(fs.readFileSync(path.join(D, "senses.json"))), words = JSON.parse(fs.readFileSync(path.join(D, "../mathread/words.json")))[set];
const rd = new MM.Reader(co, V, m.mix, {}), dim = V.dim;
const STOP = new Set("a an the of to in on and or for with by from as at is are be that which who this its it".split(" "));
const mean = (ws) => { const v = new Float64Array(dim); let n = 0; for (const w of ws) { const x = V.vec(w); if (x && !STOP.has(w)) { for (let j = 0; j < dim; j++) v[j] += x[j]; n++; } } return n ? v.map((t) => t / n) : null; };
const unit = (v) => { const n = Math.hypot(...v); return v.map((t) => t / n); };
const dot = (a, b) => { let s = 0; for (let j = 0; j < dim; j++) s += a[j] * b[j]; return s; };
const cosw = (a, b) => { const x = V.vec(a), y = V.vec(b); return x && y ? dot(x, y) : 0; };
const res = [];
for (const [w, form] of words) {
  const s = S[w], x = V.vec(w), base = rd.encode(w, form);
  const sense = unit(mean([w, w, ...s.lemmas, ...s.gloss]));   // вектор значения: слово ×2 + синонимы + толкование
  const g = s.genus.length && mean(s.genus);
  let r = { w, form, synset: s.synset, def: s.def, genus: s.genus_synset, base: base.code, base_rank: base.rank, code: base.code, mod: "", link: "" };
  if (g) {
    const h = co.encode(unit(g), 3), head = co.format(h.S, h.v, form), y = co.parts(h.S, h.v).reduce((a, p) => a.map((t, j) => t + p[j]), new Float64Array(dim));
    const resid = unit(sense.map((t, j) => t - dot(sense, unit(y)) * unit(y)[j]));
    const cand = [...new Set([...s.after, ...s.gloss])].filter((t) => V.vec(t) && t !== w && !s.genus.includes(t) && !STOP.has(t)).map((t) => [t, dot(V.vec(t), resid)]).sort((a, b) => b[1] - a[1]).slice(0, 8);
    let best = { code: head, rank: Infinity, mod: "", link: "" };   // отличие ставится всегда (без него читателю не на что опереться), лучшее по месту слова у математики
    for (const [t] of cand) {
      let e = co.encode(V.vec(t), 2); if (e.S.some((q) => h.S.includes(q))) { e = co.encode(V.vec(t), 1); if (e.S.some((q) => h.S.includes(q))) continue; }
      const link = s.after.includes(t) ? s.link : "PI", code = `${head} ${link} ${co.format(e.S, e.v, "o")}`, rank = V.rankIn(rd.scores(code), w);
      if (rank < best.rank) best = { code, rank, mod: t, link };
    }
    Object.assign(r, { head, code: best.code, mod: best.mod, link: best.link });
  }
  const sc = rd.scores(r.code), top = V.top(sc, 5).map((t) => t.word);
  Object.assign(r, { rank: V.rankIn(sc, w), top, cos1: cosw(top[0], w), sense_cos1: V.vec(top[0]) ? dot(V.vec(top[0]), sense) : 0 });
  const bs = rd.scores(r.base), bt = V.top(bs, 1)[0].word; r.base_sense_cos1 = V.vec(bt) ? dot(V.vec(bt), sense) : 0;
  res.push(r);
}
fs.writeFileSync(path.join(D, `codes_${set}_genus.json`), JSON.stringify(res, null, 1));
let seed = 3; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const order = res.map((_, i) => i).sort(() => rnd() - 0.5), key = {};
for (let k = 0; k * 20 < order.length; k++) {
  const ids = order.slice(k * 20, k * 20 + 20), name = `${set}_genus_${String(k + 1).padStart(2, "0")}`; key[name] = ids.map((i) => res[i].w);
  const txt = ids.map((i, j) => `${j + 1}. ${res[i].code}`).join("\n") + "\n"; fs.writeFileSync(path.join(D, `sheet_${name}.md`), txt);
  if (out) fs.writeFileSync(path.join(out, `list_${name}.md`), txt);
}
fs.writeFileSync(path.join(D, `key_${set}_genus.json`), JSON.stringify(key, null, 1));
const M = (a) => (a.reduce((s, t) => s + t, 0) / a.length).toFixed(2), G = res.filter((r) => r.head);
console.log(`${set}: ${res.length} слов, с родом ${G.length}; первыми: род+отличие ${res.filter((r) => r.rank === 1).length}, сайт ${res.filter((r) => r.base_rank === 1).length}; cos первого прочтения со значением: ${M(res.map((r) => r.sense_cos1))} против ${M(res.map((r) => r.base_sense_cos1))}; со словом ${M(res.map((r) => r.cos1))}`);
console.log(`  только слова с родом: первыми ${G.filter((r) => r.rank === 1).length} против ${G.filter((r) => r.base_rank === 1).length}, cos со значением ${M(G.map((r) => r.sense_cos1))} против ${M(G.map((r) => r.base_sense_cos1))}`);
for (const r of G.slice(0, 25)) console.log(`${r.w} [${r.synset} → ${r.genus}] ${r.code}  (${r.rank}: ${r.top.slice(0, 3).join(", ")})  | сайт ${r.base}`);
