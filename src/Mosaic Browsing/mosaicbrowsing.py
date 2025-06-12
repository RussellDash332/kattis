import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from random import *; from array import *
M = 998244353; R = array('I', [1])
def ntt(P):
    n = k = len(P); Z = [0]*n
    while 2*len(R) < n: u = pow(3, M//(4*len(R)), M); R.extend([r*u%M for r in R]) # 3 is a primitive root of M
    while k > 1:
        for i in range(n//k):
            r = R[i]
            for j in range(i*k, i*k+k//2): z = r*P[j+k//2]; P[j+k//2] = (P[j]-z)%M; P[j] = (P[j]+z)%M
        k >>= 1
    for i in range(1, n): Z[i] = Z[i//2]//2+(i&1)*n//2
    return array('I', (P[r] for r in Z))
def mult(p1, p2):
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1.extend([0]*(n-len(p1))); p2.extend([0]*(n-len(p2))); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]
rp, cp = map(int, input().split()); P = array('B')
for _ in range(rp): P.extend(map(int, input().split()))
rq, cq = map(int, input().split()); Q = array('I')
if rp > rq or cp > cq: print(0); exit()
for _ in range(rq): Q.extend(map(int, input().split()))
S = 0; A = array('I', [0]*rp*cq); p = 0
for r in range(rp):
    for c in range(cp): x = randint(2, 10**5); S += P[p]**2*x; A[~(r*cq+c)] = P[p]*x; p += 1
X = mult(A, Q); Z = array('I')
for r in range(rp, rq+1):
    for c in range(cq-cp+1):
        if X[r*cq+c-1] == S%M: Z.append((r-rp+1)*1002+c+1)
print(len(Z))
for rc in Z: sys.stdout.write(f'{rc//1002} {rc%1002}\n')