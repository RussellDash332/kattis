import sys; input = sys.stdin.readline
N, M = map(int, input().split())
G = {}
for _ in range(M):
    a, b, w = map(int, input().split())
    if w not in G: G[w] = []
    G[w].append((a-1, b-1))
from heapq import *
INF = 10**18; Z = []
for r in (0, 1):
    D = [INF]*N; D[0] = 0
    for w in sorted(G, reverse=r):
        g = {}
        for a, b in G[w]:
            if a not in g: g[a] = []
            g[a].append(b)
        L = {i:D[i] for i in g if D[i]<INF}; pq = [(d, i) for i, d in L.items()]
        while pq:
            dd, vv = heappop(pq)
            if vv not in L: L[vv] = INF
            if L[vv] != dd: continue
            if vv not in g: continue
            for nn in g[vv]:
                if nn not in L or L[nn] > dd+w: L[nn] = dd+w; heappush(pq, (dd+w, nn))
        for i, d in L.items(): D[i] = min(D[i], d)
    Z.append(D[-1])
print(min(Z) if min(Z) < INF else 'impossible')