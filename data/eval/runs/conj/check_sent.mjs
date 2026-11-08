// Проверка кодов предложений (как ../pipe/check_sent.mjs); аргументы: JSON {key: code}, ячейка OLD|NEW.
// В NEW вне скобок допустимы ещё связки IF, THOUGH, BUT, BECAUSE, SO, OR.
import fs from "fs";
import { codeProblems } from "../../../../worker/check.js";
const NEW = process.argv[3] === "NEW";
const PART = new Set(["E", "PI", "FROM", "FOR", "LIKE", "LA", "PE", "AND", "[", "]", ";", ...(NEW ? ["IF", "THOUGH", "BUT", "BECAUSE", "SO", "OR"] : [])]);
const CONJ = new Set(["IF", "THOUGH", "BUT", "BECAUSE", "SO", "OR"]);
const C = JSON.parse(fs.readFileSync(process.argv[2])), out = {};
for (const [k, c] of Object.entries(C)) {
  const ws = [...c.matchAll(/\{([^{}]*)\}/g)].map((m) => m[1].trim()), bad = [];
  for (const w of ws) if (w.includes("|")) bad.push(...codeProblems(w).map((p) => `{${w}}: ${p}`)); else bad.push(`{${w}}: no | FORM`);
  const rest = c.replace(/\{[^{}]*\}/g, " ").replace(/"[^"]*"/g, " ").replace(/([\[\];])/g, " $1 ").split(/\s+/).filter(Boolean);
  for (const t of rest) if (!PART.has(t)) bad.push(`outside braces: ${t}`);
  if (/[{}]/.test(c.replace(/\{[^{}]*\}/g, ""))) bad.push("unbalanced braces");
  out[k] = { n: ws.length, nc: rest.filter((t) => CONJ.has(t)).length, bad };
}
console.log(JSON.stringify(out));
