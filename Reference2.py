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