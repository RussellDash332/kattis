import sys
from heapq import *

MOD, L = 10**9 + 7, 10**7 + 3
v, e = map(int, input().split())
g = [[] for _ in range(v)]

for l in sys.stdin:
    a, b, w = map(int, l.split())
    g[a].append(b*L+w), g[b].append(a*L+w)

def dijkstra(s):
    D = [1e18]*v
    D[s], p, pq = 0, [0]*v, [s]
    p[s] = 1
    while pq:
        u = heappop(pq)
        dd, vv = u//L, u%L
        if dd == D[vv]:
            for nnww in g[vv]:
                nn, ww = nnww//L, nnww%L
                if D[nn] > dd + ww:
                    D[nn], p[nn] = dd + ww, p[vv]
                    heappush(pq, D[nn]*L+nn)
                elif D[nn] == dd + ww:
                    p[nn] = (p[nn] + p[vv]) % MOD
    return D, p

(D1, p1), (D2, p2) = dijkstra(v-1), dijkstra(0)
if D1[0] == 1e18:   print(*[-1]*v)
else:               print(*[(p1[i]*p2[i]) % MOD if D1[i] + D2[i] == D1[0] else -1 for i in range(v)])