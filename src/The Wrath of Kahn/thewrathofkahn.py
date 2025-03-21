import sys; input = sys.stdin.readline; from array import *
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
def add(u, v):
    AL[u].append(len(EL)); EL.append([v, 1, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])
n, m = map(int, input().split()); I = array('h', [0]*n); G = [set() for _ in range(n)]
V = 2*n+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
for _ in range(m): a, b = map(int, input().split()); G[a].add(b)
for k in range(n):
    for i in range(n):
        for j in G[k]: k in G[i] and G[i].add(j)
for i in range(n):
    for j in G[i]: I[j] += 1
q = deque(i for i in range(n) if I[i] == 0)
while q:
    u = q.popleft()
    for v in G[u]: I[v] -= 1; I[v] == 0 != q.append(v)
for i in range(n):
    if I[i]:
        mf += 1
        for v in range(n): G[v].discard(i)
        G[i] = set()
for i in range(n):
    for j in G[i]: add(i, j+n)
    add(source, i); add(i+n, sink)
while BFS(source, sink):
    last = [0]*V; f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
print(n-mf)