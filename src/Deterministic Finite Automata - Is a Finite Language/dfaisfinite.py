import sys; input = sys.stdin.readline
n, c, s, f = map(int, input().split()); s -= 1
S = input().strip()
F = [*map(lambda x: int(x)-1, input().split())]
T = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n)]
g = [set() for _ in range(n)]; gt = [set() for _ in range(n)]
for i in range(n):
    for j in range(c): g[i].add(T[i][j]); gt[T[i][j]].add(i)
top, vis, scc = [], set(), 0; asg = [-1]*n
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            vis.add(u); asg[u] = scc
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(n):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: scc += DFS(i, False)
vis = set()
Q = [s]
for u in Q:
    if u in vis: continue
    vis.add(u); Q.extend(g[u])
rs = {*vis}
vis = set()
Q = [*F]
for u in Q:
    if u in vis: continue
    vis.add(u); Q.extend(gt[u])
rf = {*vis}
R = rs&rf
S = {asg[i] for i in R}
print('in'*(len(R)!=len(S) or any(i in g[i] for i in R))+'finite')