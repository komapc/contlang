"""size0: chart → size.svg (plain SVG, no dependencies).  .venv/bin/python data/eval/runs/size0/plot.py"""
import json, math
from pathlib import Path

D = Path(__file__).resolve().parent
C = json.load(open(D / "curve.json"))
BLUE, BLUE_L, ORANGE, INK, INK2, GRID = "#2a78d6", "#86b6ef", "#eb6834", "#1f1f1e", "#6b6a64", "#e4e3de"
W, H = 1000, 470
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="13">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
T = lambda x, y, s, **k: out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{k.get("c", INK2)}" text-anchor="{k.get("a", "start")}" '
                                    f'font-size="{k.get("fs", 13)}" font-weight="{k.get("fw", "normal")}">{s}</text>')

def panel(x0, title, sub, ylab, ymin, ymax, yticks, yfmt):
    px, py, pw, ph = x0 + 58, 92, 380, 300
    T(x0 + 10, 30, title, c=INK, fs=16, fw="bold"); T(x0 + 10, 50, sub)
    lx = lambda L: px + (math.log10(L) - math.log10(50)) / (math.log10(20000) - math.log10(50)) * pw
    ly = lambda v: py + ph - (v - ymin) / (ymax - ymin) * ph
    for v in yticks:
        out.append(f'<line x1="{px}" x2="{px + pw}" y1="{ly(v):.1f}" y2="{ly(v):.1f}" stroke="{GRID}"/>')
        T(px - 8, ly(v) + 4, yfmt(v), a="end")
    for L in (100, 300, 1000, 3000, 10000):
        out.append(f'<line x1="{lx(L):.1f}" x2="{lx(L):.1f}" y1="{py}" y2="{py + ph}" stroke="{GRID}" stroke-width="0.7"/>')
        T(lx(L), py + ph + 18, f"{L:,}", a="middle")
    T(px + pw / 2, py + ph + 40, "units to learn L (roots, marks… + lexicon entries), log scale", a="middle")
    T(x0 + 10, 76, ylab)
    return lx, ly

def line(pts, color, dash=""):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    out.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="2" {dash}/>')

def dot(x, y, color, hollow=False):
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{"#fff" if hollow else color}" stroke="{color}" stroke-width="2"/>')

# panel 1: words (model from big1000)
lx, ly = panel(0, "Words: share of text understood", "model: big1000 + lexicon of the N most frequent words (Brown)",
               "read as close, % of word tokens", 20, 100, (20, 40, 60, 80, 100), lambda v: f"{v}%")
pts = [(lx(c["L"]), ly(100 * c["U09"])) for c in C if c["N"] <= 10000]
line([(lx(c["L"]), ly(100 * c["U"])) for c in C if c["N"] <= 10000], BLUE_L, 'stroke-dasharray="5 4"')
line(pts, BLUE)
for c in C:
    if c["N"] in (0, 300, 1000, 3000, 10000):
        dot(lx(c["L"]), ly(100 * c["U09"]), BLUE)
        T(lx(c["L"]) + 7, ly(100 * c["U09"]) + 17, f'{100 * c["U09"]:.0f}%', c=INK)
T(lx(10076) - 4, ly(98) - 8, "ceiling (entry always read right)", a="end")
T(lx(1500), ly(62), "min-co + N entries", c=BLUE, fw="bold")
dot(lx(120), ly(34), ORANGE, hollow=True)
T(lx(120) + 9, ly(34) + 4, "Toki Pona ≈ 34% (estimate, from cos)", c=INK)

# panel 2: sentences (lexn1 measurement, same judges)
lx, ly = panel(510, "Sentences: lexn1 measurement", "60 bench1 dev sentences, the same 4 judges",
               "meaning, 0–3", 0.8, 2.4, (1.0, 1.4, 1.8, 2.2), lambda v: f"{v:.1f}")
S = [(76, 0.97, "mc"), (376, 1.14, "+300"), (1076, 1.50, "+1000"), (3076, 1.79, "+3000")]
line([(lx(L), ly(v)) for L, v, _ in S], BLUE)
for L, v, n in S:
    dot(lx(L), ly(v), BLUE); T(lx(L) + 7, ly(v) + 17, f"{n}: {v:.2f}", c=INK)
out.append(f'<line x1="{lx(76):.1f}" x2="{lx(20000):.1f}" y1="{ly(2.31):.1f}" y2="{ly(2.31):.1f}" stroke="{BLUE_L}" stroke-width="2" stroke-dasharray="5 4"/>')
T(lx(20000) - 4, ly(2.31) - 8, "all words known: 2.31", a="end")
dot(lx(120), ly(1.10), ORANGE)
T(lx(70), ly(1.32), "Toki Pona (cipher): 1.10", c=INK)
out.append(f'<line x1="{lx(120):.1f}" y1="{ly(1.10)-6:.1f}" x2="{lx(110):.1f}" y2="{ly(1.30)+5:.1f}" stroke="{ORANGE}"/>')
out.append("</svg>")
(D / "size.svg").write_text("\n".join(out))
print("size.svg")
