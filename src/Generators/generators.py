import sys; input = sys.stdin.readline; from heapq import *; from array import *
n, m = map(int, input().split()); n += 1
g = [{} for _ in range(n)]
for _ in range(m): c, w = map(int, input().split()); g[0][c] = w
b = array('i', map(int, input().split()))
for i in range(1, n): s = i%(n-1)+1; g[i][s] = g[s][i] = b[i-1]
mst = 0; pq = [g[0][t]*n+t for t in g[0]]; used = array('b', [0]*n); used[0] = 1; heapify(pq)
while pq:
    w, u = divmod(heappop(pq), n)
    if used[u]: continue
    mst += w; used[u] = 1
    for v in g[u]: heappush(pq, g[u][v]*n+v)
print(mst)