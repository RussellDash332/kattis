import sys
from heapq import *

n, m, x, y = map(int, input().split())
g = {}
for line in sys.stdin:
    a, b, w, c = map(int, line.split())
    for _ in range(2):
        a, b = b, a
        if a not in g:
            g[a] = {b: [w, c]}
        else:
            g[a][b] = [w, c]

def dijkstra(D, s):
    D[s] = (0, 0, 0)
    pq = [(0, 0, 0, s)]
    while pq:
        tt, ss, dd, vv = heappop(pq)
        if (tt, ss, dd) == D[vv] and vv in g:
            for nn in g[vv]:
                w, c = g[vv][nn]
                if nn not in D or D[nn] > (tt + c//2, ss + c%2, dd + w):
                    D[nn] = (tt + c//2, ss + c%2, dd + w)
                    heappush(pq, (*D[nn], nn))
D = {}
dijkstra(D, x)
if y not in D:  print('IMPOSSIBLE')
else:           print(*D[y][::-1])