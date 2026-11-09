N, M, P = map(int, input().split())
L = [[[*map(int, input().split())] for _ in range(x)] for x in map(int, input().split())]
D = [0]+[10**9]*min(N, M, P)
E = [0]+[10**9]*N
F = [0]+[10**9]*M
G = [0]+[10**9]*P
for u, K in enumerate((E, F, G, D)):
    for q, c in L[u]:
        for i in range(len(K)-q): K[i+q] = min(K[i+q], K[i]+c)
print(min(D[s]+E[N-s]+F[M-s]+G[P-s] for s in range(len(D))))