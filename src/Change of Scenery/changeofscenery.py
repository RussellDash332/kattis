import os
c = r = 0; W = []; F = W.append
for i in os.read(0, 67_067_067):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); r = c = 0
from heapq import *
N, M, K = W[0], W[1], W[2]
G = [[] for _ in range(N)]; p = K+2
for _ in range(M): a = W[p:=p+1]-1; b = W[p:=p+1]-1; w = W[p:=p+1]; G[a] += [(b, w)]; G[b] += [(a, w)]
D = [10**9]*N; D[0] = 1; pq = [0]
while pq:
    dd, vv = divmod(heappop(pq), N)
    if dd != D[vv]//3: continue
    for nn, w in G[vv]:
        if D[nn] > 3*(new:=dd+w)+2: D[nn] = D[vv]+3*w; heappush(pq, new*N+nn)
        elif D[nn] == 3*new+1: D[nn] += 1
print('yneos'[D[-1]%3<2::2])