// Проверка кодов предложений: аргумент — JSON {key: code}; печатает {key: {n: слов, bad: [проблемы]}}.
// Слово — содержимое { }; проверяется worker/check.js; вне скобок допустимы только частицы, [ ], ; и имена в кавычках.
import fs from "fs";
import { codeProblems } from "../../../../worker/check.js";
const PART = new Set(["E", "PI", "FROM", "FOR", "LIKE", "LA", "PE", "AND", "[", "]", ";"]);
const C = JSON.parse(fs.readFileSync(process.argv[2])), out = {};
for (const [k, c] of Object.entries(C)) {
  const ws = [...c.matchAll(/\{([^{}]*)\}/g)].map((m) => m[1].trim()), bad = [];
  for (const w of ws) if (w.includes("|")) bad.push(...codeProblems(w).map((p) => `{${w}}: ${p}`));
  const rest = c.replace(/\{[^{}]*\}/g, " ").replace(/"[^"]*"/g, " ").replace(/([\[\];])/g, " $1 ").split(/\s+/).filter(Boolean);
  for (const t of rest) if (!PART.has(t)) bad.push(`outside braces: ${t}`);
  if (/[{}]/.test(c.replace(/\{[^{}]*\}/g, ""))) bad.push("unbalanced braces");
  out[k] = { n: ws.length, bad };
}
console.log(JSON.stringify(out));
