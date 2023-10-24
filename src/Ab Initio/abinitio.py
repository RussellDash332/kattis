import sys; input = sys.stdin.readline; from array import *
V, E, Q = map(int, input().split()); G = [array('b', [0]*V) for _ in range(V)]; T = C = 0; M = 10**9+7
for _ in range(E): a, b = map(int, input().split()); G[a][b] = 1
for _ in range(Q):
    q, *r = map(int, input().split())
    if q == 1:
        for i in range(len(G)): G[i].append(C)
        G.append(array('b', [C]*(len(G)+1)))
    elif q == 2 or q == 4:
        X, Y = r
        if T: X, Y = Y, X
        G[X][Y] = 1-G[X][Y]
    elif q == 3:
        X = r[0]
        for i in range(len(G)): G[i][X] = G[X][i] = C
    elif q == 5: T = 1-T
    elif q == 6: C = 1-C
print(len(G))
for i in range(len(G)):
    ans = out = 0
    for j in range(len(G)-1, -1, -1):
        if i == j: continue
        if (T and G[j][i] != C) or (not T and G[i][j] != C): out += 1; ans = (7*ans+j)%M
    print(out, ans)