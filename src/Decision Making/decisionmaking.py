n = int(input()); M = 998244353
S = [input() for _ in range(n)]
def rref(A):
    def equal(a, b): return a == b
    def leading_entry_col(A, r):
        row = A[r]; i = 0
        while i < len(A[0]) and equal(row[i], 0): i += 1
        return i
    def list_pivots(A):
        res = []
        for r in range(len(A)):
            k = leading_entry_col(A, r)
            if k != len(A[0]): res.append((r, k))
        return sorted(res, reverse=True)
    def col(A, i): return list(map(lambda x: x[i], A))
    def ero1(A, i, c):
        for j in range(len(A[0])): A[i][j] *= c; A[i][j] %= M
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]; A[i][k] %= M
    def ero3(A, i, j): A[i], A[j] = A[j], A[i]
    curr_col = curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A):
        if equal(A[curr_row][curr_col], 0):
            check_col = col(A, curr_col)[curr_row+1:]
            for i in range(len(check_col)):
                if not equal(check_col[i], 0): break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
            else: curr_col += 1
        else:
            if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, pow(A[curr_row][curr_col], -1, M))
            for i in range(curr_row+1, len(A)):
                if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1; curr_row += 1
    pivots = list_pivots(A)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A
def kmp(P):
    m = len(P); b = [0]*(m+1); i, j = 0, -1; b[0] = -1
    while i < m:
        while j >= 0 and P[i] != P[j]: j = b[j]
        i += 1; j += 1; b[i] = j
    return b[1:]
A = [[0]*(n+2) for _ in range(n+1)]; A[0][-1] = 1
for i in range(1, n+1): A[0][i] = A[i][0] = 1
for i in range(n):
    x = len(p:=kmp(S[i]+'.'+S[i]))
    while x: A[i+1][-1] += pow(2, x:=p[x-1], M)
for i in range(n):
    for j in range(n):
        A[i+1][j+1] = A[i+1][-1]; x = len(p:=kmp(S[i]+'.'+S[j]))
        while x: A[i+1][j+1] -= pow(2, x:=p[x-1], M)
R = rref(A); Z = [0]*n
for i in range(1, n+1):
    for j in range(1, n+1):
        if A[i][j]: Z[j-1] = A[i][-1]; break
print(*Z)