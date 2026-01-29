n, p, k = map(int, input().split()); M, P, Q = 10**9+7, 39582418599937, 79164837199873; R = pow(P, -1, Q)

def mult(p1, p2, M):
    R = [1, 1]
    def ntt(P, M):
        n = len(P); L = len(bin(n))-3; Z = [0]*n; k = 1
        while len(R) < n:
            u = pow(5, M//(2*len(R)), M)
            for i in range(len(R), 2*len(R)): R.append(R[i//2]*(u if i&1 else 1)%M)
        for i in range(n): Z[i] = (Z[i//2]|(i&1)<<L)//2
        P = [P[r] for r in Z]
        while k < n:
            for i in range(0, n, 2*k):
                for j in range(k): z = R[j+k]*P[i+j+k]%M; P[i+j+k] = (P[i+j]-z)%M; P[i+j] = (P[i+j]+z)%M
            k <<= 1
        return P
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2)); ntt1 = ntt(p1, M); ntt2 = ntt(p2, M)
    z = pow(n, -1, M); ret = ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)], M)[:m]
    while len(ret) > p: ret[~p] = (ret[~p]+ret[-1])%M; ret.pop()
    return ret

def mul(p1, p2):
    if sum(p2) < 11:
        C = [0]*(len(p1)+len(p2)-1)
        for i in range(len(p2)):
            if not p2[i]: continue
            for j in range(len(p1)): C[i+j] += p2[i]*p1[j]; C[i+j] %= M
        while len(C) > p: C[~p] = (C[~p]+C[-1])%M; C.pop()
        return C
    z = [(a+(b-a)*R%Q*P)%M for a, b in zip(mult(p1, p2, P), mult(p1, p2, Q))]
    while len(p1)>1 and p1[-1] == 0: p1.pop()
    while len(p2)>1 and p2[-1] == 0: p2.pop()
    return z

if n == 1: print(sum(i%p==k for i in range(10))); exit()
if p%2<1 or p%5<1: print(sum(i%p==k for i in range(1, 10))*pow(10, ~-n//2, M)%M); exit()
w = [(pow(10, i, p)+pow(10, (n-i-1)%(p-1), p))%p for i in range(p-1)]; L = [0]*p; C = [*L]
for i in range(1, 10): L[w[0]*i%p] += 1
if n%2:
    t = pow(10, n//2, p)
    for i in range(10): C[t*i%p] += 1
else: C[0] += 1
L = mul(L, C); D = [[0]*p for _ in range(p-1)]; H = ~-n//2; B = [1]; N = H//~-p
for i in range(p-1):
    for j in range(10): D[i][w[i]*j%p] += 1
for d in D: B = mul(B, d)
while N:
    if N%2: L = mul(L, B)
    B = mul(B, B); N >>= 1
for i in range(H%~-p-n%2): L = mul(L, D[i+1])
print(L[k])