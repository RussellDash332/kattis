import sys; input = sys.stdin.readline
N, M = map(int, input().split())
A = int(input())
S = [[*map(lambda x: int(x)-1, input().split()[1:])] for _ in range(M)]
T = [[] for _ in range(N)]
G = []
for u in range(M):
    s = S[u]; g = [{} for _ in range(N)]
    for i in s: T[i].append(u)
    for i in range(len(s)-1): g[s[i]][s[i+1]] = g[s[i+1]][s[i]] = A
    G.append(g)
D = [[[10**18]*(N+1) for _ in range(M)] for _ in range(N)]; Q = []
for i in range(M):
    if G[i][0]: D[0][i][0] = 0; Q.append((0, i, 0))
for s, p, c in Q:
    for q in T[s]:
        for t in G[q][s]:
            new = D[s][p][c]+A; d = c+(p!=q)
            if d <= N and new < D[t][q][d]: D[t][q][d] = new; Q.append((t, q, d))
O = [min(D[-1][j][i] for j in range(M)) for i in range(N+1)]
for _ in range(int(input())): B = int(input()); print(min(O[i]+i*B for i in range(N+1)))