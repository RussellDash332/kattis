N = int(input()); M = 10**9+7; V = [1, 1, 2, 6, 14]
if N < 5: print(V[N]); exit()
def mul(a, b):
    c = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)): c[i][j] = (c[i][j]+a[i][k]*b[k][j])%M
    return c
def matpow(m, k):
    if k == 0: return [[int(i==j) for j in range(len(m))] for i in range(len(m))]
    if k%2: return mul(matpow(m, k-1), m)
    return matpow(mul(m, m), k//2)
print(mul(matpow([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [-1, 0, 2, 0, 2]], N-4), [[i] for i in V])[4][0])