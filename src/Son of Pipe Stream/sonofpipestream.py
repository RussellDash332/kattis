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
def add(u, v, c):
    AL[u].append(len(EL)); EL.append([v, c, 0]); AL[v].append(len(EL)); EL.append([u, 0, 0])
def reset():
    global d, mf
    d = [-1]*V; mf = 0
    for e in EL: e[2] = 0
def pop():
    AL[EL.pop()[0]].pop(); AL[EL.pop()[0]].pop()
def run():
    global d, mf, last
    while BFS(source, sink):
        last = [0]*V; f = DFS(source, sink)
        while f: mf += f; f = DFS(source, sink)
        d = [-1]*V
n, p, v, a = map(float, input().split()); n = int(n); p = int(p)
V = n+1; source = n; sink = 2; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V; E = []
for _ in range(p): j, k, c = map(int, input().split()); j -= 1; k -= 1; add(j, k, c); add(k, j, c); E.append((j, k)); E.append((k, j))
add(source, 1, INF); run(); maxW = mf; # water only
add(source, 0, INF); run(); minF = mf-maxW; pop(); pop(); f1 = [e[1]-e[2] for e in EL[::2]]; reset() # water then flubber
add(source, 0, INF); run(); maxF = mf # flubber only
add(source, 1, INF); run(); pop(); pop(); f2 = [e[1]-e[2] for e in EL[::2]] # flubber then water
F = max(minF, min(maxF, a*mf)); W = mf-F
if minF == maxF: p1 = p2 = .5
else: p2 = (F-minF)/(maxF-minF); p1 = 1-p2
C = [EL[2*i][1]-p1*f1[i]-p2*f2[i] for i in range(len(EL)//2)]; EL, AL = [], [[] for _ in range(V)]; mf = 0; d = [-1]*V; M = [[0]*V for _ in range(V)]
for (j, k), c in zip(E, C): M[j][k] += c; M[k][j] -= c
for j, k in sorted(E): M[j][k] > 0 and add(j, k, M[j][k])
add(source, 0, F); run(); pop(); M = [[(0, 0)]*V for _ in range(V)]
for i in range(len(EL)//2): w, c, x = EL[2*i]; u, d, y = EL[2*i+1]; M[u][w] = ((d-y)/v, c-x); M[w][u] = ((y-d)/v, x-c)
for j, k in E[::2]: print(*map(float, M[j][k]))
print((F/v)**a*W**(1-a))