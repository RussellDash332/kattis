from itertools import *
U, N = map(int, input().split())
Z = 0
W = [input() for _ in range(N)]
G = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        lcs = 0
        for k in range(1, len(W[j])+1):
            for l in range(len(W[j])-k+1):
                if W[j][l:l+k] in W[i]: lcs = k
        G[i][j] = len(W[j])*(len(W[j])+1)//2-lcs*(lcs+1)//2
for p in permutations(range(1, N)):
    u = 0; x = 1; p = (0,)+p
    while x < N:
        if G[p[x-1]][p[x]]+u <= U: u += G[p[x-1]][p[x]]; x += 1
        else: break
    Z = max(Z, x)
print(Z)