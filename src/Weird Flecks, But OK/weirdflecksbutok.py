from random import *
import sys; sys.setrecursionlimit(5067)

def dist(a, b, c):
    return (a*a+b*b+c*c)**0.5

def cross_util(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def cross(a, b, c):
    return cross_util((b[0]-a[0], b[1]-a[1], b[2]-a[2]), (c[0]-a[0], c[1]-a[1], c[2]-a[2]))

def circumcenter(a, b, c):
    x = (c[0]-a[0], c[1]-a[1], c[2]-a[2])
    y = (b[0]-a[0], b[1]-a[1], b[2]-a[2])
    s1 = dist(*x); s2 = dist(*y)
    c = cross_util(x, y); d = (-c[0], -c[1], -c[2]); e = 2*(c[0]**2+c[1]**2+c[2]**2)
    p = cross_util(d, y); q = cross_util(c, x)
    return (a[0]+s1*s1/e*p[0]+s2*s2/e*q[0] , a[1]+s1*s1/e*p[1]+s2*s2/e*q[1], a[2]+s1*s1/e*p[2]+s2*s2/e*q[2])

def mec(p):
    def helper(n, k):
        if k >= 3:
            c = circumcenter(p[n-1], p[n-2], p[n-3])
            r = dist(c[0]-p[n-1][0], c[1]-p[n-1][1], c[2]-p[n-1][2])
            return c, r
        if n == 1: return p[0], 0
        if n == 2: return ((p[0][0]+p[1][0])/2, (p[0][1]+p[1][1])/2, (p[0][2]+p[1][2])/2), dist(p[0][0]-p[1][0], p[0][1]-p[1][1], p[0][2]-p[1][2])/2
        i = randint(0, n-k-1)
        p[i], p[n-1-k] = p[n-1-k], p[i]; p[n-1-k], p[n-1] = p[n-1], p[n-1-k]
        o, r = helper(n-1, k)
        p[n-1-k], p[n-1] = p[n-1], p[n-1-k]; p[i], p[n-1-k] = p[n-1-k], p[i]
        if dist(p[i][0]-o[0], p[i][1]-o[1], p[i][2]-o[2]) <= r+1e-9: return o, r
        p[i], p[n-1-k] = p[n-1-k], p[i]
        x = helper(n, k+1)
        p[i], p[n-1-k] = p[n-1-k], p[i]
        return x
    return helper(len(p), 0)

N = int(input())
P = [[*map(float, input().split())] for _ in range(N)]
_, rz = mec([(x, y, 0) for x, y, z in P])
_, rx = mec([(0, y, z) for x, y, z in P])
_, ry = mec([(x, 0, z) for x, y, z in P])
print(2*min(rx, ry, rz))