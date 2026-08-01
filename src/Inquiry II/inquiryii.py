V, m = map(int, input().split())
G = [set() for _ in range(V)]
for _ in range(m): a, b = map(int, input().split()); G[a-1].add(b-1); G[b-1].add(a-1)
g = [[] for _ in range(V)]
Q = [0]; v = [1]+[0]*~-V
for u in Q:
    for w in G[u]:
        if v[w]<1: v[w] = 1; Q += [w]; g[u] += [w]
E = []
for u in range(V):
    for v in g[u]: G[u].discard(v); G[v].discard(u)
for u in range(V):
    for v in G[u]:
        if u < v: E += [(u, v)]
Z = 0; Q = Q[::-1]; L = len(E)
for bm in range(1<<L):
    D = {E[i][(1<<i)&bm>0] for i in range(L)}; A = [0]*V; B = [0]*V
    for i in Q: A[i] = sum(max(A[j], B[j]) for j in g[i]); B[i] = -10**9 if i in D else 1+sum(A[j] for j in g[i])
    Z = max(Z, A[0], B[0])
print(Z)