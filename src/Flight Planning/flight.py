import sys
from collections import deque

v = int(input())
g, E = [[] for _ in range(v)], []
for line in sys.stdin:
    a, b = map(int, line.split())
    a, b = a-1, b-1
    E.append((a, b))
    g[a].append(b), g[b].append(a)

best_d, best_e, D = 2500, None, []
for (s, e) in E:
    vis, vis2 = [0]*v, [0]*v
    for i in range(v):
        if not vis[i]:
            q = deque([(i, 0)])
            while q:
                u, d = q.popleft()
                if vis[u]: continue
                f, vis[u] = u, 1
                for w in g[f]:
                    if (u == s and w == e) or (u == e and w == s): continue
                    q.append((w, d+1))
            q = deque([(f, 0)])
            while q:
                u, d = q.popleft()
                if vis2[u]: continue
                d2, vis2[u] = d, 1
                for w in g[u]:
                    if (u == s and w == e) or (u == e and w == s): continue
                    q.append((w, d+1))
            D.append(d2)
    a, b = D.pop(), D.pop()
    min_d = max(a, b, (a+1)//2 + (b+1)//2 + 1)
    if min_d < best_d: best_d, best_e = min_d, (s, e)
print(best_d)

s, e = best_e
g[s].remove(e), g[e].remove(s)
print(s+1, e+1)
for x in best_e:
    vis, q = set(), deque([x])
    while q:
        u = q.popleft()
        if u in vis: continue
        vis.add(u)
        for w in g[u]: q.append(w)
    indeg = {i: 0 for i in vis}
    for i in vis:
        for j in g[i]: indeg[j] += 1
    q = deque([i for i in indeg if indeg[i] < 2])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for w in g[u]:
            indeg[w] -= 1
            if indeg[w] == 1: q.append(w)
    print(topo[-1]+1, end=' ')