n = int(input()); MOD = 10**9+7
v = [0, 1, 1]
mat = [[0, 1, 0], [1, 1, 1], [0, 0, 1]]
def mul(a, b):
    return [[(a[i][0]*b[0][j]+a[i][1]*b[1][j]+a[i][2]*b[2][j])%MOD for j in range(3)] for i in range(3)]
def pow(mat, n):
    if n == 1: return mat
    if n % 2: return mul(mat, pow(mat, n-1))
    return pow(mul(mat, mat), n//2)
if n > 1: p = pow(mat, n-1); print((p[1][1]+p[1][2])%MOD)
else: print(1)