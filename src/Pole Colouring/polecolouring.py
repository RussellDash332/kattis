k = int(input())
m = 10**9+7
n = 8
M = [[0]*8 for _ in range(8)]
for r in range(2):
    for b in range(2):
        for wk in range(2):
            for r2 in range(2):
                for b2 in range(2):
                    for wk2 in range(2):
                        M[4*r+2*b+wk][4*r2+2*b2+wk2] = [
                            2,      # green or yellow
                            2,      # black or white
                            1,      # blue
                            0,      # impossible
                            1,      # red
                            0, 0, 0 # impossible
                        ][(r-r2)%2*4+(b-b2)%2*2+(wk-wk2)%2]

def mul(a, b, p):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n): c[i][j] += a[i][k]*b[k][j]; c[i][j] %= p
    return c

def matpow(m, k, p):
    if k == 0: return [[(i==j) for j in range(n)] for i in range(n)]
    if k%2: return mul(matpow(m, k-1, p), m, p)
    s = mul(m, m, p); return matpow(s, k//2, p)

print(matpow(M, k, m)[0][2])