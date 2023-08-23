from heapq import *
from array import *
import sys; input = sys.stdin.readline
def dijkstra(D, s):
    D[s] = 0; pq = [s]
    while pq:
        dv = heappop(pq); dd, vv = dv//n, dv%n
        if dd != D[vv]: continue
        for nn in g[vv]:
            if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, new*n+nn)
def tsp(G):
    n = len(G); C = [array('i', [10**9 for _ in range(n)]) for _ in range(1<<n)]; C[1][0] = 0
    for s in range(1<<n):
        for i in range(n):
            for j in range(n):
                if s&(1<<j) == 0: s2 = s+(1<<j); C[s2][j] = min(C[s][i]+G[i][j], C[s2][j])
    return C
for _ in range(int(input())):
    n, m = map(int, input().split())
    g = [{} for _ in range(n)]
    for _ in range(m): a, b, l = map(int, input().split()); g[a][b] = g[b][a] = l
    ii = int(input()); p = [0, *map(int, input().split())]; aa = int(input()); D = []
    for s in p: D.append(array('i', [10**9 for _ in range(n)])), dijkstra(D[-1], s)
    k = tsp([array('i', [D[i][p[j]] for j in range(len(p))]) for i in range(len(p))]); best = 0
    print(max((bin(bm-1).count('1') for bm in range(1<<len(p)) if min(k[bm][i]+D[i][0] for i in range(len(p))) <= aa), default=0))