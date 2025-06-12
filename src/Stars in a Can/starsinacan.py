import sys; input = sys.stdin.readline
from math import *
from random import *

def dist(a, b, c):
    return (a*a+b*b+c*c)**0.5

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def cross_util(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

def proj(p, q):
    a, b, c = q
    t = cross(a, b, c)
    n = dist(*t)
    u = (t[0]/n, t[1]/n, t[2]/n)
    x = dot(p, u)-dot(a, u)
    return (p[0]-u[0]*x, p[1]-u[1]*x, p[2]-u[2]*x)

def vol(a, b, c, d):
    return dot(cross(a, b, c), (d[0]-a[0], d[1]-a[1], d[2]-a[2]))
def col(a, b, c):
    return a == b or a == c or b == c or cross(a, b, c) == (0, 0, 0)
def chull(P, K=100):
    P = sorted({*P})
    N = len(P); V = []; T = []; S = []; I = []; Ln = []; Lh = []; C = []; B = []; U = [0]*N; D = [1, 0, 2, 0, 3, 0, 2, 1, 3, 1, 3, 2]; F = [-1]*12
    def af(p, q, r): l = len(C); C.append((p, q, r)); V.append(l); F[p] = F[q] = F[r] = l; T.append(l); Lh.append(-1); S.append(0); I.append(False)
    def fvp(f, d): a, b, c = fv(f); return vol(P[a], P[b], P[c], P[d]) > 0
    def fv(f): p, q, r = C[f]; return D[p], D[q], D[r]
    for i in range(2, N):
        if not col(P[0], P[1], P[i]): P[i], P[2] = P[2], P[i]; break
    for i in range(i+1, N):
        if vol(P[0], P[1], P[2], P[i]): P[i], P[3] = P[3], P[i]; break
    if vol(P[0], P[1], P[2], P[3]) < 0: P[1], P[2] = P[2], P[1]
    af(7, 1, 2); af(5, 0, 8); af(9, 6, 10); af(11, 3, 4)
    for i in range(4, N):
        for f in V:
            if fvp(f, i): Ln.append(Lh[f]); Lh[f] = len(B); B.append(i); break
    while T:
        if S[v:=T.pop()] == 1 or Lh[v] == -1: continue
        a, b, c = fv(v); S[v] = 1; M = -10**18; x = -1; i = Lh[v]; Vs = [v]; Ns = []; H = []; Q = 0
        while i != -1:
            w = vol(P[a], P[b], P[c], P[B[i]])
            if M < w: M = w; x = B[i]
            i = Ln[i]
        for f in Vs:
            for e in C[f]:
                if S[g:=F[e^1]] < 1:
                    if fvp(g, x): S[g] = 1; Vs.append(g)
                    else: S[g] = 2; Ns.append(g)
                if S[g] == 2: U[D[e]] = len(D); D.append(x); F.append(-1); D.append(D[e]); F.append(-1); H.append(e)
        for e in H: af(U[D[e]], U[D[e^1]]^1, e)
        for f in Vs:
            i = Lh[f]
            while i != -1:
                if B[i] != x:
                    if (Q:=Q+1) == K: shuffle(H); Q = 0
                    for e in H:
                        if fvp(F[e], B[i]): Ln.append(Lh[F[e]]); Lh[F[e]] = len(B); B.append(B[i]); break
                i = Ln[i]
        for f in Vs: I[f] = True; Lh[f] = -1
        for f in Ns: S[f] = 0
    return [[P[j] for j in fv(i)] for i in V if not I[i]]

def circumcenter(a, b, c):
    x = (c[0]-a[0], c[1]-a[1], c[2]-a[2])
    y = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    s1 = dist(*x); s2 = dist(*y)
    c = cross_util(x, y); d = (-c[0], -c[1], -c[2]); e = 2*(c[0]**2+c[1]**2+c[2]**2)
    p = cross_util(d, y); q = cross_util(c, x)
    return (a[0]+s1*s1/e*p[0]+s2*s2/e*q[0] , a[1]+s1*s1/e*p[1]+s2*s2/e*q[1], a[2]+s1*s1/e*p[2]+s2*s2/e*q[2])

def mec(p):
    shuffle(p); o = p[0]; r = 0; eps = 1+1e-9
    for i in range(len(p)):
        if dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2]) <= r*eps: continue
        o = p[i]; r = 0
        for j in range(i):
            if dist(o[0]-p[j][0], o[1]-p[j][1], o[2]-p[j][2]) <= r*eps: continue
            o = ((p[i][0]+p[j][0])/2, (p[i][1]+p[j][1])/2, (p[i][2]+p[j][2])/2)
            r = dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2])
            for k in range(j):
                if dist(o[0]-p[k][0], o[1]-p[k][1], o[2]-p[k][2]) <= r*eps: continue
                o = circumcenter(p[i], p[j], p[k])
                r = dist(o[0]-p[i][0], o[1]-p[i][1], o[2]-p[i][2])
    return o, r

n = int(input()); A = [tuple(map(int, input().split())) for _ in range(n)]; ans = float('inf')
for P in chull(A): p = [proj(A[l], P) for l in range(n)]; ans = min(ans, max(dist(p[l][0]-A[l][0], p[l][1]-A[l][1], p[l][2]-A[l][2]) for l in range(n))*mec(p)[1]**2)
print(ans*pi)