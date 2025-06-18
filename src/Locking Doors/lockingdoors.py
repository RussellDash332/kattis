import sys; input = sys.stdin.readline
v, e = map(int, input().split()); g, gt = [[] for _ in range(v)], [[] for _ in range(v)]; top, vis, scc = [], set(), 0; S = [-1]*v
for _ in range(e): a, b = map(int, input().split()); a -= 1; b -= 1; g[b].append(a), gt[a].append(b)
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis.add(u)
            if not t: S[u] = scc
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(v):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: scc += DFS(i, False)
Z = [0]*scc
for i in range(v):
    for j in g[i]:
        if S[i] != S[j]: Z[S[i]] = 1
print(scc-sum(Z))