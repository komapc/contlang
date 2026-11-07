"""Проверка кода в воркере (worker/check.js) и scripts/mincode/validator.py согласны: код, который принял один, принимает и другой."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
import spec  # noqa: E402
from validator import Validator  # noqa: E402

# (код, есть ли ошибка)
CASES = [
    ("GRAIN(=0) THING(=-5) PART(=-5) | o", False),
    ("THING(=+4) BIG(=+5) | o N+3", False),
    ("MOVE NEAR(=+4) | i T-2 M-5", False),
    ("TEXT | o tool", False),
    ('TIME MEASURE "10" | o', False),
    ("BIG(=-4) | o tool FOR PART(=-2) PLACE SIDE(=+5) | o", False),
    ("INSIDE(=+5) JOIN(=+5) | o FOR JOIN(=-4) TOUCH(=+4) | o tool", False),
    ("FEEL(=+4) GOOD(=-4) TIME(=+3) | i T+2 N+4", False),
    ("SAY | i !", False),
    ("THING(=+5) | o", True),           # THING до +4 (limits.levels)
    ("SEX(=+1) SOMEONE | o", True),     # SEX только |v| ≥ 3
    ("SEX(=0) SOMEONE | o", True),
    ("SEX(=-3) SOMEONE | o", False),
    ("THING(=3) | o", True),            # значение без знака
    ("THING(=+6) | o", True),
    ("PLACE(=+2) | o", True),           # у корня нет оси
    ("NOSUCH | o", True),
    ("THING BIG PART ABOVE | o", True),  # четыре корня
    ("THING BIG", True),                # нет `| форма`
    ("THING | x", True),                # нет такой части речи
    ("THING | o T+9", True),            # метка вне диапазона
    ("THING | o T+1 T+2", True),        # метка дважды
    ("THING | a I0", True),
    ("THING | o Q+1", True),            # нет такой метки
    ("THING | i tool", True),           # роль только у `o`
    ("THING | o tool agent", True),     # две роли
    ("BIG(=-4) | o FOR THING(=+5) | o", True),  # ошибка во втором слове пары
]


def test_python_validator_cases():
    v = Validator()
    for code, bad in CASES:
        errs = [i for i in v.check(code) if i.level == "error"]
        assert bool(errs) == bad, (code, errs)


def test_levels_come_from_roots_yaml():
    prompts = (REPO / "worker" / "prompts.js").read_text(encoding="utf8")
    check = json.loads(prompts.split("export const CHECK = ", 1)[1].split("\n", 1)[0].rstrip().rstrip(";"))
    assert check["levels"] == spec.levels()
    assert json.loads((REPO / "site" / "data" / "math.json").read_text(encoding="utf8"))["levels"] == spec.levels()


@pytest.mark.skipif(not shutil.which("node"), reason="нужен node")
def test_worker_agrees_with_validator():
    script = ("import { codeProblems } from './worker/check.js';"
              "const cs = JSON.parse(process.argv[1]); console.log(JSON.stringify(cs.map(codeProblems)));")
    out = subprocess.run(["node", "--input-type=module", "-e", script, json.dumps([c for c, _ in CASES])],
                         cwd=REPO, capture_output=True, text=True, check=True).stdout
    for (code, bad), probs in zip(CASES, json.loads(out)):
        assert bool(probs) == bad, (code, probs)


# предложения (режим sentence воркера): каждое слово в { }, снаружи только частицы и имена в кавычках
SENT_CASES = [
    ('"Martin" { SAY | i T-2 } E [ { SOMEONE | o N+3 } { MOVE(=-5) | i ! } AND { CARE(=+5) | i } ]', False),
    ("{ THING(=+4) BIG(=+5) | o N+3 } ; { MOVE | i T-2 }", False),
    ("{ THING | o } of { MOVE | i }", True),      # английское слово вне скобок
    ("{ THING(=3) | o }", True),                  # ошибка внутри слова
    ("{ THING | o", True),                        # скобка не закрыта
    ("MOVE | i", True),                           # нет слов в скобках
]


@pytest.mark.skipif(not shutil.which("node"), reason="нужен node")
def test_sentence_problems():
    script = ("import { sentenceProblems } from './worker/check.js';"
              "const cs = JSON.parse(process.argv[1]); console.log(JSON.stringify(cs.map(sentenceProblems)));")
    out = subprocess.run(["node", "--input-type=module", "-e", script, json.dumps([c for c, _ in SENT_CASES])],
                         cwd=REPO, capture_output=True, text=True, check=True).stdout
    for (code, bad), probs in zip(SENT_CASES, json.loads(out)):
        assert bool(probs) == bad, (code, probs)
