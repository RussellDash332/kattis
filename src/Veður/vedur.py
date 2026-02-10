def pu(i, x):
    i += n; A[i] = x
    while i > 1: i >>= 1; A[i] = max(A[i<<1], A[(i<<1)+1])
def rq(i, j):
    i += n; j += n; x = -10**9
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = max(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = max(x, A[j-1]); j >>= 1
    return x
def get(x, y):
    xa = []; ya = []; z = -10**9; ac = -1; ox = x; oy = y
    while x != -1: xa.append(x); x = par[chn[x]]
    while y != -1: ya.append(y); y = par[chn[y]]
    while xa and ya and chn[xa[-1]] == chn[ya[-1]]:
        if pos[xa[-1]] < pos[ya[-1]]: ac = xa[-1]
        else: ac = ya[-1]
        xa.pop(); ya.pop()
    for x in (ox, oy):
        while chn[x] != chn[ac]: z = max(z, rq(pos[chn[x]], pos[x]+1)); x = par[chn[x]]
        z = max(z, rq(pos[ac], pos[x]+1))
    return z

class UFDS:
    def __init__(s, N):
        s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
r, c = map(int, input().split()); n = r*c; m = [[*map(int, input().split())] for _ in range(r)]; G = [[] for _ in range(n)]; E = []; V = [m[i][j] for i in range(r) for j in range(c)]; K = ((0, -1), (-1, 0), (0, 1), (1, 0)); U = UFDS(n)
for i in range(r):
    for j in range(c):
        for di, dj in K:
            if r>i+di>-1<j+dj<c: E.append((max(V[i*c+j], V[(i+di)*c+j+dj]), i*c+j, (i+di)*c+j+dj))
for w, a, b in sorted(E):
    if U.find(a) != U.find(b): G[a].append(b); G[b].append(a); U.union(a, b)
sz = [1]*n; par = [0]*n; pos = [0]*n; chn = [0]*n; A = [-10**9]*2*n; Q = [(0, -1, 0)]; S = [(0, 0, 0)]; cur = 0
while Q:
    v, p, b = Q.pop()
    if b:
        for w in G[v]:
            if w != p: sz[v] += sz[w]
    else:
        par[v] = p; Q.append((v, p, 1))
        for w in G[v]:
            if w != p: Q.append((w, v, 0))
while S:
    v, p, t = S.pop(); pos[v] = cur; cur += 1; chn[v] = t; best = hvy = -1; pu(pos[v], V[v])
    for w in G[v]:
        if w != p and sz[w] > best: best = sz[w]; hvy = w
    if hvy == -1: continue
    for w in G[v]:
        if p != w != hvy: S.append((w, v, w))
    S.append((hvy, v, t))
for _ in range(int(input())): l1, d1, l2, d2 = map(int, input().split()); print(get(l1*c+d1-c-1, l2*c+d2-c-1))