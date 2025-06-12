from array import *
M = 998244353; R = array('I', [1])
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
    if min(len(p1), len(p2)) < 16:
        q = [0]*m
        for i in range(len(p1)):
            for j in range(len(p2)): q[i+j] += p1[i]*p2[j]; q[i+j] %= M
        return q
    while n < m: n *= 2
    p1.extend([0]*(n-len(p1))); p2.extend([0]*(n-len(p2))); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); r = array('I', ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m])
    while p1[-1] == 0: p1.pop()
    while p2[-1] == 0: p2.pop()
    while r[-1] == 0: r.pop()
    return r

def polypow(p, k):
    if k == 0: return [1]
    m = k*len(p)-k+1; n = 1
    while n < m: n *= 2
    p.extend([0]*(n-len(p))); t = ntt(p)
    while p[-1] == 0: p.pop()
    z = pow(n, -1, M); r = array('I', ntt([pow(t[-i], k, M)*z%M for i in range(n)])[:m])
    while r[-1] == 0: r.pop()
    return r

n = int(input()); e = [0]+[1]*9; z = 0
if n == 1: print(10); exit()
p = polypow([1]*10, (n+1)//2-1)
if n%2 == 0: q = mult(p, [1]*10)[::-1]
else: q = p[::-1]
for i in mult(mult(p, q), e): z = (z+i*i)%M
print(z)