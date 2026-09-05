import sys, os
c = r = 0; W = []; F = W.append
for i in os.read(0, 9_670_067):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0
M = 998244353; R = [1]
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
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]
nP = W[0]
P = sorted(W[2:2+nP])
S = sorted(W[2+nP:]); S.append(10**6+1)
def f(b):
    m = b[0]; n = b[-1]-m+1; p = [0]*n
    for i in b: p[i-m] += 1
    return mult(p, p[::-1])[n:]
q = k = 0; Z = f(P)
for s in S:
    b = []
    while q < nP and P[q] < s: b.append(P[q]); q += 1
    if not b: continue
    for i, e in enumerate(f(b)): Z[i] -= e
for i in range(len(Z)):
    if Z[i]: sys.stdout.write(f'{i+1} {Z[i]}\n'); k = 1
if not k: print('none')