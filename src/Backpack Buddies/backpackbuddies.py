import sys; input = sys.stdin.readline
from heapq import *
from array import *
n, m = map(int, input().split()); g = [{} for _ in range(n)]
for _ in range(m): a, b, w = map(int, input().split()); g[a][b] = g[b][a] = min(w, g[a][b] if b in g[a] else 13)
INF = 10**9; D = array('i', [INF]*n); D[0] = 0; pq = [0]
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd == D[vv]:
        for nn in g[vv]:
            new = ((dd+23)//24*24 if dd%24+g[vv][nn]>12 else dd)+g[vv][nn]
            if D[nn] > new: D[nn] = new; heappush(pq, new*n+nn)
day = D[-1]; D = array('i', [INF]*n); D[0] = 0; pq = [0]
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd == D[vv]:
        for nn in g[vv]:
            new = dd+g[vv][nn]+12*(dd%24+g[vv][nn]>12)
            if D[nn] > new: D[nn] = new; heappush(pq, new*n+nn)
print(day-D[-1])