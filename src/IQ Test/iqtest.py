def berlekamp_massey(S):
    C = [1]; B = [1]; L = 0; m = b = 1
    for n, s in enumerate(S):
        if abs(d:=(s+sum(C[i]*S[n-i] for i in range(1, L+1)))) > 1e-8:
            T = C[:]; c = d/b; C.extend([0]*(len(B)+m-len(C)))
            for i in range(len(B)): C[i+m] -= c*B[i]
            if 2*L > n: m += 1
            else: L = n+1-L; B = T; b = d; m = 1
        else: m += 1
    return [round(-x) for x in C[1:]]

for _ in range(int(input())):
    n, *v = map(int, input().split()); Z = berlekamp_massey(v)
    print(sum(Z[i]*v[~i] for i in range(len(Z))))