import sys; input()
from random import choice

t, r, n = [], {}, []
for l in sys.stdin:
    a, b = map(int, l.split())
    t.append((a, b))
    if a not in r: r[a] = len(r); n.append(a)
    if b not in r: r[b] = len(r); n.append(b)

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1

q, vc = [], []
for exc in range(2):
    # MCBM - Konig's theorem to find MVC
    V = len(r)
    g = [[] for _ in range(V)]
    match = [-1]*V
    free = {*(i for i in range(V) if n[i] < 2000)}
    for a, b in t:
        if exc and (a == 1009 or b == 1009): continue
        a2, b2 = r[a], r[b]; g[a2].append(b2)
    for l in range(V):
        if (can:=[r for r in g[l] if match[r] == -1]): free.discard(l); match[choice(can)] = l
    for f in free: vis = [0]*V; aug(f)

    # matching graph
    mg = [set() for _ in range(V)]
    for a in range(V):
        for b in g[a]:
            if match[b] != -1: mg[match[b]].add(b)

    # make the graph undirected for DFS prep
    for a, b in t:
        if exc and (a == 1009 or b == 1009): continue
        a2, b2 = r[a], r[b]; g[b2].append(a2)

    vis = [0]*V
    z = set() # all verts connected to unmatched free verts
    for i in range(V):
        if n[i] < 2000 and not mg[i]: # DFS on unmatched free verts for alternating path
            q.append(2*i)
            while q:
                umt = q.pop()
                u, mt = umt//2, umt%2
                if vis[u]: continue
                z.add(u); vis[u] = 1
                for w in g[u]:
                    if (u in mg[w] or w in mg[u])^(1-mt): q.append(2*w+1-mt)
    vc.append([n[i] for i in range(V) if (n[i] < 2000)^(i in z)]) # mvc = (L-Z)|(R&Z)

x, y = vc
if len(y) < len(x): print(len(y)+1, 1009, *y) # 1009 not in y so adding it should make it the optimal solution
else: print(len(x), *x)