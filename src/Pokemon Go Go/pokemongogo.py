import sys; input = sys.stdin.readline
from itertools import combinations
INF = 1e18
poke = [(0, 0, '@')]; rev = {'@': 0}
for _ in range(N:=int(input())):
    x, y, p = input().strip().split(); x, y = int(x), int(y)
    if p not in rev: rev[p] = len(rev)
    poke.append((x, y, p))
G = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N):
    x1, y1, _ = poke[i]
    for j in range(i+1, N+1):
        x2, y2, _ = poke[j]; G[i][j] = G[j][i] = abs(x1-x2) + abs(y1-y2)
n = len(G); C = [[INF for _ in range(n)] for _ in range(1<<len(rev))]; C[1][0] = 0
for s in range(1, n):
    for S in combinations(range(1, n), s):
        k = 1
        for i in S: k |= 1<<rev[poke[i][2]]
        for i in S:
            if i == 0: continue
            p = k^(1<<rev[poke[i][2]])
            C[k][i] = min(C[k][i], C[p][0]+G[0][i])
            for j in S:
                if j != i: C[k][i] = min(C[k][i], C[p][j]+G[j][i])
c, g = C[-1], G[0]; nxt = min((c[i]+g[i], i) for i in range(n))[1]
print(c[nxt]+g[nxt])