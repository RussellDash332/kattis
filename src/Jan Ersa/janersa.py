import sys; input = sys.stdin.readline
from array import *; from heapq import *
N = int(input()); G = [[] for _ in range(N)]
for _ in range(int(input())): a, b, w = map(int, input().split()); a -= 1; b -= 1; G[a] += [(b, w)]; G[b] += [(a, w)]
D = array('I', [10**9]*N*N)
for s in range(N):
    D[s*-~N] = 0; pq = [s]; s *= N
    while pq:
        dv = heappop(pq); dd, vv = dv//N, dv%N
        if dd != D[s+vv]: continue
        for nn, w in G[vv]:
            if D[s+nn] > (new:=dd+w): D[s+nn] = new; heappush(pq, new*N+nn)
z = max(range(N*N), key=lambda x: D[x]); print(z//N+1, z%N+1, D[z]*100)