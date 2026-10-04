from heapq import *
N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
W = {0}
for _ in range(M): u, v, w = map(int, input().split()); G[u] += [(v, w)]; W.add(w)
D = [-1]*N; D[0] = 0; q = [0]
for u in q:
    if D[u] == K: continue
    for v, w in G[u]:
        if D[v]<0: D[v] = D[u]+1; q.append(v)
if -1 < D[-1] <= K: print(0); exit()
def f(k):
    INF = 10**18; D = [INF]*N; D[0] = 0; pq = [(0, 0)]
    while pq:
        d, u = heappop(pq)
        if d != D[u]: continue
        if u == N-1: return d
        for v, w in G[u]:
            new = d+max(w, k)
            if D[v] > new: D[v] = new; heappush(pq, (new, v))
    return D[-1]
Z = min(f(k)-K*k for k in W); print(Z if Z<10**17 else -1)