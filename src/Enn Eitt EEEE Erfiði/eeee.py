import sys; input = sys.stdin.readline
n = int(input())
p = [input().split() for _ in range(n)]
m = {p[i][0]:i for i in range(n)}
G = [set() for _ in range(n)]
for i in range(n):
    for w in p[i][2:]:
        if w in m: G[i].add(m[w])
    G[i] = [*(G[i]-{i})]
Gt = [[] for _ in range(n)]
for i in range(n):
    for j in G[i]: Gt[j].append(i)
top, vis, scc, scc2 = [], set(), [], [0]*n
def DFS(s, t):
    stack = [2*s]; a = G if t else Gt
    if not t: scc.append(0)
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis.add(u)
            if not t: scc2[u] = len(scc)-1; scc[scc2[u]] += 1
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(n):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: DFS(i, False)
D = [set() for _ in range(len(scc))]
for i in range(n):
    for j in G[i]: D[scc2[i]].add(scc2[j])
N = n; n = len(scc); G = D; top.clear(); vis.clear()
for i in range(n):
    if i not in vis: DFS(i, True)
Z = [0]*n; B = [0]*n
for i in range(N): B[scc2[i]] |= 1<<i
for v in top:
    Z[v] |= B[v]
    for u in G[v]: Z[v] |= Z[u]
Z = [i.bit_count() for i in Z]
for i in range(N): print(Z[scc2[i]])