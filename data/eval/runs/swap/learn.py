# Шаг 1 (замена корней): атом одного кандидата при замороженных 45 атомах сайта, как ../kind/learn.py.  python learn.py NAME → atoms/NAME.json
# Полюса — шкалы Haiku из ../axes2 (proposals/), центр — середина полюсов.
import importlib.util, json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../.."); sys.path.insert(0, f"{REPO}/scripts")
from lib_code import Data, root_specs, Coder, encode_all, unit
sp = importlib.util.spec_from_file_location("sl", f"{REPO}/scripts/18_sparse_learn.py"); sl = importlib.util.module_from_spec(sp); sp.loader.exec_module(sl)
CAND = {  # имя: (+ полюс, − полюс)
    "OPEN": ("open unlocked ajar exposed unsealed accessible available clear", "closed shut locked sealed blocked fastened barred bolted"),
    "PUBLIC": ("public common communal collective shared general civic national", "private personal secret confidential intimate hidden individual covert"),
    "MAKE": ("build construct create make erect assemble found establish", "destroy demolish ruin wreck raze break smash eliminate"),
    "LAW": ("legal lawful legitimate licit permitted authorized sanctioned allowed", "illegal unlawful illicit illegitimate banned forbidden criminal prohibited"),
    "LAST": ("permanent lasting enduring eternal fixed lifelong perpetual durable", "temporary brief passing transient momentary fleeting provisional interim"),
}
N = sys.argv[1]; s = root_specs(extra=[(N, *CAND[N], None)]); d = Data([s]); names, C0, A0 = d.dictionary(s)
m = json.load(open(f"{REPO}/site/data/math.json")); K = len(m["names"]); assert names[:K] == m["names"] and names[K] == N, names
C, A = C0.copy(), A0.copy(); C[:K], A[:K] = np.array(m["dict"]["C"]), np.array(m["dict"]["A"])
R = len(C); L = [K, R + K]; O = [i for i in range(2 * R) if i not in L]; Xtr = d.V[d.train]
for it in range(sl.ITERS):
    co = Coder(C, A, head_w=sl.HW); codes = encode_all(co, Xtr); M = co.design(codes); Th = np.concatenate([C, A])
    T = np.linalg.norm(M @ Th, axis=1)[:, None] * Xtr - M[:, O] @ Th[O]
    ML = M[:, L]; th0 = np.concatenate([C0, A0])[L]
    new = np.linalg.solve(ML.T @ ML + sl.LAM * np.eye(2), ML.T @ T + sl.LAM * th0)
    new = np.stack([sl.clamp(unit(new[k]), th0[k], sl.TAU) for k in range(2)]); C[K], A[K] = new
    print(f"{N} итерация {it + 1}: cos с исходным {C[K] @ C0[K]:.2f} / {A[K] @ A0[K]:.2f}", flush=True)
os.makedirs(f"{D}/atoms", exist_ok=True); json.dump({"C": C[K].tolist(), "A": A[K].tolist(), "plus": CAND[N][0], "minus": CAND[N][1]}, open(f"{D}/atoms/{N}.json", "w"))
