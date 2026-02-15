import sys; input = sys.stdin.readline
from heapq import *
N, M, T = map(int, input().split())
G = [{} for _ in range(N)]
for _ in range(M):
    a, b, w, l, h = map(int, input().split())
    G[a-1][b-1] = G[b-1][a-1] = (w, l, h)
INF = float('inf'); D = [INF]*N; D[0] = 0; pq = [(0, 0)]
while pq:
    dd, vv = heappop(pq)
    if dd != D[vv]: continue
    for nn, (ww, aa, bb) in G[vv].items():
        x = min(max((T-dd)*aa, 0), ww)/aa
        new = dd+x+(ww-x*aa)/bb
        if D[nn] > new: D[nn] = new; heappush(pq, (new, nn))
print(D[-1])