INFP = (10**9, 10**9)
class QE:
    def __init__(s): s.og = s.rt = s.nx = None; s.us = False
def edge(fr, to): e1 = QE(); e2 = QE(); e3 = QE(); e4 = QE(); e1.og = fr; e2.og = to; e3.og = e4.og = INFP; e1.rt = e3; e2.rt = e4; e3.rt = e2; e4.rt = e1; e1.nx = e1; e2.nx = e2; e3.nx = e4; e4.nx = e3; return e1
def splice(a, b): a.nx.rt.nx, b.nx.rt.nx = b.nx.rt.nx, a.nx.rt.nx; a.nx, b.nx = b.nx, a.nx
def delete(e): splice(e, e.rt.nx.rt); splice(e.rt.rt, e.rt.rt.rt.nx.rt)
def conn(a, b): e = edge(a.rt.rt.og, b.og); splice(e, a.rt.rt.rt.nx.rt); splice(e.rt.rt, b); return e
def cross(x, p, q): return (p[0]-x[0])*(q[1]-x[1])-(p[1]-x[1])*(q[0]-x[0])
def det(a, na, b, nb, c, nc): return a[0]*(b[1]*nc-c[1]*nb)-a[1]*(b[0]*nc-c[0]*nb)+na*(b[0]*c[1]-c[0]*b[1])
def incc(a, b, c, d): return det(a, na:=a[0]**2+a[1]**2, c, nc:=c[0]**2+c[1]**2, d, nd:=d[0]**2+d[1]**2)+det(a, na, b, nb:=b[0]**2+b[1]**2, c, nc) > det(b, nb, c, nc, d, nd)+det(a, na, b, nb, d, nd)
def build(l, r, p):
    if r-l==1: R = edge(p[l], p[r]); return R, R.rt.rt
    if r-l==2:
        a = edge(p[l], p[l+1]); b = edge(p[l+1], p[r]); splice(a.rt.rt, b); c = cross(p[l], p[l+1], p[r]) 
        if (s:=(c>0)-(c<0))==0: return a, b.rt.rt
        c = conn(b, a)
        if s==1: return a, b.rt.rt
        else: return c.rt.rt, c
    lo, li = build(l, mi:=(l+r)//2, p); ri, ro = build(mi+1, r, p)
    while 1:
        if cross(ri.og, li.og, li.rt.rt.og) > 0: li = li.rt.rt.rt.nx.rt; continue
        if cross(li.og, ri.og, ri.rt.rt.og) < 0: ri = ri.rt.rt.nx; continue
        break
    b = conn(ri.rt.rt, li)
    def valid(e): return cross(e.rt.rt.og, b.og, b.rt.rt.og) < 0
    if li.og == lo.og: lo = b.rt.rt
    if ri.og == ro.og: ro = b
    while 1:
        if valid(lc:=b.rt.rt.nx):
            while incc(b.rt.rt.og, b.og, lc.rt.rt.og, lc.nx.rt.rt.og): t = lc.nx; delete(lc); lc = t
        if valid(rc:=b.rt.nx.rt):
            while incc(b.rt.rt.og, b.og, rc.rt.rt.og, rc.rt.nx.rt.rt.rt.og): t = rc.rt.nx.rt; delete(rc); rc = t
        if not valid(lc) and not valid(rc): break
        if not valid(lc) or valid(rc) and incc(lc.rt.rt.og, lc.og, rc.og, rc.rt.rt.og): b = conn(rc, b.rt.rt)
        else: b = conn(b.rt.rt, lc.rt.rt)
    return lo, ro
def delaunay_triangulation(p):
    p = sorted(p); R = build(0, len(p)-1, p); E = [e:=R[0]]
    while cross(e.nx.rt.rt.og, e.rt.rt.og, e.og) < 0: e = e.nx
    cu = e
    while 1:
        cu.us = True; p.append(cu.og); E.append(cu.rt.rt); cu = cu.rt.rt.rt.nx.rt
        if cu == e: break
    p.clear()
    for e in E:
        if e.us: continue
        cu = e
        while 1:
            cu.us = 1; p.append(cu.og); E.append(cu.rt.rt); cu = cu.rt.rt.rt.nx.rt
            if cu == e: break
    return [(p[i], p[i+1], p[i+2]) for i in range(0, len(p), 3)]
def cc(a, b, c): d = 2*cross(a, b, c); na = a[0]**2+a[1]**2; nb = b[0]**2+b[1]**2; nc = c[0]**2+c[1]**2; return (a[1]*(nc-nb)+b[1]*(na-nc)+c[1]*(nb-na))/d, (a[0]*(nb-nc)+b[0]*(nc-na)+c[0]*(na-nb))/d
def voronoi_diagram(p, K=200000):
    V = []; H = {}
    for a, b, c in delaunay_triangulation(p):
        x = cc(a, b, c)
        for s, t, u in ((a, b, c) if a < b else (b, a, c), (a, c, b) if a < c else (c, a, b), (b, c, a) if b < c else (c, b, a)):
            if (s, t) not in H: H[(s, t)] = []
            H[(s, t)].append((x, u))
    for e in H:
        if len(H[e]) == 2: V.append((H[e][0][0], H[e][1][0]))
        else: x, u = H[e][0]; m = ((e[0][0]+e[1][0])/2, (e[0][1]+e[1][1])/2); d = (m[0]-x[0], m[1]-x[1]); y = (x[0]+K*d[0], x[1]+K*d[1]); z = (x[0]-K*d[0], x[1]-K*d[1]); V.append((x, y) if (u[0]-m[0])*(y[0]-m[0])+(u[1]-m[1])*(y[1]-m[1]) < 0 else (x, z))
    return V
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
                elif i1:                    return None
                else:                       return None
def pip(p):
    z = 0
    for i in range(N):
        a = (P[i][0]-p[0], P[i][1]-p[1]); b = (P[(i+1)%N][0]-p[0], P[(i+1)%N][1]-p[1])
        if a[1] > b[1]: a, b = b, a
        if a[1] <= 0 and b[1] > 0 and a[0]*b[1] < a[1]*b[0]: z = 1-z
        if a[0]*b[1] == a[1]*b[0] and a[0]*b[0]+a[1]*b[1] <= 0: return 1
    return z
N = int(input()); Z = 0
P = [tuple(map(int, input().split())) for _ in range(N)]
E = [(P[i], P[(i+1)%N]) for i in range(N)]
V = voronoi_diagram(P)
for s in V:
    for t in E:
        x = intersect(s, t)
        if x == None: continue
        Z = max(Z, min((p[0]-x[0])**2+(p[1]-x[1])**2 for p in P))
    for i in range(2):
        if pip(s[i]): Z = max(Z, min((p[0]-s[i][0])**2+(p[1]-s[i][1])**2 for p in P))
print(Z**.5)