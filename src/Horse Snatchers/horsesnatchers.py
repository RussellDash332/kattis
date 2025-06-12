import sys; input = sys.stdin.readline; from heapq import *
n, k, m = map(int, input().split()); T, w = map(int, input().split()); s = {*map(lambda x: int(x)-1, input().split())}; g = [{} for _ in range(n)]; INF = float('inf'); Z = []
for _ in range(m): a, b, d = map(int, input().split()); g[a-1][b-1] = g[b-1][a-1] = d
D = [INF]*n; D[0] = 0; pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv] or vv in s: continue
    for nn in g[vv]:
        if D[nn] > (new:=dd+g[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
E = [INF]*n; E[-1] = 0; pq = [(0, n-1)]
while pq:
    dd, vv = heappop(pq)
    if dd != E[vv]: continue
    for nn in g[vv]:
        if E[nn] > (new:=dd+g[vv][nn]): E[nn] = new; heappush(pq, (new, nn))
for i in range(n):
    if D[i] != INF and E[i] < T*w: Z.append(D[i]/(T-E[i]/w))
if Z: v = min(Z); print(['No horse needed!', v][v > w])
else: print(['No horse needed!', 'Impossible'][T*w < E[0]])