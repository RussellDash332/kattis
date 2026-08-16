import sys; input = sys.stdin.readline
class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i])
        return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
            return 1
R, C, Q = map(int, input().split()); N = R*C
M = [[*map(int, input().split())] for _ in range(R)]
E = []
for i in range(R*C):
    if i//C+1<R: E += [(max(M[i//C][i%C], M[i//C+1][i%C]), i, i+C)]
    if i%C+1<C: E += [(max(M[i//C][i%C], M[i//C][i%C+1]), i, i+1)]
U = UFDS(N); G = [[] for _ in range(N)]
for w, a, b in sorted(E):
    if U.union(a, b): G[a] += [(b, w)]; G[b] += [(a, w)]
root = 0
tin = [0]*N
tout = [0]*N
L = (N-1).bit_length()+1
D = [[0]*L for _ in range(N)]
jmp = [[-1]*L for _ in range(N)]
stk = [(0, 0, 0, T:=0)]
while stk:
    u, p, w, b = stk.pop()
    if b: tout[u] = (T:=T+1)
    else:
        tin[u] = (T:=T+1); stk.append((u, p, w, 1)); jmp[u][0] = p; D[u][0] = w
        for i in range(1, L):
            jmp[u][i] = jmp[jmp[u][i-1]][i-1]
            D[u][i] = max(D[u][i-1], D[jmp[u][i-1]][i-1])
        for v, w in G[u]:
            if v != p: stk.append((v, u, w, 0))
def lca(a, b):
    if tin[a] <= tin[b] < tout[b] <= tout[a]: return a
    if tin[b] <= tin[a] < tout[a] <= tout[b]: return b
    for i in range(L-1, -1, -1):
        j = jmp[a][i]
        if tin[j] > tin[b] or tout[b] > tout[j]: a = j
    return jmp[a][0]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    a = r1*C+c1-C-1; b = r2*C+c2-C-1
    if a == b: print(M[r1-1][c1-1]); continue
    d = lca(a, b); z = 0
    for u in (a, b):
        for l in range(L-1, -1, -1):
            j = jmp[u][l]
            if tin[j] > tin[d]: z = max(z, D[u][l]); u = j
        if u != d: z = max(z, D[u][0])
    print(z)