"""Сборка спецификаций и подсчёт оценок на сохранённых прогонах."""
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "eval"))
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
import prepare  # noqa: E402
import score  # noqa: E402
import spec  # noqa: E402


def test_spec_has_all_roots_and_axes():
    for kind in ("enc", "dec"):
        for task in ("words", "sents"):
            t = prepare.build_spec(kind, task)
            assert "{{" not in t
            for r in spec.axis_roots():
                assert f"- {r['name']}: " in t, (kind, task, r["name"])
            assert "MAYBE" not in t and "CONTAINER" not in t
            assert f"{len(spec.root_names())} roots (NSM-like" in t


def test_drop_and_add_axis():
    t = prepare.build_spec("enc", "words", drop=["SIDE"], axes={"SEE": "visibility: -5 hidden ... +5 bright"})
    assert "- SIDE:" not in t and "- SEE: visibility" in t
    assert "44 roots (NSM-like" in t


def test_score_reproduces_saved_runs():
    run = REPO / "data" / "eval" / "runs" / "ablation3"
    G = score.load(run / "judge_map.json", [run / "scores_words.tsv"])
    import statistics as st
    assert round(st.mean(G["full"].values()), 2) == 1.73
    assert round(st.mean(G["abl"].values()), 2) == 1.87
