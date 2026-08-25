N = int(input()); M = 10**9+7; V = [1, 1, 2, 6, 14]
if N < 5: print(V[N]); exit()
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
print(mul(matpow([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [-1, 0, 2, 0, 2]], N-4), [[i] for i in V])[4][0])