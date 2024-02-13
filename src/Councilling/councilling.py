import sys; input = sys.stdin.readline
from collections import deque
INF = float('inf')

def BFS(s, t):
    d[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t: break
        for idx in AL[u]:
            v, cap, flow = EL[idx]
            if cap > flow and d[v] == -1:
                d[v] = d[u]+1
                q.append(v)
    return d[t] != -1

def DFS(u, t, f=INF):
    if u == t or f == 0: return f
    for i in range(last[u], len(AL[u])):
        last[u] = i
        v, cap, flow = EL[AL[u][i]]
        if d[v] != d[u]+1: continue
        pushed = DFS(v, t, min(f, cap - flow))
        if pushed:
            EL[AL[u][i]][2] += pushed
            EL[AL[u][i]^1][2] -= pushed
            return pushed
    return 0

def add(u, v, capacity):
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0 if directed else capacity, 0]), AL[v].append(len(EL)-1)

for _ in range(int(input())):
    P = {}; N = {}; C = {}
    Q = [input().strip().split() for _ in range(int(input()))]
    for n, pp, _, *c in Q:
        if n not in N: N[n] = len(N)
        if pp not in P: P[pp] = len(P)
        for cc in c:
            if cc not in C: C[cc] = len(C)
    V = len(P)+len(N)+len(C)+2
    directed = True; source, sink = V-2, V-1; mf = 0
    EL, AL = [], [[] for _ in range(V)]; d = [-1]*V
    for i in C: add(source, C[i], 1)
    for i in P: add(len(C)+len(N)+P[i], sink, (len(N)-1)//2)
    for n, pp, _, *c in Q:
        add(len(C)+N[n], len(C)+len(N)+P[pp], 1)
        for cc in c: add(C[cc], len(C)+N[n], 1)
    while BFS(source, sink):
        last = [0]*V
        f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    if mf != len(C): print('Impossible.')
    else:
        M = {v+len(C):k for k,v in N.items()}
        for c in C:
            for x, _, f in (EL[i] for i in AL[C[c]]):
                if f == 1: print(M[x], c); break
    print()