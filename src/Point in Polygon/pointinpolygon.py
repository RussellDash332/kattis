from math import hypot

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return (x1, y1) == (x3, y3) if d == e == 0 else (d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4))
    elif d == e == 0: return a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2)
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4)
        else:
            if a*f != c*d or b*f != c*e: return 0
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = 0
                return (i1 == i2 and i1 != 0) or i1

def pip(p, poly):
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return 'on'
    seg = (p, (p[0]+30000, p[1]+30001)) # create a ray
    return ['out', 'in'][sum(intersect(seg, (poly[i], poly[i+1])) for i in range(len(poly)-1)) % 2]

while True:
    n = int(input())
    if n == 0: break
    pts = [list(map(int, input().split())) for _ in range(n)]
    pts.append(pts[0])
    for _ in range(int(input())): print(pip(list(map(int, input().split())), pts))