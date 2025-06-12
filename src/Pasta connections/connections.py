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
    p.sort(); R = build(0, len(p)-1, p); E = [e:=R[0]]
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
class UFDS:
    def __init__(self, N):
        self.p = [*range(N)]; self.rank = [0]*N
    def find(self, i):
        if self.p[i] == i: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j):
        if (x:=self.find(i)) != (y:=self.find(j)):
            if self.rank[x] > self.rank[y]: self.p[y] = x
            else: self.p[x] = y; self.rank[y] += self.rank[x] == self.rank[y]
import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
N = int(input()); P = [tuple(map(int, input().split())) for _ in range(N)]; H = {p:i for i,p in enumerate(P)}; U = UFDS(N); E = []; Z = 0
for a, b, c in delaunay_triangulation(P): E.append(((a[0]-b[0])**2+(a[1]-b[1])**2, H[a], H[b])); E.append(((a[0]-c[0])**2+(a[1]-c[1])**2, H[a], H[c])); E.append(((b[0]-c[0])**2+(b[1]-c[1])**2, H[b], H[c]))
for w, a, b in sorted(E, key=lambda x: x[0]):
    if U.find(a) != U.find(b): U.union(a, b); Z += w**.5
print('%.2f'%Z)