Let $n=10^6$, $K=92$ and $X=\{1,2,\dots,n\}$. For integers $1\le a\le b\le n$ let $h_{a,b}\colon X\to\{0,1\}$ be the indicator of $\{x: a\le x\le b\}$ and let $h_{\varnothing}\equiv 0$. Consider the hypothesis class of intervals of length at most $K$ together with the empty hypothesis:
$\mathcal{H}=\{h_{a,b}: 1\le a\le b\le n,\ b-a+1\le K\}\cup\{h_{\varnothing}\}$.

The Littlestone dimension $\mathrm{Ldim}(\mathcal{H})$ is the largest $d$ for which there exists a complete binary tree of depth $d$ with the internal nodes labelled by points of $X$ such that for every root to leaf path (the two children of a node corresponding to the $0$ and $1$ labels of its point) there is some $h\in\mathcal{H}$ which agrees with all the labels along that path. Equivalently it is the optimal worst case number of mistakes in the realizable online setting.

Compute $\mathrm{Ldim}(\mathcal{H})$. Give a single integer.

Step 1: Recursion.
For a version space $V$, $\mathrm{Ldim}(V)\ge d$ ($d\ge 1$) iff some point $x$ splits $V$ into $V_{x,0}$ and $V_{x,1}$ with $\mathrm{Ldim}(V_{x,0})\ge d-1$ and $\mathrm{Ldim}(V_{x,1})\ge d-1$. Littlestone dimension is monotonic under passage to a subclass.

Step 2: The positive branch is a triangle, not a product.
Suppose $x$ is labelled $1$ and there are $\ell$ unrefuted points to its left and $r$ to its right in its run. A consistent interval is written as $[x-i,\ x+j]$. The version space is $R(A,B,C)=\{(i,j): 0\le i\le A,\ 0\le j\le B,\ i+j\le C\}$ where $A=\min(\ell,K-1)$, $B=\min(r,K-1)$ and $C=K-1=91$. A later query at $x-s$ will be whether $i\ge s$ and a query at $x+s$ will be whether $j\ge s$. The length constraint couples $i$ and $j$ so the class is not a product of two thresholds and we can't use $\lfloor\log_2(A+1)\rfloor+\lfloor\log_2(B+1)\rfloor$. Let $D(A,B,C)$ be its Littlestone dimension and $t(C)=D(C,C,C)$, the dimension of the triangle $T(C)=\{(i,j): i,j\ge 0,\ i+j\le C\}$.

Step 3: Recursion for the triangle family.
In $R(A,B,C)$ (with $A,B\le C$) the query $i\ge s$ ($1\le s\le A$) has children $R(A-s,B,C-s)$ (answer $1$, after we've shifted $i$ by $s$) and $R(s-1,B,C)$ (answer $0$). The query $j\ge s$ is of course symmetric. Hence $D(A,B,C)=\max_{\text{queries}}\big(1+\min(D(\text{child}_1),D(\text{child}_0))\big)$ with $D(0,0,C)=0$. In particular the query $i\ge s$ on $T(C)$ has $1$-child $T(C-s)$ and $0$-child $Z=\{i\le s-1,\ i+j\le C\}$ which contains the rectangle $[0,s-1]\times[0,C-s+1]$ of Littlestone dimension $\lfloor\log_2 s\rfloor+\lfloor\log_2(C-s+2)\rfloor$. So...
$t(C)\ge 1+\min\big(t(C-s),\ \lfloor\log_2 s\rfloor+\lfloor\log_2(C-s+2)\rfloor\big)$ for every $1\le s\le C$.

Step 4: Reduction of $\mathcal{H}$ to the triangle.
Upper bound: whatever the root $x$ is, its $1$-branched is some $R(A,B,91)\subseteq T(91)$ and so its dimension is at most $t(91)$ and hence $\mathrm{Ldim}(\mathcal{H})$ is at most $1+t(91)$.
Lower bound: take $x_m = 92 + 183(m-1)$ for $m = 1,\dots,t(91)+1$. The blocks $[x_m-91,\ x_m+91]$ are disjoint and all lie in $X$ (the last one ends at $183(t(91)+1) \le n$). Query $x_1,x_2,\dots$ in order along the all-$0$ path. When $x_m$ is queried its block will still be free so its $1$-branch will be the full triangle $T(91)$ and its $0$-branch will still contain $h_{\varnothing}$ and the later blocks. By Step 1 this gives a tree of depth $t(91)+1$. So $\mathrm{Ldim}(\mathcal{H}) = 1+t(91)$.

Step 5: Lower bound $t(91)\ge 11$.
Apply Step 3 along the chain (each line gives $C$, the split $s$, the triangle left, and the rectangle bound):
$C=1$, $s=1$: $t(0)=0$, rectangle $0+\lfloor\log_2 2\rfloor=1$. So $t(1)\ge 1$.
$C=2$, $s=1$: $t(1)\ge1$. Rectangle $0+1=1$, so $t(2)\ge2$.
$C=3$, $s=1$: $t(2)\ge2$, rectangle $0+2=2$. So $t(3)\ge 3$.
$C=7$, $s=4$: $t(3)\ge3$. Rectangle $2+2=4$, so $t(7)\ge4$.
$C=11$, $s=4$. $t(7)\ge4$. Rectangle $2+3=5$. So $t(11)\ge 5$.
$C=15$, $s=4$: $t(11)\ge5$, rectangle $2+3=5$, so $t(15)\ge 6$.
$C=19$, $s=4$: $t(15)\ge6$, rectangle $2+4=6$. So $t(19)\ge 7$.
$C=27$, $s=8$, $t(19)\ge7$. Rectangle $3+4=7$. So $t(27)\ge 8$.
$C=43$, $s=16$. $t(27)\ge8$. Rectangle $4+4=8$, so $t(43)\ge 9$.
$C=59$, $s=16$: $t(43)\ge9$, rectangle $4+5=9$, so $t(59)\ge 10$.
$C=91$, $s=32$. $t(59)\ge10$. Rectangle $5+5=10$, so $t(91)\ge11$.
For comparison the biggest rectangle you can fit inside $T(91)$ only gets us $\max_s\big(\lfloor\log_2 s\rfloor+\lfloor\log_2(93-s)\rfloor\big)=10$.

Step 6: Upper bound $t(91)\le 11$ (exhaustive verification).
The halving bound gives $t(91)\le\lfloor\log_2|T(91)|\rfloor=\lfloor\log_2 4278\rfloor=12$, which is not tight. The exact value comes from evaluating the recursion of Step 3 over all regions $R(A,B,C)$ with $A,B\le C\le 91$. These regions are closed under both types of query so the recursion is exact and requires no further assumptions. The evaluation gives $D(91,91,91)=11$: no query on $T(91)$ has both of its children of dimension at least $11$. The first values of $C$ at which $t$ increases are $1,2,3,5,8,12,17,25,36,52,73,105$ (for $t=1,\dots,12$) so $t(91)=11$ as $73\le 91<105$.

Step 7: Answer.
$\mathrm{Ldim}(\mathcal{H})=1+t(91)=1+11=12$.
