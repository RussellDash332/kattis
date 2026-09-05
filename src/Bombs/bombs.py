N, M, K = map(int, input().split()); N += 1
G = [[] for _ in range(N+1)]
B = [*map(int, input().split())]
for _ in range(M): u, v = map(int, input().split()); G[u] += [v]; G[v] += [u]
from collections import *; INF = 10**9
def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c]); AL[v].append(len(EL)); EL.append([u, 0])
lo, hi = 1, K*N+1
while lo < hi:
    mi = (lo+hi)>>1; V = -~mi*N+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; p = [-1]*V
    add(source, 0, K)
    for i in range(mi):
        for j in range(N):
            add(i*N+j, i*N+N+j, INF)
            for k in G[j]: add(i*N+j, i*N+N+k, 1)
    for i in range(N):
        if B.count(i): add(mi*N+i, sink, B.count(i))
    while True:
        d = [0]*V; d[source] = 1; q = deque([source])
        while q:
            u = q.popleft()
            if u == sink: break
            for idx in AL[u]:
                v, c = EL[idx]
                if c > 0 and d[v] == 0: d[v] = 1; q.append(v); p[v] = idx
        if not d[sink]: break
        f = INF; s = sink
        while s != source: f = min(f, EL[p[s]][1]); s = EL[p[s]^1][0]
        mf += f; s = sink
        while s != source: EL[p[s]][1] -= f; EL[p[s]^1][1] += f; s = EL[p[s]^1][0]
    if mf == K: hi = mi
    else: lo = mi+1
print(lo)