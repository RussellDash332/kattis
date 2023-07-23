import sys; input = sys.stdin.readline
from random import choice
from heapq import *

def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in g[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0

N, M, C = map(int, input().split())
R = {0, *map(int, input().split())}
INF = 10**9

V = 2*N
A = [{} for _ in range(N)]
for _ in range(M): a, b, w = map(int, input().split()); A[a][b] = w

D, P = {}, {}
D[0] = 0
pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd == D[vv]:
        for nn in A[vv]:
            if nn not in D or D[nn] >= dd + A[vv][nn]:
                if nn not in D: P[nn] = set(); D[nn] = INF
                if vv in P[nn]: continue
                if D[nn] == (x:=dd+A[vv][nn]): P[nn].add(vv)
                else: P[nn] = {vv}
                D[nn] = x; heappush(pq, (D[nn], nn))
g = [[] for _ in range(V)]
vis = set()
for i, d in sorted(D.items(), key=lambda x: x[1]):
    if i not in P: continue
    for k in [*P[i]]:
        if k in P: P[i] |= P[k]
for i in P:
    if i not in R: continue
    for j in P[i]:
        if j in R: g[j].append(i+N)

match, mcbm = [-1]*V, 0
free = set(range(N))
nfree = len(free)
for l in list(free):
    candidates = [r for r in g[l] if match[r] == -1]
    if candidates:
        mcbm += 1
        free.discard(l)
        match[choice(candidates)] = l
for f in free:
    vis = [0]*nfree
    mcbm += aug(f)
have = [0]*N
for i in range(N):
    for j in g[i]: have[i] += 1; have[j-N] += 1
print(sum(i>0 for i in have)-mcbm)