from math import *

def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) >= (r[0]-p[0])*(q[1]-p[1])

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
    h = set(upper[:-1] + lower[:-1])
    n = len(h)
    ctx, cty = sum(p[0] for p in h)/n, sum(p[1] for p in h)/n
    return sorted(h, key=lambda x: atan2(x[1]-cty, x[0]-ctx))

n, pts = int(input()), []
for _ in range(n):
    x, y, i = input().strip().split()
    if i == 'Y': x, y = map(int, (x, y)); pts.append((x, y))
ch = chull({*pts})
c = len(ch)
idx = min(range(c), key=lambda x: ch[x])
ch = ch[idx:] + ch[:idx]
print(c), [print(*i) for i in ch]