# Обучение только LAND при замороженных 44 атомах сайта (site/data/math.json): та же постановка, что scripts/18_sparse_learn.py
# (коды → гребневая регрессия с притяжением к атому из полюсов, λ 30, cos ≥ 0,85, 3 итерации), но решается только строка LAND:
# min ‖M_L θ_L − (T − M_old θ_old)‖² + λ‖θ_L − θ0_L‖².  → dict45.npz
import importlib.util, json, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../.."); sys.path.insert(0, f"{REPO}/scripts")
from lib_code import Data, root_specs, Coder, encode_all, unit
sp = importlib.util.spec_from_file_location("sl", f"{REPO}/scripts/18_sparse_learn.py"); sl = importlib.util.module_from_spec(sp); sp.loader.exec_module(sl)
NEW = [("LAND", "land ground soil earth terrain mainland", "sea ocean water lake waves seawater", "land country region territory landscape shore")]
s45 = root_specs(extra=NEW); d = Data([s45]); names, C0, A0 = d.dictionary(s45)
m = json.load(open(f"{REPO}/site/data/math.json")); assert names[:44] == m["names"]
C, A = C0.copy(), A0.copy(); C[:44], A[:44] = np.array(m["dict"]["C"]), np.array(m["dict"]["A"])
R = len(C); L = [44, R + 44]; O = [i for i in range(2 * R) if i not in L]; Xtr = d.V[d.train]
for it in range(sl.ITERS):
    co = Coder(C, A, head_w=sl.HW); codes = encode_all(co, Xtr); M = co.design(codes); Th = np.concatenate([C, A])
    T = np.linalg.norm(M @ Th, axis=1)[:, None] * Xtr - M[:, O] @ Th[O]
    ML = M[:, L]; th0 = np.concatenate([C0, A0])[L]
    new = np.linalg.solve(ML.T @ ML + sl.LAM * np.eye(2), ML.T @ T + sl.LAM * th0)
    new = np.stack([sl.clamp(unit(new[k]), th0[k], sl.TAU) for k in range(2)]); C[44], A[44] = new
    print(f"итерация {it + 1}: использований LAND {sum(44 in e[0] for e in codes) if hasattr(codes[0][0], '__iter__') else '?'}; cos с исходным {C[44] @ C0[44]:.2f} / {A[44] @ A0[44]:.2f}", flush=True)
np.savez(f"{D}/dict45.npz", names=np.array(names), C=C, A=A)
