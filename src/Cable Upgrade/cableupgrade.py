import sys; input = sys.stdin.readline
from heapq import *
n, m, s, t = map(int, input().split()); s -= 1; t -= 1
G = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    G[a] += [(b, w)]; G[b] += [(a, w)]
INF = float('inf'); D = [INF]*2*n; D[2*s] = 0; pq = [(0, 2*s)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    v, b = vv//2, vv%2
    for nn, w in G[v]:
        if D[u:=2*nn+b] > (new:=dd+w): D[u] = new; heappush(pq, (new, u))
        if b < 1 and D[u:=2*nn+1] > dd: D[u] = dd; heappush(pq, (dd, u))
z = min(D[2*t], D[2*t+1]); print(z if z < INF else 'IMPOSSIBLE')