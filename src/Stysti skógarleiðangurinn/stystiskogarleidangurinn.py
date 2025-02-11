from itertools import combinations
INF = 1e18
def tsp(G):
    n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<n)]; C[1][0] = 0
    for s in range(1, n):
        for S in combinations(range(1, n), s):
            k = 1
            for i in S: k += 1<<i
            for i in S:
                C[k][i] = min(C[k][i], C[k^(1<<i)][0]+G[0][i])
                for j in S:
                    if j != i: C[k][i] = min(C[k][i], C[k^(1<<i)][j]+G[j][i])
    k = (1<<n)-1; return min(C[k][i] for i in range(n))
n, m, s = map(int, input().split())
G = [{} for _ in range(n)]; T = [*map(int, input().split())]
for _ in range(m): a, b, w = map(int, input().split()); G[a-1][b-1] = G[b-1][a-1] = w
D = [[G[i][j] if j in G[i] else INF for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n): D[i][j] = min(D[i][j], D[i][k]+D[k][j])
print(tsp(D)+sum(sorted(T)[:n-s]))