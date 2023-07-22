import sys; input = sys.stdin.readline
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop(); u, b = ub//2, ub%2
        if b:
            if t: top.append(u)
            else: scc[u] = S
        elif u not in vis:
            vis.add(u), stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
for _ in range(int(input())):
    V, E = map(int, input().split())
    g, gt = [set() for _ in range(V)], [set() for _ in range(V)]
    for _ in range(E): a, b = map(int, input().split()); g[a-1].add(b-1), gt[b-1].add(a-1)
    top, vis, scc = [], set(), {}
    for i in range(V):
        if i not in vis: DFS(i, True)
    vis.clear(); S = 0
    for i in top[::-1]:
        if i not in vis: DFS(i, False); S += 1
    d = {i: [0, 0] for i in range(S)}
    if len({*scc.values()}) == 1: print(0); continue
    for i in range(V):
        for j in g[i]:
            if scc[i] != scc[j]: d[scc[i]][1] += 1; d[scc[j]][0] += 1
    print(max(sum(i[0]==0 for i in d.values()), sum(i[1]==0 for i in d.values())))