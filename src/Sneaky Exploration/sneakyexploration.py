import sys; input = sys.stdin.readline; from heapq import *
N = int(input()); G = [set() for _ in range(N)]
for _ in range(N-1): a, b = map(int, input().split()); G[a:=a-1].add(b:=b-1); G[b].add(a)
if N > 1 and max(map(len, G)) == N-1: print(-1); exit()
Q = [(-len(G[i]), i) for i in range(N)]; heapify(Q); V = set(); T = []
while Q:
    n, u = heappop(Q)
    if len(G[u])+n: continue
    while T: heappush(Q, T.pop())
    print(u+1); V.add(u)
    for v in G[u]:
        if v not in V: G[v].discard(u); T += [(-len(G[v]), v)] # delay neighbour to be directly processed after