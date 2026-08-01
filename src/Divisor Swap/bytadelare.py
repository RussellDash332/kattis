N, X, *A = map(int, open(0).read().split())
G = [[] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i]%A[j]<1 or A[j]%A[i]<1: G[i] += [j]; G[j] += [i]
B = [0]*N; V = [0]*N; M = []; C = [*range(N)]
for i in range(N):
    if V[i]: continue
    Q = [i]; V[i] = 1; P = {i:-1}
    for u in Q:
        for v in G[u]:
            if V[v] < 1: V[v] = 1; Q.append(v); P[v] = u
    for i, k in zip(sorted(Q, key=lambda x: A[x]), sorted(Q)): B[i] = k
    for u in Q[::-1]:
        p = next(x for x in Q if C[x] == B[u])
        if u == p: continue
        E, c = [], u
        while ~c: E += [c]; c = P[c]
        F, c = [], p
        while ~c: F += [c]; c = P[c]
        e, f = len(E)-1, len(F)-1
        while e >= 0 and f >= 0 and E[e] == F[f]: e -= 1; f -= 1
        pt = E[:e+2]+F[:f+1][::-1]
        for k in range(len(pt)-2, -1, -1): x, y = pt[k], pt[k+1]; A[C[x]], A[C[y]] = A[C[y]], A[C[x]]; C[x], C[y] = C[y], C[x]; M.append((C[x]+1, C[y]+1))
if any(a>b for a,b in zip(A, A[1:])): print('NEJ'); exit()
print('JA')
if X:
    print(len(M))
    for i in M: print(*i)