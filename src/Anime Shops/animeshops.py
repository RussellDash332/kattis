import sys; input = sys.stdin.readline
from array import *
N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
D = array('i', [10**9]*N)
X = {*map(lambda x: int(x)-1, input().split())}
for _ in range(M): a, b = map(int, input().split()); G[a-1].append(b-1); G[b-1].append(a-1)
Q = [(i, i) for i in X]
M = [set() for _ in range(N)]
for u in X: D[u] = 0
for u, s in Q: # handle non-shops first, but keep track of shop(s) that give this closest distance
    for v in G[u]:
        if D[v] >= D[u]+1:
            M[v].add(s)
            if D[v] > D[u]+1: Q.append((v, s)); D[v] = D[u]+1
Q = [(i, 0, i) for i in X]
V = array('b', [0]*N)
for u in X: D[u] = 10**9; V[u] = 1
for u, d, s in Q: # there is shop s with distance d to a city u
    for v in G[u]:
        if v == s: continue # only handle if current city is different than reference shop
        if not M[v]: D[s] = min(D[s], d+1) # both v and s are shops
        # now check if there is another shop different than s that is closest to v
        elif s in M[v]:
            M[v].discard(s)
            if M[v]: D[s] = min(D[s], d+1+D[v])
            M[v].add(s)
        elif M[v]: D[s] = min(D[s], d+1+D[v])
        if not V[v]: V[v] = 1; Q.append((v, d+1, s))
print(*(z if z < 10**9 else -1 for z in D))