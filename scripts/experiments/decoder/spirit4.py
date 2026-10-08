import json, gzip, numpy as np
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
m = json.load(open('site/data/math.json')); W = m['words']; wi = {w: i for i, w in enumerate(W)}
V = np.frombuffer(open('site/data/vocab.bin', 'rb').read(), np.int8).reshape(len(W), m['dim']).astype(float)
V /= np.linalg.norm(V, axis=1, keepdims=True) + 1e-9
unit = lambda x: x / np.linalg.norm(x, axis=-1, keepdims=True)
P = "spiritual religious sacred holy divine"
NEG = {"secular-набор": "materialistic secular worldly mundane earthly",
       "без secular": "materialistic worldly mundane earthly",
       "мирское+материя": "materialistic worldly mundane earthly material",
       "быт": "mundane everyday ordinary practical earthly",
       "торг": "materialistic commercial profitable consumer mundane"}
need = set((P + " " + " ".join(NEG.values())).split())
got = {}
with gzip.open('data/raw/numberbatch-en-19.08.txt.gz', 'rt', encoding='utf8') as f:
    next(f)
    for line in f:
        w, rest = line.split(' ', 1)
        if w in need:
            got[w] = unit(np.array(rest.split(), dtype=float))
            if len(got) == len(need): break
print("не найдены:", need - set(got))
np.savez(SP + 'spirit_poles.npz', words=np.array(list(got)), X=np.stack(list(got.values())))
probe = "islamist fundamentalist secular extremist church priest soul money wealth profit shopping consumer machine science body physical practical business atheist".split()
for lab, n in NEG.items():
    poles = set((P + " " + n).split())
    a = unit(np.mean([got[w] for w in P.split()], 0) - np.mean([got[w] for w in n.split()], 0))
    s = V @ a; o = np.argsort(s); k = np.array([w not in poles for w in W])
    print(f"\n## {lab}: −{n}\n  − край:", ", ".join([W[t] for t in o if k[t]][:14]))
    print("  + край:", ", ".join([W[t] for t in o[::-1] if k[t]][:10]))
    print("  проба:", "  ".join(f"{w} {s[wi[w]]:+.2f}" for w in probe if w in wi and w not in poles))
