import sys; input = sys.stdin.readline; from heapq import *
n, m = map(int, input().split())
b, g = map(int, input().split()); b -= 1; g -= 1
G = [[] for _ in range(n)]
for _ in range(m): u, v, w, d = map(int, input().split()); G[u-1] += [(v-1, w-d, w+d)]
INF = 10**18
def dijkstra(s, t):
    D = [INF]*n; D[s] = 0; pq = [(0, s)]
    while pq:
        dd, vv = heappop(pq)
        if dd != D[vv]: continue
        for nn, w, x in G[vv]:
            if D[nn] > (new:=dd+x if t else dd+w): D[nn] = new; heappush(pq, (new, nn))
    return D
Z = [i+1 for i, (p, q, r, s) in enumerate(zip(dijkstra(b, 0), dijkstra(b, 1), dijkstra(g, 0), dijkstra(g, 1))) if max(p, r)<=min(q, s)!=INF]
for i in Z or ['Thessi leikur verdur sennilega leidinlegur']: print(i)