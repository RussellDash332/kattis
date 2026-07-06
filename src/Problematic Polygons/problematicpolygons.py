N, M = map(int, input().split())
P = [[*map(float, input().split())] for _ in range(N)]
Q = [[*map(float, input().split())] for _ in range(M)]

def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2; (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    c1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); c2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    c1 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); c2 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    return 1
def pip(p, P):
    z = False; n = len(P)
    for i in range(n):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%n][0]-p[0], P[(i+1)%n][1]-p[1])
        if a[1] > b[1]-1e-9: a, b = b, a
        if a[1] <= 1e-9 and b[1] > -1e-9 and a[0]*b[1] < a[1]*b[0]+1e-9: z = not z
        if abs(a[0]*b[1]-a[1]*b[0]) < 1e-9 and a[0]*b[0]+a[1]*b[1] <= 1e-9: return True
    return z

from math import *
for t in range(360):
    a = pi/180*t
    R = [(x*cos(a)-y*sin(a), x*sin(a)+y*cos(a)) for x, y in P]
    if all(pip(p, Q) for p in R) and not any(intersect((R[i], R[i-1]), (Q[j], Q[j-1])) for i in range(N) for j in range(M)): print(t); break
else: print('impossible')