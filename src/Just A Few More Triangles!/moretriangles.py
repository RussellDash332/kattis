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
def sq(p):
    m = 2*len(p)-1; n = 1
    while n < m: n *= 2
    p += [0]*(n-len(p)); t = ntt(p); z = pow(n, -1, M); return ntt([t[-i]**2%M*z%M for i in range(n)])[:m]
n = int(input()); A = [0]*n
for i in range(1, n): A[i**2%n] += 1
P = sq(A); B = [0]*n; C = [0]*n
for i in range(len(P)): B[i%n] += P[i]
for i in range(n): B[2*i%n] -= A[i]; C[2*i%n] += A[i]
print(sum(A[i]*(B[i]//2+C[i]) for i in range(n)))