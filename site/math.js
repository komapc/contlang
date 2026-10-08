// Математический кодер min-co в браузере: перенос scripts/lib_code.py (Coder), см. docs/math.md.
// Код y = Σ w_j (c_r + s·v_j·a_r); кодер — точный перебор опор до трёх корней из topr лучших,
// всех уровней −5…+5 и выбора главного корня; цель — max cos(x, y).
(function (root) {
  "use strict";
  const LEVELS = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5];

  function combos(arr, k) {
    const out = [];
    const rec = (start, acc) => {
      if (acc.length === k) { out.push(acc.slice()); return; }
      for (let i = start; i < arr.length; i++) { acc.push(arr[i]); rec(i + 1, acc); acc.pop(); }
    };
    rec(0, []);
    return out;
  }

  function grid(flags) {
    let rows = [[]];
    for (const f of flags) {
      const next = [];
      for (const r of rows) for (const v of (f ? LEVELS : [0])) next.push(r.concat(v));
      rows = next;
    }
    return rows;
  }

  class Coder {
    // dict: {C, A} — массивы R×dim; has: есть ли ось у корня
    constructor(dict, has, names, opt) {
      this.C = dict.C; this.A = dict.A; this.has = has; this.names = names;
      this.s = opt.s; this.hw = opt.head_w; this.topr = opt.topr;
      this.R = this.C.length;
      const M = this.C.concat(this.A);
      this.G = M.map((a) => M.map((b) => dot(a, b)));
      this.grids = {};
    }
    grid(flags) {
      const key = flags.join("");
      return this.grids[key] || (this.grids[key] = grid(flags));
    }
    encode(x, m = 3) {
      const cx = this.C.map((c) => dot(c, x)), ax = this.A.map((a) => dot(a, x));
      const order = [...Array(this.R).keys()].sort((i, j) => (Math.abs(cx[j]) + Math.abs(ax[j])) - (Math.abs(cx[i]) + Math.abs(ax[i])));
      const cand = order.slice(0, this.topr);
      let best = { cos: -2 };
      for (let k = 1; k <= m; k++) {
        for (const S of combos(cand, k)) {
          const heads = (k > 1 && this.hw !== 1) ? [...Array(k).keys()] : [0];
          for (const h of heads) {
            const S2 = [S[h]].concat(S.filter((_, i) => i !== h));
            const w = S2.map((_, i) => (i === 0 ? 1 : this.hw));
            const idx = S2.concat(S2.map((r) => this.R + r));
            const L = idx.length;
            const b = new Float64Array(S2.map((r) => cx[r]).concat(S2.map((r) => ax[r])));
            const Gs = new Float64Array(L * L);
            for (let i = 0; i < L; i++) for (let j = 0; j < L; j++) Gs[i * L + j] = this.G[idx[i]][idx[j]];
            const U = new Float64Array(L);
            for (let i = 0; i < k; i++) U[i] = w[i];
            for (const g of this.grid(S2.map((r) => this.has[r]))) {
              for (let i = 0; i < k; i++) U[k + i] = w[i] * this.s * g[i];
              let d = 0, n = 0;
              for (let i = 0; i < L; i++) {
                d += U[i] * b[i];
                let t = 0;
                const o = i * L;
                for (let j = 0; j < L; j++) t += Gs[o + j] * U[j];
                n += U[i] * t;
              }
              const cos = d / Math.sqrt(Math.max(n, 1e-9));
              if (cos > best.cos) best = { cos, S: S2, v: g.slice() };
            }
          }
        }
      }
      return best;
    }
    // слагаемые кода по корням: w_j (c_r + s·v·a_r); их сумма — вектор кода y
    parts(S, v) {
      return S.map((r, i) => {
        const w = i === 0 ? 1 : this.hw, c = this.C[r], a = this.A[r], p = new Float64Array(c.length);
        for (let j = 0; j < p.length; j++) p[j] = w * (c[j] + this.s * v[i] * a[j]);
        return p;
      });
    }
    // лучший один корень с лучшим уровнем: «ближайшие оси» к слову
    singles(x) {
      const out = [];
      for (let r = 0; r < this.R; r++) {
        const cx = dot(this.C[r], x), ax = dot(this.A[r], x);
        const gcc = this.G[r][r], gca = this.G[r][this.R + r], gaa = this.G[this.R + r][this.R + r];
        let best = { cos: -2, v: 0 };
        for (const v of (this.has[r] ? LEVELS : [0])) {
          const t = this.s * v;
          const cos = (cx + t * ax) / Math.sqrt(Math.max(gcc + 2 * t * gca + t * t * gaa, 1e-9));
          if (cos > best.cos) best = { cos, v };
        }
        out.push({ r, name: this.names[r], has: this.has[r], cos: best.cos, v: best.v });
      }
      return out.sort((a, b) => b.cos - a.cos);
    }
    format(S, v, form = "o") {
      return S.map((r, i) => (this.has[r] ? `${this.names[r]}(=${v[i] > 0 ? "+" : ""}${v[i]})` : this.names[r])).join(" ") + ` | ${form}`;
    }
    // «GRAIN(=0) THING(=-5) | o» → опора и уровни; всё после | и слова в кавычках игнорируются
    parse(code) {
      const head = String(code).split("|")[0].replace(/"[^"]*"/g, " ");
      const S = [], v = [], unknown = [];
      for (const m of head.matchAll(/\b([A-Z][A-Z]+)\b(?:\(=\s*([+-]?\d+)\s*\))?/g)) {
        const r = this.names.indexOf(m[1]);
        if (r < 0) { if (!["E", "PI", "LA", "AND", "PE"].includes(m[1])) unknown.push(m[1]); continue; }
        S.push(r); v.push(m[2] != null && this.has[r] ? Number(m[2]) : 0);
      }
      return { S, v, unknown };
    }
  }

  function dot(a, b) { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; }

  class Vocab {
    constructor(words, int8, dim) {
      this.words = words; this.dim = dim; this.X = int8;
      this.index = new Map(words.map((w, i) => [w, i]));
      // длина строки int8 после округления не ровно 127: для «смеси» делим на настоящую (как в Python)
      this.norm = new Float64Array(words.length);
      for (let i = 0; i < words.length; i++) { let n = 0; for (let j = 0; j < dim; j++) n += int8[i * dim + j] ** 2; this.norm[i] = Math.sqrt(n); }
    }
    vec(w) {
      const i = this.index.get(w);
      if (i == null) return null;
      const x = new Float64Array(this.dim);
      let n = 0;
      for (let j = 0; j < this.dim; j++) { x[j] = this.X[i * this.dim + j]; n += x[j] * x[j]; }
      n = Math.sqrt(n);
      for (let j = 0; j < this.dim; j++) x[j] /= n;
      return x;
    }
    // Оценки всех слов для кода (parts — слагаемые по корням, см. Coder.parts):
    // w·z(2cos(слово, Σ parts) − hub) + (1−w)·И, где hub — хабовость слова (CSLS), а
    // И = −log Σ_j exp(−k·z_j)/k — мягкий минимум z-оценок близости к каждому корню: слово должно подходить ко всем.
    scores(parts, mix) {
      const N = this.words.length, D = this.dim, K = parts.length;
      const y = new Float64Array(D);
      for (const p of parts) for (let j = 0; j < D; j++) y[j] += p[j];
      const unitv = (u) => { let n = 0; for (let j = 0; j < D; j++) n += u[j] * u[j]; n = Math.sqrt(n); return u.map((t) => t / n); };
      const vs = [unitv(y)].concat(parts.map(unitv));
      const out = vs.map(() => new Float64Array(N));
      for (let i = 0; i < N; i++) {
        const o = i * D;
        for (let q = 0; q < vs.length; q++) { const u = vs[q]; let s = 0; for (let j = 0; j < D; j++) s += this.X[o + j] * u[j]; out[q][i] = s / this.norm[i]; }
      }
      const z = (a) => { let m = 0, s = 0; for (const t of a) m += t; m /= a.length; for (const t of a) s += (t - m) ** 2; s = Math.sqrt(s / a.length) || 1; return a.map((t) => (t - m) / s); };
      const cs = z(out[0].map((c, i) => 2 * c - mix.hub[i])), Z = out.slice(1).map(z), k = mix.soft;
      const res = new Float64Array(N);
      for (let i = 0; i < N; i++) {
        let e = 0; for (let q = 0; q < K; q++) e += Math.exp(-k * Z[q][i]);
        res[i] = mix.w * cs[i] + (1 - mix.w) * (-Math.log(e) / k);
      }
      return res;
    }
    top(sc, k = 10, skip) {
      const idx = [];
      for (let i = 0; i < sc.length; i++) {
        if (skip && this.words[i] === skip) continue;
        if (idx.length < k || sc[i] > sc[idx[idx.length - 1]]) { idx.push(i); idx.sort((a, b) => sc[b] - sc[a]); if (idx.length > k) idx.pop(); }
      }
      return idx.map((i) => ({ word: this.words[i], score: sc[i] }));
    }
    rankIn(sc, w) {
      const t = this.index.get(w);
      if (t == null) return null;
      let r = 1;
      for (let i = 0; i < sc.length; i++) if (i !== t && sc[i] > sc[t]) r++;
      return r;
    }
  }

  const api = { Coder, Vocab, LEVELS };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.MincoMath = api;
})(typeof self !== "undefined" ? self : this);
