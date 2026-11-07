// Проверка кодов по правилам языка (worker/check.js) по словам: аргумент — JSON-файл {phrase: code}; печатает {phrase: {n: слов, bad: [проблемы]}}.
// Слово кода — `ROOTS | FORM марки`; следующее слово начинается с корня (или кавычек) после формы и марок. Связки FROM/FOR/LIKE/PI — внутри check.js.
import fs from "fs";
import { codeProblems } from "../../../../worker/check.js";
export const words = (code) => code.replace(/(\|\s*[oiae](?:\s+(?:[A-Z][+-]?\d+|agent|tool|result|quality))*)\s+(?=(?:FROM|FOR|LIKE|PI)\b)/g, "$1 @LINK@ ")
  .replace(/(\|\s*[oiae](?:\s+(?:[A-Z][+-]?\d+|agent|tool|result|quality))*)\s+(?=[A-Z][A-Z]|")/g, "$1\n").split("\n").map((w) => w.replace(/ @LINK@ /g, " "));
const C = JSON.parse(fs.readFileSync(process.argv[2])), out = {};
for (const [k, c] of Object.entries(C)) { const ws = words(c.trim()); out[k] = { n: ws.length + (c.match(/\b(FROM|FOR|LIKE|PI)\b/g) || []).length, bad: ws.flatMap(codeProblems) }; }
console.log(JSON.stringify(out));
