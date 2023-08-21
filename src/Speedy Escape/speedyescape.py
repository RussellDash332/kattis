import sys; input = sys.stdin.readline
from heapq import *
n, m, e = map(int, input().split())
D = [[float('inf')]*n for _ in range(n)]
for _ in range(m): a, b, l = map(int, input().split()); D[a-1][b-1] = D[b-1][a-1] = min(D[a-1][b-1], l)
ex = [*map(lambda x: int(x)-1, input().split())]
b, p = map(lambda x: int(x)-1, input().split())
G = [{} for _ in range(n)]
for i in range(n):
    for j in range(n):
        if D[i][j] != float('inf'): G[i][j] = D[i][j]
for i in range(n): D[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n): D[i][j] = min(D[i][j], D[i][k]+D[k][j])
pp = D[p]; E = [(float('inf'), float('inf')) for _ in range(n)]; E[b] = (0, 0)
pq = [(0, 0, b)]
while pq:
    ss, dd, vv = heappop(pq)
    if (ss, dd) == E[vv]:
        for nn in G[vv]:
            if pp[nn] and E[nn] > (new:=(max((dd + G[vv][nn])/pp[nn], ss), dd + G[vv][nn])): E[nn] = new; heappush(pq, (*new, nn))
k = min(160*E[x][0] for x in ex)
print('IMPOSSIBLE' if k > 1e9 else k)