import sys; input = sys.stdin.readline; from array import *
V, E = map(int, input().split()); G = [{} for _ in range(V)]; Z = 0
for _ in range(E): a, b, w = map(int, input().split()); G[a-1][b-1] = G[b-1][a-1] = w
cqs = []; seen = [0]*V; P = [1<<i for i in range(23)]; I = {1<<i:i for i in range(23)}
for i in range(V):
    if not seen[i]:
        q = [i]; c = []
        for u in q:
            if seen[u]: continue
            seen[u] = 1; c.append(u); q.extend(G[u])
        cqs.append(c)

def dp(bm):
    if bm == 0: return 0
    if D[bm] != -1: return D[bm]
    nxt = bm&-bm; bm2 = bm^nxt; ans = 20**9
    while bm2: nxt2 = bm2&-bm2; ans = min(ans, G[cq[I[nxt]]][cq[I[nxt2]]]+dp(bm^nxt^nxt2)); bm2 ^= nxt2
    D[bm] = ans; return ans

for cq in cqs:
    if len(cq)%2: print('impossible'), exit(0)
    Z += dp(len(D:=array('i', [-1]*P[len(cq)]))-1)
print(Z)