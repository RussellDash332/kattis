def intersect(s1, s2):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    if a == b == 0: return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else ((x1, y1) if d*x1 + e*y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
    elif d == e == 0: return (x3, y3) if a*x3 + b*y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
        det = b*d-a*e
        if det:
            x, y = (b*f-c*e)/det, (c*d-a*f)/det
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a*f != c*d or b*f != c*e: return None
            else:
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):    i1, i2 = p, q
                elif p <= r <= q:       i1, i2 = r, min(q, s)
                elif r <= p <= s:       i1, i2 = p, min(s, q)
                else:                   i1 = i2 = None
                if i1 == i2 and i1 != None: return i1
                elif i1:                    return None # (i1, i2)
                else:                       return None

def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1] - p[i][1]*p[(i+1)%n][0]
    return abs(a)/2

from math import *
for _ in range(int(input())):
    N = int(input())
    P = [[*map(int, input().split())] for _ in range(N)]
    x1, y1 = P[0]; x2, y2 = P[1]
    M = ((x1+x2)/2, (y1+y2)/2)
    A = y2-y1; B = x1-x2; C = y1*x1-y2*x1-x1*y1+x2*y1
    AL = A*cos(pi/4)+B*sin(pi/4)
    BL = B*cos(pi/4)-A*sin(pi/4)
    CL = (A-AL)*M[0]+(B-BL)*M[1]+C
    AR = A*cos(pi/4)-B*sin(pi/4)
    BR = B*cos(pi/4)+A*sin(pi/4)
    CR = (A-AR)*M[0]+(B-BR)*M[1]+C
    assert abs(A*M[0]+B*M[1]+C) < 1e-6
    assert abs(AL*M[0]+BL*M[1]+CL) < 1e-6
    assert abs(AR*M[0]+BR*M[1]+CR) < 1e-6
    for d in range(6, 0, -1):
        D = 10**d
        L = ((M[0]-BL*D, M[1]+AL*D), (M[0]+BL*D, M[1]-AL*D))
        R = ((M[0]-BR*D, M[1]+AR*D), (M[0]+BR*D, M[1]-AR*D))
        l = r = None
        for i in range(N-1):
            S = (P[i+1], P[(i+2)%N])
            K = intersect(S, L)
            if K: l = (K, i)
            K = intersect(S, R)
            if K: r = (K, i)
        if l and r: break
    P2 = [l[0], M, r[0]]
    for i in range(min(l[1], r[1]), max(l[1], r[1])): P2.append(P[i+2])
    print(area(P2)/area(P))