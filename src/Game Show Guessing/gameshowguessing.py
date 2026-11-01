N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
X = {e:i for i,e in enumerate({x for x, y in P})}
Y = {e:i+len(X) for i,e in enumerate({y for x, y in P})}
D = [0]*(L:=len(X)+len(Y)); G = [[] for _ in D]
for i in range(N): x, y = P[i]; G[X[x]] += [i]; G[Y[y]] += [i]; D[X[x]] += 1; D[Y[y]] += 1
Q = [i for i in range(L) if D[i]==1]
R = [0]*N; B = [0]*N; r = 0
while Q:
    Q2 = []; r += 1
    for u in Q:
        if D[u] == 1:
            for e in G[u]:
                if 1-R[e]: break
            R[e] = 1; B[e] = r
            a, b = P[e]; a = X[a]; b = Y[b]
            D[a] -= 1; D[b] -= 1
            if D[a] == 1: Q2 += [a]
            if D[b] == 1: Q2 += [b]
    Q = Q2
print(B.index(0)+1 if 0 in B else B.index(max(B))+1)