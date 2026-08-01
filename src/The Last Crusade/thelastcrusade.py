'''
https://oeis.org/A055290 tells us f(n, k) = number of trees with n nodes and k leaves (= 0 if k < 2)
Essentially f(n, k) = number of trees with complexity rating n and safety rating k
So what we want is sum(f(n, k) for n in [S, S2] for k in [C, C2])
'''

def berlekamp_massey(S):
    C = [1]; B = [1]; L = 0; m = b = 1
    for n, s in enumerate(S):
        if (d:=(s+sum(C[i]*S[n-i] for i in range(1, L+1)))%M):
            T = C[:]; c = d*pow(b, -1, M)%M; C.extend([0]*(len(B)+m-len(C)))
            for i in range(len(B)): C[i+m] = (C[i+m]-c*B[i])%M
            if 2*L > n: m += 1
            else: L = n+1-L; B = T; b = d; m = 1
        else: m += 1
    return [-x%M for x in C[1:]]

def kitamasa(c, a, n):
    k = len(c)
    def m(x, y):
        z = [0]*(2*k+1)
        for i in range(k+1):
            if x[i]:
                for j in range(k+1): z[i+j] = (z[i+j]+x[i]*y[j])%M
        for i in range(2*k, k, -1):
            if z[i]:
                for j in range(k): z[i-j-1] = (z[i-j-1]+z[i]*c[j])%M
        return z[:k+1]
    b = [0, 1]+[0]*~-k; v = [1]+[0]*k; n += 1
    while n:
        if n%2: v = m(v, b)
        b = m(b, b); n >>= 1
    return sum(x*y for x,y in zip(a,v[1:]))%M

C, C2, S, S2 = map(int, input().split()); M = 10**9+7
A = [[], [0,1]+[0]*3, [0]+[1]*4, [0]*4+[1,1,2,3,4,5,7,8], [0]*5+[1,2,4,8,14,23,36,54,78,110,150,201,264,341,433,544,674,827], [0]*6+[1,2,6,14,32,64,123,219,377,616,978,1496,2236,3251,4637,6475,8899,12025,16036,21091,27432,35271,44920,56656,70873,87924,108298,132438,160943,194358,233408]]
Z = (S==1)*(C<2)
if C<2: C += 1
for k in range(S, S2+1): Z = (Z+kitamasa(c:=berlekamp_massey(p:=[s:=0]+[s:=s+i for i in A[k]]), p, C2+1)-kitamasa(c, p, C))%M
print(Z)