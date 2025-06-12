from math import *
from collections import *
from functools import *

def sgn(x):
    return (x>0)-(x<0)

def cross(a, b):
    return a[0]*b[1]-a[1]*b[0]

def intersect_line(l1, l2):
    (s1, e1), (s2, e2) = l1, l2
    d = cross((e1[0]-s1[0], e1[1]-s1[1]), q:=(e2[0]-s2[0], e2[1]-s2[1]))
    t = cross((s2[0]-s1[0], s2[1]-s1[1]), q)/d
    return (s1[0]*(1-t)+e1[0]*t, s1[1]*(1-t)+e1[1]*t)

def out(u, r):
    p, q = u; return cross((q[0]-p[0], q[1]-p[1]), (r[0]-p[0], r[1]-p[1])) < -1e-9

def cmp(l1, l2):
    a1 = atan2(y1:=l1[1][1]-l1[0][1], x1:=l1[1][0]-l1[0][0])
    a2 = atan2(l2[1][1]-l2[0][1], l2[1][0]-l2[0][0])
    if abs(a1-a2) < 1e-9: return sgn(cross((x1, y1), (l2[0][0]-l1[0][0], l2[0][1]-l1[0][1])))
    return sgn(a1-a2)

# should be able to eliminate parallel lines
INF = 10**9; B = [(INF, INF), (-INF, INF), (-INF, -INF), (INF, -INF)]
def half_plane_intersection(lines):
    lines.extend((B[i], B[(i+1)%4]) for i in range(4))
    lines.sort(key=cmp_to_key(cmp))
    n = len(lines); Q = deque()
    for i in range(n):
        (s1, e1), (s2, e2) = lines[i], lines[(i-1)%n]
        if abs(atan2(e1[1]-s1[1], e1[0]-s1[0])-atan2(e2[1]-s2[1], e2[0]-s2[0])) < 1e-9: continue
        while len(Q) > 1 and out(lines[i], intersect_line(Q[-1], Q[-2])): Q.pop()
        while len(Q) > 1 and out(lines[i], intersect_line(Q[0], Q[1])): Q.popleft()
        Q.append(lines[i])
    while len(Q) > 2 and out(Q[0], intersect_line(Q[-1], Q[-2])): Q.pop()
    while len(Q) > 2 and out(Q[-1], intersect_line(Q[0], Q[1])): Q.popleft()
    if len(Q) < 3: return []
    return [intersect_line(Q[i], Q[(i+1)%len(Q)]) for i in range(len(Q))]

def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1]-p[i][1]*p[(i+1)%n][0]
    return abs(a)/2

def solve(a, b, c, d):
    if max(a, b, c, d) == 90: return 1
    L = 10**4; HP = []
    HP.append(((0, 0), (L*cos(d*pi/180), L*sin(d*pi/180)))); HP.append(((L, 0), (L+L*cos((a+90)*pi/180), L*sin((a+90)*pi/180)))); HP.append(((L, L), (L+L*cos((b+180)*pi/180), L+L*sin((b+180)*pi/180)))); HP.append(((0, L), (L*cos((c+270)*pi/180), L+L*sin((c+270)*pi/180)))); HP.append(((0, 0), (L, 0))); HP.append(((L, 0), (L, L))); HP.append(((L, L), (0, L))); HP.append(((0, L), (0, 0)))
    return 1-area(half_plane_intersection(HP))/L/L

print(solve(*map(float, input().split())))