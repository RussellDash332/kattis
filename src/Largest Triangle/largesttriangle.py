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

pts = chull([*{tuple(map(int, input().split())) for _ in range(int(input()))}])
area, n = 0, len(pts)
if n < 3: print(0), exit(0)
elif n == 3: print(twarea(*pts)/2), exit(0)
for a in range(n):
    b, c = (a+1)%n, (a+2)%n
    area = max(area, twarea(pts[a], pts[b], pts[c]))
    while (c-a+1)%n:
        c0, c2 = c, (c+1)%n
        while c0 != c2 and (new:=twarea(pts[a], pts[b], pts[c2])) >= twarea(pts[a], pts[b], pts[c]):
            area, c = max(area, new), c2
            c2 = (c2+1)%n
        b = (b+1)%n
print(area/2)