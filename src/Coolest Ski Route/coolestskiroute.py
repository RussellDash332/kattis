N, M = map(int, input().split())
I = [0]*N; G = [[] for _ in range(N)]; D = [0]*N
for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1; G[a] += [(b, w)]; I[b] += 1
Q = [i for i in range(N) if I[i]<1]
for u in Q:
    for v, _ in G[u]: I[v] -= 1; I[v]<1!=Q.append(v)
for u in Q[::-1]:
    for v, w in G[u]: D[u] = max(D[u], D[v]+w)
print(max(D))