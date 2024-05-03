import sys; input = sys.stdin.readline
n = int(input()); g = {}; q = []; r = {}; m = {}
for _ in range(n):
    a, b = input().strip().split(); q.append(a)
    if b not in g: g[b] = []
    if a not in r: r[a] = 0
    g[b].append(a); r[a] += 1
for x in g:
    if x not in r:
        s = [x]
        while s:
            u = s.pop(); m[u] = x
            if u in g: s.extend(g[u])
for i in q: print(i, m[i])