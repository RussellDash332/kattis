def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])
def chull(pts):
    n = len(pts)
    if n < 3: return n
    upper, lower = pts[:2], pts[-1:-3:-1]
    for i in range(2, n):
        while len(upper) > 1 and not ccw(upper[-2], upper[-1], pts[i]): upper.pop()
        upper.append(pts[i])
    for i in range(n-2, -1, -1):
        while len(lower) > 1 and not ccw(lower[-2], lower[-1], pts[i]): lower.pop()
        lower.append(pts[i])
    return n-max(len(upper), 1)-max(len(lower), 1)+2

N = Z = int(input())
P = sorted([tuple(map(float, input().split())) for _ in range(N)])
for i in range(N):
    x1, y1 = P[i]
    for j in range(i):
        x2, y2 = P[j]; a, b, c = y2-y1, x1-x2, (y2-y1)*x1-(x2-x1)*y1
        for z in range(2):
            p1, p2 = [], []
            for k in range(N):
                x, y = P[k]
                if k != i and k != j: (p1, p2)[a*x+b*y<c].append(P[k])
                elif k == i: (p1, p2)[z].append(P[k])
                else: (p2, p1)[z].append(P[k])
            if len(p1) == len(p2): Z = min(Z, chull(p1)+chull(p2))
print(Z)