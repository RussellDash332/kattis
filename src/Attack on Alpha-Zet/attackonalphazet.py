import sys; input = sys.stdin.readline
R, C = map(int, input().split()); N = R*C
G = [[] for _ in range(N)]
M = [input() for _ in range(R+1)]; P = []
for i in range(R):
    for j in range(C):
        u = i*C+j
        for di, dj in ((0, 1), (1, 0)):
            if R>i+di>-1<j+dj<C and ((dj and M[i+1][2*j+2] < '|') or (di and M[i+1][2*j+1] < '_')): G[u] += [u+di*C+dj]; G[u+di*C+dj] += [u]
for _ in range(int(input())): a, b = map(int, input().split()); P += [a*C+b-C-1]
Q = [[] for _ in range(N)]; R = []; d = [0]*N; par = [*range(N)]; d[0] = 1; s = [(0, 0)]
for i, (a, b) in enumerate(zip(P, P[1:])): R.append([a, b, -1]), Q[a].append(i), Q[b].append(i)
def find(i):
    p = [i]
    while par[p[-1]] != p[-1]: p += [par[p[-1]]]
    for u in p: par[u] = p[-1]
    return p[-1]
while s:
    ub, p = s.pop(); u = ub//2
    if ub%2:
        for x in Q[u]:
            if R[x][1] == u: R[x][0], R[x][1] = R[x][1], R[x][0]
            R[x][2] = find(R[x][1])
        par[u] = p
    else:
        s.append((ub+1, p))
        for t in G[u]:
            if t != p: d[t] = d[u]+1; s.append((2*t, u))
print(sum(d[a]+d[b]-2*d[lca] for a, b, lca in R))