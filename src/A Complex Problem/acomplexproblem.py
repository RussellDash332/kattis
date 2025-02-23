import sys; input = sys.stdin.readline
M, N = map(int, input().split()); R = {}; S = []; SS = []
for _ in range(M):
    a, b = input().strip().split()
    if a not in R: R[a] = len(R)
    if b not in R: R[b] = len(R)
    S.append((R[a], R[b]))
for _ in range(N):
    a, b = input().strip().split()
    if a not in R: R[a] = len(R)
    if b not in R: R[b] = len(R)
    SS.append((R[a], R[b]))
V = len(R); G = [[] for _ in range(V)]; Gt = [[] for _ in range(V)]
for a, b in S+SS: G[a].append(b); Gt[b].append(a)
top, vis, scc = [], {}, 0
def DFS(s, t):
    stack = [2*s]; a = G if t else Gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis[u] = scc
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(V):
    if i not in vis: DFS(i, True)
vis = {}
for i in top[::-1]:
    if i not in vis: scc += DFS(i, False)
D = [{} for _ in range(scc)]; X = [0]*scc
for a, b in S: D[vis[a]][vis[b]] = 0
for a, b in SS: D[vis[a]][vis[b]] = 1
for i in range(scc-1, -1, -1):
    for j in D[i]: X[i] = max(X[i], D[i][j]+X[j])
print(max(X)+1, scc)