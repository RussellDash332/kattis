X = int(input())
N, M, T = map(int, input().split())
S = []; C = []; G = [[] for _ in range(N)]
for _ in range(M): a, b = map(int, input().split()); a -= 1; b -= 1; G[a] += [b]; G[b] += [a]
for _ in range(N): t, p = map(int, input().split()); S += [t]; C += [p]
from functools import *; import sys; sys.setrecursionlimit(2067)
@cache
def dp(v, t):
    if t < 0: return 10**18
    elif t > 0: return min(C[v]+dp(v, t-S[v]), min(C[x]+dp(x, t-T-S[x]) for x in G[v]))
    else: return 10**18*(v>0)
Z = C[0]+dp(0, X-S[0]); print(['It is a trap.', Z][Z < 10**18])