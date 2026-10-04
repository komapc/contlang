"""Проверка кода min-co по roots.yaml.

    python3 scripts/mincode/validator.py FILE...   # строки вида "12. КОД" или просто код

Уровни: error (неправильный код), warning (старая запись или спорное место).
Правила: кавычки непрозрачны; слово = корни `|` часть речи метки; корней не больше
лимита (ABSTRACT сверх лимита); значение оси только у корней с осью, в −5…+5
(MANY: 0…+5); метки из списка, каждая не более одного раза, в своём диапазоне,
`I0` запрещён; `!` и `?` без значения; скобки сбалансированы.
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

        def end_word():
            nonlocal word, state, seen_labels, has_bar
            if word:
                body = [r for r in word if r != self.extra]
                if len(body) > self.max_roots:
                    add("error", "too_many_roots", f"{len(body)} корней (лимит {self.max_roots}): {' '.join(word)}")
                if word.count(self.extra) > 1:
                    add("error", "too_many_roots", f"{self.extra} дважды")
                if not has_bar:
                    add("warning", "no_form", f"слово без `| форма`: {' '.join(word)}")
            word, state, seen_labels, has_bar = [], "roots", set(), False

        for m in TOKEN.finditer(code):
            k = m.lastgroup
            if k == "arg":
                k = "root"
            if k == "ws":
                continue
            t = m.group(0)
            if k == "q":
                end_word()
            elif k == "badq":
                add("error", "bad_quote", "непарная кавычка")
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
                    continue
                if state != "roots":
                    end_word()
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
            elif k == "num":
                add("warning", "unquoted_number", t)
            else:
                add("error", "stray", t)
        end_word()
        if depth > 0:
            add("error", "brackets", "незакрытая `[`")
        return issues


def iter_codes(path):
    for line in open(path, encoding="utf8"):
        m = re.match(r"\s*\d+\.\s*(.*\S)", line)
        if m:
            yield m.group(1)


def main():
    v = Validator()
    for f in sys.argv[1:]:
        n = bad = 0
        kinds = Counter()
        for code in iter_codes(f):
            n += 1
            iss = [i for i in v.check(code) if i.level == "error"]
            bad += bool(iss)
            kinds.update({i.kind + ": " + i.msg.split(" ")[0] for i in iss})
        print(f"{f}: {n} кодов, с ошибками {bad} ({100 * bad / max(n, 1):.0f}%)")
        for kk, c in kinds.most_common(8):
            print("   ", c, kk)


if __name__ == "__main__":
    main()
