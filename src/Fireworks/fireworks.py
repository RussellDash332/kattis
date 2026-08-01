M = 998244353; R = [1, 1]
def ntt(P):
    n = len(P); L = len(bin(n))-3; Z = [0]*n; k = 1
    while len(R) < n:
        u = pow(3, M//(2*len(R)), M) # 3 is a primitive root of M
        for i in range(len(R), 2*len(R)): R.append(R[i//2]*(u if i&1 else 1)%M)
    for i in range(n): Z[i] = (Z[i//2]|(i&1)<<L)//2
    P = [P[r] for r in Z]
    while k < n:
        for i in range(0, n, 2*k):
            for j in range(k): z = R[j+k]*P[i+j+k]%M; P[i+j+k] = (P[i+j]-z)%M; P[i+j] = (P[i+j]+z)%M
        k <<= 1
    return P
def mul(p1, p2):
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1 = p1+[0]*(n-len(p1)); p2 = p2+[0]*(n-len(p2)); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]
N, r, g = map(int, input().split())
S = input()
A, B, C = ([int(i==k) for i in S]for k in 'RGX')
RG = mul(A, B); RX = mul(A, C); GX = mul(B, C); XX = mul(C, C)
print(max(RG[i]+min(RX[i],g)+min(GX[i],r)+min(XX[i]//2,g-min(RX[i],g),r-min(GX[i],r)) for i in range(2*N-1)))