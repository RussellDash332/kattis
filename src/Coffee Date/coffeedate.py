import sys; input = sys.stdin.readline; from heapq import *
B, N, E, L = map(int, input().split()); G = [[] for _ in range(B)]; INF = 10**9
for _ in range(N):
    C, S = map(int, input().split()); p = 0
    s = [*map(int, input().split())]
    t = [*map(int, input().split())]
    for i in range(S-1): G[s[i]] += [(s[i+1], C, p, t[i])]; p += t[i]
def dijkstra(s):
    D = [INF]*B; D[s] = 0; pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn, cc, ss, tt in G[vv]:
            if D[nn] > (new:=dd+(ss-dd)%cc+tt): D[nn] = new; heappush(pq, (new, nn))
    return D
Z = min(max(a, b) for a, b in zip(dijkstra(E), dijkstra(L)))
print(Z if Z < INF else 'NO COFFEE FOR YOU')