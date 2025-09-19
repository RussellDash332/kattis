import sys; input = sys.stdin.readline
n = int(input()); t = [*map(int, input().split())]; G = [{} for _ in range(n)]
for _ in range(n-1): a, b, w = map(int, input().split()); G[a:=a-1][b:=b-1] = w; G[b][a] = w
T = [{} for _ in range(n)]; Q = [(0, -1)]; V = set()
while Q:
    u, p = Q.pop()
    if u in V: continue
    if ~p: T[p][u] = G[p][u]
    V.add(u); Q.extend((v, u) for v in G[u])
Q = [(0, 0)]; A = B = 0; Z = [0]*n; S = [1]*n; U = [*t]
for u, d in Q:
    A += d; B += t[u]*d
    for v in T[u]: Q.append((v, d+T[u][v]))
while Q: u, _ = Q.pop(); S[u] += sum(S[v] for v in T[u]); U[u] += sum(U[v] for v in T[u])
Q = [(0, A, B)]
while Q:
    u, a, b = Q.pop(); Z[u] = t[u]*a+b
    for v in T[u]: Q.append((v, a+T[u][v]*(n-2*S[v]), b+T[u][v]*(U[0]-2*U[v])))
print(*Z)