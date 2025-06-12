from math import *
def csa(r, a, b, c, d):
    z = (atan2(b, a)-atan2(d, c))%(2*pi); return r*r/2*(z-sin(z))
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
def area(p):
    a, n = 0, len(p)
    for i in range(n): a += p[i][0]*p[(i+1)%n][1]-p[i][1]*p[(i+1)%n][0]
    return abs(a)/2
def f(x1, y1, r1, x2, y2, r2):
    s = (x2-x1)**2+(y2-y1)**2
    if s > (r1+r2)**2: print(0); exit()
    elif s == (r1+r2)**2: return [((x1*r2+x2*r1)/(r1+r2), (y1*r2+y2*r1)/(r1+r2))]
    elif s <= (r1-r2)**2: return (r1>r2)-(r1<r2)
    else:
        q = (2*(r1**2+r2**2)*s-(r1**2-r2**2)**2-s*s)**.5
        m = ((x1+x2)/2 + (r1**2-r2**2)*(x2-x1)/(2*s), (y1+y2)/2 + (r1**2-r2**2)*(y2-y1)/(2*s))
        v = (q*(y2-y1)/(2*s), q*(x1-x2)/(2*s))
        return [(m[0]+v[0], m[1]+v[1]), (m[0]-v[0], m[1]-v[1])]
N = int(input()); C = [[*map(int, input().split())] for _ in '.'*N]; V = dict(); I = [0]*N
for i in range(N):
    x1, y1, r1 = C[i]
    for j in range(i):
        x2, y2, r2 = C[j]
        v = f(x1, y1, r1, x2, y2, r2)
        if v == 1: I[j] += 1
        if v == -1: I[i] += 1
        if type(v) == list:
            for p, q in v:
                ok = 1
                for k in range(N):
                    if k == i or k == j: continue
                    x, y, r = C[k]
                    if (x-p)**2+(y-q)**2-r*r > 1e-12: ok = 0; break
                if not ok: continue
                k = (round(p, 12), round(q, 12))
                if k not in V: V[k] = set()
                V[k].add(i); V[k].add(j)
if max(I) == N-1: print(pi*C[I.index(N-1)][2]**2); exit()
P = chull([*V]); Z = area(P)
for i in range(len(P)):
    z = float('inf')
    for j in V[P[i]]&V[P[i-1]]: x, y, r = C[j]; z = min(z, csa(r, P[i][0]-x, P[i][1]-y, P[i-1][0]-x, P[i-1][1]-y))
    Z += z
print(Z)