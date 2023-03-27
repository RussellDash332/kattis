import sys
from collections import deque
from math import ceil

v, e = map(int, input().split())
g = [[] for _ in range(v)]
for line in sys.stdin:
    a, b = map(int, line.split())
    g[a].append(b), g[b].append(a)
D = []

vis, vis2 = [0]*v, [0]*v
for i in range(v):
    if not vis[i]:
        q = deque([(i, 0)])
        while q:
            u, d = q.popleft()
            if vis[u]: continue
            f = u # furthest
            vis[f] = 1
            for w in g[f]: q.append((w, d+1))
        q = deque([(f, 0)])
        while q:
            u, d = q.popleft()
            if vis2[u]: continue
            d2 = d
            vis2[u] = 1
            for w in g[u]: q.append((w, d+1))
        D.append(d2)

D.sort()
for _ in range(len(D)-1):
    a, b = D.pop(), D.pop()
    D.append(max(a, b, ceil(a/2) + ceil(b/2) + 1))
print(D[0])