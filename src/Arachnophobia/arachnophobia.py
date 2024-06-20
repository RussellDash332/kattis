import sys; input = sys.stdin.readline; from heapq import *; from array import *
n, m, T = map(int, input().split()); g = [{} for _ in range(n)]
for _ in range(m): a, b, w = map(int, input().split()); g[a][b] = g[b][a] = w
s, t = map(int, input().split()); INF = 10**9; _, *x = map(int, input().split()); lo, hi = 0, INF; Z = array('i', [INF]*n); pq = [*x]; heapify(pq)
for i in x: Z[i] = 0
while pq:
    dv = heappop(pq); dd, vv = dv//n, dv%n
    if dd != Z[vv]: continue
    for nn in g[vv]:
        if Z[nn] > (new:=dd+g[vv][nn]): Z[nn] = new; heappush(pq, new*n+nn)

def f(k):
    if Z[s] < k: return 0
    D = array('i', [INF]*n); D[s] = 0; pq = [s]
    while pq:
        dv = heappop(pq); dd, vv = dv//n, dv%n
        if dd != D[vv]: continue
        for nn in g[vv]:
            if Z[nn] >= k and D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, new*n+nn)
    return D[t] <= T

while hi-lo>1:
    mi = (lo+hi)//2
    if f(mi): lo = mi
    else: hi = mi-1
print(hi if f(hi) else hi-1)