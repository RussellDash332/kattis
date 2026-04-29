import sys; input = sys.stdin.readline
from math import *

def twarea(p, q, r):
    return abs((p[1]-q[1])*(q[0]-r[0])-(q[1]-r[1])*(p[0]-q[0]))

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

H = chull([[*map(float, input().split())] for _ in range(int(input()))])
m = len(H); z = 0
if m == 2: z = hypot(H[0][0]-H[1][0], H[0][1]-H[1][1])
else:
    j = 1
    for i in range(m):
        while twarea(H[i], H[(i+1)%m], H[(j+1)%m]) >= twarea(H[i], H[(i+1)%m], H[j]): j = (j+1)%m
        z = max(z, hypot(H[i][0]-H[j][0], H[i][1]-H[j][1]), hypot(H[(i+1)%m][0]-H[j][0], H[(i+1)%m][1]-H[j][1]))
print(z)