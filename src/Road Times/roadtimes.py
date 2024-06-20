import sys; input = sys.stdin.readline; from heapq import *; from array import *
C = []; V = int(input()); INF = 10**9; EPS = 1e-5; g = [{} for _ in range(V)]; R = {}; A = []; E = array('h')
for i in range(V):
    a = [*map(int, input().split())]
    for j in range(V):
        if a[j] > 0: g[i][j] = a[j]; R[(i, j)] = len(R); E.append(a[j])
for _ in range(int(input())):
    s, t, d = map(int, input().split()); D = array('i', [INF]*V); D[s] = 0; pq = [s]; a = array('i', [0]*len(R)); P = array('b', [-1]*V); p = t
    while pq:
        dd, vv = divmod(heappop(pq), V)
        if dd != D[vv]: continue
        for nn in g[vv]:
            if D[nn] > (new:=dd+g[vv][nn]): P[nn] = vv; D[nn] = new; heappush(pq, new*V+nn)
    while P[p] != -1: a[R[(P[p], p)]] = 1; d -= g[P[p]][p]; p = P[p]
    a.append(d); A.append(a); A.append(array('i', [-i for i in a]))
for i in range(len(R)): e = E[i]; a = [0]*len(R)+[e]; a[i] = 1; A.append(array('i', a))
for _ in range(int(input())):
    s, t = map(int, input().split()); D = array('i', [INF]*V); D[s] = 0; pq = [s]; c = array('b', [0]*len(R)); P = array('b', [-1]*V); p = t; z = 0
    while pq:
        dd, vv = divmod(heappop(pq), V)
        if dd != D[vv]: continue
        for nn in g[vv]:
            if D[nn] > (new:=dd+g[vv][nn]): P[nn] = vv; D[nn] = new; heappush(pq, new*V+nn)
    while P[p] != -1: c[R[(P[p], p)]] = 1; z += g[P[p]][p]; p = P[p]
    C.append((s, t, z, c))
m = len(A); n = len(A[0])-1; X = n+2; D0 = [0]*X*(m+2+2*len(C)); N = [*range(n)]+[-1]; B = [0]*m; D0[-X+n] = 1; r = 0
for i in range(m):
    for j in range(n): D0[i*X+j] = A[i][j]
    B[i] = n+i; D0[i*X+n] = -1; D0[i*X+X-1] = A[i][-1]
for i in range(1, m):
    if D0[i*X+X-1] < D0[r*X+X-1]: r = i
for i in range(len(C)):
    *_, c = C[i]
    for j in range(len(c)): D0[(m+2*i)*X+j] = c[j]; D0[(m+2*i+1)*X+j] = -c[j]

def pivot(D, N, B, r, s):
    k = 1/D[r*X+s]
    for i in range(len(D)//X):
        if i == r: continue
        for j in range(X):
            if j != s: D[i*X+j] -= D[r*X+j]*D[i*X+s]*k
    for i in range(X): D[r*X+i] *= k
    for i in range(len(D)//X): D[i*X+s] *= -k
    D[r*X+s] = k; B[r], N[s] = N[s], B[r]

def find(D, N, B, p):
    x = -p-1
    while True:
        s = r = -1
        for i in range(n+1):
            if (p==0 or N[i] != -1) and (s == -1 or D[x*X+i] < D[x*X+s] or (D[x*X+i]==D[x*X+s] and N[i] < N[s])): s = i
        if D[x*X+s] > -EPS: break
        for i in range(m):
            if D[i*X+s] > EPS and (r == -1 or D[i*X+X-1]/D[i*X+s] < D[r*X+X-1]/D[r*X+s] or (D[i*X+X-1]*D[r*X+s] == D[r*X+X-1]*D[i*X+s] and B[i] < B[r])): r = i
        pivot(D, N, B, r, s)

if D0[r*X+X-1] < -EPS: pivot(D0, N, B, r, n); find(D0, N, B, 0)
for i in range(m):
    if B[i] != -1: continue
    s = -1
    for j in range(n):
        if s == -1 or D0[i*X+j] < D0[i*X+s] or (D0[i*X+j] == D0[i*X+s] and N[j] < N[s]): s = j
    pivot(D0, N, B, i, s)
for i in range(len(C)): s, t, z, _ = C[i]; D = D0[:m*X]+D0[(m+2*i)*X:(m+2*i+1)*X]+D0[-X:]; find(D, array('h', N), array('h', B), 1); L = z-D[m*X+X-1]; D = D0[:m*X]+D0[(m+2*i+1)*X:(m+2*i+2)*X]+D0[-X:]; find(D, array('h', N), array('h', B), 1); H = z+D[m*X+X-1]; print(s, t, L, H)