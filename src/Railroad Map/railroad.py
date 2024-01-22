input = __import__('sys').stdin.readline
for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    g = [[0, {}] for _ in range(n+1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        for _ in range(2):
            a, b = b, a
            g[a][0] += 1
            if b not in g[a][1]: g[a][1][b] = []
            g[a][1][b].append(w)
    q = []
    for i in range(1, n+1):
        if g[i][0] == 2: q.append(i)
    for i in q:
        if g[i][0] == 2:
            e = []
            for j in g[i][1]:
                for k in g[i][1][j]: e.append((j, k))
            (a, b), (c, d) = e
            g[a][0] -= 1; g[c][0] -= 1
            g[i] = [0, {}]
            g[a][1].pop(i)
            if a != c: g[c][1].pop(i)
            g[a][0] += 1; g[c][0] += 1
            if c not in g[a][1]: g[a][1][c] = []
            if a not in g[c][1]: g[c][1][a] = []
            g[a][1][c].append(b+d), g[c][1][a].append(b+d)
            if g[a][0] == 2: q.append(a)
            if a != c and g[c][0] == 2: q.append(c)
    E = set()
    for i in range(1, n+1):
        for j in g[i][1]:
            for k in g[i][1][j]: E.add((min(i, j), max(i, j), k))
    print(len(E))
    for e in E: print(*e)
    print()