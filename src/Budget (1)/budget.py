import sys; input = sys.stdin.readline; from collections import deque; INF = float('inf')

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
    EL.append([v, c, 0]), AL[u].append(len(EL)-1), EL.append([u, 0, 0]), AL[v].append(len(EL)-1)

for _ in range(int(input())):
    input()
    ok = 1; R, C = map(int, input().split()); Rs = [*map(int, input().split())]; Cs = [*map(int, input().split())]; U = [[INF]*C for _ in range(R)]; L = [[0]*C for _ in range(R)]
    for _ in range(int(input())):
        a, b, c, v = input().split(); a = [int(a)-1]; b = [int(b)-1]; v = int(v)
        if a[0] == -1: a = [*range(R)]
        if b[0] == -1: b = [*range(C)]
        for i in a:
            for j in b:
                if c != '<': L[i][j] = max(L[i][j], v+(c=='>'))
                if c != '>':U[i][j] = min(U[i][j], v-(c=='<'))
    for i in range(R):
        for j in range(C):
            U[i][j] -= L[i][j]; Rs[i] -= L[i][j]; Cs[j] -= L[i][j]
            if U[i][j] < 0 or Rs[i] < 0 or Cs[j] < 0: ok = 0; break
    if not ok: print('IMPOSSIBLE\n'); continue
    M = [[0]*C for _ in range(R)]; V = R+C+2; source, sink = V-2, V-1; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V
    for i in range(R):
        add(source, i, Rs[i])
        for j in range(C): add(i, R+j, U[i][j])
    for i in range(C): add(R+i, sink, Cs[i])
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
    if mf != sum(Rs): print('IMPOSSIBLE\n'); continue
    else:
        for i in range(len(EL)//2):
            if (r:=EL[2*i+1][0]) < R and (c:=EL[2*i][0]-R) < C: M[r][c] = EL[2*i][2]+L[r][c]
        for x in M: print(*x)
        print()