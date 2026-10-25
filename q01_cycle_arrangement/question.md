# Q01 — Regions of a Catalan-type arrangement on a 10-cycle

**Domain:** Mathematics
**Sub-topic:** Combinatorics — hyperplane arrangements (characteristic polynomials, finite-field method)
**Modality:** text-only (`not_applicable`)
**Answer type:** exact match, integer

---

## Question

Let $\mathcal{A}$ be the hyperplane arrangement in $\mathbb{R}^{10}$, with coordinates $x_1,\dots,x_{10}$, consisting of the $30$ hyperplanes

$$x_i - x_{i+1} = c \quad (1 \le i \le 9,\; c \in \{-1,0,1\}) \qquad\text{and}\qquad x_{10} - x_1 = c \quad (c \in \{-1,0,1\}).$$

Equivalently, $\mathcal{A}$ consists of the hyperplanes $x_i - x_j \in \{-1,0,1\}$ for every edge $\{i,j\}$ of the cycle graph $1\!-\!2\!-\!\cdots\!-\!10\!-\!1$ (and for no other pairs $\{i,j\}$). A region of $\mathcal{A}$ is a connected component of $\mathbb{R}^{10}\setminus\bigcup_{H\in\mathcal{A}}H$.

How many regions does $\mathcal{A}$ have? Give the exact integer.

## Final answer

`980574`

**Also accepted:** $4^{10}-3^{10}-8953$

## Step-by-step solution

Throughout, $n = 10$ and $T_n$ denotes the central trinomial coefficient $T_n = [x^n](1+x+x^2)^n = \sum_{k\ge 0}\binom{n}{k}\binom{n-k}{k}$, i.e. the number of sequences in $\{-1,0,1\}^n$ with sum $0$. We prove $r(\mathcal{A}) = 4^n - 3^n - T_n$ for every $n \ge 3$ and then evaluate at $n = 10$.

**Step 1: Reduce region counting to the characteristic polynomial.**
By Zaslavsky's theorem, the number of regions of a real arrangement $\mathcal{A}$ in $\mathbb{R}^n$ is $r(\mathcal{A}) = (-1)^n \chi_{\mathcal{A}}(-1)$, where $\chi_{\mathcal{A}}(t) = \sum_{X \in L(\mathcal{A})} \mu(\hat 0, X)\, t^{\dim X}$ is the characteristic polynomial of the intersection lattice $L(\mathcal{A})$.

**Step 2: Finite-field method.**
Every hyperplane of $\mathcal{A}$ is defined over $\mathbb{Z}$. By the finite-field method (Athanasiadis), for all sufficiently large primes $p$,
$$\chi_{\mathcal{A}}(p) = \#\Bigl\{x \in \mathbb{F}_p^{\,n} : x \notin \bigcup_{H \in \mathcal{A}} H\Bigr\},$$
where each $H$ is reduced modulo $p$. Because $\chi_{\mathcal{A}}$ is a polynomial, it suffices to find a polynomial in $p$ that equals this count for all large $p$. Below we take $p > 2n$.

**Step 3: Parametrize the complement.**
Write $S = \mathbb{F}_p \setminus \{-1,0,1\}$, so $|S| = p-3$. A point $x \in \mathbb{F}_p^n$ is determined by $x_1$ and the differences $d_i = x_{i+1} - x_i$ ($1 \le i \le n-1$), and $x_n - x_1 = d_1 + \dots + d_{n-1}$. The point avoids all hyperplanes iff
$$d_i \in S \ (1 \le i \le n-1) \qquad\text{and}\qquad d_1 + \dots + d_{n-1} \in S .$$
The condition is symmetric under $c \mapsto -c$, so the orientation of the edges is irrelevant. Hence
$$\chi_{\mathcal{A}}(p) = p\,\bigl[(p-3)^{n-1} - M\bigr], \qquad M = \#\{d \in S^{\,n-1} : d_1+\dots+d_{n-1} \in \{-1,0,1\}\}.$$
The term $M$ is where the cycle differs from a path: the closing edge imposes a constraint on the *sum* of the other differences, which is not independent of them.

**Step 4: Count tuples in $S^{n-1}$ with prescribed sum.**
For $s \in \mathbb{F}_p$ let $N(s) = \#\{d \in S^{n-1} : \sum_i d_i = s\}$. Apply inclusion–exclusion over the set $A \subseteq [n-1]$ of coordinates that are *forced* into $\{-1,0,1\}$:
$$N(s) = \sum_{A \subseteq [n-1]} (-1)^{|A|}\, \#\{d \in \mathbb{F}_p^{\,n-1} : d_i \in \{-1,0,1\} \text{ for } i \in A,\ \textstyle\sum_i d_i = s\}.$$
If $A \ne [n-1]$, at least one coordinate is free in $\mathbb{F}_p$, so the sum is equidistributed and the count is $3^{|A|} p^{\,n-1-|A|}/p = 3^{|A|} p^{\,n-2-|A|}$. If $A = [n-1]$, the count is the number of $(d_1,\dots,d_{n-1}) \in \{-1,0,1\}^{n-1}$ with integer sum congruent to $s$ mod $p$; since $|\sum d_i| \le n-1 < p/2$, this is the trinomial coefficient $T(n-1,s) := [x^{s}](x^{-1}+1+x)^{n-1}$ for the representative $s \in (-p/2, p/2)$. Therefore
$$N(s) = \sum_{k=0}^{n-2} \binom{n-1}{k} (-3)^k p^{\,n-2-k} + (-1)^{n-1} T(n-1,s) = \frac{(p-3)^{n-1} - (-3)^{n-1}}{p} + (-1)^{n-1} T(n-1,s).$$

**Step 5: Sum over $s \in \{-1,0,1\}$ and identify the central trinomial coefficient.**
$$M = N(-1)+N(0)+N(1) = \frac{3\bigl[(p-3)^{n-1} - (-3)^{n-1}\bigr]}{p} + (-1)^{n-1}\bigl[T(n-1,-1)+T(n-1,0)+T(n-1,1)\bigr].$$
Appending one more step $d_n \in \{-1,0,1\}$ to a sequence with sum $-1$, $0$ or $1$ to reach total $0$ shows $T(n-1,-1)+T(n-1,0)+T(n-1,1) = T(n,0) = T_n$. Hence
$$M = \frac{3(p-3)^{n-1} - 3(-3)^{n-1}}{p} + (-1)^{n-1} T_n .$$

**Step 6: Assemble the characteristic polynomial.**
$$\chi_{\mathcal{A}}(p) = p(p-3)^{n-1} - 3(p-3)^{n-1} + 3(-3)^{n-1} - (-1)^{n-1} T_n\, p = (p-3)^n + (-1)^{n-1}\bigl(3^n - T_n\, p\bigr),$$
using $3(-3)^{n-1} = (-1)^{n-1} 3^n$. Thus
$$\chi_{\mathcal{A}}(t) = (t-3)^n + (-1)^{n-1}\bigl(3^n - T_n\, t\bigr).$$
Consistency checks: $\chi_{\mathcal{A}}(0) = (-3)^n + (-1)^{n-1}3^n = 0$, as required because every hyperplane contains the line $\mathbb{R}(1,\dots,1)$; and the coefficient of $t^{n-1}$ is $-3n$, the number of hyperplanes.

**Step 7: Evaluate at $t = -1$.**
$$r(\mathcal{A}) = (-1)^n \chi_{\mathcal{A}}(-1) = (-1)^n(-4)^n + (-1)^n(-1)^{n-1}\bigl(3^n + T_n\bigr) = 4^n - 3^n - T_n .$$
Check at $n=3$: the arrangement is the full Catalan arrangement of $A_2$, with $3!\,C_3 = 30$ regions, and $4^3 - 3^3 - T_3 = 64 - 27 - 7 = 30$.

**Step 8: Numerical value for $n = 10$.**
$T_{10} = \sum_{k=0}^{5}\binom{10}{k}\binom{10-k}{k} = 1 + 90 + 1260 + 4200 + 3150 + 252 = 8953$, $4^{10} = 1048576$, $3^{10} = 59049$. Therefore
$$r(\mathcal{A}) = 1048576 - 59049 - 8953 = 980574 .$$

## References

- T. Zaslavsky, *Facing up to arrangements: face-count formulas for partitions of space by hyperplanes*, Mem. Amer. Math. Soc. 154 (1975).
- C. A. Athanasiadis, *Characteristic polynomials of subspace arrangements and finite fields*, Adv. Math. 122 (1996), 193–233.
- R. P. Stanley, *Hyperplane arrangements, interval orders, and trees*, Proc. Natl. Acad. Sci. USA 93 (1996), 2620–2625 (for the count $n!\,C_n$ of regions of the Catalan arrangement used in the $n=3$ check).

## Grading rubric (10 points)

| # | Criterion | Points | Final answer? |
|---|---|---|---|
| 1 | Gives $980574$ (or an exactly equivalent expression such as $4^{10}-3^{10}-8953$). | 5 | yes |
| 2 | Obtains the characteristic polynomial $\chi_{\mathcal{A}}(t) = (t-3)^{10} - 3^{10} + 8953\,t$, or equivalently the point count $(p-3)^{10} - 59049 + 8953\,p$ over $\mathbb{F}_p$. | 2 | no |
| 3 | Identifies the correction coming from the closing edge $x_{10}-x_1$ as the central trinomial coefficient $T_{10} = 8953$ (the number of $(d_1,\dots,d_9)\in\{-1,0,1\}^9$ with sum in $\{-1,0,1\}$, equivalently $[x^{10}](1+x+x^2)^{10}$). | 2 | no |
| 4 | Reduces the region count to $(-1)^{10}\chi_{\mathcal{A}}(-1)$ (Zaslavsky) and computes $\chi_{\mathcal{A}}$ by counting points of $\mathbb{F}_p^{10}$ off the hyperplanes (finite-field method). | 1 | no |

**Common wrong answers:**
- $1048576$ ($=4^{10}$): treats the closing constraint $x_{10}-x_1\notin\{-1,0,1\}$ as independent of the other nine, i.e. uses $\chi(t)=(t-3)^{10}$.
- $989527$ ($=4^{10}-3^{10}$): drops the trinomial correction term.
- $986388$: uses $T_9 = 3139$ instead of $T_{10}$.
- $998480$ ($=4^{10}-3^{10}+8953$): sign error on the trinomial term.
- $60949324800$ ($=10!\,C_{10}$): counts regions of the full Catalan arrangement on all $\binom{10}{2}$ pairs instead of the cycle's 10 edges.
