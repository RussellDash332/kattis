def pu(i, x):
    i += n; A[i] = x
    while i > 1: i >>= 1; A[i] = min(A[i<<1], A[(i<<1)+1])
def rq(i, j):
    i += n; j += n; x = 10**18
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = min(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = min(x, A[j-1]); j >>= 1
    return x
def get(x, y):
    xa = []; ya = []; z = 10**18; ac = -1; ox = x; oy = y
    while x != -1: xa.append(x); x = par[chn[x]]
    while y != -1: ya.append(y); y = par[chn[y]]
    while xa and ya and chn[xa[-1]] == chn[ya[-1]]:
        if pos[xa[-1]] < pos[ya[-1]]: ac = xa[-1]
        else: ac = ya[-1]
        xa.pop(); ya.pop()
    for x in (ox, oy):
        while chn[x] != chn[ac]: z = min(z, rq(pos[chn[x]], pos[x]+1)); x = par[chn[x]]
        z = min(z, rq(pos[ac]+1, pos[x]+1))
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
n, m, q = map(int, input().split()); E = []; G = [{} for _ in range(n)]; U = UFDS(n)
for _ in range(m): u, v, t = map(int, input().split()); E.append((-t, u-1, v-1))
for w, a, b in sorted(E):
    if U.find(a) != U.find(b): G[a][b] = G[b][a] = -w; U.union(a, b)
sz = [1]*n; par = [0]*n; pos = [0]*n; chn = [0]*n; A = [10**18]*2*n; Q = [(0, -1, 0)]; S = [(0, 0, 0, 10**18)]; cur = X = 0
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
    v, p, t, x = S.pop(); pos[v] = cur; cur += 1; chn[v] = t; best = hvy = -1; pu(pos[v], x)
    for w in G[v]:
        if w != p and sz[w] > best: best = sz[w]; hvy = w
    if hvy == -1: continue
    for w in G[v]:
        if p != w != hvy: S.append((w, v, w, G[v][w]))
    S.append((hvy, v, t, G[v][hvy]))
for _ in range(q): a, b, h = map(int, input().split()); a ^= X; b ^= X; h ^= X; z = get(a-1, b-1) >= h; X += z; sys.stdout.write('NJeeibbbb\n\n'[z::2])