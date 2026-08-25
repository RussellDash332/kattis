n, p = map(float, input().split()); n = int(n)

if p == 1: print(5*(n//101)), exit(0)
if p == 0: print(5*n), exit(0)
c = [[0]*102 for _ in range(102)]
for i in range(101):
    m = p
    for j in range(1, i+1): c[i][i-j], m = m, m*(1-p)
    c[i][100], c[i][101] = m/p, 5*m/p
c[-1][-1] = 1

def mul(a, b):
    c = [[0]*102 for _ in range(102)]
    for i, ci in enumerate(c):
        for j, ax in enumerate(a[i]):
            for k, by in enumerate(b[j]): ci[k] += ax*by
    return c

def pow(mat, n):
    if n == 1: return mat
    if n % 2: return mul(pow(mat, n-1), mat)
    return pow(mul(mat, mat), n//2)

print(pow(c, n)[100][-1])