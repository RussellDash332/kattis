from collections import *; INF = 10**9
M, N, K = map(int, input().split())

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

V = M+N+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
for i in range(N): add(i+M, sink, 1)
for _ in range(K): x, y = map(int, input().split()); add(x-1, y+M-1, 1)
for i in range(M): add(source, i, 1)
while BFS(source, sink):
    last = [0]*V; f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
Z = mf
for i in range(M):
    snap = [EL[x][2] for x in AL[i]]
    add(source, i, 2); inc = 0
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: inc += f; f = DFS(source, sink)
        d = [-1]*V
    EL.pop(); EL.pop(); AL[i].pop(); AL[source].pop()
    for j, x in enumerate(AL[i]):
        if EL[x][2] != snap[j]: s = EL[x][0]-M; EL[2*s][2] = EL[2*s+1][2] = 0
        EL[x][2] = snap[j]; EL[x^1][2] = -snap[j]
    Z = max(Z, mf+inc)
    if inc > 1: break
print(Z)