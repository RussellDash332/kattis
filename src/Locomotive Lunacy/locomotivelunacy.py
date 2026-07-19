import sys; input = sys.stdin.readline; from heapq import *
N, M = map(int, input().split())
s, t = map(int, input().split())
G = [[] for _ in range(2*N)]
for _ in range(M): u, v, c = map(int, input().split()); G[u] += [(v, c), (v+N, c//2)]; G[u+N] += [(v+N, c)]
D = [Z:=10**18]*2*N; D[s] = 0; pq = [(0, s)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, w in G[vv]:
        if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, (new, nn))
z = min(D[t], D[t+N]); print(z if z < 10**18 else -1)