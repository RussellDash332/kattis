from fractions import *

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
        for j in range(len(A[0])): A[i][j] *= c
    def ero2(A, i, j, c):
        for k in range(len(A[0])): A[i][k] += c*A[j][k]
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
            if not equal(A[curr_row][curr_col], 1): ero1(A, curr_row, 1/A[curr_row][curr_col])
            for i in range(curr_row+1, len(A)):
                if not equal(A[i][curr_col], 0): ero2(A, i, curr_row, -A[i][curr_col])
            curr_col += 1
            curr_row += 1
    pivots = list_pivots(A)
    for i in range(len(pivots)-1):
        for j in range(pivots[i][0]-1, -1, -1): ero2(A, j, pivots[i][0], -A[j][pivots[i][1]])
    return A

M = {'1': 1}; Q = []
for _ in range(int(input())):
    l, r = input().split(' = '); l = ('* '+l).split(); r = ('* '+r).split(); q = []
    for i in range(len(l)//2):
        if l[2*i+1] not in M: M[l[2*i+1]] = len(M)+1
        q.append((-1, 1)[l[2*i]=='*']*M[l[2*i+1]])
    for i in range(len(r)//2):
        if r[2*i+1] not in M: M[r[2*i+1]] = len(M)+1
        q.append((1, -1)[r[2*i]=='*']*M[r[2*i+1]])
    Q.append(q)
A = [[Fraction(0)]*(len(M)+1) for _ in Q]
for i in range(len(Q)):
    for x in Q[i]:
        if x > 0: A[i][x-1] += 1
        else: A[i][-x-1] -= 1
A.append([Fraction(1)]+[Fraction(0)]*len(M)); A = rref(A)
if A[0] != [1]+[0]*len(M): print('invalid'); exit()
for i in range(1, len(Q)+1):
    if sum(A[i][j]==0 for j in range(len(M))) == len(M)-1 and A[i][-1] == 0: print('invalid'); exit()
print('valid')