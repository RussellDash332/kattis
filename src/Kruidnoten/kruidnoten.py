import sys; input = sys.stdin.readline; from heapq import *
n, m, k = map(int, input().split())
G = [{} for _ in range(n)]; P = [0]*n; INF = float('inf')
for _ in range(m): a, b, w = map(int, input().split()); G[a-1][b-1] = G[b-1][a-1] = w
for _ in range(k): v, p = map(float, input().split()); P[int(v)-1] = p
D = [INF]*n; D[0] = 0; pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn in G[vv]:
        if D[nn] > (new:=dd+G[vv][nn]): D[nn] = new; heappush(pq, (new, nn))
E = [INF]*n; E[-1] = 0; pq = [(0, n-1)]
while pq:
    dd, vv = heappop(pq)
    if dd != E[vv]: continue
    for nn in G[vv]:
        if E[nn] > (new:=dd+G[vv][nn]): E[nn] = new; heappush(pq, (new, nn))
V = sorted(range(n), key=lambda x: D[x]+E[x])
X = [P[V[0]]]; Y = [1-P[V[0]]]
for i in range(1, n): X.append(Y[-1]*P[V[i]]); Y.append(Y[-1]*(1-P[V[i]]))
print(sum(X[i]*(D[V[i]]+E[V[i]]) for i in range(n)) if max(P) == 1 else 'impossible')