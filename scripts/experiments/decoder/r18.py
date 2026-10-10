"""r18: какое слово-уточнение понятно читателю. Цели — леммы, для которых r13 depth+neigh ставит цель первой.
Для главного и уровня из r13 перебираются все допустимые уточнения (300 ближайших, правила r13) и берутся те,
при которых математика (смесь, кандидаты KIND_D[h, d]) ставит цель первой. Из них выбор:
  r13   — как в r13 (лучшее по r12 read_words без уровня);
  gloss — слово из толкования или примеров WordNet цели (по лемме), иначе — частое;
  freq  — самое частое слово (место в словаре сайта, он по частоте);
  sim   — самое близкое к цели по cos.
Пишет data/eval/runs/modifier_choice/{key.json, codes_*.md}. Запуск: r18.py [число слов] [seed]."""
import sys, random
SP = __import__('os').path.dirname(__import__('os').path.abspath(__file__)) + '/'
ARGV = sys.argv[1:]
exec(open(SP + 'r13.py').read().split("\nif __name__ == '__main__':")[0])
N_, SEED = (int(ARGV[0]) if ARGV else 30), (int(ARGV[1]) if len(ARGV) > 1 else 5)
R13 = json.load(open(SP + 'r13.json'))
used = {k[0] for k in json.load(open('data/eval/runs/level_notation/key.json'))}

def gloss_lemmas(w):
    out = set()
    for s in wn.synsets(w)[:3]:
        for tok in re.findall(r"[a-z]+", (s.definition() + ' ' + ' '.join(s.examples())).lower()):
            out |= {tok} | {x for p in 'nvar' for x in [wn.morphy(tok, p)] if x}
    return out

def choose(w):
    t = wi[w]; h_w, d, m13 = R13[w]['depth+neigh'][1]; h = wi[h_w]
    ex = {h} | {j for j, x in enumerate(W) if same(x, W[h]) and j != t}
    hsyn = heads2(t)[h][0]
    ss = wn.synsets(w)[:3]; syn = {l.lower() for s in ss for l in s.lemma_names()}
    near = [int(j) for j in np.argsort(-(V @ V[t]))[:300]]
    def ok(m_):
        x = W[m_]
        if m_ == h or m_ == t or m_ not in gset or not wn.synsets(x) or namey(m_) or x in syn or same(x, w) or same(x, W[h]): return False
        return not any(hsyn in up(s, 8) or s == hsyn for s in syns(x))
    good1 = [m_ for m_ in near if ok(m_) and rank_in(pair_mix(h, m_), t, KIND_D[h, d] - ex - {m_})[0] == 1]
    if not good1: return None
    gl = gloss_lemmas(w)
    freq = min(good1)                                       # словарь сайта упорядочен по частоте
    gls = [m_ for m_ in good1 if W[m_] in gl]
    return {'word': w, 'head': h_w, 'd': d, 'n_ok': len(good1), 'r13': m13,
            'gloss': W[min(gls)] if gls else W[freq], 'gloss_hit': bool(gls),
            'freq': W[freq], 'sim': W[max(good1, key=lambda m_: V[m_] @ V[t])]}

if __name__ == '__main__':
    pool = sorted(w for w, b in R13.items() if b.get('depth+neigh', [9])[0] == 1 and w.isalpha() and w in _low
                  and wn.morphy(w) == w and w not in used and not namey(wi[w]))
    random.Random(SEED).shuffle(pool)
    out = []
    for w in pool:
        c = choose(w)
        if c: out.append(c); print(c, flush=True)
        if len(out) == N_: break
    D = 'data/eval/runs/modifier_choice/'; __import__('os').makedirs(D, exist_ok=True)
    json.dump(out, open(D + 'key.json', 'w'), ensure_ascii=False, indent=0)
    for v in ('r13', 'gloss', 'freq', 'sim'):
        open(D + f'codes_{v}.md', 'w').write(''.join(f"{i}. {c['head']} PI(={c['d']}) {c[v]}\n" for i, c in enumerate(out, 1)))
    print('с уточнением из толкования:', sum(c['gloss_hit'] for c in out), 'из', len(out))
