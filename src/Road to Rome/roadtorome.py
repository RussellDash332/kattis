def area(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1])-(r[0]-p[0])*(q[1]-p[1])
def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not area(upper[-2], upper[-1], pts[i]) > 0: upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not area(lower[-2], lower[-1], pts[i]) > 0: lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]
import sys; input = sys.stdin.readline; from math import *; Z = 10**18
P = chull([[*map(int, input().split())] for _ in range(int(input()))]); n = len(P); j = 1
for i in range(n):
    while area(P[i-1], P[i], P[(j+1)%n]) > area(P[i-1], P[i], P[j]): j = (j+1)%n
    Z = min(Z, area(P[i-1], P[i], P[j])/hypot(P[i-1][0]-P[i][0], P[i-1][1]-P[i][1]))
print(Z)