import sys; input = sys.stdin.readline; from random import *

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in G[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

M = 10**6; n, x, y = map(int, input().split()); G = [[] for _ in range(2*n)]; P = [[*map(int, input().split())] for _ in range(n)]
for i in range(n):
    li, wi = P[i]
    for j in range(n):
        if i == j: continue
        lj, wj = P[j]
        if x*lj <= M*li <= y*lj and x*wj <= M*wi <= y*wj: G[i].append(j+n)
match, mcbm = [-1]*2*n, 0
free = {*range(n)}; nfree = len(free)
for l in [*free]:
    if (candidates:=[r for r in G[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*nfree; mcbm += aug(f)
print(n-mcbm)