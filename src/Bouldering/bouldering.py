h, w, r, S = map(int, input().split()); T = 0
M = [input() for _ in range(h)]
R = {}
for i in range(h):
    for j in range(w):
        if '0'<M[i][j]<='9': R[(i, j)] = (len(R), t:=int(M[i][j])); T += t
N = len(R); S -= R[max(R)][1]; S = min(S, T)
if S < 0: print('impossible'); exit()
G = [[] for _ in range(N)]
K = [(di, dj, (di*di+dj*dj)**.5) for di in range(r+1) for dj in range(-r, r+1) if (di or dj) and di*di+dj*dj<=r*r]
for i, j in R:
    k, x = R[(i, j)]
    for di, dj, w in K:
        if (i+di, j+dj) in R: m, y = R[(i+di, j+dj)]; G[k] += [(m, y, w)]; G[m] += [(k, x, w)]
from heapq import *
INF = 10**9; D = [INF]*N*-~S; D[-1] = 0; pq = [(0, N*-~S-1)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    ss, v = divmod(vv, N)
    for nn, ds, w in G[v]:
        if ss>=ds and D[u:=(ss-ds)*N+nn] > (new:=dd+w): D[u] = new; heappush(pq, (new, u))
Z = min(D[::N]); print(['impossible', Z][Z<INF])