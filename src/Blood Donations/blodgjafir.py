# overkill with flow
from collections import deque; INF = float('inf')
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
def add(u, v, c): AL[u].append(len(EL)); EL.append([v, c, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])
from collections import *
N = int(input())
S = input().split()
M = int(input())
T = input().split()
simple = S[0][-1] not in '+-'
S = Counter(S)
T = Counter(T)
K = ['O', 'A', 'B', 'AB']
if simple:
    V = 10; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    for i in range(4):
        add(source, i, S[K[i]]); add(V-6+i, sink, T[K[i]])
        for j in range(4):
            if K[i].replace('O', '') in K[j]: add(i, V-6+j, INF)
else:
    V = 18; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    for i, x in enumerate(i+v for i in K for v in '+-'):
        add(source, i, S[x]); add(V-10+i, sink, T[x])
        for j, y in enumerate(i+v for i in K for v in '+-'):
            if x[:-1].replace('O', '') in y[:-1] and x[-1] >= y[-1]: add(i, V-10+j, INF)
while BFS(source, sink):
    last = [0]*V; f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
print('NJeeibbbb'[mf==M::2])