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
from math import *
M = {}; P = []
for i in range(int(input())):
    x, y = map(int, input().split())
    P.append((x, y)); M[P[-1]] = i+1
while len(P) > 3:
    A = []
    for i in range(N:=len(Q:=chull(P))):
        d = abs(atan2(Q[i-1][1]-Q[i][1], Q[i-1][0]-Q[i][0])-atan2(Q[(i+1)%N][1]-Q[i][1], Q[(i+1)%N][0]-Q[i][0]))
        if d > pi: d = 2*pi-d
        A.append(d)
    if min(A)<pi/2: P.remove(Q[A.index(min(A))])
    else: print(len(Q)); print(*(M[p] for p in Q)); exit()
print('impossible')