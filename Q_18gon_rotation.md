# Summit Question — 18-gon rotation mapping torus

- **Domain:** Mathematics
- **Sub-topic:** Low-dimensional topology (periodic surface maps, mapping tori)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $P\subset\mathbb{R}^2$ be a regular $18$-gon centred at the origin. Glue each side of $P$ to the side directly opposite it, using the translation of $\mathbb{R}^2$ that carries the one onto the other. The quotient $S=P/\!\sim$ is a closed, connected, orientable surface. The rotation of $\mathbb{R}^2$ by angle $2\pi/3$ about the origin maps $P$ to itself and respects the gluing, so it descends to an orientation-preserving homeomorphism $\rho\colon S\to S$.

Let $M_\rho=S\times[0,1]/(x,1)\sim(\rho(x),0)$ be the mapping torus of $\rho$. Compute $H_1(M_\rho;\mathbb{Z})$. Write the answer as a direct sum of cyclic groups in invariant-factor form.
```

---

## Final Answer

```
$\mathbb{Z}^3\oplus\mathbb{Z}/3$
```

### Also accepted

```
$\mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z}/3$
```

```
$\mathbb{Z}^3\oplus\mathbb{Z}_3$
```

---

## Solution

```
Step 1: Cell structure of $S$.
Number the sides of $P$ as $s_1,\dots,s_{18}$ counter-clockwise, each oriented counter-clockwise. Side $s_j$ is glued to $s_{j+9}$ by a translation; because the two sides run in opposite directions around $\partial P$, $s_{j+9}$ is $s_j$ traversed backwards. This gives $9$ edges $e_1,\dots,e_9$, with $e_j$ the image of $s_j$. Following the gluing of corners, corner $j$ (between $s_{j-1}$ and $s_j$) is identified only with corners of the same parity, so there are exactly two vertex classes, $A$ (odd corners) and $B$ (even corners). There is one face. Hence $\chi(S)=2-9+1=-6$ and $S$ has genus $g=4$.

Step 2: $H_1(S)$ as a lattice.
The boundary word of the face abelianises to $0$, so $\partial_2=0$ and $H_1(S)=\ker\partial_1$. Corners alternate $A,B,A,B,\dots$, so $\partial e_j=(-1)^{j+1}(B-A)$. Put $\varepsilon_j=(-1)^{j+1}e_j$; then $\partial\varepsilon_j=B-A$ for every $j$, and $H_1(S)=L:=\{\sum_{j=1}^{9}c_j\varepsilon_j : \sum_j c_j=0\}\cong\mathbb{Z}^8$.

Step 3: The basic rotation.
Let $r$ be the rotation by $2\pi/18$, which also descends to $S$. It maps $s_j$ to $s_{j+1}$, so $r_*(e_j)=e_{j+1}$ for $j\le 8$, and $r_*(e_9)=[s_{10}]=-e_1$. In the $\varepsilon$-basis, $r_*(\varepsilon_j)=-\varepsilon_{j+1}$ (indices mod $9$), so $r_*=-\sigma$, where $\sigma$ is the cyclic shift of order $9$. Since $\rho=r^{6}$ and the power is even, $\rho_*=\sigma^{6}$ on $L$.

Step 4: Module structure.
Identify $\mathbb{Z}^9=\mathbb{Z}[x]/(x^9-1)$ with $\sigma$ acting as multiplication by $x$. Then $L$ is the augmentation ideal $(x-1)\,\mathbb{Z}[x]/(x^9-1)$, and multiplication by $x-1$ gives a $\mathbb{Z}[x]$-module isomorphism $\mathbb{Z}[x]/(\Psi)\cong L$, where $\Psi(x)=(x^9-1)/(x-1)=\Phi_3(x)\Phi_9(x)$, with $\Phi_3=x^2+x+1$ and $\Phi_9=x^6+x^3+1$.

Step 5: Reduce to a quotient ring.
By the Wang sequence, $H_1(M_\rho)\cong\mathbb{Z}\oplus\operatorname{coker}(\rho_*-I)$, and $\operatorname{coker}(\rho_*-I)\cong R:=\mathbb{Z}[x]/(\Phi_3\Phi_9,\ x^6-1)$. Modulo $x^6-1$ we have $\Phi_9\equiv x^3+2$. Since $x^6-1=(x-1)\Phi_3(x^3+1)$, the ideal equals $\Phi_3\cdot J$ with $J=((x-1)(x^3+1),\ x^3+2)$.

Step 6: Split off the free part.
Because $\Phi_3$ is not a zero divisor in $\mathbb{Z}[x]$, there is an exact sequence $0\to\mathbb{Z}[x]/J\xrightarrow{\cdot\Phi_3}R\to\mathbb{Z}[x]/(\Phi_3)\to 0$. It splits because $\mathbb{Z}[x]/(\Phi_3)\cong\mathbb{Z}^2$ is free. Hence $R\cong\mathbb{Z}^2\oplus\mathbb{Z}[x]/J$.

Step 7: Compute $\mathbb{Z}[x]/J$.
In $\mathbb{Z}[x]/J$ we have $x^3=-2$, so $x^3+1=-1$. Then $(x-1)(x^3+1)=0$ forces $x=1$. Substituting back gives $1=-2$, so $3=0$. Hence $\mathbb{Z}[x]/J\cong\mathbb{Z}/3$.

Step 8: Consistency check with Riemann–Hurwitz.
The fixed points of $\rho$ are the centre and the two vertex points $A$ and $B$: every $A$-corner goes to an $A$-corner, and no edge is mapped to itself because $j+6\not\equiv j,\ j+9 \pmod{18}$. With $3$ fixed points, Riemann–Hurwitz gives $2\cdot 4-2=3(2h-2)+3\cdot 2$, so the quotient has genus $h=1$. Then $\operatorname{rank}\ker(\rho_*-I)=2h=2$, matching the $\mathbb{Z}^2$ in Step 6.

Step 9: Assemble.
$H_1(M_\rho;\mathbb{Z})\cong\mathbb{Z}\oplus\mathbb{Z}^2\oplus\mathbb{Z}/3=\mathbb{Z}^3\oplus\mathbb{Z}/3$.
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $H_1(M_\rho;\mathbb{Z})\cong\mathbb{Z}^3\oplus\mathbb{Z}/3$, or an exactly equivalent form.
```

### Criterion 2 — 2 points

```
Identifies that $S$ has two vertex classes and genus $4$, and that $H_1(S)$ is the sum-zero lattice in $\mathbb{Z}^9$ (equivalently $\mathbb{Z}[x]/(\Phi_3\Phi_9)$ with the rotation acting through the cyclic shift).
```

### Criterion 3 — 1 point

```
Obtains free rank $3$ for $H_1(M_\rho)$, e.g. from $3$ fixed points and quotient genus $1$ via Riemann–Hurwitz, or from $\gcd(\Phi_3\Phi_9,\ x^6-1)=\Phi_3$.
```

### Criterion 4 — 2 points

```
Shows that the torsion subgroup of $\operatorname{coker}(\rho_*-I)$ is $\mathbb{Z}/3$.
```

---

## Common Wrong Answers

```
$\mathbb{Z}^3$
```

```
$\mathbb{Z}^4$
```

```
$\mathbb{Z}^3\oplus\mathbb{Z}/9$
```

Notes (for reference, not for pasting):
- $\mathbb{Z}^3$ — gets the rank from Riemann–Hurwitz and assumes there is no torsion.
- $\mathbb{Z}^4$ — treats all corners as one vertex (as in the $4g$-gon model), so uses $H_1=\mathbb{Z}[x]/(x^9+1)$.
- $\mathbb{Z}^3\oplus\mathbb{Z}/9$ — drops the $\Phi_3$ factor when computing the torsion.
