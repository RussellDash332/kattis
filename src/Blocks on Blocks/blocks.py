def mul(a, b):
    c = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            c[i][j] = 0
            for k in range(4): c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= 10000
    return c

def matpow(mat, n):
    if n == 1: return mat
    elif n % 2: return mul(mat, matpow(mat, n-1))
    return matpow(mul(mat, mat), n//2)

# https://oeis.org/A001169
def f(n):
    M = ((0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 4, -7, 5)); x = (1, 2, 6, 19)
    if n < 5: return x[n-1]
    A = matpow(M, n-4)[3]; return sum(A[i]*x[i] for i in range(4))%10000
for _ in range(int(input())): print(f'Case {_+1}:', f(int(input())))