import sys; input = sys.stdin.readline; from array import *; from heapq import *
N = int(input()); G = [{} for _ in range(N)]; P = []; C = array('i', [0]*N); c = 0; E = set(); INF = 10**18
for i in range(N):
    j, w = map(int, input().split()); j -= 1
    if j not in G[i]: G[i][j] = 10**9
    G[i][j] = G[j][i] = min(G[i][j], w); E.add((min(i, j), max(i, j)))
for _ in range(int(input())):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    if b not in G[a]: G[a][b] = 10**9
    G[a][b] = G[b][a] = min(G[a][b], w); E.add((min(a, b), max(a, b)))
for _ in range(int(input())): a, b = map(int, input().split()); a -= 1; b -= 1; P.append((a, b))
Z = []; RR = []; VV = []; SS = []; M = [0]*N; D = [0]*N; EE = []
for i in range(N):
    if C[i]: continue
    c += 1; S = [(i, -1)]; T = []; V = []; RR.append([])
    while S:
        u, p = S.pop()
        if C[u]: continue
        C[u] = c; M[u] = len(V); V.append(u)
        if p != -1: T.append((M[p], M[u])); D[u] = D[p]+G[p][u]; E.discard((min(p, u), max(p, u)))
        for v in G[u]: S.append((v, u))
    ST = [[] for _ in range(len(V))]
    for a, b in T: ST[a].append(b); ST[b].append(a)
    VV.append(V); SS.append(ST); EE.append([])
for a, b in E: EE[C[a]-1].append((a, b))
for i in range(len(P)):
    a, b = P[i]
    if C[a] == C[b]: Z.append(0); RR[C[a]-1].append(i)
    else: Z.append(-1)
for r, v, g, e in zip(RR, VV, SS, EE):
    # Tarjan's OLCA
    n = len(v); Q = [[] for _ in range(n)]; R = []; d = array('i', [0]*n); par = array('i', range(n)); d[0] = 1; s = [(0, 0)]
    for i, k in enumerate(r): a, b = P[k]; a = M[a]; b = M[b]; R.append([a, b, -1, k]), Q[a].append(i), Q[b].append(i)
    def find(i):
        if par[i] == i: return i
        par[i] = find(par[i]); return par[i]
    while s:
        ub, p = s.pop(); u = ub//2
        if ub%2:
            for x in Q[u]:
                if R[x][1] == u: R[x][0], R[x][1] = R[x][1], R[x][0]
                R[x][2] = find(R[x][1])
            par[u] = p
        else:
            s.append((ub+1, p))
            for t in g[u]:
                if t != p: d[t] = d[u]+1; s.append((2*t, u))
    for a, b, lca, k in R: Z[k] = D[v[a]]+D[v[b]]-2*D[v[lca]]
    # Dijkstra through each extra edge
    for t, _ in e:
        U = [INF]*n; U[M[t]] = 0; pq = [(0, M[t])]
        while pq:
            dd, vv = heappop(pq)
            if dd != U[vv]: continue
            for nn in G[v[vv]]:
                if U[M[nn]] > (new:=dd+G[v[vv]][nn]): U[M[nn]] = new; heappush(pq, (new, M[nn]))
        for aa, bb, _, k in R: Z[k] = min(Z[k], U[aa]+U[bb])
print(*Z)