import sys; input = sys.stdin.readline
from collections import deque
INF = float('inf')

def can(x):
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
            pushed = DFS(v, t, min(f, cap - flow))
            if pushed: EL[AL[u][i]][2] += pushed; EL[AL[u][i]^1][2] -= pushed; return pushed
        return 0

    def add(u, v, c):
        EL.append([v, c, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

    EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    for i in range(n):
        add(source, i, A[i]); add(i, i+n, A[i])
        for j in G[i]: add(i, j+n, INF)
    for i in range(n): A[i] and add(i+n, sink, (1, x)[i in B])
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    return mf >= len(B)*x+C

for _ in range(int(input())):
    n = int(input()); A = [*map(int, input().split())]; G = [[] for _ in range(n)]; V = 2*n+2; source, sink = V-2, V-1; B = set()
    for i in range(n):
        s = input()
        for j in range(n):
            if s[j] == 'Y': G[i].append(j)
    for i in range(n):
        for j in G[i]:
            if A[i] > 0 and A[j] == 0: B.add(i)
    C = sum(i>0 for i in A)-len(B); lo, hi = 0, sum(A)
    while hi-lo>1:
        mi = (lo+hi)//2
        if can(mi): lo = mi
        else: hi = mi-1
    print(hi if can(hi) else hi-1)