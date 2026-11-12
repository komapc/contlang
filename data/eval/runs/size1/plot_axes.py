"""size1: "learn X axes → how surely is a word guessed" → axes.svg.  .venv/bin/python data/eval/runs/size1/plot_axes.py"""
import json, math
from pathlib import Path

D = Path(__file__).resolve().parent
A = json.load(open(D / "axes.json"))
C = {(x["lang"], x["k"]): x["U"] for x in json.load(open(D / "curve.json")) if x["N"] == 0 and x["a_lex"] == 0.9}
BLUE, ORANGE, INK, INK2, GRID = "#2a78d6", "#eb6834", "#1f1f1e", "#6b6a64", "#e4e3de"
RAMP = {1: "#d3d2cc", 2: "#b5b4ad", 3: "#96958f", 6: "#706f69", 9: "#4d4c47", "all": "#1f1f1e"}
RN = {1: "1 value", 2: "2 values", 3: "3 values", 6: "6 values", 9: "9 values", "all": "all X values"}
W, H = 800, 560
px, py, pw, ph = 70, 90, 520, 340
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="13">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def T(x, y, s, c=INK2, a="start", fs=13, fw="normal"):
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{c}" text-anchor="{a}" font-size="{fs}" font-weight="{fw}">{s}</text>')
lx = lambda X: px + (math.log10(X) - math.log10(5)) / (math.log10(300) - math.log10(5)) * pw
ly = lambda v: py + ph - v / 100 * ph
T(10, 30, "Learn X axes: how surely is a word guessed?", c=INK, fs=16, fw="bold")
T(10, 50, "machine: X principal axes of word vectors, a word = its values (11 levels) on its r strongest axes; people: min-co roots, size1")
T(10, 74, "read as close, % of word tokens, no lexicon")
for v in (0, 20, 40, 60, 80, 100):
    out.append(f'<line x1="{px}" x2="{px + pw}" y1="{ly(v):.1f}" y2="{ly(v):.1f}" stroke="{GRID}" stroke-width="0.7"/>')
    T(px - 8, ly(v) + 4, f"{v}%", a="end")
for X in (5, 10, 20, 51, 120, 300):
    out.append(f'<line x1="{lx(X):.1f}" x2="{lx(X):.1f}" y1="{py}" y2="{py + ph}" stroke="{GRID}" stroke-width="0.7"/>')
    T(lx(X), py + ph + 18, f"{X}", a="middle")
T(px + pw / 2, py + ph + 40, "axes (roots) to learn X, log scale", a="middle")
for r in (1, 2, 3, 6, 9, "all"):
    pts = sorted((x["X"], 100 * x["U"]) for x in A["res"] if x["r"] == r)
    d = " ".join(f"{lx(X):.1f},{ly(u):.1f}" for X, u in pts)
    out.append(f'<polyline points="{d}" fill="none" stroke="{RAMP[r]}" stroke-width="2"/>')
for k, sh in ((1, -1), (2, 0), (3, 1)):
    u = 100 * C[("mc", k)]
    out.append(f'<circle cx="{lx(51) + 7 * sh:.1f}" cy="{ly(u):.1f}" r="5" fill="{BLUE}" stroke="#fff" stroke-width="1.5"/>')
    u = 100 * C[("tp", k)]
    out.append(f'<circle cx="{lx(120) + 7 * sh:.1f}" cy="{ly(u):.1f}" r="5" fill="{ORANGE}" stroke="#fff" stroke-width="1.5"/>')
T(lx(51) - 14, ly(100 * C[("mc", 3)]) - 12, "min-co", c=BLUE, a="end", fw="bold")
T(lx(120) + 14, ly(100 * C[("tp", 3)]) - 10, "Toki Pona", c=ORANGE, fw="bold")
lgx, lgy = px + pw + 20, py + 10
T(lgx, lgy, "machine, values per word", c=INK, fw="bold")
for j, r in enumerate((1, 2, 3, 6, 9, "all"), 1):
    y = lgy + 18 * j
    out.append(f'<line x1="{lgx}" x2="{lgx + 30}" y1="{y - 4}" y2="{y - 4}" stroke="{RAMP[r]}" stroke-width="2"/>')
    u = next(100 * x["U"] for x in A["res"] if x["r"] == r and x["X"] == 51)
    T(lgx + 36, y, f"{RN[r]}: {u:.0f}% at 51", c=INK)
T(lgx, lgy + 150, "min-co (51 roots)", c=INK, fw="bold")
for j, (k, nm, rt) in enumerate(((1, "1 word", 1.7), (2, "up to 2", 1.9), (3, "up to 3", 2.7)), 1):
    T(lgx, lgy + 150 + 18 * j, f"{nm}: {100 * C[('mc', k)]:.0f}% ({rt} roots)", c=INK)
T(lgx, lgy + 240, "Toki Pona (120 words)", c=INK, fw="bold")
T(lgx, lgy + 258, " / ".join(f"{100 * C[('tp', k)]:.0f}" for k in (1, 2, 3)) + "% (1 / ≤2 / ≤3 words)", c=INK)
T(10, H - 30, f"Machine reader: nearest word vector among 21,514 Brown lemmas with a frequency prior — it knows every word's exact position. "
              f"Close = same word,", fs=10.5)
T(10, H - 15, f"WordNet synonym or cosine ≥ {A['theta']:.2f} (agrees with the human judges on 91% of size1 answers). People's points: measured. "
              f"See axes.txt.", fs=10.5)
out.append("</svg>")
(D / "axes.svg").write_text("\n".join(out))
print("axes.svg")
