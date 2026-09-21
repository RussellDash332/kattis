from heapq import *
N, M, W = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M): a, b, w = map(int, input().split()); G[a-1] += [(b-1, -w)]
D = [10**9]*N; D[0] = 0; pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, w in G[vv]:
        if D[nn] > (new:=max(dd+w, -W)): D[nn] = new; heappush(pq, (new, nn))
print(-D[-1])