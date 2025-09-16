import sys; input = sys.stdin.readline; from heapq import *; sys.setrecursionlimit(10**5)
N = int(input()); G = [[] for _ in range(N)]; T = [set() for _ in range(N)]; V = set()
C = [*map(int, input().split())]; K = [*map(int, input().split())]
for _ in range(N-1): a, b = map(int, input().split()); G[a-1].append(b-1); G[b-1].append(a-1)
Q = [(0, -1)]
while Q:
    u, p = Q.pop()
    if u in V: continue
    V.add(u); Q.extend((v, u) for v in G[u])
    if ~p: T[p].add(u)
def f(v):
    q = []
    for u in T[v]: f(u); c, k = C[u], K[u]; heappush(q, (-c/k, c, k, u))
    while q and C[v]*q[0][2] < K[v]*q[0][1]:
        _, c2, k2, u = heappop(q); C[v] += c2; K[v] += k2; T[v].discard(u)
        while T[u]: w = T[u].pop(); T[v].add(w); c, k = C[w], K[w]; heappush(q, (-c/k, c, k, w))
f(0); print(C[0]/K[0])