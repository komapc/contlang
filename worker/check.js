// Проверка кода по правилам языка — те же правила, что scripts/mincode/validator.py, для одного слова или пары через связку:
// корни, лимит, знак и допустимые значения оси (слева от `|`), часть речи, метки и роль (справа).
// Правила берутся из CHECK (worker/prompts.js, собирается из roots.yaml); согласие с validator.py — tests/test_check_parity.py.
import { CHECK } from "./prompts.js";

// В паре через связку (FROM, FOR, LIKE, PI) каждое слово проверяется отдельно.
const LINKS = /\b(?:FROM|FOR|LIKE|PI)\b/;
const fmt = (x) => (x > 0 ? "+" : "") + x;

export function codeProblems(code) {
  return String(code || "").split(LINKS).flatMap(wordProblems);
}

function wordProblems(word) {
  const bar = word.indexOf("|");
  const body = (bar < 0 ? word : word.slice(0, bar)).replace(/"[^"]*"/g, " ").trim();
  const roots = [], bad = [];
  for (const t of body ? body.split(/\s+/) : []) {
    const m = t.match(/^([A-Z]+)(?:\(=([+-]?)(\d+)\))?$/);
    if (!m) { bad.push(`malformed token ${t}`); continue; }
    if (CHECK.particles.includes(m[1])) continue;
    if (!CHECK.roots.includes(m[1])) bad.push(`unknown root ${m[1]}`);
    roots.push(m[1]);
    if (!m[3]) continue;
    const v = Number((m[2] || "+") + m[3]), lv = CHECK.levels[m[1]];
    if (m[3] !== "0" && !m[2]) bad.push(`value without sign in ${t} (write (=+${m[3]}))`);
    if (CHECK.noaxis.includes(m[1])) bad.push(`${m[1]} has no axis, write it without a value`);
    else if (v < -5 || v > 5) bad.push(`value out of range in ${t} (-5…+5)`);
    else if (lv && !lv.includes(v)) bad.push(`${m[1]} takes only ${lv.map(fmt).join(" ")}`);
  }
  if (roots.length > CHECK.max_roots) bad.push(`${roots.length} roots, the limit is ${CHECK.max_roots}`);
  if (bar < 0) {
    if (roots.length) bad.push("no `| form` after the roots (write `| o`, `| i`, `| a` or `| e`)");
    return bad;
  }
  return bad.concat(formProblems(word.slice(bar + 1)));
}

// справа от `|`: часть речи, затем метки (каждая один раз, в своём диапазоне, без I0), `!` `?`, у `o` одна роль
function formProblems(form) {
  const bad = [], seen = new Set();
  const toks = form.trim().split(/\s+/).filter(Boolean);
  if (!toks.length || !CHECK.pos.includes(toks[0])) { bad.push(`after \`|\` the part of speech comes first (${CHECK.pos.join(", ")})`); return bad; }
  const pos = toks[0];
  let role = null;
  for (const t of toks.slice(1)) {
    if (t === "|") { bad.push("second `|` in a word"); continue; }
    if (CHECK.particles.includes(t) || /^[A-Z]{2,}/.test(t) || t.startsWith('"')) break;  // дальше другое слово; его здесь не проверяем
    if (CHECK.bare.includes(t)) continue;
    if (CHECK.roles.includes(t)) {
      if (pos !== "o") bad.push(`role ${t} only after \`| o\``);
      else if (role) bad.push(`two roles: ${role}, ${t}`);
      role = t;
      continue;
    }
    const m = t.match(/^([A-Z])([+-]?\d+)?$/);
    if (!m || !CHECK.labels[m[1]]) { bad.push(`unknown label ${t}`); continue; }
    if (!m[2]) { bad.push(`label ${t} needs a value`); continue; }
    const v = Number(m[2]), [lo, hi] = CHECK.labels[m[1]];
    if (v < lo || v > hi) bad.push(`${t} out of range (${fmt(lo)}…${fmt(hi)})`);
    if (m[1] === "I" && v === 0) bad.push("do not write I0");
    if (seen.has(m[1])) bad.push(`label ${m[1]} twice`);
    seen.add(m[1]);
  }
  return bad;
}
