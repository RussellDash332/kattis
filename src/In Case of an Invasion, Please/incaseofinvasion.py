import os
c = r = 0; W = []; F = W.append
for i in os.read(0, 1<<25):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0
N, M, S = W[0], W[1], W[2]
G = [[] for _ in range(N)]
P = W[3:3+N]; U = sum(P); p = N+2
for _ in range(M): a, b, w = W[p:=p+1], W[p:=p+1], W[p:=p+1]; a -= 1; b -= 1; G[a].append((b, w)); G[b].append((a, w))
INF = 10**15

from heapq import *
def dijkstra(s):
    D = [INF]*N; D[s] = 0; pq = [s]
    while pq:
        dv = heappop(pq); dd, vv = dv//N, dv%N
        if dd == D[vv]:
            for nn, w in G[vv]:
                if D[nn] > (new:=dd+w): D[nn] = new; heappush(pq, new*N+nn)
    return D
D = []; C = []
for i in range(S): D.extend(dijkstra(W[p:=p+1]-1)); C.append(W[p:=p+1])

lo, hi = 0, max(d for d in D if d<INF)
H = [[] for _ in range(2**S)]; K = [[] for _ in range(2**S)]
for i in range(2**S):
    for j in range(2**S):
        if i|j == i: H[i].append(j)
    for j in range(S):
        if i&(1<<j): K[i].append(j)
while lo < hi:
    mi = (lo+hi)>>1; B = [0]*(2**S)
    for i in range(N):
        b = 0
        for j in range(S):
            if D[N*j+i] <= mi: b |= 1<<j
        B[b] += P[i]
    for i in range(2**S):
        c = 0
        for j in H[i]: c += B[j]
        for j in K[i]: c -= C[j]
        if c>0: lo = mi+1; break
    else: hi = mi
print(lo)