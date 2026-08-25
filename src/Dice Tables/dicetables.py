def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i, ci in enumerate(c):
        for j, ax in enumerate(a[i]):
            for k, by in enumerate(b[j]): ci[k] = (ci[k]+ax*by)%M
    return c
def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(len(m))] for i in range(len(m))]
    if k%2: return mul(matpow(m, k-1), m)
    return matpow(mul(m, m), k//2)
M = 10**9+9; A = [[int(i==j) for j in range(20)] for i in range(20)]
for v, w in zip(map(int, input().split()), [4, 6, 8, 12, 20]): A = mul(matpow([[(j<=i<w) for j in range(20)] for i in range(20)], v), A)
print(sum(a[0] for a in A)%M)