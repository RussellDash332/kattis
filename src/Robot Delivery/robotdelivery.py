import sys; input = sys.stdin.readline
from random import *; from array import *; from collections import *
R, C, N = map(int, input().split())
M = [input() for _ in range(R)]
P = {}; Q = {}
for i in range(R):
    for j in range(C):
        if M[i][j] == 'R': P[i*C+j] = len(P)
        if M[i][j] == 'P': Q[i*C+j] = len(Q)
G = [[] for _ in range(2*N)]; K = ((0, 1), (1, 0), (-1, 0), (0, -1))
for ij in P:
    i, j = divmod(ij, C); F = deque([(i, j)]); S = array('h', [0]*R*C); S[i*C+j] = 1
    while F:
        r, c = F.popleft()
        if r*C+c in Q: G[P[i*C+j]].append((Q[r*C+c]+N, S[r*C+c]-1))
        for dr, dc in K:
            if R>r+dr>-1<c+dc<C and M[r+dr][c+dc] != '#' and not S[(r+dr)*C+c+dc]: S[(r+dr)*C+c+dc] = S[r*C+c]+1; F.append((r+dr, c+dc))
def f(x):
    def aug(l):
        if vis[l]: return 0
        vis[l] = 1
        for r, d in G[l]:
            if d > x: continue
            if match[r] == -1 or aug(match[r]): match[r] = l; return 1
        return 0
    match, mcbm = array('h', [-1]*2*N), 0; free = {*range(N)}
    for l in [*free]:
        if (candidates:=[r for r, d in G[l] if match[r] == -1 and d <= x]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
    for f in free: vis = array('b', [0]*N); mcbm += aug(f)
    return mcbm == N
lo, hi = 0, 2*(R+C)
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)