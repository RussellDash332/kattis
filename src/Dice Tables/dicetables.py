def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)): c[i][j] += a[i][k]*b[k][j]; c[i][j] %= M
    return c
def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(len(m))] for i in range(len(m))]
    if k%2: return mul(matpow(m, k-1), m)
    return matpow(mul(m, m), k//2)
M = 10**9+9; A = [[int(i==j) for j in range(20)] for i in range(20)]
for v, w in zip(map(int, input().split()), [4, 6, 8, 12, 20]): A = mul(matpow([[(j<=i<w) for j in range(20)] for i in range(20)], v), A)
print(sum(a[0] for a in A)%M)