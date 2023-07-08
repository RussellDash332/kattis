import sys; input = sys.stdin.readline
from collections import deque
INF = 1e18

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

def add_edge(u, v, capacity):
    EL.append([v, capacity, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

EL = []
for _ in range(int(input())):
    n = int(input())
    b = [input() for _ in range(n)]
    s = [0]*n
    u = set()
    for i in range(n):
        for j in range(i+1, n):
            if b[i][j] == '.': u.add((i, j))
            elif b[i][j] == 'd': s[i] += 1; s[j] += 1
            else: x = 2*int(b[i][j]); s[i] += x; s[j] += 2-x
    w, ss = [], sum(s)
    for i in range(n):
        u2 = set()
        for a, b in list(u):
            if a == i or b == i: u2.add((a, b)), u.discard((a, b))
        s[i] += 2*len(u2); ss += 2*len(u2)
        U = len(u)
        V = U+n+2
        source, sink = V-2, V-1
        AL = [[] for _ in range(V)]; EL.clear()
        for j in range(U): add_edge(source, j, 2)
        for j, (a, b) in enumerate(u): add_edge(j, U+a, 2), add_edge(j, U+b, 2)
        for j in range(U, U+n): add_edge(j, sink, s[i]), add_edge(source, j, s[j-U])
        mf, d = 0, [-1]*V
        while BFS(source, sink):
            last = [0]*V
            f = DFS(source, sink)
            while f: mf += f; f = DFS(source, sink)
            d = [-1]*V
        if mf == ss+2*U: w.append(str(i+1))
        u |= u2; s[i] -= 2*len(u2); ss -= 2*len(u2)
    print(' '.join(w))