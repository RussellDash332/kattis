from heapq import *; import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m, _ = map(int, input().split())
g = [[] for _ in range(n)]
INF = 10**18; D = [INF]*n; pq = []
for k in map(int, input().split()): D[k-1] = 0; pq.append((0, k-1))
heapify(pq)
for _ in range(m): a, b, w = map(int, input().split()); g[b-1].append((a-1, w))
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, w in g[vv]:
        if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, (new, nn))
Z = max(D); print(Z if Z < INF else 'danger')