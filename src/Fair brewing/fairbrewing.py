from collections import deque; INF = 10**18; from array import *
import sys; input = sys.stdin.readline; from bisect import *
K, N, M = map(int, input().split()); E = []
for _ in range(M): a, b, c = map(int, input().split()); E.append((c, a-1, b-1))
V = 2*K+N+2; source, sink = V-2, V-1; E.sort()
def f(l):
    def add(u, v, d=0): AL[u].append(len(EL)); EL.append([v, 1]); AL[v].append(len(EL)); EL.append([u, d])
    EL, AL = [], [[] for _ in range(V)]; mf = 0; p = array('i', [-1]*V)
    for c, a, b in E[bisect(E, (l, -1, -1)):]: add(a, b, 1)
    for i in range(K): add(source, i); add(K+i, sink)
    while True:
        d = array('i', [0]*V); d[source] = 1; q = deque([source])
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
    return mf==K
lo, hi = 0, 10**9
while hi-lo>1:
    if f(mi:=(lo+hi)//2): lo = mi
    else: hi = mi-1
ans = hi if f(hi) else hi-1
print(ans or 'Expand brewery')