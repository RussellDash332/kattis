import sys; input = sys.stdin.readline; from heapq import *
n, m, x = map(int, input().split()); g = [{} for _ in range(n)]; INF = 10**18
for _ in range(m):
    a, b, w = map(int, input().split())
    if b-1 not in g[a-1]: g[a-1][b-1] = INF
    g[a-1][b-1] = g[b-1][a-1] = min(g[a-1][b-1], w)

def f(k):
    D = [INF]*n; D[0] = 0; pq = [0]
    while pq:
        dv = heappop(pq); dd, vv = dv//n, dv%n
        if dd != D[vv]: continue
        for nn in g[vv]:
            if g[vv][nn] <= k and D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, new*n+nn)
    return D[-1]
M = (100+x)*f(INF); lo, hi = 0, 10**9
while hi-lo>1:
    mi = (lo+hi)//2
    if 100*f(mi) <= M: hi = mi
    else: lo = mi+1
print(lo if 100*f(lo) <= M else lo+1)