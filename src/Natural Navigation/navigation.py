import sys; input = sys.stdin.readline
from array import *
N, M, K = map(int, input().split())
G = [[] for _ in range(N)]; R = {}; X = {}
for _ in range(M):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    _, *v = map(int, input().split()); G[b] += [(a, w, v)]
    for c in v:
        if (u:=(a<<10)+c) not in R: R[u] = X[u] = 0
        R[u] += 1
from heapq import *
INF = 10**14; D = array('L', [INF]*N); D[N-1] = 0; pq = [N-1]
while pq:
    dd, vv = divmod(heappop(pq), N)
    if dd != D[vv]: continue
    for nn, ww, cc in G[vv]:
        new = dd+ww
        for c in cc:
            R[u:=(nn<<10)+c] -= 1
            if X[u] < new: X[u] = new
            x = X[u]
            if R[u] == 0 and D[nn] > x: D[nn] = x; heappush(pq, x*N+nn)
Z = D[0]; print(['impossible', Z][Z<INF])