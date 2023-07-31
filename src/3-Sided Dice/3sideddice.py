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
def area(poly):
    a, n = 0, len(poly)
    for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]
    return a
def pip(p, poly):
    if area(poly) == 0: return min(poly) < p < max(poly)
    for i in range(len(poly)-1):
        if abs(dist(poly[i], p) + dist(p, poly[i+1]) - dist(poly[i], poly[i+1])) < 1e-9: return False
    s = sum((2*ccw(p, poly[i], poly[i+1])-1) * angle(poly[i], p, poly[i+1]) for i in range(len(poly)-1))
    return abs(abs(s) - 2*pi) < 1e-9

while True:
    x1, y1, z1 = map(int, input().split())
    if x1+y1+z1!=1e4: break
    x2, y2, z2 = map(int, input().split())
    x3, y3, z3 = map(int, input().split())
    p = [*map(int, input().split())]
    a = (y2-y1)*(z3-z1)-(y3-y1)*(z2-z1)
    b = -(x2-x1)*(z3-z1)+(x3-x1)*(z2-z1)
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    d = x1*a+y1*b+z1*c
    # plane that contains the triangle: ax + by + cz = d
    # project to xy axis if all projections are not collinear else xz axis
    if (y2-y1)*(x3-x1) != (y3-y1)*(x2-x1): poly = [(x1, y1), (x2, y2), (x3, y3), (x1, y1)]
    else: p = (p[0], p[2]); poly = [(x1, z1), (x2, z2), (x3, z3), (x1, z1)]
    print(['NO', 'YES'][pip(p, poly)]), input()