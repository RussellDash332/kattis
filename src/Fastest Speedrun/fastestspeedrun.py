class UFDS:
    def __init__(s, N): s.p = [*range(N)]; s.r = [0]*N
    def find(s, i):
        if s.p[i] == i: return i
        s.p[i] = s.find(s.p[i]); return s.p[i]
    def union(s, i, j):
        if (x:=s.find(i)) != (y:=s.find(j)):
            if s.r[x] > s.r[y]: s.p[y] = x
            else: s.p[x] = y; s.r[y] += s.r[x] == s.r[y]
import os; c = r = 0; O = []; F = O.append
for i in os.read(0, os.fstat(0).st_size):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0
N = O[0]+1; p = 0; T = [[] for _ in range(N)]; INF = 10**18; W = [0]*N; L = [0]*N; C = [None]*N; Z = 0; U = UFDS(N)
for i in range(1, N):
    x = O[p:=p+1]; f = O[p:=p+1]
    for j in range(N): T[i].append((O[p:=p+1], j))
    T[i].append((f, x))
while 1:
    r = U.find(0); D = []; S = [0]*N; S[r] = 1; q = 2; Y = [0]*N
    for v in range(N):
        if v == U.find(v): W[v] = INF if v != r else 0; C[v] = None
    for v in range(N):
        while T[v] and U.find(v) == U.find(T[v][-1][1]): T[v].pop()
        if T[v]:
            w, u = T[v][-1]; c = w-L[v]; x = U.find(v)
            if W[x] > c: W[x] = c; C[x] = (u, v)
    for v in range(N):
        if v == U.find(v) and not S[v]:
            u = v; s = []
            while not S[u]: S[u] = q; s.append(u); u = U.find(C[u][0])
            if S[u] == q:
                Y[u] = 1; c = [u]
                while s[-1] != u: Y[s[-1]] = 1; c.append(s.pop())
                D.append(c)
            q += 1
    if not D:
        for v in range(N):
            if v == U.find(v): Z += W[v]
        break
    for v in range(N):
        if Y[x:=U.find(v)]:
            if v == x: Z += W[v]
            L[v] += W[x]
    for k in D:
        for c in k: U.union(k[0], c)
print(Z)