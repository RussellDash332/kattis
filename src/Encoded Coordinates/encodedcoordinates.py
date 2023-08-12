def mul(a, b, p): # 4x4
    c = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            c[i][j] = a[i][0]*b[0][j]
            for k in range(1, 4): c[i][j] += a[i][k]*b[k][j]
            c[i][j] %= p
    return c
def matpow(mat, n, p):
    if n == 0: return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    elif n == 1: return [[mat[i][j]%p for j in range(4)] for i in range(4)]
    elif n % 2: return mul(mat, matpow(mat, n-1, p), p)
    return matpow(mul(mat, mat, p), n//2, p)
for _ in range(int(input())):
    p = int(input())
    ax, bx, cx, kx, nx = map(int, input().split())
    ay, by, cy, ky, ny = map(int, input().split())
    x = int(input())
    matx = matpow([[0, 1, 1, 0], [kx, 0, 0, 1], [1, kx, 0, 0], [0, 0, 1, 0]], nx-1, p)[0]
    maty = matpow([[0, 1, 1, 0], [ky, 0, 0, 1], [1, ky, 0, 0], [0, 0, 1, 0]], ny-1, p)[0]
    val = set()
    for i in range(p):
        if (matx[0]*ax+matx[1]*bx+matx[2]*cx+matx[3]*i)%p == x: val.add((maty[0]*ay+maty[1]*by+maty[2]*cy+maty[3]*i)%p)
    if len(val) > 1: print('UNKNOWN')
    else: print(*val)