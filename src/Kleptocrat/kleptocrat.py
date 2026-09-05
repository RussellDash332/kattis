import sys; input = sys.stdin.readline
N, M, Q = map(int, input().split()); G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    G[a] += [(b, w)]; G[b] += [(a, w)]
T = [[] for _ in range(N)]; D = [-1]*N; D[0] = 0; q = [0]; B = [0]*61
for u in q:
    for v, w in G[u]:
        if D[v]<0: T[u] += [(v, w)]; D[v] = D[u]^w; q += [v]
        else:
            x = D[u]^D[v]^w
            for i in range(60, -1, -1):
                if x&(1<<i):
                    if B[i]<1: B[i] = x; break
                    x ^= B[i]
for _ in range(Q):
    a, b = map(int, input().split()); z = D[a-1]^D[b-1]
    for i in range(60, -1, -1):
        if B[i]: z = min(z, z^B[i])
    print(z)