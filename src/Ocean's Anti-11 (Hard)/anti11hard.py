MOD = 10**9+7; L = 11; R = range
def mul(a, b):
    c = [[0]*L for _ in R(L)]
    for i in R(L):
        for j in R(L):
            for k in R(L): c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= MOD
    return c
def mp(m, n):
    if n == 1: return m
    elif n % 2: return mul(m, mp(m, n-1))
    return mp(mul(m, m), n//2)
for _ in R(int(input())):
    n, b = input().strip().split(); M = [[0]*L for _ in R(L)]
    for i in R(len(b)):
        for c in '01':
            ll = 0
            for l in R(i, -1, -1):
                if b[l] == c and b[:l] == b[i-l:i]: ll = l+1; break
            M[i][ll] += 1
    print(sum(mp(M, int(n))[0][:len(b)])%MOD)