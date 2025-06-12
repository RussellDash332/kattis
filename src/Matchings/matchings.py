import sys; input = sys.stdin.readline
M = 998244353; R = [1]
def ntt(P):
    n = k = len(P); P = [*P]; Z = [0]*n
    while 2*len(R) < n: u = pow(3, M//(4*len(R)), M); R.extend([r*u%M for r in R]) # 3 is a primitive root of M
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
    ntt1 = ntt(p1+[0]*(n-len(p1))); ntt2 = ntt(p2+[0]*(n-len(p2)))
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]
cp, rp = map(int, input().split()); P = [[*map(int, input().split())] for _ in range(rp)]
cq, rq = map(int, input().split()); Q = [[*map(int, input().split())] for _ in range(rq)]
V = [0]*((rp+rq)*cq-1); A = [0]*rp*cq; B = [0]*rq*cq
for r in range(rp):
    for c in range(cp): A[~(r*cq+c)] = P[r][c]
for r in range(rq):
    for c in range(cq): B[r*cq+c] = Q[r][c]
X = mult(A, B)
for i in range(len(V)): V[i] += X[i]
for r in range(rp):
    for c in range(cp): A[~(r*cq+c)] ^= 1
for i in range(len(B)): B[i] ^= 1
X = mult(A, B); Z = 0
for i in range(len(V)): V[i] += X[i]
for c in range(cq-cp+1):
    for r in range(rq-rp+1): Z = max(Z, V[(r+rp)*cq+c-1])
for c in range(cq-cp+1):
    for r in range(rq-rp+1):
        if Z == V[(r+rp)*cq+c-1]: print(c, r)