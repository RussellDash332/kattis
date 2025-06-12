import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N, M = map(int, input().split()); Z = [*map(int, input().split())]; L = [[] for _ in range(N)]; G = [[] for _ in range(N)]; E = []; S = [-1]*N; U = [-1]*N; l = [-1]*N; h = [-1]*N; p = [-1]*N; R = [[] for _ in range(N)]; C = 0; A = [-1]*N; I = [-1]*N; B = [[] for _ in range(N)]; T = [[] for _ in range(N)]; D = [-1]*N; s1 = [0]; s2 = []; sf = []; Q = [0]; X = [10**9]*N; X[0] = 0; P = [0]; V = [0]*N; V[0] = 1
for _ in range(M): a, b = map(int, input().split()); L[a:=a-1].append(b:=b-1); L[b].append(a); E.append((a, b))
for u in Q:
    for v in L[u]:
        if X[v] == 10**9: X[v] = X[u]+1; Q.append(v)
for u in range(N):
    for v in L[u]:
        if X[u]+1 == X[v]: G[u].append(v)
while s1:
    v, b = divmod(s1.pop(), 2)
    if b:
        for u in s2.pop(): p[A[u]] = A[v]
    elif A[v] == -1:
        A[v] = l[C] = S[C] = U[C] = C; h[C] = v; C += 1; tmp = []; s1.append(2*v+1)
        for u in G[v]:
            if A[u] == -1: s1.append(2*u); tmp.append(u)
        s2.append(tmp)
for i in range(N):
    for j in G[i]: R[A[j]].append(A[i])
def find(v):
    sf.append(2*v); z = -1
    while U[v:=sf[-1]>>1] != v: sf.append(2*U[v]+1)
    while sf:
        v, c = divmod(sf.pop(), 2)
        if U[v] == v: z = -1 if c else v
        elif z < 0: z = v
        else: l[v] = l[U[v] if S[l[v]] > S[l[U[v]]] else v]; U[v] = z; z = z if c else l[v]
    return z
for t1 in range(C-1, -1, -1):
    for t2 in R[t1]: S[t1] = min(S[t1], S[find(t2)])
    if t1: B[S[t1]].append(t1)
    for t2 in B[t1]: v = find(t2); I[t2] = S[t2] if S[v]==S[t2] else v
    if t1: U[t1] = p[t1]
for t in range(1, C):
    if I[t] != S[t]: I[t] = I[I[t]]
for t in range(1, C): D[h[t]] = h[I[t]]
D[0] = 0
for v in range(1, N): T[D[v]].append(v)
for u in P:
    for v in G[u]:
        if not V[v]: V[v] = 1; P.append(v)
while P:
    u = P.pop()
    for v in T[u]: Z[u] += Z[v]
for a, b in E:
    if X[a]+1 == X[b] and D[b] == a: sys.stdout.write(str(Z[b])+'\n')
    elif X[b]+1 == X[a] and D[a] == b: sys.stdout.write(str(Z[a])+'\n')
    else: sys.stdout.write('0\n')