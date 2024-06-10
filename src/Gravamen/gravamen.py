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

    EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V; mtc = [-1]*L
    for i in range(L): j, k = G[i]; add(i, j, 1); add(i, k, 1); add(source, i, 1)
    for i in range(L, L+I+C): add(i, sink, x)
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    for i in range(0, len(EL), 2):
        if EL[i+1][0] < L and EL[i][2]: mtc[EL[i+1][0]] = EL[i][0]
    return mf == L, mtc

I, C, L = map(int, input().split()); V = I+C+L+2; source, sink = V-2, V-1; G = []; lo, hi = 0, L
for _ in range(L): a, b = map(int, input().split()); G.append((L+a-1, L+I+b-1))
while hi-lo>1:
    mi = (lo+hi)//2
    if can(mi)[0]: hi = mi
    else: lo = mi+1
mtc = can(lo if can(lo)[0] else lo+1)[1]
for i in range(L):
    if mtc[i] < L+I: print('INDV', mtc[i]-L+1)
    else: print('CORP', mtc[i]-L-I+1)