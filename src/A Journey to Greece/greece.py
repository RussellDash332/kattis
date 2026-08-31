import sys; input = sys.stdin.readline
from heapq import *; from array import *
N, P, M, U, T = map(int, input().split()); INF = 10**9
B = {0}; G = [[] for _ in range(N)]
for _ in range(P):
    v, t = map(int, input().split())
    U -= t; B.add(v)
for _ in range(M):
    s, d, t = map(int, input().split())
    G[s] += [(d, t)]; G[d] += [(s, t)]
def dijkstra(s):
    D = array('i', [INF]*N); D[s] = 0; pq = [s]
    while pq:
        dv = heappop(pq); dd, vv = dv//N, dv%N
        if dd != D[vv]: continue
        for nn, w in G[vv]:
            if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, new*N+nn)
    return D
B = sorted(B); E = [dijkstra(v) for v in B]
G = [[e[b] for b in B] for e in E]

from itertools import combinations
def tsp(G):
    n = len(G); C = [[INF for _ in range(2*n)] for _ in range(1<<n)]; C[1][0] = 0
    for s in range(1, n):
        for S in combinations(range(1, n), s):
            k = 1
            for i in S: k += 1<<i
            for i in S:
                C[k][i] = min(C[k][i], C[k^(1<<i)][0]+G[0][i]); C[k][i+n] = min(C[k][i+n], C[k^(1<<i)][0]+T, C[k^(1<<i)][n]+G[0][i])
                for j in S:
                    if j != i: C[k][i] = min(C[k][i], C[k^(1<<i)][j]+G[j][i]); C[k][i+n] = min(C[k][i+n], C[k^(1<<i)][j]+T, C[k^(1<<i)][j+n]+G[j][i])
    k = (1<<n)-1; return min(C[k][i]+G[i][0] for i in range(n)), min(C[k][i+n]+G[i][0] for i in range(n))

z, y = tsp(G)
if z <= U: print('possible without taxi'); exit()
print(['possible with taxi', 'impossible'][y>U])