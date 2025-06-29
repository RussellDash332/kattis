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
import sys; input = sys.stdin.readline; N = int(input()); V = {}
for _ in range(N):
    x, y = map(int, input().split())
    if (x, y) in V: continue
    V[(x, y)] = _+1
C = [V[x] for x in chull([*V])]; m = C.index(min(C)); print(len(C)); print(*(C[m:]+C[:m]))