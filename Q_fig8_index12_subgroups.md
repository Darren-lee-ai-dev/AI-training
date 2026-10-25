# Summit Question — Index-12 subgroups of the figure-eight 0-surgery

- **Domain:** Mathematics
- **Sub-topic:** Low-dimensional topology / combinatorial group theory (torus bundles, subgroup growth)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $K\subset S^3$ be the figure-eight knot, and let $M=S^3_0(K)$ be the closed $3$-manifold obtained by $0$-framed Dehn surgery on $K$. How many subgroups of index exactly $12$ does $\pi_1(M)$ have? Count all subgroups of index $12$, not only normal ones and not up to conjugacy. Give a single integer.
```

---

## Final Answer

```
$47$
```

---

## Solution

```
Step 1: $M$ is a torus bundle.
$K$ is fibred with fibre a once-punctured torus, and the $0$-framing is the slope of the fibre's boundary, so $0$-surgery caps each fibre to a torus. Hence $M=T^2\times[0,1]/((x,1)\sim(Ax,0))$, where $A\in SL_2(\mathbb{Z})$ is the homological monodromy. Its characteristic polynomial is the Alexander polynomial $t^2-3t+1$. The class number of discriminant $5$ is $1$, so $A$ is conjugate to $\begin{pmatrix}2&1\\1&1\end{pmatrix}$; the count below is a conjugacy invariant.

Step 2: Fundamental group.
$G=\pi_1(M)=N\rtimes\langle t\rangle$ with $N=\mathbb{Z}^2$ and $tnt^{-1}=An$.

Step 3: Parametrise finite-index subgroups.
Let $U\le G$ have index $n$. Put $L=U\cap N$, and let $m\mathbb{Z}$ be the image of $U$ in $G/N\cong\mathbb{Z}$; then $n=m\,[N:L]$. Choose $u=t^m n_0\in U$. Then $U=L\rtimes\langle u\rangle$, and conjugation by $u$ acts on $N$ as $A^m$, so $L$ is $A^m$-invariant. Conversely, every $A^m$-invariant $L$ of index $n/m$ and every $n_0\in N$ give such a subgroup, and $n_0$ matters only modulo $L$. Hence
$s_n=\sum_{m\mid n}\frac{n}{m}\,c(A^m,\tfrac{n}{m})$,
where $c(B,k)$ is the number of $B$-invariant sublattices of index $k$ in $\mathbb{Z}^2$.

Step 4: Facts about $c(B,k)$.
$c(B,k)$ is multiplicative over coprime factors of $k$ (CRT). For a prime $p$, $c(B,p)$ is the number of $B$-invariant lines in $\mathbb{F}_p^2$. If $B\equiv I\pmod k$, then every sublattice of index $k$ is invariant, so $c(B,k)=\sigma(k)$, the sum of the divisors of $k$.

Step 5: Powers of $A$.
$A^2=\begin{pmatrix}5&3\\3&2\end{pmatrix}$, $A^3=\begin{pmatrix}13&8\\8&5\end{pmatrix}$, $A^4=\begin{pmatrix}34&21\\21&13\end{pmatrix}$.
Mod $2$: $A$ and $A^2$ have characteristic polynomial $x^2+x+1$, which is irreducible, so they have no invariant line. Mod $3$: $A$ has characteristic polynomial $x^2+1$, which is irreducible. Also $A^3\equiv I\pmod 4$, $A^4\equiv I\pmod 3$ and $A^6\equiv I\pmod 2$.

Step 6: The terms for $n=12$.
$m=1$: $12\,c(A,12)=12\,c(A,4)\,c(A,3)=0$, since $c(A,3)=0$.
$m=2$: $6\,c(A^2,6)=6\,c(A^2,2)\,c(A^2,3)=0$, since $c(A^2,2)=0$.
$m=3$: $4\,c(A^3,4)=4\,\sigma(4)=4\cdot 7=28$.
$m=4$: $3\,c(A^4,3)=3\,\sigma(3)=3\cdot 4=12$.
$m=6$: $2\,c(A^6,2)=2\,\sigma(2)=2\cdot 3=6$.
$m=12$: $1\cdot c(A^{12},1)=1$.

Step 7: Total.
$s_{12}=0+0+28+12+6+1=47$.
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $47$.
```

### Criterion 2 — 1 point

```
Identifies $M$ as the torus bundle with monodromy conjugate to $\begin{pmatrix}2&1\\1&1\end{pmatrix}$ (characteristic polynomial $t^2-3t+1$), so $\pi_1(M)\cong\mathbb{Z}^2\rtimes_A\mathbb{Z}$.
```

### Criterion 3 — 2 points

```
Parametrises index-$n$ subgroups by $(m,\ L,\ n_0)$, with $L$ an $A^m$-invariant sublattice of index $n/m$ and $n_0\in\mathbb{Z}^2/L$, giving $s_n=\sum_{m\mid n}\frac{n}{m}c(A^m,\frac{n}{m})$.
```

### Criterion 4 — 2 points

```
Shows $A^3\equiv I\pmod 4$, so all $7$ index-$4$ sublattices are $A^3$-invariant, giving the term $4\cdot 7=28$.
```

---

## Common Wrong Answers

```
$1$
```

```
$15$
```

```
$5$
```

Notes (for reference, not for pasting):
- $1$ — counts only subgroups with abelian quotient: $H_1(M)=\mathbb{Z}$ has a single index-$12$ subgroup.
- $15$ — omits the factor $n/m$ (the choice of $n_0\in N/L$): $0+0+7+4+3+1$.
- $5$ — requires $L$ to be $A$-invariant, not $A^m$-invariant: $0+0+4\cdot1+0+0+1$.

Verification (for reference): the formula was checked against brute-force enumeration of transitive homomorphisms $\pi_1(M)\to S_n$ for $n=2,\dots,6$, which give $1,1,5,6,19$ subgroups. The $n=12$ terms were recomputed by enumerating all sublattices in Hermite normal form.
