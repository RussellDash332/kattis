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

def proj(p, a, b):
    return a+((p-a)/(b-a)).real*(b-a)

from cmath import *
P = chull([[*map(int, input().split())] for _ in range(int(input()))])
P = [complex(*p) for p in P]
Z = 1e9
for i in range(len(P)):
    q = [proj(p, P[i], P[i-1]) for p in P]
    h = max(abs(r-p) for r, p in zip(q, P))
    w = abs(max(q, key=lambda x:(x.real, x.imag))-min(q, key=lambda x:(x.real, x.imag)))
    Z = min(Z, h, w)
print(Z)