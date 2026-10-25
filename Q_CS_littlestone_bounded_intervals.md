# Summit Question — Littlestone dimension of length-bounded intervals

- **Domain:** Computer Science/AI
- **Sub-topic:** Computational learning theory (online learning, Littlestone dimension)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $n=10^6$ and $X=\{1,2,\dots,n\}$. For integers $1\le a\le b\le n$ let $h_{a,b}\colon X\to\{0,1\}$ be the indicator of $\{x: a\le x\le b\}$, and let $h_{\varnothing}\equiv 0$. For each integer $K\ge 1$ consider the class of intervals of length at most $K$ together with the empty hypothesis:
$\mathcal{H}_K=\{h_{a,b}: 1\le a\le b\le n,\ b-a+1\le K\}\cup\{h_{\varnothing}\}$.

The Littlestone dimension $\mathrm{Ldim}(\mathcal{H})$ is the largest $d$ for which there exists a complete binary tree of depth $d$ with the internal nodes labelled by points of $X$ such that for every root to leaf path (the two children of a node corresponding to the $0$ and $1$ labels of its point) there is some $h\in\mathcal{H}$ which agrees with all the labels along that path. Equivalently it is the optimal worst case number of mistakes in the realizable online setting.

What is the smallest $K$ such that $\mathrm{Ldim}(\mathcal{H}_K)\ge 13$? Give a single integer.
```

---

## Final Answer

```
$106$
```

---

## Solution

```
Step 1: Recursion and monotonicity.
For a version space $V$, $\mathrm{Ldim}(V)\ge d$ ($d\ge1$) iff some point $x$ splits $V$ into $V_{x,0}$ and $V_{x,1}$ with both of Littlestone dimension $\ge d-1$. Littlestone dimension is monotone under passing to a subclass; in particular $\mathcal{H}_K\subseteq\mathcal{H}_{K+1}$, so $\mathrm{Ldim}(\mathcal{H}_K)$ is non-decreasing in $K$.

Step 2: The positive branch is a staircase region, not a product.
Suppose $x$ is labelled $1$ while $\ell$ unrefuted points lie to its left and $r$ to its right in its run. Writing a consistent interval as $[x-i,\ x+j]$, the version space is
$R(A,B,C)=\{(i,j)\in\mathbb{Z}^2: 0\le i\le A,\ 0\le j\le B,\ i+j\le C\}$ with $A=\ell$, $B=r$, $C=K-1$.
These regions are defined for arbitrary caps $A,B,C\ge0$, and $R(A,B,C)=R(\min(A,C),\min(B,C),C)$. A later query at $x-s$ asks whether $i\ge s$, and a query at $x+s$ asks whether $j\ge s$. Because of the coupling $i+j\le C$ the class is not a product of two threshold classes. Let $D(A,B,C)$ be its Littlestone dimension, $t(C)=D(C,C,C)$ the dimension of the triangle $T(C)=R(C,C,C)$, and note $D(A,B,C)=\lfloor\log_2(A+1)\rfloor+\lfloor\log_2(B+1)\rfloor$ when $A+B\le C$ (then $R$ is a rectangle).

Step 3: Recursion on regions.
In $R(A,B,C)$ the query $i\ge s$ ($1\le s\le A$) has children $R(A-s,B,C-s)$ (answer $1$, after shifting $i$ by $s$) and $R(s-1,B,C)$ (answer $0$); the query $j\ge s$ ($1\le s\le B$) has children $R(A,B-s,C-s)$ and $R(A,s-1,C)$. After normalising with $\min(\cdot,C)$ every child is again of the form $R(A',B',C')$ with $A',B'\le C'$, so
$D(A,B,C)=\max_{\text{queries}}\big(1+\min(D(\text{child}_1),D(\text{child}_0))\big)$, with $D(0,0,C)=0$.

Step 4: Reduction of $\mathcal{H}_K$ to the triangle.
Upper bound: whatever the root $x$ is, its $1$-branch is a region $R(A,B,K-1)\subseteq T(K-1)$, so $\mathrm{Ldim}(\mathcal{H}_K)\le 1+t(K-1)$.
Lower bound: put $d=t(K-1)+1$ and $x_m=K+(2K-1)(m-1)$ for $m=1,\dots,d$. The blocks $[x_m-K+1,\ x_m+K-1]$ are disjoint and lie in $X$, because $(2K-1)d\le 211\cdot 13<n$ for all $K\le 106$. Query $x_1,x_2,\dots$ along the all-$0$ path. When $x_m$ is queried its block is still free, so its $1$-branch is the full triangle $T(K-1)$, and its $0$-branch still contains $h_{\varnothing}$ and the later blocks. By Step 1 this is a tree of depth $d$. Hence $\mathrm{Ldim}(\mathcal{H}_K)=1+t(K-1)$ for $K\le 106$, and the question asks for the smallest $K$ with $t(K-1)\ge 12$.

Step 5: Triangles via a split chain.
The query $i\ge s$ on $T(C)$ has $1$-child $T(C-s)$ and $0$-child containing the rectangle $[0,s-1]\times[0,C-s+1]$, so
$t(C)\ge 1+\min\big(t(C-s),\ \lfloor\log_2 s\rfloor+\lfloor\log_2(C-s+2)\rfloor\big)$.
Applying this with $(C,s)=(1,1),(2,1),(3,1),(5,2),(8,2),(12,4),(18,4),(26,8),(38,8),(54,16)$ gives $t(1)\ge1$, $t(2)\ge2$, $t(3)\ge3$, $t(5)\ge4$, $t(8)\ge5$, $t(12)\ge6$, $t(18)\ge7$, $t(26)\ge8$, $t(38)\ge9$, $t(54)\ge10$. For example $(54,16)$: $t(38)\ge9$ and $\lfloor\log_2 16\rfloor+\lfloor\log_2 40\rfloor=4+5=9$. By monotonicity $t(31)\ge8$ and $t(57)\ge10$.

Step 6: Lower bound $t(105)\ge 12$ (explicit tree).
Each line is a region, the query used, and its two children. "rect $w\times h$" is a rectangle of dimension $\lfloor\log_2 w\rfloor+\lfloor\log_2 h\rfloor$.
$R(105,105,105)\ge12$: query $i\ge32$; children $R(73,73,73)$ and $R(31,105,105)$.
$R(31,105,105)\ge11$: query $j\ge32$; children $R(31,73,73)$ and rect $32\times32$ (dim $10$).
$R(31,73,73)\ge10$: query $j\ge16$; children $R(31,57,57)$ and rect $32\times16$ (dim $9$).
$R(31,57,57)\ge9$: query $j\ge26$; children $T(31)$ (dim $\ge8$, Step 5) and rect $32\times26$ (dim $9$).
$R(73,73,73)\ge11$: query $i\ge16$; children $T(57)$ (dim $\ge10$, Step 5) and $R(15,73,73)$.
$R(15,73,73)\ge10$: query $j\ge32$; children $R(15,41,41)$ and rect $16\times32$ (dim $9$).
$R(15,41,41)\ge9$: query $j\ge16$; children $R(15,25,25)$ and rect $16\times16$ (dim $8$).
$R(15,25,25)\ge8$: query $j\ge8$; children $R(15,17,17)$ and rect $16\times8$ (dim $7$).
$R(15,17,17)\ge7$: query $j\ge5$; children $T(12)$ (dim $\ge6$, Step 5) and $R(15,4,17)$.
$R(15,4,17)\ge6$: query $i\ge8$; children $R(7,4,9)$ and rect $8\times5$ (dim $5$).
$R(7,4,9)\ge5$: query $i\ge4$; children $R(3,4,5)$ and rect $4\times5$ (dim $4$).
$R(3,4,5)\ge4$: query $j\ge2$; children $R(3,2,3)$ and rect $4\times2$ (dim $3$).
$R(3,2,3)\ge3$: query $j\ge1$; children $R(2,1,2)$ and rect $4\times1$ (dim $2$).
$R(2,1,2)\ge2$: query $i\ge1$; children $T(1)$ (dim $\ge1$) and rect $1\times2$ (dim $1$).
Reading the lines bottom-up proves every claimed bound, so $t(105)\ge12$ and $\mathrm{Ldim}(\mathcal{H}_{106})\ge13$.

Step 7: Upper bound $t(104)\le 11$ (certificate).
By symmetry only queries $i\ge s$ on $T(104)$ need checking. Their children are $T(104-s)$ and $Z_s=R(s-1,104,104)$, and both families are monotone in $s$ (in opposite directions). If $s\ge32$ then $T(104-s)\subseteq T(72)$; if $s\le31$ then $Z_s\subseteq R(30,104,104)$. So it suffices that $t(72)\le10$ and $D(30,104,104)\le10$. Both values come from evaluating the exact recursion of Step 3 over all regions with $C\le104$:
for C in 0..104, for A in 0..C, for B in 0..A: D[A][B][C] = max over s of 1+min(D[child_1], D[child_0]) (both query types, children normalised by min(.,C), using D symmetric in A,B), with D[0][0][C]=0.
The evaluation gives $t(72)=10$ (the values of $C$ where $t$ first reaches $1,\dots,12$ are $1,2,3,5,8,12,17,25,36,52,73,105$) and $D(30,104,104)=10$ (while $D(31,104,104)=11$). Hence no query on $T(104)$ has both children of dimension $\ge11$, so $t(104)\le11$ and $\mathrm{Ldim}(\mathcal{H}_{105})=12$. A short executable implementation (Python 3, standard library only) that reproduces these values is given below the solution.

Step 8: Answer.
By Steps 1, 4, 6 and 7, $\mathrm{Ldim}(\mathcal{H}_K)\le12$ for $K\le105$ and $\mathrm{Ldim}(\mathcal{H}_{106})\ge13$. The smallest such $K$ is $106$.
```

### Reference implementation (append to the solution)

```python
# Exact Littlestone dimension D(A,B,C) of the region
# R(A,B,C) = {(i,j): 0<=i<=A, 0<=j<=B, i+j<=C} under threshold queries
# "i>=s" and "j>=s" (Step 3). Python 3, standard library only.
# Runs in about a minute.

def build(Cmax):
    D = []  # D[C][A][B] for 0 <= A, B <= C
    for C in range(Cmax + 1):
        T = [[0] * (C + 1) for _ in range(C + 1)]
        for A in range(C + 1):
            for B in range(C + 1):
                if A == 0 and B == 0:
                    continue
                best = 0
                for s in range(1, A + 1):          # query i >= s
                    c1 = C - s
                    v1 = D[c1][min(A - s, c1)][min(B, c1)]   # answer 1
                    v0 = T[s - 1][B]                         # answer 0
                    best = max(best, 1 + min(v1, v0))
                for s in range(1, B + 1):          # query j >= s
                    c1 = C - s
                    v1 = D[c1][min(A, c1)][min(B - s, c1)]   # answer 1
                    v0 = T[A][s - 1]                         # answer 0
                    best = max(best, 1 + min(v1, v0))
                T[A][B] = best
        D.append(T)
    return D

D = build(105)
print("t(72)        =", D[72][72][72])     # 10
print("D(30,104,104) =", D[104][30][104])  # 10
print("D(31,104,104) =", D[104][31][104])  # 11
print("t(104)       =", D[104][104][104])  # 11
print("t(105)       =", D[105][105][105])  # 12
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $106$.
```

### Criterion 2 — 2 points

```
Recognises that after a positive label at $x$ the remaining class is $\{(i,j): i,j\ge0,\ i+j\le K-1\}$ (a triangle, because of the length bound) with threshold queries on $i$ and on $j$, not a product of two independent threshold classes.
```

### Criterion 3 — 1 point

```
Shows that $\mathrm{Ldim}(\mathcal{H}_K)=1+t(K-1)$ for all $K\le106$ (upper bound from the root's positive branch; lower bound from $t(K-1)+1$ disjoint free blocks of $2K-1$ points, which fit in $X$ in this range), where $t(C)$ is the Littlestone dimension of the triangle $i+j\le C$. With monotonicity in $K$ this reduces the question to the smallest $C$ with $t(C)\ge12$.
```

### Criterion 4 — 2 points

```
Shows $t(105)\ge12$ (e.g. root split $i\ge32$ into the triangle $i+j\le73$ and the region $i\le31,\ i+j\le105$) and $t(104)\le11$.
```

---

## Common Wrong Answers

```
$64$
```

```
$91$
```

```
$127$
```

```
$128$
```

Notes (for reference, not for pasting):
- $64$ : treats the positive branch as a product of two thresholds with $K$ options each, $1+2\lfloor\log_2 K\rfloor\ge13$.
- $91$ : uses the halving bound $1+\lfloor\log_2(K(K+1)/2)\rfloor\ge13$ as if it were exact.
- $127$ : uses only the largest rectangle inside the triangle, $1+\max_s(\lfloor\log_2 s\rfloor+\lfloor\log_2(K+1-s)\rfloor)\ge13$.
- $128$ : uses $2\lfloor\log_2 K\rfloor$ (two independent endpoints, no outer split).

Verification (for reference): the recursion of Step 3 was evaluated exactly over all regions with $C\le120$. For the full class $\mathcal{H}_K$, a brute force over explicit hypothesis sets agrees with an exact gap-multiset dynamic program for all $K\le4$, $n\le11$, and the dynamic program confirms $\mathrm{Ldim}=1+t(K-1)$ once $n$ is large enough, for every $K\le7$. Every line of the Step 6 tree was checked by hand. Step 7 rests on two computed ranks of the exact recursion. These were reproduced by a second, independent full-table implementation (no symmetry reduction), identical in logic to the Python reference program, giving $t(72)=10$, $D(30,104,104)=10$, $D(31,104,104)=11$, $t(104)=11$, $t(105)=12$.
