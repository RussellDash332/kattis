from math import *
EPS = 1e-11
def clamp(x):
    return max(min(x, 1), -1)
def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def vadd(a, b):
    return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def vsub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def unit(a):
    z = hypot(*a); return tuple(v/z for v in a)
def ang(a, b):
    return atan2(hypot(*cross(a, b)), dot(a, b))
def arc(a, b, x):
    return 0 if abs(dot(x, c:=cross(a, b))) > EPS*hypot(*c) else abs(ang(a, x)+ang(x, b)-ang(a, b)) < EPS
def pipgc(q, P):
    n = len(P)
    for i in range(n):
        if arc(P[i], P[i-1], q): return 1 # on the polygon?
    for i in range(n):
        m = unit(vadd(a:=P[i-1], b:=P[i])); nm = unit(cross(a, b)); cs = cos(EPS); sn = sin(EPS); rn = cross(r:=vsub([cs*v for v in m], [sn*v for v in nm]), q); z = hypot(*rn)
        if z < EPS: continue
        if any(arc(r, q, p) for p in P): continue
        cz = 0; rn = tuple(v/z for v in rn)
        for j in range(n):
            x = cross(rn, cross(a:=P[j-1], b:=P[j])); z = hypot(*x)
            if z > EPS: x = tuple(v/z for v in x); nx = (-x[0], -x[1], -x[2]); cz ^= (arc(r, q, x) and arc(a, b, x)) or (arc(r, q, nx) and arc(a, b, nx))
        return cz == 1
    return 0
Q = unit([*map(float, input().split())]); N = int(input()); Z = 1e9
for _ in range(N):
    n = int(input()); P = [unit([*map(float, input().split())]) for _ in range(n)]
    if pipgc(Q, P): print(0); exit()
    for i in range(n): c = unit(cross(a:=P[i-1], b:=P[i])); k = clamp(dot(Q, c)); x = vsub(Q, [k*v for v in c]); xx = hypot(*x); Z = min(Z, abs(asin(k)) if arc(a, b, tuple(v/xx for v in x) if xx > EPS else a) else min(ang(Q, a), ang(Q, b)))
print(Z*6371)