import sys; input = sys.stdin.readline; from heapq import *
n, m, q = map(int, input().split()); P = [[*map(int, input().split())] for _ in range(n)]; G = [{} for _ in range(n)]; INF = float('inf'); D = [INF]*n; D[0] = 0; pq = [(0, 0)]
for _ in range(m): a, b = map(int, input().split()); x1, y1, z1 = P[a-1]; x2, y2, z2 = P[b-1]; G[a-1][b-1] = G[b-1][a-1] = ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**.25
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in G[vv]:
        if D[nn] > (new:=dd+G[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
for _ in range(q): c, t = map(int, input().split()); x = t/D[c-1]; print('impossible' if x < 2 else (x-(x*x-4)**.5)*D[c-1])