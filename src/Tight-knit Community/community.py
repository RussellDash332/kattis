N, M, K = map(int, input().split()); G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split()); a -= 1; b -= 1
    G[a] += [b]; G[b] += [a]
D = [*map(len, G)]; Q = [i for i in range(N) if D[i] < K]; V = [1]*N
for u in Q:
    if V[u]:
        V[u] = 0
        for v in G[u]:
            if V[v]: D[v] -= 1; D[v]<K!=Q.append(v)
print('YNEOS'[1-any(V)::2])