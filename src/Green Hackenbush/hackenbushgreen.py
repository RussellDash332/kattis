import sys; input = sys.stdin.readline; sys.setrecursionlimit(106700)
N, M = map(int, input().split()); N += 1; G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    if a<0: a = 0
    if b<0: b = 0
    G[a] += [b]
    if a != b: G[b] += [a]
K = [0]*N; L = [0]*N; T = [0]
def f(u, p):
    T[0] += 1; K[u] = L[u] = T[0]; z = 0
    for v in G[u]:
        if v == p: p += N; continue # +N to handle parallel edges
        if K[v]: L[u] = min(L[u], K[v])
        else:
            s = f(v, u); L[u] = min(L[u], L[v])
            if L[v] > K[u]: z ^= 1^(1+s)
            else: z ^= s
    if p > N: p -= N
    for v in G[u]: z ^= v != p and K[u] <= K[v]
    return z
print('*'+str(f(0, -1)))