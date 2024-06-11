from collections import deque
INF = float('inf'); B = int(input()); H = int(input()); R, C = map(int, input().split()); S = [[*map(int, input())] for _ in range(R)]; Z = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        for k in range(R):
            for l in range(C): Z[i][j] += S[k][l]/((k-i)**2+(l-j)**2+H*H)
        Z[i][j] = int(Z[i][j] >= B)

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

def add(u, v, c, d=1):
    EL.append([v, c, 0]), AL[u].append(len(EL)-1), EL.append([u, 0 if d else c, 0]), AL[v].append(len(EL)-1)

V = R*C+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
for i in range(R):
    for j in range(C):
        if Z[i][j] == 0: add(i*C+j, sink, INF)
add(source, 0, INF); add(source, C-1, INF); add(source, R*C-R, INF); add(source, R*C-1, INF)
for i in range(1, R-1): add(source, i*C, INF); add(source, i*C+(C-1), INF)
for i in range(1, C-1): add(source, i, INF); add(source, (R-1)*C+i, INF)
for i in range(R):
    for j in range(C-1): add(i*C+j, i*C+j+1, k:=(11, 43)[Z[i][j]&Z[i][j+1]], 0)
for i in range(R-1):
    for j in range(C): add(i*C+j, i*C+j+C, k:=(11, 43)[Z[i][j]&Z[i+1][j]], 0)
while BFS(source, sink):
    last = [0]*V; f = DFS(source, sink)
    while f: mf += f; f = DFS(source, sink)
    d = [-1]*V
print(mf)