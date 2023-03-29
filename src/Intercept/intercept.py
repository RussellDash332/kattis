import sys
from heapq import *
v, e = map(int, input().split())
g1, g2 = [{} for _ in range(v)], [{} for _ in range(v)]
for l in sys.stdin:
    if e > 0:
        a, b, w = map(int, l.split())
        g1[a][b] = g2[b][a] = w
        e -= 1
    else:
        s, t = map(int, l.split())

def dijkstra(pq, D, g):
    while pq:
        dd, vv, pp = heappop(pq)
        if dd == D[vv][0] and pp == D[vv][1]:
            for nn in g[vv]:
                if nn not in D or D[nn][0] > dd + g[vv][nn]:
                    D[nn] = (dd + g[vv][nn], pp)
                    heappush(pq, (D[nn][0], nn, D[nn][1]))
                elif D[nn][0] == dd + g[vv][nn]:
                    D[nn] = (dd + g[vv][nn], D[nn][1] + pp)
                    heappush(pq, (D[nn][0], nn, D[nn][1]))

D1, D2, pq1, pq2 = {s: (0, 1)}, {t: (0, 1)}, [(0, s, 1)], [(0, t, 1)]
dijkstra(pq1, D1, g1), dijkstra(pq2, D2, g2)
T, S = D1[s][1]*D2[s][1], D1[t][0]
for i in range(v):
    if i in D1 and i in D2 and D1[i][0]+D2[i][0] == S and D1[i][1]*D2[i][1] == T: print(i, end=' ')