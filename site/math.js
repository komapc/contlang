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

  // lists — допустимые уровни каждого корня кода
  function grid(lists) {
    let rows = [[]];
    for (const l of lists) {
      const next = [];
      for (const r of rows) for (const v of l) next.push(r.concat(v));
      rows = next;
    }
    return rows;
  }

  class Coder {
    // dict: {C, A} — массивы R×dim; has: есть ли ось у корня
    constructor(dict, has, names, opt) {
      this.C = dict.C; this.A = dict.A; this.has = has; this.names = names;
      this.s = opt.s; this.hw = opt.head_w; this.topr = opt.topr;
      // веса позиций: главный 1, второй и третий — head_w (или opt.wts = [1, w2, w3])
      this.wts = opt.wts || [1, this.hw, this.hw];
      this.R = this.C.length;
      // допустимые уровни: opt.levels {корень: [уровни]} сужает −5…+5 (спецификация: THING до +4, SEX только явный пол)
      const lv = (opt && opt.levels) || {}, sig = [];
      for (const n in lv) if (!lv[n].length) throw new Error("empty levels for " + n);
      this.lv = names.map((n, r) => (!has[r] ? [0] : lv[n] || LEVELS));
      this.lid = this.lv.map((l) => { const k = l.join(","); let i = sig.indexOf(k); if (i < 0) { sig.push(k); i = sig.length - 1; } return i; });
      const M = this.C.concat(this.A);
      this.G = M.map((a) => M.map((b) => dot(a, b)));
      this.grids = {};
    }
    grid(S) {
      const key = S.map((r) => this.lid[r]).join(",");
      return this.grids[key] || (this.grids[key] = grid(S.map((r) => this.lv[r])));
    }
    encode(x, m = 3) {
      const cx = this.C.map((c) => dot(c, x)), ax = this.A.map((a) => dot(a, x));
      const order = [...Array(this.R).keys()].sort((i, j) => (Math.abs(cx[j]) + Math.abs(ax[j])) - (Math.abs(cx[i]) + Math.abs(ax[i])));
      const cand = order.slice(0, this.topr);
      let best = { cos: -2 };
      for (let k = 1; k <= m; k++) {
        for (const S of combos(cand, k)) {
          const heads = (k > 1 && this.wts.slice(0, k).some((t) => t !== 1)) ? [...Array(k).keys()] : [0];
          for (const h of heads) {
            const S2 = [S[h]].concat(S.filter((_, i) => i !== h));
            const w = S2.map((_, i) => this.wts[i]);
            const idx = S2.concat(S2.map((r) => this.R + r));
            const L = idx.length;
            const b = new Float64Array(S2.map((r) => cx[r]).concat(S2.map((r) => ax[r])));
            const Gs = new Float64Array(L * L);
            for (let i = 0; i < L; i++) for (let j = 0; j < L; j++) Gs[i * L + j] = this.G[idx[i]][idx[j]];
            const U = new Float64Array(L);
            for (let i = 0; i < k; i++) U[i] = w[i];
            for (const g of this.grid(S2)) {
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
        const w = this.wts[i] ?? this.hw, c = this.C[r], a = this.A[r], p = new Float64Array(c.length);
        for (let j = 0; j < p.length; j++) p[j] = w * (c[j] + this.s * v[i] * a[j]);
        return p;
      });
    }
    // cos вектора кода (S, v) со словом x
    cosOf(x, S, v) {
      const y = new Float64Array(x.length);
      for (const p of this.parts(S, v)) for (let j = 0; j < y.length; j++) y[j] += p[j];
      return dot(y, x) / Math.sqrt(Math.max(dot(y, y) * dot(x, x), 1e-12));
    }
    // лучший один корень с лучшим уровнем: «ближайшие оси» к слову
    singles(x) {
      const out = [];
      for (let r = 0; r < this.R; r++) {
        const cx = dot(this.C[r], x), ax = dot(this.A[r], x);
        const gcc = this.G[r][r], gca = this.G[r][this.R + r], gaa = this.G[this.R + r][this.R + r];
        let best = { cos: -2, v: 0 };
        for (const v of this.lv[r]) {
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
        if (r < 0) { if (!["E", "PI", "FROM", "FOR", "LIKE", "LA", "AND", "PE"].includes(m[1])) unknown.push(m[1]); continue; }
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
      if (mix.neg) for (let j = 0; j < D; j++) y[j] -= mix.neg[j];
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
    // Z[i·R + r]: z-оценка cos(слово i, центр корня r) по словарю (для штрафа за сродство с неупомянутым корнем); считается один раз
    rootZ(C) {
      if (this._Z && this._Zc === C) return this._Z;
      const N = this.words.length, D = this.dim, R = C.length, Z = new Float32Array(N * R), a = new Float64Array(N);
      for (let r = 0; r < R; r++) {
        const n = Math.sqrt(dot(C[r], C[r])); let mu = 0, sd = 0;
        for (let i = 0; i < N; i++) { let t = 0; const o = i * D; for (let j = 0; j < D; j++) t += this.X[o + j] * C[r][j]; a[i] = t / (n * this.norm[i]); mu += a[i]; }
        mu /= N; for (let i = 0; i < N; i++) sd += (a[i] - mu) ** 2; sd = Math.sqrt(sd / N) || 1;
        for (let i = 0; i < N; i++) Z[i * R + r] = (a[i] - mu) / sd;
      }
      this._Z = Z; this._Zc = C; return Z;
    }
    // сведения о словах (site/data/words.json): часть речи по WordNet, лемма, служебные слова
    setMeta(meta) {
      const N = this.words.length;
      this.pos = new Float32Array(N * 4).fill(-1);
      meta.pos.forEach((p, i) => { if (p) for (let j = 0; j < 4; j++) this.pos[i * 4 + j] = Number(p[j]) / 9; });
      this.group = Int32Array.from(meta.lemma, (l, i) => (l >= 0 ? l : i));
      this.stop = new Uint8Array(N); meta.stop.forEach((i) => { this.stop[i] = 1; });
    }
    // поправка оценок под форму кода: служебные слова убираются, слово не той части речи теряет pen·(1 − доля смыслов этой части речи)
    adjust(sc, form, pen) {
      if (!this.pos) return sc;
      const j = "oiae".indexOf(form), out = Float64Array.from(sc);
      for (let i = 0; i < out.length; i++) {
        if (this.stop[i]) { out[i] = -Infinity; continue; }
        if (j >= 0 && pen && this.pos[i * 4] >= 0) out[i] -= pen * (1 - this.pos[i * 4 + j]);
      }
      return out;
    }
    // связи ConceptNet (graph.json из scripts/site/build_graph.py; на сайте не грузится): для каждого слова — [сосед, отношение, вес, направление: 1 — слово →, −1 — ← слово]
    setGraph(g) {
      this.rel = g.rel; this.adj = Array.from(this.words, () => []);
      for (const [a, b, r, w] of g.edges) { this.adj[a].push([b, r, w, 1]); this.adj[b].push([a, r, w, -1]); }
    }
    // связь каждого слова с modWords по графу: max по m из modWords и рёбрам (w, m) веса relW[отношение+направление]·вес·decay(место m)
    // relW: {"UsedFor>": 1, "PartOf>": 1, "HasA<": 1, "RelatedTo": 0.5, ...}; «>» — слово → m, «<» — m → слово; без стрелки — любое направление
    graphScore(modWords, relW) {
      const N = this.words.length, out = new Float64Array(N);
      if (!this.adj) return out;
      modWords.forEach((mw, k) => {
        const t = this.index.get(mw); if (t == null) return;
        const g = this.group ? this.group[t] : t, decay = 1 / (1 + k / 3);
        for (const [b, r, w, dir] of this.adj[g]) {
          const name = this.rel[r], rw = relW[name] ?? relW[name + (dir === 1 ? "<" : ">")] ?? 0;   // ребро g → b: для b это «m → слово»
          if (rw) out[b] = Math.max(out[b], rw * Math.min(w, 4) / 4 * decay);
        }
      });
      if (this.group) for (let i = 0; i < N; i++) if (this.group[i] !== i) out[i] = Math.max(out[i], out[this.group[i]]);
      return out;
    }
    // пара через связку: z(scAll) + lam·z(rel), rel слова — его наибольший cos с одним из modWords
    // (векторы Numberbatch несут связи ConceptNet: key ~ door, furniture ~ house)
    pair(scAll, modWords, lam) {
      const N = this.words.length, D = this.dim, vs = modWords.map((w) => this.vec(w)).filter(Boolean), rel = new Float64Array(N);
      for (let i = 0; i < N; i++) {
        let b = -1;
        for (const v of vs) { let s = 0; for (let j = 0; j < D; j++) s += this.X[i * D + j] * v[j]; if (s > b) b = s; }
        rel[i] = scAll[i] === -Infinity ? -Infinity : b / this.norm[i];
      }
      return Vocab.zsum(scAll, rel, lam);
    }
    static zsum(a, b, lam) {
      const z = (x) => {
        let n = 0, m = 0, q = 0;
        for (const t of x) if (t > -Infinity) { n++; m += t; }
        m /= n; for (const t of x) if (t > -Infinity) q += (t - m) ** 2;
        const s = Math.sqrt(q / n) || 1; return x.map((t) => (t > -Infinity ? (t - m) / s : -Infinity));
      };
      const za = z(a), zb = z(b);
      return za.map((t, i) => t + lam * zb[i]);
    }
    // cos каждого слова с центром слов words (среднее их векторов)
    cosCenter(words) {
      const N = this.words.length, D = this.dim, y = new Float64Array(D);
      for (const w of words) { const v = this.vec(w); if (v) for (let j = 0; j < D; j++) y[j] += v[j]; }
      let n = 0; for (const t of y) n += t * t; n = Math.sqrt(n) || 1;
      const out = new Float64Array(N);
      for (let i = 0; i < N; i++) { let s = 0; for (let j = 0; j < D; j++) s += this.X[i * D + j] * y[j]; out[i] = s / n / this.norm[i]; }
      return out;
    }
    // z(sc) + lam·z(cos с центром words); убранные слова (−Infinity) остаются убранными (PRF, Reader.prf)
    toward(sc, words, lam) {
      const c = this.cosCenter(words);
      for (let i = 0; i < c.length; i++) if (sc[i] === -Infinity) c[i] = -Infinity;
      return Vocab.zsum(sc, c, lam);
    }
    // словоформы одной леммы (tool, tools) идут как одно слово: показывается лемма с оценкой лучшей формы, место считается по леммам
    top(sc, k = 10, skip) {
      const best = new Map();
      for (let i = 0; i < sc.length; i++) {
        if ((skip && this.words[i] === skip) || sc[i] === -Infinity) continue;
        const g = this.group ? this.group[i] : i, b = best.get(g);
        if (b == null || sc[i] > sc[b]) best.set(g, i);
      }
      return [...best.entries()].sort((a, b) => sc[b[1]] - sc[a[1]]).slice(0, k).map(([g, i]) => ({ word: this.words[g], score: sc[i] }));
    }
    // k ближайших к x слов-лемм, кроме служебных и словоформ skip
    near(x, k, skip) {
      const N = this.words.length, D = this.dim, t = this.index.get(skip), gs = t == null ? -1 : (this.group ? this.group[t] : t), out = [];
      for (let i = 0; i < N; i++) {
        if ((this.stop && this.stop[i]) || (this.group && this.group[i] !== i) || i === gs || (this.group && this.group[i] === gs)) continue;
        let s = 0; for (let j = 0; j < D; j++) s += this.X[i * D + j] * x[j];
        out.push([s / this.norm[i], i]);
      }
      return out.sort((a, b) => b[0] - a[0]).slice(0, k).map(([, i]) => this.words[i]);
    }
    rankIn(sc, w) {
      const t = this.index.get(w);
      if (t == null) return null;
      const G = (i) => (this.group ? this.group[i] : i), gt = G(t), best = new Map();
      for (let i = 0; i < sc.length; i++) { const g = G(i); if (!best.has(g) || sc[i] > best.get(g)) best.set(g, sc[i]); }
      const st = Math.max(sc[t], best.get(gt));
      let r = 1;
      for (const [g, s] of best) if (g !== gt && s > st) r++;
      return r;
    }
  }

  // Чтение кода векторами: слова, часть речи, пары. Общее для сайта и проверочных скриптов (scripts/site/eval_math.js).
  // opt: posPen — штраф за чужую часть речи; pairK, pairLam — сколько прочтений уточняющего слова брать и с каким весом связи;
  // modW — вес корней уточняющего слова в общем векторе (0: они уводят чтение от главного, по 107 парам слепых тестов место 203 → 112);
  // pairN — сколько соседей слова кодер пробует вторым словом (Reader.encode);
  // prfMu, prfK — PRF: сдвиг оценок к центру prfK лучших прочтений. Выключен: парам моделей помогает, а круг математики портит (docs/math.md, раздел 9).
  // graphW — вес связи по графу ConceptNet (Vocab.setGraph), relW — какие отношения считает каждая частица.
  const READ = { selfCheck: false, keepHead: true, absLam: 0.5, absTau: 1, negW: 0, posPen: 1.5, pairK: 10, pairLam: 0.25, prfK: 20, prfMu: 0, modW: 0, pairN: 40, graphW: 0, relW: {
    PI: { "PartOf>": 1, "AtLocation>": 1, "HasA<": 1, "MadeOf>": 1, "UsedFor>": 1, "IsA>": 0.5, "CapableOf>": 0.5, "ReceivesAction>": 0.5, RelatedTo: 0.5 },
    FOR: { "UsedFor>": 1, "CapableOf>": 1, "AtLocation>": 0.5, "PartOf>": 0.5, RelatedTo: 0.5 },
    FROM: { "MadeOf>": 1, RelatedTo: 0.5 },
    LIKE: { RelatedTo: 0.5 },
  } };
  const LINK = /\b(PI|FROM|FOR|LIKE)\b/;  // связки, вводящие уточняющее существительное (roots.yaml, particles)
  class Reader {
    constructor(co, V, mix, opt) { this.co = co; this.V = V; this.mix = mix; this.opt = Object.assign({}, READ, opt); }
    static form(word) { return ((String(word).split("|")[1] || "").trim().match(/^[oiae]\b/) || [""])[0]; }
    // слова кода: [{text, link}] — link: частица перед словом (у главного "")
    static words(code) {
      const parts = String(code).split(LINK), out = [{ text: parts[0], link: "" }];
      for (let i = 1; i < parts.length; i += 2) out.push({ text: parts[i + 1] || "", link: parts[i] });
      return out;
    }
    // корни всех слов кода одним набором
    parse(code) {
      const S = [], v = [], unknown = [];
      for (const w of Reader.words(code)) { const p = this.co.parse(w.text); S.push(...p.S); v.push(...p.v); unknown.push(...p.unknown); }
      return { S, v, unknown };
    }
    // «не упомянут — значит, мал»: из суммы вычитается negW·|y|·(единичный вектор суммы центров НЕупомянутых корней); при negW = 0 — как раньше
    // negVec — свой вес у каждого корня: вычитается |y|·Σ negVec[r]·C[r] по неупомянутым r (без нормировки суммы)
    mixFor(S, parts) {
      const w = this.opt.negW, wv = this.opt.negVec; if (!w && !wv) return this.mix;
      const C = this.co.C, D = C[0].length, n = new Float64Array(D), y = new Float64Array(D);
      for (let r = 0; r < C.length; r++) if (!S.includes(r)) { const k = wv ? wv[r] : 1; for (let j = 0; j < D; j++) n[j] += k * C[r][j]; }
      for (const p of parts) for (let j = 0; j < D; j++) y[j] += p[j];
      const ny = Math.sqrt(dot(y, y)), nn = wv ? 1 : Math.sqrt(dot(n, n)) || 1;
      return Object.assign({}, this.mix, { neg: n.map((t) => ((wv ? 1 : w) * ny * t) / nn) });
    }
    // оценки слов для набора корней; form — часть речи (o/i/a/e) или "" (без штрафа)
    roots(S, v, form) { const parts = this.co.parts(S, v); return this.absent(this.V.adjust(this.V.scores(parts, this.mixFor(S, parts)), form || "", this.opt.posPen), S); }
    // штраф за сродство: слово теряет absLam·max(0, max_{r ∉ S} Z − absTau) — если бы слово было сильно похоже на корень, кодер его назвал бы (data/eval/runs/absence)
    absent(sc, S) {
      const lam = this.opt.absLam; if (!lam) return sc;
      const Z = this.V.rootZ(this.co.C), R = this.co.R, tau = this.opt.absTau, inS = new Uint8Array(R); S.forEach((r) => (inS[r] = 1));
      for (let i = 0; i < sc.length; i++) { let mx = -9; const o = i * R; for (let r = 0; r < R; r++) if (!inS[r] && Z[o + r] > mx) mx = Z[o + r]; if (mx > tau) sc[i] -= lam * (mx - tau); }
      return sc;
    }
    // PRF: оценки сдвигаются к центру prfK лучших прочтений
    prf(sc) { return this.opt.prfMu ? this.V.toward(sc, this.V.top(sc, this.opt.prfK).map((n) => n.word), this.opt.prfMu) : sc; }
    // прочтения одного уточняющего слова: слово в кавычках, если оно есть в словаре, иначе pairK лучших
    readings(text) {
      const q = (text.match(/"([^"]+)"/) || [])[1];
      if (q && this.V.index.has(q.toLowerCase())) return [q.toLowerCase()];
      const p = this.co.parse(text);
      return p.S.length ? this.V.top(this.roots(p.S, p.v, Reader.form(text)), this.opt.pairK).map((n) => n.word) : [];
    }
    // оценки всех слов для кода: корни главного слова (+ modW·корни уточняющих), PRF (если prfMu), + pairLam·связь с прочтениями уточняющих слов (Vocab.pair)
    // + graphW·связь по графу с учётом частицы (Vocab.graphScore)
    scores(code) {
      const ws = Reader.words(code), h = this.co.parse(ws[0].text);
      if (!h.S.length) return new Float64Array(this.V.words.length).fill(-Infinity);  // у главного слова нет корней — читать нечего
      let parts = this.co.parts(h.S, h.v);
      if (this.opt.modW) for (const w of ws.slice(1)) { const p = this.co.parse(w.text); parts = parts.concat(this.co.parts(p.S, p.v).map((a) => a.map((t) => t * this.opt.modW))); }
      const sc = this.prf(this.V.adjust(this.V.scores(parts, this.mixFor(h.S, parts)), Reader.form(ws[0].text), this.opt.posPen));
      const rd = ws.slice(1).map((w) => ({ link: w.link, words: this.readings(w.text) })), mods = rd.flatMap((r) => r.words);
      if (!mods.length) return sc;
      const out = this.V.pair(sc, mods, this.opt.pairLam), gw = this.opt.graphW;
      if (gw) for (const r of rd) { const g = this.V.graphScore(r.words, this.opt.relW[r.link] || {}); for (let i = 0; i < out.length; i++) out[i] += gw * g[i]; }
      return out;
    }
    // код слова кодером; если векторы не ставят слово первым — пара «код PI второе слово»: второе слово — один из pairN
    // ближайших соседей слова, закодированный не более чем двумя корнями, без корней главного (иначе пара лишь удваивает его вес).
    // Векторы связку не различают (graphW = 0), поэтому PI. → {code, rank, base, rank0, mod}
    // form — часть речи слова, если известна (иначе код с o, оценки без штрафа за часть речи)
    // самопроверка: кандидаты — лучшие коды в 1, 2, 3 корня и их соседи (значение ±1, без одного корня); берётся код,
    // при котором слово читается выше всего, при равенстве — короче. keepHead: головной корень кода в 3 корня не меняется.
    // data/eval/runs/ideas, data/eval/runs/selfcheck
    best(word, form, keepHead = this.opt.keepHead) {
      const co = this.co, x = this.V.vec(word), base = co.encode(x), lv = (r) => co.lv[r], cand = [];
      for (const k of [1, 2, 3]) {
        const e = k === 3 ? base : co.encode(x, k);
        cand.push([e.S, e.v]);
        e.S.forEach((r, i) => {
          if (co.has[r]) for (const d of [-1, 1]) { const nv = e.v[i] + d; if (lv(r).includes(nv)) cand.push([e.S, e.v.map((t, j) => (j === i ? nv : t))]); }
          if (e.S.length > 1) cand.push([e.S.filter((_, j) => j !== i), e.v.filter((_, j) => j !== i)]);
        });
      }
      let out = null;
      for (const [S, v] of cand) {
        if (keepHead && S[0] !== base.S[0]) continue;
        const r = this.V.rankIn(this.roots(S, v, form || ""), word);
        if (!out || r < out.r || (r === out.r && S.length < out.S.length)) out = { S, v, r };
      }
      return out;
    }
    encode(word, form) {
      const V = this.V, co = this.co, x = V.vec(word);
      if (!x) return null;
      const b = this.opt.selfCheck ? this.best(word, form) : co.encode(x), base = co.format(b.S, b.v, form || "o"), sc = this.prf(this.roots(b.S, b.v, form || "")), rank0 = V.rankIn(sc, word);
      const out = { code: base, rank: rank0, base, rank0, mod: "", S: b.S, v: b.v, cos: co.cosOf(x, b.S, b.v) };
      if (rank0 === 1) return out;
      for (const n of V.near(x, this.opt.pairN, word)) {
        const e = co.encode(V.vec(n), 2);
        if (e.S.some((r) => b.S.includes(r))) continue;
        const mc = co.format(e.S, e.v, "o"), r = V.rankIn(V.pair(sc, this.readings(mc), this.opt.pairLam), word);
        if (r < out.rank) Object.assign(out, { code: `${base} PI ${mc}`, rank: r, mod: n });
      }
      return out;
    }
  }

  const api = { Coder, Vocab, Reader, LEVELS };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.MincoMath = api;
})(typeof self !== "undefined" ? self : this);
