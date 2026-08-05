import sys; input = sys.stdin.readline
N, M, K = map(int, input().split())
P = [1, *map(int, input().split()), N]
g = [[] for _ in range(N)]; gt = [[] for _ in range(N)]
for _ in range(M):
    q, r, s = input().strip().split(); q = int(q)-1; r = int(r)-1; g[q] += [r]; gt[r] += [q]
    if s > 'm': g[r] += [q]; gt[q] += [r]
top, vis, scc = [], set(), [0]*N; cnt = 1
def DFS(s, t):
    stack = [2*s]; a = g if t else gt
    while stack:
        ub = stack.pop()
        u, b = ub//2, ub%2
        if b and t: top.append(u)
        elif u not in vis:
            if not t: scc[u] = cnt
            vis.add(u)
            stack.append(2*u+1)
            for v in a[u]:
                if v not in vis: stack.append(2*v)
    return 1
for i in range(N):
    if i not in vis: DFS(i, True)
vis.clear()
for i in top[::-1]:
    if i not in vis: cnt += DFS(i, False)
S = [[] for _ in range(cnt)]
for i in P: S[scc[i-1]].append(i)
S2 = [[] for _ in range(cnt)]
for i in range(N): S2[scc[i]].append(i)

H = [set() for _ in range(cnt)]; I = [0]*cnt; T = []
for i in range(N):
    for j in g[i]:
        if scc[i] != scc[j] and scc[j] not in H[scc[i]]: H[scc[i]].add(scc[j]); I[scc[j]] += 1
Q = [i for i in range(cnt) if I[i]<1]
for u in Q:
    if S[u]: T.append(u)
    for v in H[u]: I[v] -= 1; I[v]<1!=Q.append(v)

def par(s):
    Q = [s]; Z = [-1]*N; Z[s] = s
    for u in Q:
        for v in g[u]:
            if Z[v] < 0: Z[v] = u; Q += [v]
    return Z
Z = [1]; cur = scc[0]
def trav(s, t):
    p = par(s); z = [t]
    while 1:
        if p[z[-1]] == z[-1]: break
        z += [p[z[-1]]]
        if z[-1] < 0: print('impossible'); exit()
    Z.extend(i+1 for i in z[-2::-1])
for s in T:
    if s != cur: trav(Z[-1]-1, S2[s][0])
    for i in S[s]: trav(Z[-1]-1, i-1)
    cur = s
if Z[-1] != N: trav(Z[-1]-1, N-1)
K = []
for i in Z:
    if not K or K[-1] != i: K.append(i)
print(*K)