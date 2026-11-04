R, C = map(int, input().split()); L = 9903
M = [[*map(int, input().split())] for _ in range(R)]
G = [set() for _ in range(L)]; H = [set() for _ in G]
for i in range(1, R):
    for j in range(C):
        if M[i][j] != M[i-1][j]: G[M[i][j]].add(M[i-1][j]); H[M[i-1][j]].add(M[i][j])
for i in range(C): G[0].add(M[-1][i]); H[M[-1][i]].add(0)
Q = [0]; D = [10**9]*L; D[0] = 0
for u in Q:
    for v in G[u]:
        if D[v]>D[u]+1: D[v] = D[u]+1; Q += [v]
B = [i for i in {*M[0]}]
Q = [B[0]]; E = [10**9]*L; E[B[0]] = 0
for u in Q:
    for v in H[u]:
        if E[v]>E[u]+1: E[v] = E[u]+1; Q += [v]
Q = [B[-1]]; F = [10**9]*L; F[B[-1]] = 0
for u in Q:
    for v in H[u]:
        if F[v]>F[u]+1: F[v] = F[u]+1; Q += [v]
if B[0] == B[-1]: print(D[B[0]])
else: print(min(D[x]+E[x]+F[x] for x in range(L)))