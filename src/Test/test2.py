import sys; input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0: break
    rev, el, m = {}, [], []
    for _ in range(N):
        a, b, c, d, e, p = input().strip().split()
        for x in [a, b, c, d, e, p]:
            if x not in rev: rev[x] = len(rev); m.append(x)
        for x in [a, b, c, d, e]:
            if x != p: el.append((rev[p], rev[x]))
    V = len(rev)
    g, gt = [[] for _ in range(V)], [[] for _ in range(V)]
    for a, b in el: g[a].append(b), gt[b].append(a)
    top, vis, scc = [], set(), []
    def DFS(s, add):
        vis.add(s)
        a = gt if add else g
        for v in a[s]:
            if v not in vis: DFS(v, add)
        if add: top.append(s)
        else: scc[-1].append(m[s])
    for i in range(V):
        if i not in vis: DFS(i, True)
    vis.clear()
    for i in top[::-1]:
        if i not in vis: scc.append([]), DFS(i, False)
    for i in sorted(map(sorted, scc)): print(' '.join(i))
    print()