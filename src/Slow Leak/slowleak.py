INF = float('inf')
def fw(g, v):
    D = [[g[i][j] if i in g and j in g[i] else INF for j in range(v)] for i in range(v)]
    for k in range(v):
        for i in range(v):
            for j in range(v):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

import sys
n, m, t, d = map(int, input().split())
s = [1] + list(map(int, input().split())) + [n]
g = {}
for line in sys.stdin:
    a, b, w = map(int, line.split())
    a, b = a-1, b-1
    for _ in range(2):
        if a not in g: g[a] = {}
        g[a][b] = w
        a, b = b, a
D = fw(g, n)
g2 = {}
for ss in s:
    ss -= 1
    for tt in s:
        tt -= 1
        if ss != tt:
            if D[ss][tt] <= d:
                a, b = ss, tt
                if D[a][b] != INF:
                    for _ in range(2):
                        if a not in g2: g2[a] = {}
                        g2[a][b] = D[a][b]
                        a, b = b, a
r = fw(g2, n)[0][-1] # could've used Dijkstra but lazy
print('stuck' if r == INF else r)