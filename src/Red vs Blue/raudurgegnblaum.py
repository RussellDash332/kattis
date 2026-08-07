import sys; input = sys.stdin.readline; from heapq import *
N, M = map(int, input().split())
B, S, R = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M): x, y, p = map(float, input().split()); x = round(x)-1; y = round(y)-1; G[x] += [(y, p)]*(p>0)
H = []; INF = 10**9
for s in range(N):
    D = [INF]*N; D[s] = R; pq = [(R, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn, p in G[vv]:
            new = (dd+S)/p
            if D[nn] > new: D[nn] = new; heappush(pq, (new, nn))
    H += [[i-R for i in D]]
D = [INF]*N; D[0] = 0; pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in range(N):
        new = dd+B+H[vv][nn]
        if D[nn] > new: D[nn] = new; heappush(pq, (new, nn))
print(D[-1]-B)