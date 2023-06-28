from heapq import *
n = int(input())
g, c = [{-1: 0} for _ in range(n)], [-1]*n
for _ in range(n):
    a, b = map(int, input().split()); a -= 1; b -= 1
    for _ in range(2):
        if b not in g[a]: g[a][b] = 0
        g[a][b] += 1; g[a][-1] += 1
        a, b = b, a
q = [(g[i][-1], i) for i in range(n)]
heapify(q)
while q:
    d, i = heappop(q)
    if d > 0 and d == g[i][-1] and c[i] == -1 and g[i][-1]:
        for j in g[i]:
            if j != -1: e = j
        if e in g[i]:
            c[i] = e
            g[i][e] -= 1; g[e][i] -= 1; g[i][-1] -= 1; g[e][-1] -= 1
            if g[i][e] == 0: g[i].pop(e), g[e].pop(i)
            heappush(q, (g[e][-1], c[i]))
for i in range(n): print(i+1, c[i]+1)