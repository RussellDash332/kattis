import sys; input = sys.stdin.readline
n, k = map(int, input().split()); a = []; z = [None]*n; s = []; g = [[] for _ in range(n)]; d = [0]*n; t = []
for _ in range(n): e, m, h = map(int, input().split()); a.append((m, h, e))
a.sort(key=lambda x: 3*10**6*x[0]+x[1]); p = {e[2]:i for i,e in enumerate(a)}
for i in range(n):
    while s and s[-1][1] <= a[i][1]: z[s.pop()[0]] = p[a[i][2]]
    s.append((i, a[i][1]))
for i in range(n):
    if z[i] != None: g[z[i]].append(i); d[i] += 1
q = [i for i in range(n) if d[i] == 0]; w = [1]*n
for u in q:
    t.append(u)
    for v in g[u]:
        d[v] -= 1
        if d[v] == 0: q.append(v)
while t:
    u = t.pop()
    for v in g[u]: w[u] += w[v]
for _ in range(k): m = p[int(input())]; r = z[m]; print(a[r][2] if r != None else 0, w[m]-1)