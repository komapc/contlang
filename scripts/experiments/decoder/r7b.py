import sys; sys.argv = ['x', '0']
exec(open(__import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/' + 'r7.py').read().split("if __name__")[0])
ix = {n: i for i, n in enumerate(names)}; wi = {w: i for i, w in enumerate(W)}
def P(code): 
    out = []
    for t in code.split():
        n, _, v = t.partition('(='); out.append((ix[n], int(v.rstrip(')')) if v else 0))
    return [a for a, b in out], [b for a, b in out]
pairs = [("VALUE GIVE(=+4)", "GIVE(=+3) VALUE", "pay", "sell"), ("PLACE CONSUME(=+5)", "CONSUME(=+5) PLACE", "restaurant", "eat"),
         ("TEXT SOMEONE", "SOMEONE TEXT", "letter", "writer"), ("BODY MOVE(=+3)", "MOVE(=+3) BODY", "leg", "walk"),
         ("HEAT(=+3) CONSUME(=+5)", "CONSUME(=+5) HEAT(=+3)", "cook", "eat"), ("SOMEONE FIGHT(=+3)", "FIGHT(=+3) SOMEONE", "soldier", "war")]
for key in ("A сейчас 1/.6/.6", "M центр модиф. ×.25"):
    print("\n##", key)
    for c1, c2, w1, w2 in pairs:
        row = []
        for c in (c1, c2):
            R, v = P(c); wc, wa = VARS[key]; Pp = parts(R, v, wc, wa); Sv = V @ unit(sum(Pp)); Z = zc(V @ unit(np.stack(Pp)).T)
            pw = np.array(wc[:len(R)]) + np.array(wa[:len(R)]); soft = -np.log((np.exp(-2 * Z) * pw / pw.max()).sum(1)) / 2
            mix = 0.5 * zc(2 * Sv - hub(key)) + 0.5 * soft; rk = lambda w: int((mix > mix[wi[w]]).sum()) + 1
            row.append(f"`{c}` → {', '.join(W[t] for t in np.argsort(-mix)[:4])} ({w1} #{rk(w1)}, {w2} #{rk(w2)})")
        print("| " + " | ".join(row) + " |")
