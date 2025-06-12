from array import *
M = 998244353; R = array('I', [1])
def ntt(P):
    n = k = len(P); P = [*P]; Z = [0]*n
    while 2*len(R) < n: u = pow(3, M//(4*len(R)), M); R.extend([r*u%M for r in R])
    while k > 1:
        for i in range(n//k):
            r = R[i]
            for j in range(i*k, i*k+k//2): z = r*P[j+k//2]; P[j+k//2] = (P[j]-z)%M; P[j] = (P[j]+z)%M
        k >>= 1
    for i in range(1, n): Z[i] = Z[i//2]//2+(i&1)*n//2
    return [P[r] for r in Z]
def mult(p1, p2):
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2)); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); r = ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]
    while r and r[-1] == 0: r.pop()
    return r
def add(p1, p2):
    p = [0]*max(len(p1), len(p2))
    for i in range(len(p1)): p[i] += p1[i]
    for i in range(len(p2)): p[i] += p2[i]
    return p
def f(a, b):
    Z = [[] for _ in range(9)]
    if b-a==1: Z[S[a]] = [0, 1]; return Z
    m = (a+b)//2; l = f(a, m); r = f(m, b)
    for i, j in K:
        Z[3*i+j] = add(l[3*i+j], r[3*i+j])
        for s in range(i, j+1):
            P = []
            for t in range(s, j+1): P = add(P, r[3*t+j])
            Z[3*i+j] = add(Z[3*i+j], mult(l[3*i+s], P))
    return Z
K = ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)); H = {'B':0, 'Y':1, 'R':2}; S = array('I', (4*H[i] for i in input())); D = f(0, N:=len(S)); Z = []; F = array('I', [1]); I = array('I', [1]); A = N
for i in range(N): F.append(F[-1]*(i+1)%M); I.append(I[-1]*pow(i+1, -1, M)%M)
for i, j in K: Z = add(Z, D[3*i+j])
for i in range(len(Z)): A -= Z[i]*F[i]*F[N-i]*I[N]; A %= M
print(A)