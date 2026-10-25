# Summit Question — Expected query cost of two-level majority on uniform inputs

- **Domain:** Computer Science/AI
- **Sub-topic:** Query complexity (distributional decision-tree complexity, recursive majority)
- **Modality:** text-only
- **Task type:** not_applicable
- **Answer type:** exact_match

---

## Question

```
Let $f(x_1,\dots,x_9)=\mathrm{MAJ}_3\big(\mathrm{MAJ}_3(x_1,x_2,x_3),\ \mathrm{MAJ}_3(x_4,x_5,x_6),\ \mathrm{MAJ}_3(x_7,x_8,x_9)\big)$, where $\mathrm{MAJ}_3$ is the majority of three bits. The nine input bits are independent and uniformly random. An algorithm reads the bits one at a time, chooses each next bit based on everything it has read so far, and stops as soon as the value of $f$ is determined.

What is the smallest possible expected number of bits read? Give the answer as a reduced fraction.
```

---

## Final Answer

```
$\frac{393}{64}$
```

## Also accepted

```
$393/64$
```

```
$6.140625$
```

---

## Solution

```
Step 1: Reduction to block states.
Call the triples $(x_1,x_2,x_3)$, $(x_4,x_5,x_6)$, $(x_7,x_8,x_9)$ blocks. Because the bits are i.i.d. uniform and the unread bits of a block are exchangeable, the only thing that matters about a block is what has been read in it. Each block is in one of six states: $E$ (nothing read), $Z$ (one bit read, it was $0$), $O$ (one bit read, it was $1$), $M$ (two bits read, one $0$ and one $1$), or decided $0$ or decided $1$. Reading a bit of a block moves it: $E\to Z$ or $O$, $Z\to 0$ or $M$, $O\to M$ or $1$, $M\to 0$ or $1$, each with probability $\frac12$. The game ends when two blocks are decided with the same value. A global state is an unordered multiset of three block states, and flipping every bit maps a state to one of the same value, so we identify a state with its flip (e.g. $1ZE\equiv 0OE$). The optimal expected cost $V$ satisfies $V=0$ at terminal states and otherwise
$V(S)=\min_{\text{block }B\text{ of }S}\Big(1+\tfrac12 V(S_{B\to\text{child}_0})+\tfrac12 V(S_{B\to\text{child}_1})\Big)$.
This recursion is exact: it is the dynamic program over all partial assignments, collapsed by symmetry.

Step 2: The natural answer $25/4$ and why it is not optimal.
One $\mathrm{MAJ}_3$ on uniform bits costs $2+\frac12=\frac52$ in expectation. The directional strategy evaluates one block fully, then another, and the third only if the first two disagree (probability $\frac12$), costing $\frac52\cdot\big(2+\frac12\big)=\frac{25}{4}$. For AND-OR (NAND) trees with i.i.d. leaves, depth-first directional evaluation is optimal (Tarsi; Saks and Wigderson), which makes $25/4$ tempting. For majority it fails: after one bit of a block has been read, that block is still undecided, and it pays to look at a fresh block before finishing the first one.

Step 3: Values of all states (bottom up). Each line gives the value, the block read by an optimal move, its two children (a decided outcome is written $0$), and the values of the other moves.
$01M=1$: read $M$; children terminal, terminal.
$0MM=\frac32$: read $M$; children terminal, $01M$.
$01O=\frac32$: read $O$; children $01M$, terminal.
$0MZ=\frac74$: read $M$; children terminal, $01O$ (reading $Z$ also gives $\frac74$).
$0MO=\frac74$: read $M$; children terminal, $01O$ (reading $O$: $\frac94$).
$0ZZ=\frac{15}{8}$: read $Z$; children terminal, $0MZ$.
$0OZ=\frac{15}{8}$: read $Z$; children terminal, $0MO$ (reading $O$: $\frac{21}{8}$).
$0EZ=\frac{17}{8}$: read $Z$; children terminal, $0EM$ (reading $E$: $\frac{23}{8}$).
$0EM=\frac94$: read $M$; children terminal, $01E$ (reading $E$: $\frac{11}{4}$).
$01E=\frac52$: read $E$; children $01O$, $01Z\equiv 01O$.
$MMM=\frac52$: read $M$; children $0MM$, $1MM\equiv 0MM$.
$0OO=\frac{21}{8}$: read $O$; children $0MO$, $01O$.
$MMO=\frac{11}{4}$: read $M$; children $0MO$, $1MO\equiv 0MZ$ (reading $O$: $3$).
$MOZ=\frac{23}{8}$: read $M$; children $0OZ$, $1OZ\equiv 0OZ$ (reading $O$ or $Z$: $\frac{13}{4}$).
$0EO=\frac{13}{4}$: read $E$; children $0OZ$, $0OO$ (reading $O$: $\frac{27}{8}$).
$EMM=\frac{13}{4}$: read $M$; children $0EM$, $1EM\equiv 0EM$ (reading $E$: $\frac{15}{4}$).
$MOO=\frac{13}{4}$: read $M$; children $0OO$, $1OO\equiv 0ZZ$ (reading $O$ also gives $\frac{13}{4}$).
$OOZ=\frac{27}{8}$: read $O$; children $MOZ$, $1OZ\equiv 0OZ$ (reading $Z$: $\frac{63}{16}$).
$OOO=\frac{57}{16}$: read $O$; children $MOO$, $1OO\equiv 0ZZ$.
$EMO=\frac{59}{16}$: read $M$; children $0EO$, $1EO\equiv 0EZ$ (reading $E$: $\frac{65}{16}$; reading $O$: $\frac{15}{4}$).
$0EE=\frac{59}{16}$: read $E$; children $0EZ$, $0EO$.
$EOO=\frac{125}{32}$: read $O$; children $EMO$, $E1O\equiv 0EZ$ (reading $E$: $\frac{143}{32}$).
$EOZ=\frac{35}{8}$: read $E$; children $OOZ$, $OZZ\equiv OOZ$ (reading $O$ or $Z$: $\frac{143}{32}$).
$EEM=\frac{75}{16}$: read $M$; children $0EE$, $1EE\equiv 0EE$ (reading $E$, with children $EMZ\equiv EMO$ and $EMO$, also gives $\frac{75}{16}$).
$EEO=\frac{329}{64}$: read $E$; children $EOZ$, $EOO$ (reading $O$: $\frac{83}{16}=\frac{332}{64}$).
$EEE=\frac{393}{64}$: read $E$; children $EEO$, $EEZ\equiv EEO$.

Step 4: The decisive comparison.
After the first bit (say a $1$ in block $A$), finishing block $A$ costs $1+\frac12V(EEM)+\frac12V(0EE)=1+\frac12\cdot\frac{75}{16}+\frac12\cdot\frac{59}{16}=\frac{83}{16}$. Reading a bit of a fresh block $B$ instead costs $1+\frac12V(EOZ)+\frac12V(EOO)=1+\frac12\cdot\frac{35}{8}+\frac12\cdot\frac{125}{32}=\frac{329}{64}<\frac{332}{64}$. If the two bits agree ($EOO$), the optimal play continues in one of those two blocks; if they disagree ($EOZ$), it opens the third block. So the optimum is not directional.

Step 5: Answer.
$V(EEE)=1+V(EEO)=1+\frac{329}{64}=\frac{393}{64}=6.140625$, strictly less than the directional $\frac{25}{4}=\frac{400}{64}$.
```

### Reference implementation (append to the solution)

```python
# Optimal expected number of reads for MAJ3(MAJ3,MAJ3,MAJ3) on uniform bits.
# Exhaustive DP over all 3^9 partial assignments. Python 3, standard library only.
from fractions import Fraction as F
from functools import lru_cache

def maj(v):
    if v.count(1) >= 2: return 1
    if v.count(0) >= 2: return 0
    return None

def val(s):
    return maj([maj(list(s[3*i:3*i+3])) for i in range(3)])

@lru_cache(None)
def E(s):
    if val(s) is not None:
        return F(0)
    best = None
    for i in range(9):
        if s[i] is None:
            a = list(s); a[i] = 0
            b = list(s); b[i] = 1
            c = 1 + (E(tuple(a)) + E(tuple(b))) / 2
            best = c if best is None else min(best, c)
    return best

print(E((None,) * 9))   # 393/64
```

---

## Rubric (10 points)

### Criterion 1 — Final answer — 5 points

```
Gives $\frac{393}{64}$ (equivalently $6.140625$).
```

### Criterion 2 — 2 points

```
Recognises that the directional strategy (evaluate whole sub-majorities one at a time, cost $\frac{25}{4}$) is not optimal for majority, unlike the AND-OR/NAND case.
```

### Criterion 3 — 1 point

```
Reduces the problem to an exact dynamic program over block states (nothing read, one $0$, one $1$, one $0$ and one $1$, decided), using the exchangeability of unread bits and the $0\leftrightarrow1$ symmetry.
```

### Criterion 4 — 2 points

```
Shows that after the first bit, reading a bit of a fresh block (expected total $\frac{329}{64}$ remaining) beats finishing the started block ($\frac{83}{16}$), and obtains $1+\frac{329}{64}=\frac{393}{64}$.
```

---

## Common Wrong Answers

```
$\frac{25}{4}$
```

```
$\frac{20}{3}$
```

```
$\frac{64}{9}$
```

```
$6$
```

Notes (for reference, not for pasting):
- $25/4$: the directional strategy, assumed optimal by analogy with AND-OR trees.
- $20/3$: uses $8/3$ (the randomized worst-case cost of $\mathrm{MAJ}_3$) per block, $\frac83\cdot\frac52$.
- $64/9$: $(8/3)^2$, the randomized directional recurrence, which answers a different (worst-case randomized) question.
- $6$: guesses a round number below $25/4$ without an exact computation.

Verification (for reference): the full DP over all $3^9$ partial assignments (reference program) and the independent block-state DP of Step 3 both give $393/64$; the block-state DP restricted to directional strategies gives $25/4$. Under the uniform distribution on non-constant blocks (the standard hard distribution) the optimum equals the directional value $20/3$, so the gap is specific to i.i.d. uniform leaves.
