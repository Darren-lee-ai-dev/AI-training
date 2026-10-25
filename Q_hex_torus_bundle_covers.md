# Summit Question — 12-sheeted covers of a hexagonal torus bundle

- **Domain:** Mathematics
- **Sub-topic:** Low-dimensional topology / covering spaces (torus bundles, subgroups of finite index)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $P\subset\mathbb{R}^2$ be a regular hexagon centred at the origin, with sides $s_1,\dots,s_6$ labelled counter-clockwise. Glue each side to the opposite side by the translation of $\mathbb{R}^2$ carrying one onto the other; the quotient $T=P/\!\sim$ is a torus, oriented by the standard orientation of $\mathbb{R}^2$. For $i=1,2$ let $\delta_i\subset T$ be the simple closed curve that is the image of the straight segment joining the midpoints of $s_i$ and $s_{i+3}$. Let $h\colon T\to T$ be the map induced by the rotation of $\mathbb{R}^2$ by angle $\pi$ about the origin, and for a simple closed curve $\gamma$ let $T_\gamma$ be the positive (left-handed) Dehn twist about $\gamma$. Define
$f=T_{\delta_1}\circ T_{\delta_2}^{-2}\circ h\colon T\to T$,
and let $M_f=T\times[0,1]/(x,1)\sim(f(x),0)$ be its mapping torus.

How many connected $12$-sheeted covering spaces does $M_f$ have, counted up to isomorphism of coverings (homeomorphisms commuting with the covering maps, not required to preserve basepoints)? Give a single integer.
```

---

## Final Answer

```
$28$
```

---

## Solution

```
Step 1: Homology of $T$ and the curves.
$\delta_1$ and $\delta_2$ meet exactly once, transversally, at the centre, so $\langle\delta_1,\delta_2\rangle=\pm1$ and $(\delta_1,\delta_2)$ is a basis of $H_1(T)=\mathbb{Z}^2$. Take the sign $+1$; the opposite sign conjugates every matrix below by $\operatorname{diag}(1,-1)$ and does not change the count.

Step 2: The monodromy $A=f_*$.
A twist acts by $(T_\gamma^{\,k})_*(x)=x+k\langle\gamma,x\rangle\gamma$, and the half-turn acts by $h_*=-I$. So $T_{\delta_2}^{-2}$ sends $\delta_1\mapsto\delta_1+2\delta_2$ and fixes $\delta_2$, and $T_{\delta_1}$ fixes $\delta_1$ and sends $\delta_2\mapsto\delta_1+\delta_2$. Hence $(T_{\delta_1}T_{\delta_2}^{-2})_*=B=\begin{pmatrix}3&1\\2&1\end{pmatrix}$, and $A=-B=\begin{pmatrix}-3&-1\\-2&-1\end{pmatrix}$, with $\operatorname{tr}A=-4$. Since $-I$ is central, the order in which the three maps are composed does not matter.

Step 3: Covers as subgroups.
$\pi_1(M_f)=G=N\rtimes\langle t\rangle$ with $N=\mathbb{Z}^2$ and $tnt^{-1}=An$. Connected $12$-sheeted covers up to isomorphism correspond to conjugacy classes of index-$12$ subgroups of $G$.

Step 4: Parametrise subgroups.
Every index-$n$ subgroup is $U=L\rtimes\langle t^m n_0\rangle$, where $m\mid n$, $L=U\cap N$ is an $A^m$-invariant sublattice of index $n/m$, and $n_0\in N/L$.

Step 5: Conjugation action.
Conjugating by $n_1\in N$ changes $n_0$ to $n_0+(A^{-m}-I)n_1$, so only $[n_0]\in C_L:=\operatorname{coker}\big((A^m-I)\text{ on }N/L\big)$ matters. Conjugating by $t$ maps $(L,[n_0])\mapsto(AL,[An_0])$. Hence each $\langle A\rangle$-orbit of $L$, of size $o$, contributes the number of $\langle A^o\rangle$-orbits on $C_L$. In every case below $A^o$ acts trivially on $C_L$, so the contribution is $|C_L|$.

Step 6: Local data.
Mod $2$: $A\equiv\begin{pmatrix}1&1\\0&1\end{pmatrix}$, which is unipotent with a unique invariant line $\ell_2$, and $A^2\equiv I$.
Mod $3$: $A\equiv\begin{pmatrix}0&2\\1&2\end{pmatrix}$ has characteristic polynomial $(x-1)^2$ and $A\not\equiv I$, so it has a unique invariant line $\ell_3$. The same holds for $A^2$ and $A^4$, and $A$ acts by $1$ on $N/L_3$, where $L_3$ is the preimage of $\ell_3$.
Index $4$: the index-$4$ sublattices with cyclic quotient lie in $L_2=\{y\equiv0 \bmod 2\}$; they are $\langle(1,0),(0,4)\rangle$ and $\langle(1,2),(0,4)\rangle$. Neither is invariant under $A$ or $A^3$: $A(1,0)=(-3,-2)$, $A(1,2)=(-5,-4)$, $A^3(1,0)=(-41,-30)$, $A^3(1,2)=(-71,-52)$. So $2N$ is the only invariant index-$4$ sublattice for $A$ and for $A^3$.

Step 7: Contributions by $m$.
$m=1$ (index $12$): $L=2N\cap L_3$ is unique. $C_L=\operatorname{coker}(A-I)$ on $(\mathbb{Z}/2)^2\times\mathbb{Z}/3$ has order $2\cdot3=6$. Contribution $6$.
$m=2$ (index $6$): the $A^2$-invariant sublattices are $L=L'\cap L_3$, with $L'$ any of the $3$ index-$2$ sublattices. $A$ fixes $\ell_2$ and swaps the other two lines, giving $L$-orbits of sizes $1$ and $2$. $A^2$ is trivial on $N/L\cong\mathbb{Z}/6$, so $|C_L|=6$ for each. Contribution $6+6=12$.
$m=3$ (index $4$): $L=2N$, and $C_L=\operatorname{coker}(A^3-I)$ on $(\mathbb{Z}/2)^2$ has order $2$. Contribution $2$.
$m=4$ (index $3$): $L=L_3$, and $C_L=N/L_3\cong\mathbb{Z}/3$. Contribution $3$.
$m=6$ (index $2$): $A^6\equiv I \pmod 2$, so all $3$ index-$2$ sublattices are invariant, forming orbits of sizes $1$ and $2$, each with $C_L=\mathbb{Z}/2$. Contribution $2+2=4$.
$m=12$ (index $1$): contribution $1$.

Step 8: Total.
$6+12+2+3+4+1=28$. (The number of index-$12$ subgroups is $12+18+4+3+6+1=44$.)
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $28$.
```

### Criterion 2 — 1 point

```
Computes the monodromy $f_*=-\begin{pmatrix}3&1\\2&1\end{pmatrix}$ (up to conjugacy), in particular using $h_*=-I$ for the half-turn.
```

### Criterion 3 — 2 points

```
Reduces the count to orbits: index-$12$ subgroups $L\rtimes\langle t^mn_0\rangle$ up to conjugacy correspond to $\langle A\rangle$-orbits of pairs $(L,[n_0])$ with $L$ an $A^m$-invariant sublattice of index $12/m$ and $[n_0]\in\operatorname{coker}\big((A^m-I)\text{ on }\mathbb{Z}^2/L\big)$.
```

### Criterion 4 — 2 points

```
Obtains the contributions $6$ (for $m=1$) and $12$ (for $m=2$), i.e. a unique $A$-invariant index-$12$ sublattice with cokernel of order $6$, and two $\langle A\rangle$-orbits of $A^2$-invariant index-$6$ sublattices each with cokernel of order $6$.
```

---

## Common Wrong Answers

```
$44$
```

```
$21$
```

```
$8$
```

Notes (for reference, not for pasting):
- $44$ — counts index-$12$ subgroups instead of conjugacy classes (i.e. based covers).
- $21$ — ignores the half-turn, i.e. uses $B$ instead of $A=-B$; the subgroup count is still $44$, but the conjugacy classes change.
- $8$ — counts only the $\langle A\rangle$-orbits of the lattices $L$ and forgets the $[n_0]$ parameter.

Verification (for reference): the lattice/orbit method was checked against brute-force enumeration of transitive homomorphisms $\pi_1(M_f)\to S_n$ up to conjugation for $n=2,\dots,6$ (classes $3,4,7,1,12$), and against two other torus bundles. The values $28$ for $A$ and $21$ for $B$ were recomputed by union–find over all $44$ subgroups. Both twist conventions give $28$.
