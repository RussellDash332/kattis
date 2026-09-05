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
for _ in range(int(input())):
    W, P = map(int, input().split())
    V = W+P+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    A = []; w = F = 0; B = []
    for i in range(W):
        x, y, f, r = map(int, input().split())
        A += [(x, y, r, f)]
    for i in range(P):
        x, y, f = map(int, input().split())
        if (x-A[0][0])**2+(y-A[0][1])**2 <= A[0][2]**2: w += f; continue
        B += [(x, y, f, i)]
    w += A[0][3]
    for i in range(1, W):
        add(i, sink, w-A[i][3])
        if w<A[i][3]: print('Lonesome Willy'); break
    else:
        for x, y, f, j in B:
            z = 0
            for i in range(W):
                x2, y2, r, _ = A[i]
                if (x-x2)**2+(y-y2)**2 <= r*r: add(j+W, i, INF); z = 1
            if z: add(source, j+W, f); F += f
        while BFS(source, sink):
            last = [0]*V; f = DFS(source, sink)
            while f: mf += f; f = DFS(source, sink)
            d = [-1]*V
        print('SLuointeisnogm eS uWciclelsys'[mf<F::2])