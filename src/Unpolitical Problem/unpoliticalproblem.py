import sys; input = sys.stdin.readline; from heapq import *
N, M = map(int, input().split())
G = [[] for _ in range(N)]; INF = 10**18
for _ in range(M): a, b, w = map(int, input().split()); a -= 1; b -= 1; G[a].append((b, w)); G[b].append((a, w))
R = int(input()); T = [i-1 for i in map(int, input().split())]
K = int(input()); C = [*map(int, input().split())]; P = []
for t in range(K): k, *x = map(int, input().split()); P.append([i-1 for i in x])
def dijkstra(s):
    D = [INF]*N; D[s] = 0; pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn, w in G[vv]:
            if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, (new, nn))
    return D
D = [dijkstra(i) for i in T]; Z = 0
for i in range(K):
    v = []
    for u in P[i]: v.append(min(d[u] for d in D))
    v.sort()
    while len(v) > C[i]: v.pop()
    if v[-1] == INF or len(v) < C[i]: print('MAGA!'); exit()
    Z += sum(v)
print(Z)