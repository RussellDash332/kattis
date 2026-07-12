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

def pip(p, P):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = not z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return True
    return z

from math import *; from bisect import *
L = chull([[*map(int, input().split())] for _ in '.'*int(input())])
S = [[*map(int, input().split())] for _ in '.'*int(input())]
K = L.index(min(L))
L = L[K:]+L[:K]
X, Y = L[0]
A = [atan2(y-Y, x-X) for x, y in L[1:]]
Z = 0
for x, y in S:
    b = bisect_left(A, a:=atan2(y-Y, x-X))
    if b==len(A) or (b==0 and A[b]>a): continue
    Z += pip((x, y), (L[0], L[b], L[b+1]))
print(Z)