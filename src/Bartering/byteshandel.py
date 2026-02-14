import sys; input = sys.stdin.readline; from heapq import *
N, M = map(int, input().split()); T = []; G = [[] for _ in range(N)]; K = []; Q = [(1, 0)]; D = [10**18]*N; D[0] = 1
for i in range(M):
    r, k = map(int, input().split()); C = []
    for _ in range(k): c, j = map(int, input().split()); C.append((j, c)); G[j].append(i)
    T.append((C, r)); K.append(k)
while Q:
    p, u = heappop(Q)
    if D[u] != p: continue
    for v in G[u]:
        K[v] -= 1
        if K[v] < 1:
            t, r = T[v]; z = 0
            for f, c in t: z += D[f]*c
            if z < D[r]: D[r] = z; heappush(Q, (z, r))
print(D[-1])