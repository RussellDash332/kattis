import sys; input = sys.stdin.readline
M = 10**9+7; P = 31

B, W = map(int, input().split()); X = pow(P, W-1, M)
S = [[*map(int, input().split())] for _ in range(B)]
T = [[*map(int, input().split())] for _ in range(W)]

Z = [[1]*(B-W+1) for _ in range(B-W+1)]

for _ in range(2):
    D = [[S[i][j+1]-S[i][j] for j in range(B-1)] for i in range(B)]
    E = [[T[i][j+1]-T[i][j] for j in range(W-1)] for i in range(W)]
    H1 = []; H2 = []; H3 = []

    for i in range(B):
        h = [0]
        for j in range(W-1): h[-1] = (h[-1]*P+D[i][j])%M
        for j in range(W-1, B-1):
            h.append((h[-1]*P-X*D[i][j-W+1]+D[i][j])%M)
        H1.append(h)
    H2.append([0]*(B-W+1))
    for i in range(W): H2[-1] = [(H2[-1][j]*P+H1[i][j])%M for j in range(B-W+1)]
    for i in range(W, B):
        H2.append([(H2[-1][j]*P-X*P*H1[i-W][j]+H1[i][j])%M for j in range(B-W+1)])
    for i in range(W):
        h = 0
        for j in range(W-1): h *= P; h += E[i][j]; h %= M
        H3.append(h)
    H = 0
    for i in range(W): H = (H*P+H3[i])%M
    for i in range(B-W+1):
        for j in range(B-W+1):
            Z[i][j] *= H2[i][j] == H

    D = [*zip(*D)]
    E = [*zip(*E)]

print(sum(map(sum, Z)))