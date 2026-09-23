N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a] += [b]; G[b] += [a]
d = len(G[0])
if any(len(g)-d for g in G) or N-2**d: print('no'); exit()
B = [0]*N; Q = []; D = [-1]*N; D[0] = 0
for i in range(d): v = G[0][i]; Q += [v]; B[v] = 2**i; D[v] = 1
for u in Q:
    for v in G[u]:
        if D[v] < 0: D[v] = D[u]+1; B[v] = B[u]; Q += [v]
        elif D[v] == D[u]+1: B[v] |= B[u]
P = {2**i for i in range(d)}
for i in range(N):
    for j in G[i]:
        if B[i]^B[j] not in P: print('no'); exit()
print('yes')