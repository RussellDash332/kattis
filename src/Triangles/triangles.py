import sys; input = sys.stdin.readline
from math import *

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]
def norm(a):
    return hypot(*a)
def angle(a, o, b):
    v1, v2 = (a[0]-o[0], a[1]-o[1]), (b[0]-o[0], b[1]-o[1])
    return acos(dot(v1, v2)/(norm(v1)*norm(v2)))
def ccw(p, q, r):
    return (q[0]-p[0])*(r[1]-p[1]) > (r[0]-p[0])*(q[1]-p[1])
def pip(p, poly):
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return True
    s = sum((2*ccw(p, poly[i], poly[i+1])-1) * angle(poly[i], p, poly[i+1]) for i in range(len(poly)-1))
    return abs(abs(s) - 2*pi) < 1e-9

for _ in range(int(input())):
    x1, y1, z1, x2, y2, z2, x3, y3, z3 = map(int, input().split())
    x4, y4, z4, x5, y5, z5, x6, y6, z6 = map(int, input().split())
    a = (y2-y1)*(z3-z1)-(y3-y1)*(z2-z1)
    b = -(x2-x1)*(z3-z1)+(x3-x1)*(z2-z1)
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    d = x1*a+y1*b+z1*c
    # plane that contains the 1st triangle: ax + by + cz = d
    # to find intersection along (x4, y4, z4)-(x5, y5, z5):
    # => a*(x4*t+x5*(1-t)) + b*(y4*t+y5*(1-t)) + c*(z4*t+z5*(1-t)) = d
    # => (a*(x4-x5) + b*(y4-y5) + c*(z4-z5))t = d-a*x5-b*y5-c*z5
    nt1, dt1 = d-a*x5-b*y5-c*z5, a*(x4-x5)+b*(y4-y5)+c*(z4-z5)
    nt2, dt2 = d-a*x6-b*y6-c*z6, a*(x4-x6)+b*(y4-y6)+c*(z4-z6)
    nt3, dt3 = d-a*x6-b*y6-c*z6, a*(x5-x6)+b*(y5-y6)+c*(z5-z6)
    if dt1 == 0 or dt2 == 0 or dt3 == 0: print('NO'); continue
    t1, t2, t3 = nt1/dt1, nt2/dt2, nt3/dt3; pts = set()
    if 0 <= t1 <= 1: pts.add((x4*t1+x5*(1-t1), y4*t1+y5*(1-t1), z4*t1+z5*(1-t1)))
    if 0 <= t2 <= 1: pts.add((x4*t2+x6*(1-t2), y4*t2+y6*(1-t2), z4*t2+z6*(1-t2)))
    if 0 <= t3 <= 1: pts.add((x5*t3+x6*(1-t3), y5*t3+y6*(1-t3), z5*t3+z6*(1-t3)))
    if len(pts) != 2: print('NO'); continue
    pts = [*pts]
    # project to xy axis if all projections are not collinear else xz axis
    if (y2-y1)*(x3-x1) != (y3-y1)*(x2-x1): poly = [(x1, y1), (x2, y2), (x3, y3), (x1, y1)]
    else: poly = [(x1, z1), (x2, z2), (x3, z3), (x1, z1)]
    print(['NO', 'YES'][pip(pts[0], poly)^pip(pts[1], poly)])