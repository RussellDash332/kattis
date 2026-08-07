import sys; input = sys.stdin.readline; print = sys.stdout.write; from heapq import *
N, M, Q = map(int, input().split()); E = []; g, gt = [[] for _ in range(N)], [[] for _ in range(N)]; INF = 10**18
for _ in range(M): a, b, t = map(int, input().split()); a -= 1; b -= 1; E += [(a, b, t)]; g[a] += [b]; gt[b] += [a]
top, vis, scc = [], set(), [0]*N; cnt = 0
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis.add(u)
            if not t: scc[u] = cnt
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(N):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: cnt += DFS(i, False)
R = [[] for _ in range(cnt)]; S = [[] for _ in range(cnt)]; B = 0; G = [[] for _ in range(cnt)]
for i in range(N): R[scc[i]].append(i)
for a, b, w in E:
    if scc[a] == scc[b]: S[scc[a]].append((a, b, w))
    else: G[scc[a]].append(scc[b])
for i in range(cnt):
    V = len(R[i]); H = {e:i for i,e in enumerate(R[i])}; K = [(H[a], H[b], w) for a, b, w in S[i]]; D = [INF]*V; D[0] = 0
    for _ in range(V-1):
        for a, b, w in K:
            if D[a] < INF and D[b] > D[a]+w: D[b] = D[a]+w
    for a, b, w in K:
        if D[b] > D[a]+w: B |= 1<<i; break
T = [1<<i for i in range(cnt)]; U = [1<<i for i in range(cnt)]
for i in range(cnt-1, -1, -1):
    for j in G[i]: T[i] |= T[j]
for i in range(cnt):
    for j in G[i]: U[j] |= U[i]
D = []; F = [[] for _ in range(N)]
for a, b, w in E:
    if B&(1<<scc[a])<1>B&(1<<scc[b]): F[a] += [(b, w)]
for s in range(N):
    d = [INF]*N; d[s] = 0; pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd != d[vv]: continue
        for nn, w in F[vv]:
            if d[nn] > (new:=dd+w): d[nn] = new; heappush(pq, (new, nn))
    D.append(d)
for _ in range(Q):
    a, b = map(int, input().split()); a -= 1; b -= 1
    if T[scc[a]]&(1<<scc[b]) < 1: print('engin leid\n')
    elif T[scc[a]]&U[scc[b]]&B: print('nogu hlytt\n')
    else: print(str(D[a][b])+'\n')