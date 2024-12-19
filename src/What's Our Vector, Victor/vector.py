def mul(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])): C[i][j] += A[i][k]*B[k][j]
    return C

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def normalize(a):
    n = dot(a, a)**0.5
    return [x/n for x in a]

def transpose(A):
    return [*map(list, zip(*A))]

def rref(A):
    def equal(a, b): return abs(a-b) < 1e-9
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
    curr_col = 0
    curr_row = 0
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
    return A, sorted(list_pivots(A))

# QR decomposition resolves the issue when A^T A is singular, since the usual A^T Ax = A^T b approach won't work
def QR(A):
    at = transpose(A)
    E = [normalize(at[0])]
    for i in range(1, len(at)):
        u = at[i]
        for j in range(i): k = dot(E[j], u); u = sub(u, [k*x for x in E[j]])
        E.append(normalize(u))
    # make the factorization complete
    for i in range(len(at), d):
        u = [1]*len(at[0])
        for j in range(len(at)): k = dot(E[j], u); u = sub(u, [k*x for x in E[j]])
        E.append(normalize(u))
    return transpose(E), mul(E, A)

def solve(d, n, P, verify=0):
    for i in range(1, n):
        for j in range(d): P[i][j] -= P[0][j]

    # Offset x by the first vector base for all equations
    # Now suppose the offset solution is x', then |x'| = P[0][d] = r0
    # As for the remaining n-1 equations, suppose this is |(x1-p1, x2-p2, ..., xd-pd)| = r
    # Since we have |(x1, x2, ..., xd)| = r0, then we must have -2(p1x1 + p2x2 + ... + pdxd) + |p|^2 = r^2-r0^2 => p.x = (r0^2+|p|^2-r2)/2
    r0 = P[0][d]; A = []; b = []
    for i in range(1, n): r = P[i][d]; p = [*P[i]]; p.pop(); b.append([(r0*r0+sum(q*q for q in p)-r*r)/2]); A.append(p)

    # suppose A = R'Q', then A' = QR and R'Q'x = b => x = Q * inv(R')b
    # v = inv(R')b is the solution to R'v = b
    Q, R = QR(transpose(A)); Rt = transpose(R)
    V = [[v[-1]] for v in rref([Rt[i]+b[i] for i in range(len(b))])[0]]
    while len(V) != len(Q[0]): V.append([0])
    X = transpose(mul(Q, V))[0]
    if r0*r0 > dot(X, X): # avoid FPE and complex numbers
        V[-1][0] += (r0*r0-dot(X, X))**0.5
        X = transpose(mul(Q, V))[0]

    # wrap up
    Z = [X[i]+P[0][i] for i in range(d)]
    if verify:
        for i in range(1, n):
            for j in range(d): P[i][j] += P[0][j]
        for i in range(n):
            dist = sum((P[i][j]-Z[j])**2 for j in range(d))
            target = P[i][d]**2
            assert abs(dist-target)<1e-5, (i, dist, target, abs(dist-target))
    return Z

import sys; input = sys.stdin.readline
d, n = map(int, input().split()); n = min(n, d+1); P = [[*map(float, input().split())] for _ in range(n)]
if n == 1: print(*P[0][:-2], P[0][-1]+P[0][-2])
else: print(*solve(d, n, P))