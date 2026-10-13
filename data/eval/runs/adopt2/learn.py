# Обученный словарь на 44 и на 47 корнях тем же способом, что data/sparse_dict_learned.npz (scripts/18_sparse_learn.py: гребневая
# регрессия с притяжением к атомам из полюсов, λ 30, cos ≥ 0,85, 3 итерации), на одних и тех же словах (без слов-полюсов всех 47).
# Новые корни — списки полюсов как semaxis в roots.yaml. roots.yaml и site/ не трогаются.  → dict44.npz, dict47.npz
import importlib.util, os, sys, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../.."); sys.path.insert(0, f"{REPO}/scripts")
from lib_code import Data, root_specs
sp = importlib.util.spec_from_file_location("sl", f"{REPO}/scripts/18_sparse_learn.py"); sl = importlib.util.module_from_spec(sp); sp.loader.exec_module(sl)
NEW = [("LAND", "land ground soil earth terrain mainland", "sea ocean water lake waves seawater", "land country region territory landscape shore"),
       ("SACRED", "holy sacred divine blessed saint godly", "cursed demonic devilish damned unholy satanic", "religion faith spirit worship magic soul"),
       ("CONTAINER", "box jar bottle crate chest canister", "tray saucer platter plate dish lid", "container vessel receptacle bin pot bag")]
s44, s47 = root_specs(), root_specs(extra=NEW)
d = Data([s47])
for tag, s in (("44", s44), ("47", s47)):
    names, C0, A0 = d.dictionary(s); log = []
    C, A = sl.learn(d, C0, A0, log=log); print(tag, "; ".join(log), flush=True)
    np.savez(f"{D}/dict{tag}.npz", names=np.array(names), C=C, A=A, C0=C0, A0=A0)
    if tag == "47":
        for i in range(44, 47): print(names[i], "cos с исходным: центр %.2f ось %.2f" % (C[i] @ C0[i], A[i] @ A0[i]))
