N, M, *_ = map(int, input().split())
W = {*map(int, input().split())}
F = {*map(int, input().split())}
G = [[] for _ in range(4*N)]; n = 4*N
for _ in range(M):
    a, b, w = map(int, input().split())
    for i in range(4): G[4*a+i] += [(4*b+(i|(b in W)|(2*(b in F))), w)]; G[4*b+i] += [(4*a+(i|(a in W)|(2*(a in F))), w)]

from heapq import *; INF = float('inf'); D = [INF]*n; D[s:=(0 in W)+2*(0 in F)] = 0; pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, w in G[vv]:
        if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, (new, nn))
print(D[3])