import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from heapq import *; from array import *
N, M = map(int, input().split())
G = [[] for _ in range(N)]
T = [[] for _ in range(N)]
for _ in range(M): a, b = map(int, input().split()); G[a] += [b]; T[b] += [a]
Q = array('I', [0]); D = array('I', [N]*N); D[0] = 0
for u in Q:
    for v in G[u]:
        if D[v]==N: D[v] = D[u]+1; Q.append(v)
E = array('I', [10**9]*N); E[-1] = 0; pq = [N-1]
while pq:
    dd, vv = divmod(heappop(pq), N)
    if dd!=E[vv]: continue
    for nn in T[vv]:
        if E[nn]>(new:=max(dd+1, D[nn])): E[nn] = new; heappush(pq, new*N+nn)
sys.stdout.write(' '.join(map(str, E[:-1])))