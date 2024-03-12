import sys; input = sys.stdin.readline
n, m = map(int, input().split())
c = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]; A = []; B = []
for _ in range(n): d1, m1, d2, m2, *f = map(int, input().split()); A.append([*f, (c[m2-1]+d2-c[m1-1]-d1)%365]); B.append(A[-1].copy())

def list_pivots(A, M):
    def leading_entry_col(A, r):
        row = A[r]; i = 0
        while i < len(A[0]) and row[i]%M == 0: i += 1
        return i
    res = []
    for r in range(len(A)):
        k = leading_entry_col(A, r)
        if k != len(A[0]): res.append((r, k))
    return sorted(res, reverse=True)
def rref(A, M):
    def col(A, i): return list(map(lambda x: x[i], A))
    def ero1(A, i, c):
        for j in range(len(A[0])): A[i][j] *= c; A[i][j] %= M
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]; A[i][k] %= M
    def ero3(A, i, j): A[i], A[j] = A[j], A[i]
    curr_col = curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A):
        if A[curr_row][curr_col]%M == 0:
            check_col = col(A, curr_col)[curr_row+1:]
            for i in range(len(check_col)):
                if check_col[i]%M != 0: break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
            else: curr_col += 1
        else:
            if A[curr_row][curr_col]%M != 0: ero1(A, curr_row, pow(A[curr_row][curr_col], -1, M))
            for i in range(curr_row+1, len(A)):
                if A[i][curr_col]%M != 0: ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1
            curr_row += 1
    pivots = list_pivots(A, M)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    for i in range(len(A)):
        for j in range(len(A[0])): A[i][j] %= M
    return A

def bz(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bz(b, a%b); return (q, p-q*(a//b))
def crt(a, m, b, n):
    return (a-m*bz(m, n)[0]*(a-b))%365

m5 = [0]*m; m73 = [0]*m
r5 = rref(A, 5); r73 = rref(B, 73)
p5 = set(); p73 = set()
for _, cc in list_pivots(r5, 5): p5.add(cc)
for _, cc in list_pivots(r73, 73): p73.add(cc)
for i in range(n):
    for j in range(m):
        if r5[i][j] and j in p5: m5[j] = r5[i][m]
        if r73[i][j] and j in p73: m73[j] = r73[i][m]
for i in range(m): print(365-(365-crt(m5[i], 5, m73[i], 73))%365)