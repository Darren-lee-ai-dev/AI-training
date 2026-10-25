# Summit Question — Littlestone dimension of intervals

- **Domain:** Computer Science/AI
- **Sub-topic:** Computational learning theory (online learning, Littlestone dimension)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $n=10^6$ and $X=\{1,2,\dots,n\}$. For integers $1\le a\le b\le n$ let $h_{a,b}\colon X\to\{0,1\}$ be the indicator of $\{x: a\le x\le b\}$, and let $h_{\varnothing}\equiv 0$. The hypothesis class is defined as $\mathcal{H}=\{h_{a,b}: 1\le a\le b\le n\}\cup\{h_{\varnothing}\}$.

The Littlestone dimension $\mathrm{Ldim}(\mathcal{H})$ is the largest $d$ for which there exists a complete binary tree of depth $d$ with the internal nodes labelled by points of $X$ such that for every root to leaf path (the two children of a node corresponding to the $0$ and $1$ labels of its point) there is some $h\in\mathcal{H}$ which agrees with all the labels along that path. Equivalently it is the optimal worst case number of mistakes in the realizable online setting.

Let $d=\mathrm{Ldim}(\mathcal{H})$. How many ordered pairs $(x,y)\in X\times X$ are there such that at least one complete binary tree of depth $d$ with the property above has its root labelled $x$ and the root's $0$-child labelled $y$? Give a single integer.
```

---

## Final Answer

```
$34030012510$
```

---

## Solution

```
Step 1: Recursion.
For a version space $V$, $\mathrm{Ldim}(V)\ge d$ ($d\ge 1$) if and only if some point $x$ splits $V$ into $V_{x,0}$ and $V_{x,1}$ such that $\mathrm{Ldim}(V_{x,0})\ge d-1$ and $\mathrm{Ldim}(V_{x,1})\ge d-1$.

Step 2: After the first positive label.
A maximal block of unlabelled points is a run. If $x$ is labelled $1$ and is in a run with $L$ points to its left and $R$ to its right then the version space is $\{h_{a,b}\}$ with $a$ ranging over $L+1$ values and $b$ over $R+1$ values (chosen independently). This is a product of two threshold classes on disjoint domains and so its Littlestone dimension is $\lambda(L,R)=\lfloor\log_2(L+1)\rfloor+\lfloor\log_2(R+1)\rfloor$.

Step 3: Prior to any positive label.
The state is the multiset of run lengths and $h_{\varnothing}$ is always consistent. Let $Q_d$ mean $\mathrm{Ldim}\ge d$. $Q_1$ holds iff some run is non-empty and $Q_d$ holds iff some point of a run splits it into pieces $(L,R)$ with $\lambda(L,R)\ge d-1$ such that the resulting state satisfies $Q_{d-1}$. A point which does this is said to be a placement of requirement $d-1$.

Step 4: Shortest way to meet a requirement.
A run of length $m$ admits $\lambda\ge v$ if and only if $m\ge\mu(v):=\min_{\alpha+\beta=v}(2^\alpha+2^\beta-1)$. This gives $\mu(2k)=2^{k+1}-1$ and $\mu(2k+1)=3\cdot 2^k-1$. In particular $Q_2$ holds if and only if the longest run has length $a\ge 2$.

Step 5: Two-run lemma.
For $d\ge 3$ put $j=\lfloor(d-1)/2\rfloor$, $\beta(d)=3\cdot 2^{j-1}-1$ and $N(d)=\mu(d-1)+2^{j-1}$ so that $N(2j+1)=5\cdot 2^{j-1}-1$ and $N(2j+2)=7\cdot 2^{j-1}-1$. Let $a\ge b$ be the two longest runs ($b=0$ if there's only one). Then...
$Q_d$ if and only if $a\ge N(d)$ or $(a\ge\mu(d-1)$ and $b\ge\beta(d))$.
The proof is by induction on $d$, with the base cases $d=2,3$ checked directly.

Step 6: Sufficiency.
If $a$ is greater than or equal to $\mu(d-1)$ and $b$ is greater than or equal to $\beta(d)$: when $d=2j+1$ cut the $a$-run into $(2^j-1,\ a-2^j)$ so that $\lambda$ is greater than or equal to $2j$. When $d=2j+2$ cut it into $(2^j-1,\ a-2^j)$ with $a-2^j$ greater than or equal to $2^{j+1}-1$ so that $\lambda$ is greater than or equal to $2j+1$. In either case the new state satisfies the second clause of $Q_{d-1}$.
If $a\ge N(d)$, when $d=2j+1$, cut into $(2^{j-1}-1,\ a-2^{j-1})$. So $\lambda\ge 2j$. Also, $a-2^{j-1}\ge 2^{j+1}-1\ge N(d-1)=7\cdot2^{j-2}-1$. When $d=2j+2$, cut into $(2^j-1,\ a-2^j)$. Here, $a-2^j\ge5\cdot2^{j-1}-1=N(d-1)$. So $\lambda\ge 2j+1$. In both cases, the first part of $Q_{d-1}$ holds.

Step 7: Necessity.
The requirement $d-1$ needs a run of length $\ge\mu(d-1)$, so $a\ge\mu(d-1)$. Suppose $b<\beta(d)$. Since $\beta(d)<\mu(d-1)$ the placement is in the $a$-run, giving pieces $L$ and $R$ and all other runs are shorter than $\beta(d)$. Let $R$ be the larger piece and $r=\lfloor\log_2(R+1)\rfloor$.
Case $d=2j+1$: By $Q_{d-1}$, $R$ is at least $\min(N(d-1),\mu(d-2))=6\cdot2^{j-2}-1$. So $r$ is at least $j$. Since $L+1$ is at least $2^{2j-r}$, we have $a=L+R+1$ is at least $2^{2j-r}+\max(2^r,6\cdot2^{j-2})-1$. This is at least $10\cdot2^{j-2}-1=N(d)$.
Case $d=2j+2$: either $R\ge N(d-1)=5\cdot 2^{j-1}-1$ so $r\ge j+1$ and $a\ge 2^{2j+1-r}+\max(2^r,5\cdot 2^{j-1})-1\ge 7\cdot 2^{j-1}-1$; or both of the second set of conditions are satisfied ($R\ge 2^{j+1}-1$ and $L\ge 3\cdot 2^{j-1}-1$) so again $a\ge 7\cdot 2^{j-1}-1$. Either way $a\ge N(d)$.

Step 8: The full domain.
We start with a single run of length $n$ so that $\mathrm{Ldim}(\mathcal{H})\ge d$ iff $n\ge N(d)$. The thresholds are $N=1,2,4,6,9,13,19,27,39,55,\dots$ for $d=1,2,3,\dots$ and for $d\ge 5$ we have $N(d)=2N(d-2)+1$.

Step 9: The value of $d$ for $n=10^6$.
$N(38)=7\cdot 2^{17}-1=917503\le n$ and $N(39)=5\cdot 2^{18}-1=1310719>n$. Hence $d=\mathrm{Ldim}(\mathcal{H})=38$.

Step 10: Condition for a root.
By Step 1, $x$ is the root of a depth-$38$ tree iff $\mathrm{Ldim}(V_{x,1})\ge 37$ and $\mathrm{Ldim}(V_{x,0})\ge 37$. With $L=x-1$, $R=n-x$, put $u=L+1=x$ and $v=R+1=n-x+1$, so $u+v=n+1=1000001$. By Step 2 the first condition is $\lfloor\log_2 u\rfloor+\lfloor\log_2 v\rfloor\ge 37$. By Steps 3 and 5 the second condition is $Q_{37}$ for the two runs $L,R$. For $d=37$ ($j=18$): $N(37)=5\cdot 2^{17}-1=655359$, $\mu(36)=2^{19}-1=524287$, $\beta(37)=3\cdot 2^{17}-1=393215$.

Step 11: The positive-branch condition.
Since $u+v=1000001<2^{20}$, both floors are at most $19$, and they cannot both be $19$ (that would need $u+v\ge 2^{20}$). So one of $u,v$ lies in $[2^{19},2^{20})$ and the other is at least $2^{18}$. Take $u$ to be the larger: $u\in[524288,\ 1000001-262144]=[524288,\ 737857]$, which is $213570$ values, and the same number with the roles of $u$ and $v$ swapped. In total $427140$ points pass this condition.

Step 12: The negative-branch condition.
With $u$ the larger, the larger run is $u-1\ge 524287=\mu(36)$ automatically. So $Q_{37}$ holds iff $u-1\ge 655359$ or $v-1\ge 393215$, that is, iff $u\ge 655360$ or $u\le 1000001-393216=606785$. It fails exactly for $606786\le u\le 655359$, which is $48574$ values. Each side therefore keeps $213570-48574=164996$ values.

Step 13: The valid roots.
The two sides are disjoint ($u\neq v$ since $n+1$ is odd). By the mirror symmetry $x\mapsto n+1-x$ it suffices to treat $x\le n/2$, where the valid roots are $x\in[262144,344641]$ (Case A: $R=n-x\ge 655359$) and $x\in[393216,475713]$ (Case B: $L=x-1\ge 393215$), each with $82498$ points.

Step 14: Condition for a $0$-child.
A pair $(x,y)$ is valid iff $x$ is a valid root and, in the state after the $0$-labels at $x$ and $y$, $y$ satisfies $\lambda\ge 36$ inside its run and the three resulting runs satisfy $Q_{36}$. For $d=36$ ($j=17$): $N(36)=7\cdot 2^{16}-1=458751$, $\mu(35)=3\cdot 2^{17}-1=393215$, $\beta(36)=3\cdot 2^{16}-1=196607$, and $\mu(36)=524287$. If $y$ splits a run of length $m$ into $p,q$ with $p+q=m-1$, put $P=p+1$, $Q=q+1$, $P+Q=m+1$.

Step 15: Case A, $x\in[262144,344641]$.
The left run $L\le 344640<\mu(36)$ cannot host $\lambda\ge 36$, so $y$ lies in the right run, $m=n-x\in[655359,737856]$, and the other run is $o=L\ge 262143\ge\beta(36)$. Since $o<393215$, $Q_{36}$ holds iff $\max(p,q)\ge 393215$ (the second-largest run is then automatically $\ge\beta(36)$). With $P\ge Q$, so $P\ge 393216$: either $P<2^{19}$, needing $Q\ge 2^{18}$, i.e. $P\in[393216,\ m+1-262144]$; or $P\ge 2^{19}$, needing $Q\ge 2^{17}$, i.e. $P\in[524288,\ m+1-131072]$. Each range has $m-655358$ values, and either piece may be the larger, so $x$ has $4(m-655358)=4(344642-x)$ valid $0$-children. Summing over Case A: $4\sum_{k=1}^{82498}k=2\cdot 82498\cdot 82499=13612005004$.

Step 16: Case B, $x\in[393216,475713]$.
The left run $L\le 475712<\mu(36)$ again cannot host $\lambda\ge 36$, so $y$ lies in the right run, $m=n-x\in[524287,606784]$, with $o=L\ge 393215=\mu(35)$. Since $P+Q=m+1\le 606785<2^{19}+2^{17}$, $\lambda\ge 36$ forces $P,Q\ge 2^{18}$, so $p,q\ge 262143\ge\beta(36)$ and $Q_{36}$ holds automatically. The number of valid $y$ is $(m+1-262144)-262144+1=m-524286=475714-x$. Summing over Case B: $\sum_{k=1}^{82498}k=3403001251$.

Step 17: Answer.
One side contributes $13612005004+3403001251=17015006255$ pairs, and the mirror side the same. The total is $2\cdot 17015006255=34030012510$.
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $34030012510$.
```

### Criterion 2 — 1 point

```
Shows that once a point $x$ receives label $1$, the remaining class is a product of two threshold classes, with Littlestone dimension $\lfloor\log_2(L+1)\rfloor+\lfloor\log_2(R+1)\rfloor$, where $L,R$ are the numbers of unrefuted points to the left and right of $x$ in its run.
```

### Criterion 3 — 2 points

```
Identifies the valid roots: $x$ or $n+1-x$ in $[262144,344641]\cup[393216,475713]$ ($329992$ roots), via the $0$-branch condition: largest run $\ge655359$, or largest $\ge524287$ and second $\ge393215$.
```

### Criterion 4 — 2 points

```
For $x\le n/2$, finds the number of valid $0$-children: $4(344642-x)$ for $x\in[262144,344641]$ and $475714-x$ for $x\in[393216,475713]$ (or equivalent).
```

---

## Common Wrong Answers

```
$17015006255$
```

```
$27224010008$
```

```
$20418007506$
```

Notes (for reference, not for pasting):
- $17015006255$ — forgets the mirror-image roots $x>n/2$.
- $27224010008$ — omits Case B (roots whose smaller side supplies the $\mu(35)$ run), counting only Case A on both sides.
- $20418007506$ — in Case A counts each $0$-child split only once (factor $2$ instead of $4$), forgetting that either piece may be the larger.

Verification (for reference): the recursion was evaluated exactly by two independent programs. One is a brute force over explicit hypothesis sets for $n\le11$. The other is a dynamic program over run multisets for $n\le40$ and over run pairs for $n\le500$. All agree with the thresholds $N(d)$ up to $d=16$, and the two-run lemma was checked for every pair of runs up to length $200$. The root count computed from the lemma matches the exact dynamic program for every $n\le 200$. The pair count computed from the lemma matches the exact multiset dynamic program (which handles three runs directly) for every $n\le 40$, and the count $34030012510$ for $n=10^6$ was obtained by enumerating every valid root and counting its $0$-children exactly.
