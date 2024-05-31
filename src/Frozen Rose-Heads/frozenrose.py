import sys; input = sys.stdin.readline
while True:
    try: n, r = map(int, input().split())
    except: break
    g = [{} for _ in range(n)]; t = [[] for _ in range(n)]; T = []; s = [(r-1, -1)]; d = [0]*n; z = [float('inf')]*n
    for _ in range(n-1): a, b, w = map(int, input().split()); g[a-1][b-1] = g[b-1][a-1] = w
    while s:
        u, p = s.pop()
        if p != -1: t[p].append(u); d[u] += 1
        for x in g[u]:
            if x != p: s.append((x, u))
    q = [i for i in range(n) if d[i] == 0]
    for u in q:
        T.append(u)
        for v in g[u]:
            d[v] -= 1
            if d[v] == 0: q.append(v)
    while T:
        u = T.pop(); s = 0
        if not t[u]: continue
        for v in t[u]: s += min(z[v], g[u][v])
        z[u] = s
    print(z[r-1])