# Обучение только KIND при замороженных 45 атомах сайта (site/data/math.json), как ../adopt3/learn.py для LAND:
# коды → гребневая регрессия с притяжением к атому из полюсов (λ 30, cos ≥ 0,85, 3 итерации), решается только строка KIND.  → dict46.npz
# KIND: −5 один случай, пример, образец … +5 вид, тип, класс (без значения — вид, сорт).
import importlib.util, json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../.."); sys.path.insert(0, f"{REPO}/scripts")
from lib_code import Data, root_specs, Coder, encode_all, unit
sp = importlib.util.spec_from_file_location("sl", f"{REPO}/scripts/18_sparse_learn.py"); sl = importlib.util.module_from_spec(sp); sp.loader.exec_module(sl)
NEW = [("KIND", "kind type category class sort genre variety species", "example instance sample specimen case illustration", "kind type sort example sample model pattern")]
s = root_specs(extra=NEW); d = Data([s]); names, C0, A0 = d.dictionary(s)
m = json.load(open(f"{REPO}/site/data/math.json")); K = len(m["names"]); assert names[:K] == m["names"] and names[K] == "KIND", names
C, A = C0.copy(), A0.copy(); C[:K], A[:K] = np.array(m["dict"]["C"]), np.array(m["dict"]["A"])
R = len(C); L = [K, R + K]; O = [i for i in range(2 * R) if i not in L]; Xtr = d.V[d.train]
for it in range(sl.ITERS):
    co = Coder(C, A, head_w=sl.HW); codes = encode_all(co, Xtr); M = co.design(codes); Th = np.concatenate([C, A])
    T = np.linalg.norm(M @ Th, axis=1)[:, None] * Xtr - M[:, O] @ Th[O]
    ML = M[:, L]; th0 = np.concatenate([C0, A0])[L]
    new = np.linalg.solve(ML.T @ ML + sl.LAM * np.eye(2), ML.T @ T + sl.LAM * th0)
    new = np.stack([sl.clamp(unit(new[k]), th0[k], sl.TAU) for k in range(2)]); C[K], A[K] = new
    print(f"итерация {it + 1}: cos с исходным {C[K] @ C0[K]:.2f} / {A[K] @ A0[K]:.2f}", flush=True)
np.savez(f"{D}/dict46.npz", names=np.array(names), C=C, A=A)
json.dump({"C": C[K].tolist(), "A": A[K].tolist()}, open(f"{D}/kind.json", "w"))
