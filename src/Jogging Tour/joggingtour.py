from math import *; INF = 1e18
def dp(G):
    mem = [[INF]*n for _ in range(1<<n)]
    for i in range(n): mem[1<<i][i] = 0
    for i in range(1<<n):
        for j in range(n):
            if i&(1<<j)==0:
                for k in range(n):
                    if i&(1<<k): mem[i|(1<<j)][j] = min(mem[i|(1<<j)][j], mem[i][k]+G[k][j])
    return min(mem[-1])
def rot(x, y, a): return x*cos(a)-y*sin(a), y*cos(a)+x*sin(a)
n = int(input()); P = [[*map(int, input().split())] for _ in range(n)]; Z = INF
for i in range(n):
    x1, y1 = P[i]
    for j in range(i):
        x2, y2 = P[j]; a = atan2(y1-y2, x2-x1); Q = [rot(*p, a) for p in P]; G = [[INF]*n for _ in range(n)]
        for ii in range(n):
            x3, y3 = Q[ii]
            for jj in range(ii): x4, y4 = Q[jj]; G[ii][jj] = G[jj][ii] = abs(x3-x4)+abs(y3-y4)
        Z = min(Z, dp(G))
print(Z)