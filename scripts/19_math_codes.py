"""Коды без языковой модели для слепой проверки декодером (docs/math.md).

Математический кодер (lib_code.Coder) кодирует слова двумя словарями:
корни из полюсов roots.yaml и обученный словарь (data/sparse_dict_learned.npz).
Слова: 12 орудий из прошлого слепого теста (roundtrip_tools) и 12 случайных
существительных из отложенной части. Пишет data/math_codes.tsv
(слово, источник, код полюсов, код обученного словаря); коды без
оригиналов отдаются слепым декодерам, результат — data/translation_test/roundtrip_math.md.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from lib_code import POS_FORM, Coder, Data, fmt_code, root_specs, s15, unit  # noqa: E402

TOOLS = "knife hammer saw needle key spoon brush scissors pen broom ladder thermometer".split()
OUT = ROOT / "data" / "math_codes.tsv"


def main():
    specs = root_specs()
    d = Data([specs])
    names, C0, A0 = d.dictionary(specs)
    D = np.load(ROOT / "data" / "sparse_dict_learned.npz")
    assert list(D["names"]) == names
    C, A = D["C"], D["A"]
    rng = np.random.default_rng(1)
    nouns = [d.vocab[i] for i in d.test if d.pos.get(d.vocab[i]) == "noun"]
    sample = list(rng.choice(nouns, 12, replace=False))
    vec = s15.load_subset(set(d.vec) | set(TOOLS))
    co0, co1 = Coder(C0, A0, head_w=0.6), Coder(C, A, head_w=0.6)
    lines = ["word\tsource\tcode_poles\tcode_learned"]
    for src, ws in (("tools", TOOLS), ("test", sample)):
        for w in ws:
            x = unit(unit(vec[w]) - d.mu)
            form = POS_FORM.get(d.pos.get(w, "noun"), "o")
            c0 = fmt_code(names, A0, *co0(x)[:2], form)
            c1 = fmt_code(names, A, *co1(x)[:2], form)
            lines.append(f"{w}\t{src}\t{c0}\t{c1}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
