"""Проверка кода min-co по roots.yaml.

    python3 scripts/mincode/validator.py FILE...   # строки вида "12. КОД" или просто код

Уровни: error (неправильный код), warning (старая запись или спорное место).
Правила: кавычки непрозрачны; слово = корни `|` часть речи метки; корней не больше
лимита (ABSTRACT сверх лимита); значение оси только у корней с осью, в −5…+5
(MANY: 0…+5); метки из списка, каждая не более одного раза, в своём диапазоне,
`I0` запрещён; `!` и `?` без значения; скобки сбалансированы.
Запись предложения с границами слов `{ ROOTS | FORM }` (check_braced): вне `{ }` только частицы, `[ ]`, `;` и имена в кавычках.
"""
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spec  # noqa: E402

TOKEN = re.compile(r'''
    (?P<q>"[^"]*")
  | (?P<badq>")
  | (?P<br>[\[\]])
  | (?P<semi>;)
  | (?P<bar>\|)
  | (?P<root>[A-Z]{2,}[A-Z0-9]*)(?P<arg>\([^)]*\))?
  | (?P<lab>[A-Z](?:[+-]?\d+)?)
  | (?P<bang>[!?])
  | (?P<suf>-[oiae]\b(?:\([^)]*\))?)
  | (?P<num>\d+(?:-[a-z])?)
  | (?P<low>[a-z]+)
  | (?P<ws>\s+|,)
  | (?P<other>.)
''', re.X)


@dataclass
class Issue:
    level: str  # error | warning
    kind: str
    msg: str


class Validator:
    def __init__(self, doc=None):
        doc = doc or spec.load()
        self.roots = {r["name"]: r for r in doc["roots"]}
        self.particles = {p["name"] for p in doc["particles"] if p["name"].isalpha()}
        self.labels = {m["name"]: m for m in doc["labels"]}
        self.max_roots = doc["limits"]["max_roots"]
        self.extra = doc["limits"]["extra_root"]
        self.pos = {p["name"] for p in doc["pos"]}

    def check(self, code):
        issues = []

        def add(level, kind, msg):
            issues.append(Issue(level, kind, msg))

        depth = 0
        word = []  # корни текущего слова (без форм)
        state = "roots"  # roots | pos | labels
        seen_labels = set()
        has_bar = False
        after_and = False  # предыдущая частица — AND: модификатор без формы допустим (`AND SAME(=-5)`)
        word_after_and = False

        def end_word():
            nonlocal word, state, seen_labels, has_bar, word_after_and
            if word:
                body = [r for r in word if r != self.extra]
                if len(body) > self.max_roots:
                    add("error", "too_many_roots", f"{len(body)} корней (лимит {self.max_roots}): {' '.join(word)}")
                if word.count(self.extra) > 1:
                    add("error", "too_many_roots", f"{self.extra} дважды")
                if not has_bar and not word_after_and:
                    add("error", "no_form", f"слово без `| форма`: {' '.join(word)}")
            word, state, seen_labels, has_bar, word_after_and = [], "roots", set(), False, False

        for m in TOKEN.finditer(code):
            k = m.lastgroup
            if k == "arg":
                k = "root"
            if k == "ws":
                continue
            t = m.group(0)
            was_and, after_and = after_and, False
            if k == "q":
                # кавычки перед `|` входят в слово (`TIME MEASURE "10" | o`), иначе это отдельный элемент
                if not (word and state == "roots" and re.match(r"\s*\|", code[m.end():])):
                    end_word()
            elif k == "badq":
                add("error", "bad_quote", "непарная кавычка")
            elif k == "semi":
                if not word and not has_bar and state == "roots" and not code[:m.start()].strip():
                    add("warning", "empty_clause", "`;` в начале кода")
                end_word()
            elif k == "br":
                end_word()
                depth += 1 if t == "[" else -1
                if depth < 0:
                    add("error", "brackets", "лишняя `]`")
                    depth = 0
            elif k == "bar":
                if state != "roots":
                    add("error", "bar", "второй `|` в слове")
                has_bar = True
                state = "pos"
            elif k == "root":
                name = m.group("root")
                arg = m.group("arg")
                if name in self.particles:
                    end_word()
                    after_and = name == "AND"
                    continue
                if state != "roots":
                    end_word()
                if not word:
                    word_after_and = was_and
                if name not in self.roots:
                    add("error", "unknown_root", name)
                    word.append(name)
                    continue
                word.append(name)
                if arg:
                    mv = re.fullmatch(r"\(=([+-]?\d+)\)", arg)
                    if not mv:
                        add("warning", "old_notation", f"{name}{arg}")
                        continue
                    r = self.roots[name]
                    if not r.get("axis"):
                        add("error", "axis_on_axisless", f"{name}{arg}")
                        continue
                    v = int(mv.group(1))
                    lo = 0 if r.get("one_sided") else -5
                    if not lo <= v <= 5:
                        add("error", "axis_range", f"{name}{arg} (допустимо {lo}…5)")
                    if re.search(r"\+0\b|-0\b", mv.group(1)):
                        add("warning", "old_notation", f"{name}{arg}: пиши (=0)")
            elif k == "lab":
                letter = t[0]
                if letter in self.particles:
                    end_word()
                    continue
                if state == "roots":
                    add("error", "label_before_bar", f"метка `{t}` до `|`")
                    continue
                state = "labels"
                if letter not in self.labels or self.labels[letter].get("bare"):
                    add("error", "unknown_label", t)
                    continue
                val = t[1:]
                if not val:
                    add("error", "label_value", f"метка {letter} без значения")
                    continue
                v = int(val)
                lo, hi = self.labels[letter]["range"]
                if not lo <= v <= hi:
                    add("error", "label_range", f"{t} (допустимо {lo}…{hi})")
                if letter == "I" and v == 0:
                    add("error", "label_value", "`I0` не писать")
                if letter in seen_labels:
                    add("error", "dup_label", f"метка {letter} дважды")
                seen_labels.add(letter)
            elif k == "bang":
                if state == "roots":
                    add("warning", "old_notation", f"`{t}` до `|`")
                elif t not in {m["name"] for m in self.labels.values() if m.get("bare")}:
                    add("error", "unknown_label", t)
                state = "labels" if state != "roots" else state
            elif k == "low":
                if state == "pos" and t in self.pos:
                    state = "labels"
                elif state == "pos":
                    add("error", "bad_pos", t)
                else:
                    add("error", "bare_word", f"неоформленное слово `{t}`")
            elif k == "suf":
                add("warning", "old_notation", f"суффикс {t}")
                has_bar = True
            elif k == "num":
                add("warning", "unquoted_number", t)
            else:
                add("error", "stray", t)
        end_word()
        if depth > 0:
            add("error", "brackets", "незакрытая `[`")
        return issues


def check_braced(self, code):
    """Запись с явными границами слов: каждое слово в `{ … }`, вне фигурных скобок только
    частицы, `[ ]`, `;`. Внутри — ровно одно слово; без `|` допустим только модификатор после AND."""
    issues = []
    out = re.sub(r"\{[^{}]*\}", " ", code)
    out = re.sub(r'"[^"]*"', " ", out)  # имя в кавычках вне скобок допустимо как отдельный элемент
    for m in re.finditer(r"[A-Z]{2,}[A-Z0-9]*|[a-z]+|\d+|[^\s\[\];,]", out):
        t = m.group(0)
        if t not in self.particles:
            issues.append(Issue("error", "outside_word", f"вне `{{ }}`: {t}"))
    if code.count("{") != code.count("}") or re.search(r"\{[^}]*\{|\}[^{]*\}", code):
        issues.append(Issue("error", "braces", "скобки `{ }` не парны или вложены"))
    prev = ""
    pos = 0
    for m in re.finditer(r"\{([^{}]*)\}", code):
        before = re.findall(r"[A-Z]+", re.sub(r"\{[^{}]*\}", " ", code[pos:m.start()]))
        pos = m.end()
        body = m.group(1)
        if body.count("|") > 1:
            issues.append(Issue("error", "bar", "два `|` в одних `{ }`"))
        lead = "AND " if before and before[-1] == "AND" else ""
        issues += self.check(lead + body)
    return issues


TOKI_WORD = re.compile(r"([A-Z]{2,}[A-Z0-9]*?)([+-]\d+|0)?((?:\.(?:[A-Z][+-]?\d+|[!?]))*)")


def check_toki(self, code):
    """Запись в стиле токи пона: слово = КОРЕНЬ[±v] с метками через `.`, без `|` и суффиксов."""
    issues = []

    def add(kind, msg, level="error"):
        issues.append(Issue(level, kind, msg))

    depth = 0
    for tok in re.findall(r'"[^"]*"|\[|\]|;|[^\s\[\];"]+|"', code):
        if tok.startswith('"'):
            if tok == '"':
                add("bad_quote", "непарная кавычка")
            continue
        if tok in "[]":
            depth += 1 if tok == "[" else -1
            if depth < 0:
                add("brackets", "лишняя `]`")
                depth = 0
            continue
        if tok == ";" or tok in self.particles:
            continue
        m = TOKI_WORD.fullmatch(tok)
        if not m:
            add("stray", tok)
            continue
        name, axis, labs = m.groups()
        r = self.roots.get(name)
        if not r:
            # корень мог приклеить цифру к имени, например GOOD0; попробуем без хвоста
            add("unknown_root", name)
            continue
        if axis is not None:
            if not r.get("axis"):
                add("axis_on_axisless", f"{name}{axis}")
            else:
                v = int(axis)
                lo = 0 if r.get("one_sided") else -5
                if not lo <= v <= 5:
                    add("axis_range", f"{name}{axis}")
        seen = set()
        for lab in filter(None, labs.split(".")):
            letter = lab[0]
            if letter not in self.labels:
                add("unknown_label", lab)
                continue
            if letter in seen:
                add("dup_label", lab)
            seen.add(letter)
            if self.labels[letter].get("bare"):
                if len(lab) > 1:
                    add("label_value", lab)
                continue
            val = lab[1:]
            if not val:
                add("label_value", f"{lab}: нет значения")
                continue
            lo, hi = self.labels[letter]["range"]
            if not lo <= int(val) <= hi or (letter == "I" and int(val) == 0):
                add("label_range", lab)
    if depth > 0:
        add("brackets", "незакрытая `[`")
    return issues


Validator.check_toki = check_toki


def check_any(self, code):
    """Предложение с `{ }` проверяется как записанное по границам слов, иначе обычным разбором."""
    return self.check_braced(code) if "{" in code or "}" in code else self.check(code)


Validator.check_braced = check_braced
Validator.check_any = check_any


def iter_codes(path):
    for line in open(path, encoding="utf8"):
        m = re.match(r"\s*\d+\.\s*(.*\S)", line)
        if m:
            yield m.group(1)


def main():
    v = Validator()
    braces = "--braces" in sys.argv  # принудительно; без флага `{` в коде включает режим сам
    files = [a for a in sys.argv[1:] if a != "--braces"]
    for f in files:
        n = bad = 0
        kinds = Counter()
        for code in iter_codes(f):
            n += 1
            iss = [i for i in (v.check_braced(code) if braces else v.check_any(code)) if i.level == "error"]
            bad += bool(iss)
            kinds.update({i.kind + ": " + i.msg.split(" ")[0] for i in iss})
        print(f"{f}: {n} кодов, с ошибками {bad} ({100 * bad / max(n, 1):.0f}%)")
        for kk, c in kinds.most_common(8):
            print("   ", c, kk)


if __name__ == "__main__":
    main()
