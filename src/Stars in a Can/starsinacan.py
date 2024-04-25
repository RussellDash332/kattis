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

# O(n^2) KACTL, no four points are coplanar
def chull(A):
    F = []; n = len(A); K = ((1, 2), (1, 3), (2, 3))
    E = [[[] for _ in range(n)] for _ in range(n)]
    def mf(i, j, k, l):
        q = cross(A[i], A[j], A[k])
        if dot(q, A[l]) > dot(q, A[i]): q = (-q[0], -q[1], -q[2])
        E[i][j].append(k); E[i][k].append(j); E[j][k].append(i); F.append([q, i, j, k])
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4): mf(i, j, k, 6-i-j-k)
    for i in range(4, n):
        j = 0
        while j < len(F):
            f = F[j]
            if dot(f[0], A[i]) > dot(f[0], A[f[1]]):
                for a, b in K: E[f[a]][f[b]].remove(f[6-a-b])
                F[j], F[-1] = F[-1], F[j]; F.pop(); j -= 1
            j += 1
        for j in range(len(F)):
            f = F[j]
            for a, b in K:
                if len(E[f[a]][f[b]]) != 2: mf(f[a], f[b], i, f[6-a-b])
    for f in F:
        if dot(cross(A[f[1]], A[f[2]], A[f[3]]), f[0]) <= 0: f[2], f[3] = f[3], f[2]
    return F

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
for i, j, k in [x[1:] for x in chull(A)]:
    P = (A[i], A[j], A[k])
    p = [proj(A[l], P) for l in range(n)]
    ans = min(ans, max(dist(p[l][0]-A[l][0], p[l][1]-A[l][1], p[l][2]-A[l][2]) for l in range(n))*mec(p)[1]**2)
print(ans*pi)