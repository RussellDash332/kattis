from math import *
n = int(input()); p = [[*map(int, input().split())] for _ in range(n)]; p.append((0, 0)); n += 1
g = [[hypot(p[i][0]-p[j][0], p[i][1]-p[j][1]) for j in range(n)] for i in range(n)]

def check(x):
    visited = [0]*n; disc = [10**9]*n; low = [10**9]*n; time = [0]
    def DFS(u, par=-1):
        visited[u] = 1; children = 0; disc[u] = low[u] = time[0]; time[0] += 1
        for v in range(n):
            if v != u and g[u][v] <= x:
                if not visited[v]:
                    children += 1
                    if not DFS(v, u): return 0
                    low[u] = min(low[u], low[v])
                    if par != -1 and low[v] >= disc[u]: return 0
                elif par != v: low[u] = min(low[u], disc[v])
        return 1
    return DFS(n-1) and all(visited)

lo, hi = 0, max(map(max, g))
while abs(lo-hi) > 5e-7:
    mi = (lo+hi)/2
    if check(mi): hi = mi
    else: lo = mi
print(mi)