from functools import *
N, M = map(int, input().split())
D = [[0]*N for _ in range(N)]
for i in range(N): D[i][i] = 1
G = [0]*N; B = {1<<i:i for i in range(N)}
for _ in range(M): a, b = map(int, input().split()); D[a:=a-1][b:=b-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N): D[i][j] |= D[i][k]&D[k][j]
for i in range(N):
    for j in range(N):
        if D[i][j]: G[i] |= 1<<j
@cache
def bt(bm):
    if bm == 0: return 0
    bm2 = bm
    while bm2:
        nxt = bm2&-bm2
        if not bt(bm-(bm&G[B[nxt]])): return 1
        bm2 -= nxt
    return 0
print('BAetrlgiu r'[bt(2**N-1)::2])