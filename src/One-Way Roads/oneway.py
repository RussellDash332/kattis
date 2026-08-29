from collections import *; INF = float('inf')
N = int(input())
M = int(input())
V = N+M+2; source, sink = V-2, V-1
E = []
for _ in range(M): a, b = map(int, input().split()); E += [(a-1, b-1)]
def f(x):
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
    EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    for t in range(M): a, b = E[t]; add(source, N+t, 1); add(N+t, a, 1); add(N+t, b, 1)
    for i in range(N): add(i, sink, x)
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    return mf == M
lo, hi = 0, N
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)