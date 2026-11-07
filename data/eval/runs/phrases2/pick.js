// Отбор 60 фраз по классам (dec.md) из cand.json; часть речи и коды — математика сайта (site/math.js).
//   deg   — слово степени первым (deg.json): наречие степени + признак или глагол (very small), прилагательное степени + имя (intense heat);
//   light — глагол-связка (LIGHT) + имя действия (первый смысл WordNet — действие, событие, сообщение…) с родственным глаголом (decision → decide);
//   axis  — признак (a/e) + главное (o/i), лучший одиночный корень признака (с осью) есть в коде главного слова;
//   indep — прилагательное + имя, лучший корень признака не в коде имени.
// Слова — базовые формы (без словоформ), не имена собственные; относительные прилагательные (political) исключены из axis и indep. По 15 случайных (seed) в классе.   node data/eval/runs/phrases2/pick.js
const fs = require("fs"), path = require("path"), SITE = path.resolve(__dirname, "../../../../site"), MM = require(path.join(SITE, "math.js"));
const m = JSON.parse(fs.readFileSync(path.join(SITE, "data/math.json"))), meta = JSON.parse(fs.readFileSync(path.join(SITE, "data/words.json")));
const V = new MM.Vocab(m.words, new Int8Array(fs.readFileSync(path.join(SITE, "data/vocab.bin"))), m.dim); V.setMeta(meta);
const co = new MM.Coder(m.dict, m.has_axis, m.names, m), rd = new MM.Reader(co, V, m.mix);
const DEG = JSON.parse(fs.readFileSync(path.join(__dirname, "deg.json"))), LIGHT = ["make", "take", "give", "have", "do", "get", "pay"], DEGADJ = ["extreme", "intense", "slight", "utter"];
const REL = new Set(JSON.parse(fs.readFileSync(path.join(__dirname, "cand.json"))).relational);
const cand = JSON.parse(fs.readFileSync(path.join(__dirname, "cand.json")));
const STOP = new Set(meta.stop || []);
const ok = (w) => { const i = V.index.get(w); return i !== undefined && !(V.infl && V.infl[i]) && !(V.proper && V.proper[i]) && !STOP.has(i); };
// по словам с запоминанием: rd.encode считает оценки всех слов словаря — медленно
const memo = (f) => { const c = new Map(); return (w) => { if (!c.has(w)) c.set(w, f(w)); return c.get(w); }; };
const best = memo((w) => co.singles(V.vec(w)).find((s) => s.has)), enc = memo((w) => rd.encode(w)), posOf = memo((w) => rd.posOf(w));
const cls = { deg: [], light: [], axis: [], indep: [] };
for (const k of cand.phrases) {
  const [a, b] = k.split("_"), ph = a + " " + b;
  if (DEG[a] !== undefined || DEG[b] !== undefined) {  // слово степени первым: наречие степени — при признаке или глаголе, прилагательное степени — при имени
    const d = a, h = b, adj = DEGADJ.includes(d);
    if (DEG[a] !== undefined && DEG[h] === undefined && ok(h) && (adj ? posOf(h) === "o" : "ai".includes(posOf(h)))) cls.deg.push({ phrase: ph, cls: "deg", head: h, mod: d });
    continue;
  }
  if (LIGHT.includes(a) && ok(b) && posOf(b) === "o" && cand.verb_of[b]) { cls.light.push({ phrase: ph, cls: "light", head: b, mod: a }); continue; }
  if (!ok(a) || !ok(b) || REL.has(a) || REL.has(b)) continue;  // относительные прилагательные (political) — не признак качества
  const pa = posOf(a), pb = posOf(b);
  let h, d;
  if ("ae".includes(pa) && "oi".includes(pb)) [d, h] = [a, b]; else if ("ae".includes(pb) && "oi".includes(pa)) [d, h] = [b, a]; else continue;
  const hp = posOf(h), dp = posOf(d);
  if (!((hp === "o" && dp === "a") || (hp === "i" && dp === "e") || (hp === "i" && dp === "a" && h === a))) continue;  // прил. + имя, глагол + наречие
  const e = enc(h), r = best(d);
  if (e.S.includes(r.r)) cls.axis.push({ phrase: ph, cls: "axis", head: h, mod: d });
  else if (hp === "o" && dp === "a" && d === a) cls.indep.push({ phrase: ph, cls: "indep", head: h, mod: d });
}
let s = 20261107; const rnd = () => ((s = (s * 1103515245 + 12345) % 2147483648) / 2147483648);
const sample = (arr, n) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a.slice(0, n); };
const items = [];
for (const c of Object.keys(cls)) { console.log(c, cls[c].length, "кандидатов"); const sm = sample(cls[c], 15); items.push(...sm); console.log("  " + sm.map((x) => x.phrase).join(", ")); }
fs.writeFileSync(path.join(__dirname, "items.json"), JSON.stringify(items, null, 0));
