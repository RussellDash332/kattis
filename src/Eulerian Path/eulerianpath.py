while True:
    v, e = map(int, input().split())
    if not v + e: break
    g, di, do = [[] for _ in range(v)], [0]*v, [0]*v
    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        di[b] += 1; do[a] += 1
    oi1, io1, eq = [], [], []
    for i in range(v):
        if di[i] - do[i] in [-1, 0, 1]: [eq, io1, oi1][di[i] - do[i]].append(i)
    if len(oi1) > 1 or len(io1) > 1 or len(oi1) + len(io1) + len(eq) != v: print('Impossible'); continue
    source = oi1[0] if oi1 else 0
    ans, idx, stack = [], [0]*v, [source]
    while stack:
        u = stack[-1]
        if idx[u] < len(g[u]):  stack.append(g[u][idx[u]]); idx[u] += 1
        else:                   ans.append(u), stack.pop()
    ans = ans[::-1]
    g = [set(u) for u in g]
    can = True
    if len(ans) != e+1: print('Impossible'); continue
    for a, b in zip(ans, ans[1:]):
        if b not in g[a]: can = False; break
    if can: print(*ans)
    else: print('Impossible')