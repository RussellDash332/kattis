N = int(input()); M = []; R = {}; P = []; B = set(); Q = []; free = set()
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) not in R: R[(x1, y1)] = len(R); P += [(x1, y1)]
    if (x2, y2) not in R: R[(x2, y2)] = len(R); P += [(x2, y2)]
    Q += [(R[(x1, y1)], R[(x2, y2)])]; B.add(Q[-1]); B.add(Q[-1][::-1])
    if (x1+y1)%2: free.add(R[(x1, y1)])
    if (x2+y2)%2: free.add(R[(x2, y2)])
V = len(R); G = [[] for _ in range(V)]
for i in range(V):
    x, y = P[i]
    for dx, dy in ((1, 0), (0, 1)):
        if (x+dx, y+dy) in R and (i, j:=R[(x+dx, y+dy)]) not in B: G[i] += [j]; G[j] += [i]

from random import *
def aug(l):
    if vis[l]: return 0
    vis[l] = 1
    for r in G[l]:
        if match[r] == -1 or aug(match[r]): match[r] = l; return 1
    return 0
match, mcbm = [-1]*V, 0
for l in [*free]:
    if (candidates:=[r for r in G[l] if match[r] == -1]): mcbm += 1; free.discard(l); match[choice(candidates)] = l
for f in free: vis = [0]*V; mcbm += aug(f)
Z = [-1]*V; K = 0
for i in range(V):
    if ~(j:=match[i]) and Z[i]<0 and Z[j]<0: Z[i] = Z[j] = K; K += 1
if min(Z)<0: print('impossible'); exit()
for i, j in Q: print(Z[i], Z[j])