import sys; input = sys.stdin.readline
from collections import deque; INF = 10**18
def BFS(s, t):
    d[s] = 0; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1: d[v] = d[u]+1; q.append(v)
    return d[t] != -1
def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i; v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap-flow))
        if pushed: EL[AL[u][i]][2] += pushed; EL[AL[u][i]^1][2] -= pushed; return pushed
    return 0
def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])
D, A = map(int, input().split()); H = {}; E = []; L = []; M = []
for _ in range(A): ty, s, q = input().split(); H[ty] = (int(s), _); L.append(int(q))
for i in range(D):
    t, s, q, _, *r = input().strip().split(); r = {*r}; s = int(s); M.append(int(q))
    for ty in H:
        if ty in r: continue
        if H[ty][0] >= s: E.append((H[ty][1], i+A))
V = D+A+2; source, sink = V-2, V-1; S = sum(M); lo, hi = 0, 10**12; EL, AL = [], [[] for _ in range(V)]
for a, b in E: add(a, b, INF)
for i in range(A): add(source, i, L[i])
while lo < hi:
    mf = 0; d = [-1]*V; mi = (lo+hi)//2
    for e in EL: e[2] = 0
    for i in range(D): add(i+A, sink, mi*M[i])
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    if mf != S*mi: hi = mi
    else: lo = mi+1
    for _ in range(D): u = EL.pop()[0]; v = EL.pop()[0]; AL[u].pop(); AL[v].pop()
print(max(lo-1, 0))