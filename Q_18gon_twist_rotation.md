# Summit Question — 18-gon: Dehn twist composed with rotation

- **Domain:** Mathematics
- **Sub-topic:** Low-dimensional topology (mapping class groups, mapping tori)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $P\subset\mathbb{R}^2$ be a regular $18$-gon centred at the origin. Glue each
side of $P$ to the side directly opposite it, using the translation of $\mathbb{R}^2$
that carries the one onto the other. The quotient $S=P/\!\sim$ is a closed, connected
surface, oriented by the standard orientation of $\mathbb{R}^2$.
The rotation of $\mathbb{R}^2$ by angle $2\pi/3$ about the origin maps $P$ to itself
and respects the gluing, so it descends to a homeomorphism $\rho\colon S\to S$. Let
$\delta\subset S$ be the image of the straight segment joining the midpoints of two
opposite sides of $P$; it is a simple closed curve through the image of the centre of
$P$. Let $T_\delta$ denote the positive (left-handed) Dehn twist about $\delta$, and
define $f=T_\delta^{\,3}\circ\rho\colon S\to S$ (apply $\rho$ first).
Let $M_f=S\times[0,1]/(x,1)\sim(f(x),0)$ be the mapping torus of $f$. Compute
$H_1(M_f;\mathbb{Z})$. Write the answer as a direct sum of cyclic groups in
invariant-factor form.
```

---

## Final Answer

```
$\mathbb{Z}^2\oplus\mathbb{Z}/3\oplus\mathbb{Z}/3$
```

### Also accepted

```
$\mathbb{Z}^2\oplus(\mathbb{Z}/3)^2$
```

```
$\mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z}/3\oplus\mathbb{Z}/3$
```

```
$\mathbb{Z}^2\oplus\mathbb{Z}_3\oplus\mathbb{Z}_3$
```

---

## Solution

```
Step 1: Cell structure.
Sides $s_1,\dots,s_{18}$ (counter-clockwise); $s_{j+9}$ is glued to $s_j$ reversed, giving edges $e_1,\dots,e_9$ with $[s_k]=e_k$ ($k\le 9$) and $[s_k]=-e_{k-9}$ ($k\ge 10$). Corners split by parity into two vertices $A,B$; one face. $\chi(S)=2-9+1=-6$, so the genus is $4$.

Step 2: $H_1(S)$.
$\partial_2=0$ and $\partial e_j=(-1)^{j+1}(B-A)$, so $H_1(S)=\{\sum_j c_je_j:\ \sum_j(-1)^{j+1}c_j=0\}\cong\mathbb{Z}^8$.

Step 3: Diameter classes.
Let $\delta_j$ be the segment from the midpoint of $s_j$ to that of $s_{j+9}$. Homotoping it to the boundary arc gives $[\delta_j]=\sum_{k=j+1}^{j+8}[s_k]$. By rotational symmetry, take $\delta=\delta_1$.

Step 4: Intersections.
Distinct diameters meet once, at the centre: $\langle\delta_i,\delta_j\rangle=+1$ for $i<j$.

Step 5: Basis.
The Gram matrix of $\delta_1,\dots,\delta_8$ has determinant $1$, and the intersection form is unimodular, so $\delta_1,\dots,\delta_8$ is a $\mathbb{Z}$-basis. Also $\delta_9=-\delta_1+\delta_2-\delta_3+\delta_4-\delta_5+\delta_6-\delta_7+\delta_8$.

Step 6: $\rho_*$.
The rotation $r$ by $2\pi/18$ sends $\delta_j\mapsto\delta_{j+1}$ and $\delta_9\mapsto-\delta_1$. With $\delta_{j+9}:=-\delta_j$, $\rho=r^6$ gives $\rho_*\delta_j=\delta_{j+6}$.

Step 7: Twist.
$(T_\delta^{\,m})_*x=x+m\langle\delta_1,x\rangle\delta_1$, so $\delta_1\mapsto\delta_1$ and $\delta_j\mapsto\delta_j+m\delta_1$ for $j\ge 2$ ($m=3$; $m=-3$ for the opposite convention).

Step 8: $f_*=(T^m)_*\rho_*$.
$\delta_1\mapsto\delta_7+m\delta_1$, $\delta_2\mapsto\delta_8+m\delta_1$, $\delta_3\mapsto\delta_9+m\delta_1$, $\delta_4\mapsto-\delta_1$, $\delta_5\mapsto-\delta_2-m\delta_1$, $\delta_6\mapsto-\delta_3-m\delta_1$, $\delta_7\mapsto-\delta_4-m\delta_1$, $\delta_8\mapsto-\delta_5-m\delta_1$.

Step 9: Relations.
$H_1(M_f)\cong\mathbb{Z}\oplus\operatorname{coker}(f_*-I)$ (Wang sequence). With generators $y_1,\dots,y_8$:
(R1) $(m-1)y_1+y_7=0$
(R2) $my_1-y_2+y_8=0$
(R3) $(m-1)y_1+y_2-2y_3+y_4-y_5+y_6-y_7+y_8=0$
(R4) $-y_1-y_4=0$
(R5) $-my_1-y_2-y_5=0$
(R6) $-my_1-y_3-y_6=0$
(R7) $-my_1-y_4-y_7=0$
(R8) $-my_1-y_5-y_8=0$

Step 10: Eliminate.
R1, R2, R4, R5 and R6 solve for $y_7,y_8,y_4,y_5,y_6$. Then R7 is vacuous, R8 becomes $my_1=0$, and R3 becomes $(m-3)y_1+3(y_2-y_3)=0$.

Step 11: Evaluate at $m=\pm3$.
Both signs give $3y_1=0$ and $3(y_2-y_3)=0$, so $\operatorname{coker}(f_*-I)\cong\mathbb{Z}\oplus\mathbb{Z}/3\oplus\mathbb{Z}/3$. The torsion has order $9$ but is not cyclic.

Step 12: Answer.
$H_1(M_f;\mathbb{Z})\cong\mathbb{Z}^2\oplus\mathbb{Z}/3\oplus\mathbb{Z}/3$.
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $H_1(M_f;\mathbb{Z})\cong\mathbb{Z}^2\oplus\mathbb{Z}/3\oplus\mathbb{Z}/3$, or an exactly equivalent form.
```

### Criterion 2 — 2 points

```
Identifies that $S$ has two vertex classes and genus $4$, so that $H_1(S)\cong\mathbb{Z}^8$ is the kernel of $\partial_1$ (not the free group on all $9$ edges).
```

### Criterion 3 — 1 point

```
Uses that two distinct diameters meet exactly once, at the centre, with intersection number $\langle\delta_i,\delta_j\rangle=\pm1$, so the twist acts by a nontrivial transvection $x\mapsto x\pm3\langle\delta,x\rangle\delta$.
```

### Criterion 4 — 2 points

```
Shows that the torsion of $\operatorname{coker}(f_*-I)$ is $\mathbb{Z}/3\oplus\mathbb{Z}/3$, not cyclic of order $9$ (e.g. relations reducing to $3y_1=0$ and $3(y_2-y_3)=0$, or $f_*-I$ having rank $5$ modulo $3$).
```

---

## Common Wrong Answers

```
$\mathbb{Z}^2\oplus\mathbb{Z}/9$
```

```
$\mathbb{Z}^3\oplus\mathbb{Z}/3$
```

```
$\mathbb{Z}^2\oplus\mathbb{Z}/3$
```

```
$\mathbb{Z}\oplus\mathbb{Z}/112$
```

Notes (for reference, not for pasting):
- $\mathbb{Z}^2\oplus\mathbb{Z}/9$ — finds that the torsion has order $9$ and assumes it is cyclic.
- $\mathbb{Z}^3\oplus\mathbb{Z}/3$ — treats the twist as acting trivially on homology (e.g. thinks $\delta$ is null-homologous), so gets the answer for $\rho$ alone.
- $\mathbb{Z}^2\oplus\mathbb{Z}/3$ — uses a single twist ($m=1$) and drops the exponent $3$.
- $\mathbb{Z}\oplus\mathbb{Z}/112$ — misses the orientation reversal $r_*(\delta_9)=-\delta_1$ and writes $\delta_9=\delta_1+\dots+\delta_8$.
- Each wrong answer was obtained by recomputing $H_1(M_f)$ with that specific mistake.
