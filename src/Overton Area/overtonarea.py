def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])
def chull(pts):
    if len(pts) < 3: return pts
    pts, n = sorted(pts), len(pts)
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        if len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        if len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return upper[:-1] + lower[:-1]
def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1]-p[i][1]*p[(i+1)%n][0]
    return abs(a)
import sys; input = sys.stdin.readline; P = []
for _ in range(int(input())): x, y = map(int, input().split()); P.append((x, y))
print(area(chull(P)))