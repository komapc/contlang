// Проверка кодов предложений (как ../pipe/check_sent.mjs); аргументы: JSON {key: code}, вариант OLD|NEW.
// В NEW слово `ROOT | p` (отношение) допустимо: один корень, без меток; проверяется как `ROOT | e`.
import fs from "fs";
import { codeProblems } from "../../../../worker/check.js";
const PART = new Set(["E", "PI", "FROM", "FOR", "LIKE", "LA", "PE", "AND", "[", "]", ";"]);
const C = JSON.parse(fs.readFileSync(process.argv[2])), NEW = process.argv[3] === "NEW", out = {};
for (const [k, c] of Object.entries(C)) {
  const ws = [...c.matchAll(/\{([^{}]*)\}/g)].map((m) => m[1].trim()), bad = [];
  let np = 0;
  for (let w of ws) {
    const m = w.match(/^(.*)\|\s*p\b(.*)$/);
    if (m && NEW) {
      np++;
      if (m[2].trim()) bad.push(`{${w}}: a relation word (| p) takes no marks`);
      if (m[1].trim().split(/\s+/).length !== 1) bad.push(`{${w}}: a relation word (| p) has exactly one root`);
      w = `${m[1].trim()} | e`;
    }
    if (w.includes("|")) bad.push(...codeProblems(w).map((p) => `{${w}}: ${p}`)); else bad.push(`{${w}}: no | FORM`);
  }
  const rest = c.replace(/\{[^{}]*\}/g, " ").replace(/"[^"]*"/g, " ").replace(/([\[\];])/g, " $1 ").split(/\s+/).filter(Boolean);
  for (const t of rest) if (!PART.has(t)) bad.push(`outside braces: ${t}`);
  if (/[{}]/.test(c.replace(/\{[^{}]*\}/g, ""))) bad.push("unbalanced braces");
  out[k] = { n: ws.length, np, bad };
}
console.log(JSON.stringify(out));
