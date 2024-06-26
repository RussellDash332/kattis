def mtc(p, s):
    for i in range(min(len(p), len(s)), 0, -1):
        if p[-i:] == s[:i]: return i
    return 0

def rref(A):
    def leading_entry_col(A, r):
        row = A[r]; i = 0
        while i < len(A[0]) and row[i] == 0: i += 1
        return i
    def list_pivots(A):
        res = []
        for r in range(len(A)):
            k = leading_entry_col(A, r)
            if k != len(A[0]): res.append((r, k))
        return sorted(res, reverse=True)
    def col(A, i): return list(map(lambda x: x[i], A))
    def ero1(A, i, c):
        for j in range(len(A[0])): A[i][j] *= c
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]
    def ero3(A, i, j): A[i], A[j] = A[j], A[i]
    curr_col = curr_row = 0
    while curr_col < len(A[0]) and curr_row < len(A):
        if A[curr_row][curr_col] == 0:
            check_col = col(A, curr_col)[curr_row+1:]
            for i in range(len(check_col)):
                if check_col[i] != 0: break
                elif i == len(check_col)-1: i += 1
            if i < len(check_col): ero3(A, curr_row, curr_row+i+1)
            else: curr_col += 1
        else:
            if A[curr_row][curr_col] != 1: ero1(A, curr_row, 1/A[curr_row][curr_col])
            for i in range(curr_row+1, len(A)):
                if A[i][curr_col] != 0: ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1; curr_row += 1
    pivots = list_pivots(A)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A

from fractions import *
g = [i=='H' for i in input()]; k = [i=='H' for i in input()]; p = Fraction(int(input()[-1]), 10); n = len(g); m = len(k); A = [[0]*(n+m+3) for _ in range(n+m+2)]; s = []
for i in range(n):
    s.append(1-g[i]); mg = mtc(s, g); mk = mtc(s, k); s[-1] = g[i]
    A[i][i] = 1; A[i][mk+n+1 if mg<mk else mg] -= (p, 1-p)[g[i]]; A[i][n+m+1 if mtc(s, k)==m else i+1] -= (1-p, p)[g[i]]
s = []
for i in range(m):
    if mtc(s, g) == i: A[n+i+1][n+i+1] = 1; s.append(k[i]); continue
    s.append(1-k[i]); mg = mtc(s, g); mk = mtc(s, k); s[-1] = k[i]
    A[n+i+1][n+i+1] = 1; A[n+i+1][mk+n+1 if mg<mk else mg] -= (p, 1-p)[k[i]]; A[n+i+1][n if i != m-1 and mtc(s, g)==n else n+i+2] -= (1-p, p)[k[i]]
A[n][n] = A[n][-1] = A[-1][-2] = 1; A[-1][-1] = 0; print(float(rref(A)[0][-1]))