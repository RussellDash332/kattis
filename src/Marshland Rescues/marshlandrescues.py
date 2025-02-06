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

import sys; input = sys.stdin.readline
N = int(input())
P = [[*map(int, input().split())] for _ in range(N)]
L = [(P[i], P[(i+1)%len(P)]) for i in range(len(P))]
D = [(a[1]-b[1], b[0]-a[0]) for a, b in L]
for i in range(N): x, y = D[i]; d = (x*x+y*y)**.5; D[i] = (x/d, y/d)
def f(r):
    M = []
    for i in range(N): dx, dy = D[i][0]*r, D[i][1]*r; (s1, e1), (s2, e2) = L[i]; M.append(((s1+dx, e1+dy), (s2+dx, e2+dy)))
    try: return bool(half_plane_intersection(M))
    except: return 0
lo = 0; hi = 1e8
while abs(lo-hi)>1e-7:
    mi = (lo+hi)/2
    if f(mi): lo = mi
    else: hi = mi
print(mi)