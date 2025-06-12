n, K = map(int, input().split()); M = 10**9+7

from collections import defaultdict
sup = lambda: defaultdict(lambda: 0)

def mul(a, b):
    c = defaultdict(sup)
    for i in a:
        for k in a[i]:
            for j in b[k]: c[i][j] += a[i][k]*b[k][j]; c[i][j] %= M
    return c

def pow(mat, n):
    if n == 1: return mat
    if n % 2: return mul(pow(mat, n-1), mat)
    return pow(mul(mat, mat), n//2)

Z = defaultdict(sup); H = []
for i in range(1<<n): Z[i][i] = 1
for v in (0, 1):
    A = defaultdict(sup)
    for i in range(1<<n):
        for j in range(1<<n-1):
            bm = (v<<n)|(2*j)|(bin(j).count('1')%2); nxt = i; ok = 1
            for k in range(n):
                if (bm>>k)%2 > (bm>>k+1)%2 == (i>>k)%2: ok = 0; break
                if (bm>>k)%2 < (bm>>k+1)%2: nxt |= 1<<k
            if ok: A[i][nxt] += 1
    H.append(A)
for v in map(int, input()): Z = mul(Z, H[v])
print(pow(Z, K)[0][(1<<n)-1])