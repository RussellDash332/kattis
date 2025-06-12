import sys; input = sys.stdin.readline
from math import *
PREC = 1e-9

def rref(A):
    def equal(a, b): return abs(a-b) < PREC
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
    #check_rref(A)
    return A

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])

def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]

def pip(P, p):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z

def check(ans):
    assert abs(sum(ans[i]*pp[i][0] for i in range(n))-x)<PREC
    assert abs(sum(ans[i]*pp[i][1] for i in range(n))-y)<PREC
    assert abs(sum(ans)-1)<PREC, ans
    assert all(1+PREC>=q>=-PREC for q in ans)

def check_rref(A):
    for i in range(len(A)):
        for j in range(len(A)):
            assert abs(A[i][j]-(i==j))<PREC

n = int(input()); pp = [(x+1, y+1) for x, y in zip(map(int, input().split()), map(int, input().split()))]; x, y = map(int, input().split()); x += 1; y += 1; h = {}
for i in range(n): h[pp[i]] = i
pp.append(pp[0])

if n == 1:
    if abs(pp[0][0]-x)<PREC and abs(pp[0][1]-y)<PREC: print('Yes\n1')
    else: print('No')
    exit(0)
elif n == 2:
    A = rref([[pp[0][0], pp[1][0], x], [pp[0][1], pp[1][1], y]])
    ans = [A[0][-1], A[1][-1]]
    try: check(ans); print('Yes'); print(*ans)
    except: print('No')
    exit(0)

p = chull(pp)
while p[0] == p[-1] and len(p) > 1: p.pop()

if len(p) == 1:
    if abs(p[0][0]-x)<PREC and abs(p[0][1]-y)<PREC: print('Yes'); ans = [0]*n; ans[h[p[0]]] = 1; print(*ans)
    else: print('No')
    exit(0)
elif len(p) == 2:
    A = rref([[p[0][0], p[1][0], x], [p[0][1], p[1][1], y]])
    ans = [0]*n; ans[h[p[0]]] = A[0][-1]; ans[h[p[1]]] = A[1][-1]
    try: check(ans); print('Yes'); print(*ans)
    except: print('No')
    exit(0)

p.append(p[0])
if not pip(p, (x, y)): print('No'), exit(0)
p.pop()

while len(p) > 3:
    p1 = p[:len(p)//2+1]; p1.append(p[0])
    p2 = p[len(p)//2:]; p2.append(p[0]); p2.append(p[len(p)//2])
    if pip(p1, (x, y)): p = p1
    else: p = p2
    p.pop()
(a, d), (b, e), (c, f) = p
A = [r[-1] for r in rref([[a, b, c, x], [d, e, f, y], [1]*4])]
ans = [0]*n
ans[h[(a, d)]] = A[0]
ans[h[(b, e)]] = A[1]
ans[h[(c, f)]] = A[2]
#check(ans)
print('Yes'); print(*ans)