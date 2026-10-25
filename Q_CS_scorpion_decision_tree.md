# Summit Question — Decision-tree complexity of scorpion graphs on 7 vertices

- **Domain:** Computer Science/AI
- **Sub-topic:** Computational complexity (query complexity, evasiveness of graph properties)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $V=\{1,2,\dots,7\}$. An unknown simple graph $G$ on vertex set $V$ is accessed only through queries of the form "is $\{u,v\}\in E(G)$?" for unordered pairs $u\ne v$; each query is answered truthfully. A deterministic decision tree for a property $P$ is an adaptive strategy that, after its queries, always outputs whether $G$ has $P$, and its cost is the maximum number of queries it makes over all $2^{21}$ graphs on $V$. The deterministic decision-tree complexity $D(P)$ is the minimum cost of such a tree.

Call $G$ a scorpion graph if there are three distinct vertices $b,t,s$ (body, tail, sting) such that $\deg(b)=5$, $\deg(t)=2$, $\deg(s)=1$, $\{b,t\}\in E(G)$ and $\{t,s\}\in E(G)$. (Consequently $\{b,s\}\notin E(G)$: the five neighbours of $b$ are $t$ and the four vertices of $V\setminus\{b,t,s\}$. The only neighbours of $t$ are $b$ and $s$, and the only neighbour of $s$ is $t$. The six pairs among the four vertices of $V\setminus\{b,t,s\}$ are unconstrained.)

Compute $D(P)$ for the property $P$ = "$G$ is a scorpion graph". Give the final answer as a single integer, preceded by a brief justification of how it was obtained.
```

---

## Final Answer

```
$18$
```

---

## Solution

```
Step 1: Minimax formulation.
A partial assignment $\alpha$ fixes some of the $21$ pairs as edges or non-edges. Let $\mathrm{vals}(\alpha)\subseteq\{0,1\}$ be the set of values of $P$ over all completions of $\alpha$. Then $D(\alpha)=0$ if $|\mathrm{vals}(\alpha)|=1$, and otherwise $D(\alpha)=\min_{e\text{ free}}\big(1+\max(D(\alpha\cup\{e\notin E\}),\ D(\alpha\cup\{e\in E\}))\big)$. Also $\mathrm{vals}(\alpha)=\mathrm{vals}(\alpha\cup\{e\notin E\})\cup\mathrm{vals}(\alpha\cup\{e\in E\})$ for any free pair $e$. The answer is $D(\varnothing)$.

Step 2: Why the natural answer $21$ is wrong.
For monotone nontrivial graph properties the Aanderaa–Karp–Rosenberg conjecture asserts evasiveness ($D=\binom{n}{2}$), but $P$ is not monotone: adding an edge can create or destroy a scorpion. Scorpion graphs are the classical example of a non-evasive property (Best, van Emde Boas and Lenstra, 1974); the general strategy locates a candidate body and sting from degree information and verifies the scorpion with $O(n)$ queries, so evasiveness cannot be assumed. For small $n$ the exact value must be computed.

Step 3: Symmetry reduction.
$P$ is invariant under relabelling the vertices, so $D(\alpha)=D(\pi\alpha)$ and $\mathrm{vals}(\alpha)=\mathrm{vals}(\pi\alpha)$ for every permutation $\pi$ of $V$. It therefore suffices to evaluate the recursion of Step 1 on one canonical representative per orbit of partial assignments under the $5040$ relabellings. The canonical form used is the lexicographically smallest encoding over all relabellings that respect a relabelling-invariant ordering of the vertices (by counts of known edges, known non-edges and free pairs at each vertex, refined once by the multiset of neighbours' counts); ties are broken by trying every permutation within each class, so the form is exact.

Step 4: Soundness of the memoisation.
The memo key of a state is the encoding of an actual relabelling of that state (the minimum over a set of relabellings). Hence two states with the same key are isomorphic and have the same value of $D$ and of $\mathrm{vals}$. The search is therefore exact whether or not the key is fully canonical; canonicity only affects how much work is shared.

Step 5: Evaluation (entry point: Program.Depth(7), called from Program.Main in the reference implementation).
Captured output (.NET Framework 4.0.30319, 64-bit, Windows 10.0.26200):
n=4: D(scorpion) = 6 of 6
n=5: D(scorpion) = 10 of 10
n=6: D(scorpion) = 14 of 15
n=7: D(scorpion) = 18 of 21
The $n=7$ search memoises $2{,}060{,}074$ keyed states and runs in about $160$ s. (On $n$ vertices the body has degree $n-2$.)

Step 6: Upper-bound certificate $D(P)\le 18$.
An explicit decision tree with $16{,}627$ nodes was extracted from the search and saved as scorpion7_certificate.txt (format described in its header). The short verifier below runs this tree on all $2^{21}=2{,}097{,}152$ graphs and compares its output with a direct scorpion test. Result: $0$ wrong outputs, and at most $18$ queries on every graph. This check does not use the search or the memo keys. As a consistency check, the number of scorpion graphs found is $13{,}440=7\cdot6\cdot5\cdot2^{6}$ (choose $b,t,s$; the $6$ pairs among the other four vertices are free).

Step 7: Lower bound $D(P)\ge 18$ (independent implementation).
A second, separately written program (depth-bounded search "can $P$ be decided within $q$ queries?", with a different memo key: vertices sorted by their numbers of known edges and non-edges, all relabellings within ties) reports: $n=7$, $q=17$: False; $n=7$, $q=18$: True; and $n=6$, $q=13$: False; $n=6$, $q=14$: True. For $n=6$ the value $14$ was also confirmed by evaluating the recursion of Step 1 over all $3^{15}$ partial assignments with no symmetry reduction at all.

Step 8: Answer.
$D(P)=18$.
```

### Reference implementation (append to the solution)

```csharp
// Exact deterministic decision-tree complexity of "G is a scorpion graph" on n labelled vertices,
// by exhaustive minimax over partial edge assignments modulo vertex relabelling.
// C# (.NET); prints D for n = 4,5,6,7. The n = 7 case takes a few minutes.
using System; using System.Collections.Generic; using System.Linq;
public static class Program {
  static int N, E; static int[] eu, ev; static int[,] eid;
  static Dictionary<long, byte> memo;   // canonical state -> vals | depth<<2
  static void Setup(int n) {
    N = n; var a = new List<int>(); var b = new List<int>(); eid = new int[n, n];
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) { eid[i, j] = eid[j, i] = a.Count; a.Add(i); b.Add(j); }
    eu = a.ToArray(); ev = b.ToArray(); E = eu.Length;
  }
  static bool Scorpion(int mask) {
    var deg = new int[N]; var adj = new bool[N, N];
    for (int e = 0; e < E; e++) if (((mask >> e) & 1) == 1) { deg[eu[e]]++; deg[ev[e]]++; adj[eu[e], ev[e]] = adj[ev[e], eu[e]] = true; }
    for (int b = 0; b < N; b++) { if (deg[b] != N - 2) continue;
      for (int t = 0; t < N; t++) { if (t == b || !adj[b, t] || deg[t] != 2) continue;
        for (int s = 0; s < N; s++) if (s != b && s != t && adj[t, s] && deg[s] == 1) return true; } }
    return false;
  }
  static long Canon(int known, int present) {
    var inv = new long[N];
    for (int e = 0; e < E; e++) { int k = (known >> e) & 1, p = (present >> e) & 1; long c = k == 0 ? 1L : (p == 1 ? 1L << 16 : 1L << 8); inv[eu[e]] += c; inv[ev[e]] += c; }
    var inv2 = new long[N];
    for (int v = 0; v < N; v++) { long h = inv[v] * 1000003L; var ls = new List<long>();
      for (int w = 0; w < N; w++) { if (w == v) continue; int e = eid[v, w]; int k = (known >> e) & 1, p = (present >> e) & 1; int c = k == 0 ? 0 : (p == 1 ? 2 : 1); ls.Add(inv[w] * 3 + c); }
      ls.Sort(); foreach (var x in ls) h = h * 1315423911L + x; inv2[v] = h; }
    var order = Enumerable.Range(0, N).OrderBy(v => inv2[v]).ToArray();
    var cls = new List<List<int>>();
    for (int i = 0; i < N; i++) { if (i == 0 || inv2[order[i]] != inv2[order[i - 1]]) cls.Add(new List<int>()); cls[cls.Count - 1].Add(order[i]); }
    long best = long.MaxValue; Assign(cls, 0, 0, new int[N], known, present, ref best); return best;
  }
  static void Assign(List<List<int>> cls, int ci, int baseL, int[] pos, int known, int present, ref long best) {
    if (ci == cls.Count) { int nk = 0, np = 0;
      for (int e = 0; e < E; e++) { if (((known >> e) & 1) == 0) continue; int ne = eid[pos[eu[e]], pos[ev[e]]]; nk |= 1 << ne; if (((present >> e) & 1) == 1) np |= 1 << ne; }
      long key = ((long)(uint)np << E) | (long)(uint)nk; if (key < best) best = key; return; }
    Perm(cls[ci].ToArray(), 0, cls, ci, baseL, pos, known, present, ref best);
  }
  static void Perm(int[] arr, int k, List<List<int>> cls, int ci, int baseL, int[] pos, int known, int present, ref long best) {
    if (k == arr.Length) { for (int i = 0; i < arr.Length; i++) pos[arr[i]] = baseL + i; Assign(cls, ci + 1, baseL + arr.Length, pos, known, present, ref best); return; }
    for (int i = k; i < arr.Length; i++) { var t = arr[k]; arr[k] = arr[i]; arr[i] = t; Perm(arr, k + 1, cls, ci, baseL, pos, known, present, ref best); t = arr[k]; arr[k] = arr[i]; arr[i] = t; }
  }
  static int Solve(int known, int present) {
    long key = Canon(known, present); byte r; if (memo.TryGetValue(key, out r)) return r;
    int full = (1 << E) - 1, res;
    if (known == full) res = Scorpion(present) ? 2 : 1;
    else {
      int u = 0; while (((known >> u) & 1) == 1) u++;
      int vals = (Solve(known | 1 << u, present) & 3) | (Solve(known | 1 << u, present | 1 << u) & 3);
      if (vals != 3) res = vals;
      else { int best = 255;
        for (int e = 0; e < E; e++) { if (((known >> e) & 1) == 1) continue;
          int c0 = Solve(known | 1 << e, present) >> 2, c1 = Solve(known | 1 << e, present | 1 << e) >> 2;
          best = Math.Min(best, 1 + Math.Max(c0, c1)); }
        res = 3 | (best << 2); } }
    memo[key] = (byte)res; return res;
  }
  public static int Depth(int n) { Setup(n); memo = new Dictionary<long, byte>(); return Solve(0, 0) >> 2; }
  public static void Main() {
    foreach (int n in new[] { 4, 5, 6, 7 })
      Console.WriteLine("n=" + n + ": D(scorpion) = " + Depth(n) + " of " + (n * (n - 1) / 2));
  }
}
```

### Certificate verifier (append to the solution; needs scorpion7_certificate.txt)

```python
# Checks the depth-18 decision-tree certificate on all 2^21 graphs on 7 vertices.
# Python 3, standard library only.
pairs = [(u, v) for u in range(7) for v in range(u + 1, 7)]
idx = {p: i for i, p in enumerate(pairs)}
tree = {}
for line in open("scorpion7_certificate.txt"):
    if line.startswith("#"):
        continue
    p = line.split()
    if p[0] == "L":
        tree[int(p[1])] = ("L", int(p[2]))
    else:
        tree[int(p[1])] = ("Q", int(p[2]), int(p[3]), int(p[4]))

def scorpion(g):
    deg = [0] * 7
    for e, (u, v) in enumerate(pairs):
        if g >> e & 1:
            deg[u] += 1
            deg[v] += 1
    adj = lambda x, y: g >> idx[(min(x, y), max(x, y))] & 1
    for b in range(7):
        if deg[b] != 5:
            continue
        for t in range(7):
            if t == b or deg[t] != 2 or not adj(b, t):
                continue
            for s in range(7):
                if s != b and s != t and deg[s] == 1 and adj(t, s):
                    return True
    return False

wrong = 0
maxd = 0
for g in range(1 << 21):
    node, d = 0, 0
    while tree[node][0] == "Q":
        _, e, c0, c1 = tree[node]
        node = c1 if g >> e & 1 else c0
        d += 1
    if (tree[node][1] == 1) != scorpion(g):
        wrong += 1
    maxd = max(maxd, d)
print("wrong outputs:", wrong, " max queries:", maxd)   # expected: 0 and 18
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $18$.
```

### Criterion 2 — 2 points

```
Recognises that the scorpion property is not monotone, so evasiveness ($D=21$) cannot be assumed, and that scorpion graphs admit an adaptive strategy using fewer than $21$ queries.
```

### Criterion 3 — 1 point

```
Reduces the computation to the minimax recursion over partial edge assignments, using invariance of the property under vertex relabelling.
```

### Criterion 4 — 2 points

```
Correctly determines a smaller instance: the analogous property on $6$ vertices (body degree $4$) has $D=14$, or on $5$ vertices (body degree $3$) has $D=10$.
```

---

## Common Wrong Answers

```
$21$
```

```
$20$
```

```
$19$
```

Notes (for reference, not for pasting):
- $21$ — assumes every nontrivial graph property is evasive.
- $20$, $19$ — find a strategy saving one or two queries but not the optimal one.

Verification (for reference): the key is supported by three separate computations. (1) Exhaustive minimax modulo relabelling (reference implementation, entry point Program.Depth(7)) gives $18$. (2) An explicit $16{,}627$-node decision tree (scorpion7_certificate.txt) was checked on all $2^{21}$ graphs: $0$ errors, maximum depth $18$, which certifies $D\le18$ independently of the search. (3) A separately written depth-bounded search reports that $17$ queries do not suffice and $18$ do, which certifies $D\ge18$. The symmetry-reduced search was also validated against an unreduced exhaustive search on $6$ vertices for ten properties. The decisive step is computational: no hand-checkable $17$-query impossibility proof is given.
