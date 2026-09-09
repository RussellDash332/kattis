import sys; input = sys.stdin.readline
from heapq import *
N, M, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w, c = input().split()
    a = int(a); b = int(b); w = int(w)
    G[a] += [(b, w*(c>'K'), w)]; G[b] += [(a, w*(c>'K'), w)]
INF = float('inf')
for _ in range(Q):
    s, t = map(int, input().split())
    D = [(INF, INF)]*N; D[s] = (0, 0); pq = [(0, 0, s)]
    while pq:
        cc, dd, vv = heappop(pq)
        if (cc, dd) != D[vv]: continue
        for nn, c, w in G[vv]:
            if D[nn] > (new:=(cc+c, dd+w)): D[nn] = new; heappush(pq, (*new, nn))
    print(*(D[t] if D[t][0] < INF else ['IMPOSSIBLE']))