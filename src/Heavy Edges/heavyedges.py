import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
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
N, M = map(int, input().split()); E = {}
for _ in range(M):
    a, b, w = map(int, input().split()); a -= 1; b -= 1
    if w not in E: E[w] = []
    E[w].append((min(a, b), max(a, b)))
def bridge(G):
    N = len(G); T = 0; V = [0]*N; D = [-1]*N; L = [-1]*N; X = [0]*N; B = 0
    for i in range(N):
        if not V[i]:
            S = [(2*i, -1)]
            while S:
                vs, p = S.pop(); v, s = divmod(vs, 2)
                if s&1: L[v] = min(L[v], L[p]); B += (L[p]>D[v])*(G[v][p]==1)
                else:
                    if V[v]: S.pop(); continue
                    if p != -1: X[p] += 1
                    V[v] = 1; D[v] = L[v] = T; T += 1
                    for to in G[v]:
                        if to == p: continue
                        if V[to]: L[v] = min(L[v], D[to])
                        else: S.append((vs^1, to)); S.append((2*to, v))
    return B
U = UFDS(N); Z = M
for w in sorted(E):
    F = []; H = {}
    for a, b in E[w]:
        a = U.find(a); b = U.find(b)
        if a not in H: H[a] = len(H)
        if b not in H: H[b] = len(H)
        F.append((a, b))
    G = [{} for _ in range(len(H))]
    for a, b in F:
        U.union(a, b)
        if H[a] == H[b]: continue
        if H[b] not in G[H[a]]: G[H[a]][H[b]] = G[H[b]][H[a]] = 0
        G[H[a]][H[b]] += 1; G[H[b]][H[a]] += 1
    Z -= bridge(G)
print(Z)