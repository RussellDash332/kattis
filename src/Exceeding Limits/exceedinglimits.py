import sys; input = sys.stdin.readline
from heapq import *
N, M, T = map(int, input().split())
INF = 1e18; G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w, v = map(int, input().split())
    a -= 1; b -= 1
    G[a] += [(b, w, v)]; G[b] += [(a, w, v)]
def f(x):
    D = [INF]*N; D[0] = 0; pq = [(0, 0)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn, w, v in G[vv]:
            if D[nn] > (new:=dd+w/(v+x)): D[nn] = new; heappush(pq, (new, nn))
    return D[-1]
if f(0) <= T: print(0); exit()
lo, hi = 0, 1e9
while abs(hi-lo)>1e-6:
    if f(mi:=(lo+hi)/2) < T: hi = mi
    else: lo = mi
print(lo)