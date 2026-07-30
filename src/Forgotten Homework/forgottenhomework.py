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

M = 10**9+7
n, i, j = map(int, input().split())
A = [i==j, *map(int, input().split())]
Z = berlekamp_massey(A)
print(sum(Z[i]*A[~i] for i in range(len(Z)))%M)