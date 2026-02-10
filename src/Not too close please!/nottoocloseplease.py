import sys, os, io; from array import *
c = r = 0; R = array('I'); F = R.append
for i in os.read(0, os.fstat(0).st_size):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0
N, Q = R[0], R[1]; z = 1
G = [[] for _ in range(N)]
for _ in range(N-1): a = R[z:=z+1]-1; b = R[z:=z+1]-1; G[a].append(b); G[b].append(a)
M = 10**9+7
F = array('I', [f:=1]+[f:=f*-~i%M for i in range(N)])
I = array('I', [f:=pow(f, -1, M)]+[f:=f*(N-i)%M for i in range(N)])
B = array('I', [0, 1])
for _ in range(N): B.append((B[-1]+B[-2])%M)
T = [[] for _ in range(N)]
q = array('I', [0]); U = array('I', [0]*N); U[0] = 1; d = 0; E = array('I', [0]*N); H = array('I')
sz = array('I', [1]*N); par = array('i', [-1]*N); pos = array('I', [0]*N); chn = array('I', [0]*N); A = array('I', [10**9]*2*N)
while q:
    u = q.pop(); E[u] = d; d += 1; H.append(u)
    for v in G[u]:
        if U[v]<1: U[v] = U[u]+1; par[v] = u; T[u].append(v); q.append(v)
U = array('I', [i-1 for i in U]); S = [(0, 0, 0)]; cur = 0
for i in range(N):
    for j in G[H[~i]]: sz[H[~i]] += sz[j]
def pu(i, x):
    i += N; A[i] = x
    while i > 1: i >>= 1; A[i] = min(A[i<<1], A[(i<<1)+1])
def rq(i, j):
    i += N; j += N; x = 10**9
    while i < j:
        if (i^1)&1: i >>= 1
        else: x = min(x, A[i]); i = (i>>1)+1
        if (j^1)&1: j >>= 1
        else: x = min(x, A[j-1]); j >>= 1
    return x
def L(x, y):
    xa = []; ya = []; z = 10**9; ac = -1; ox = x; oy = y
    while x != -1: xa.append(x); x = par[chn[x]]
    while y != -1: ya.append(y); y = par[chn[y]]
    while xa and ya and chn[xa[-1]] == chn[ya[-1]]:
        if pos[xa[-1]] < pos[ya[-1]]: ac = xa[-1]
        else: ac = ya[-1]
        xa.pop(); ya.pop()
    for x in (ox, oy):
        while chn[x] != chn[ac]: z = min(z, rq(pos[chn[x]], pos[x]+1)); x = par[chn[x]]
        z = min(z, rq(pos[ac], pos[x]+1))
    return H[z]
while S:
    v, p, t = S.pop(); pos[v] = cur; cur += 1; chn[v] = t; best = hvy = -1; pu(pos[v], E[v])
    for w in G[v]:
        if w != p and sz[w] > best: best = sz[w]; hvy = w
    if hvy == -1: continue
    for w in G[v]:
        if p != w != hvy: S.append((w, v, w))
    S.append((hvy, v, t))
for _ in range(Q):
    if R[z:=z+1] == 1: x = R[z:=z+1]-1; y = R[z:=z+1]-1; r = R[z:=z+1]; n = U[x]+U[y]-2*U[L(x, y)]+1; sys.stdout.write(str(0 if n+1 < 2*r else F[n-r+1]*I[~r]*I[2*r-n-2]%M)+'\n')
    else:
        m = R[z:=z+1]-1; t = sorted((R[z:=z+1]-1 for _ in range(m+1)), key=lambda x: E[x]); v = {*t}
        for i in range(m): v.add(L(t[i], t[i+1]))
        v = sorted(v, key=lambda x: E[x]); w = len(v); V = [[] for _ in range(w)]; W = {e:i for i,e in enumerate(v)}; D = [[1, 1] for _ in range(w)]
        for i in range(w-1): V[W[L(v[i], v[i+1])]].append(W[v[i+1]])
        for i in range(w-1, -1, -1):
            for j in V[i]: d = U[v[j]]-U[v[i]]; x, y = D[j]; D[i][0] *= x*B[d+1]+y*B[d]; D[i][0] %= M; D[i][1] *= x*B[d]+y*B[d-1]; D[i][1] %= M
        sys.stdout.write(str((D[0][0]+D[0][1])%M)+'\n')