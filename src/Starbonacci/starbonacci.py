def mult(A, B):
    C = [0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        if A[i]:
            for j in range(len(B)): C[i+j] += A[i]*B[j]; C[i+j] %= M
    return C
def rem(A, B):
    Z = [*A]
    for i in range(len(Z)-1, len(B)-2, -1):
        if Z[i]:
            for j in range(len(B)): Z[k:=i+j-len(B)+1] -= Z[i]*B[j]; Z[k] %= M
    while Z and Z[-1] == 0: Z.pop()
    return Z
def kitamasa(c, a, n):
    d = [1]; x = [0, 1]; f = [-i for i in c[::-1]]+[1]
    while n:
        if n%2: d = rem(mult(d, x), f)
        n >>= 1; x = rem(mult(x, x), f)
    return sum(p*q for p,q in zip(a,d))%M
M = 10**9+7; N, K = map(int, input().split()); K -= 1
print(kitamasa([1]*K, [0]*~-K+[1], N+K-2))