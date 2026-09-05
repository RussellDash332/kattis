from cmath import *
def cross(a, b):
    return (a.conjugate()*b).imag
def intersect(a, b, c, d):
    z = cross(b-a, d-c)
    return a+cross(c-a, d-c)/z*(b-a) if z else None
def area(P):
    return abs(sum(cross(P[i], P[i-1]) for i in range(len(P))))/2
N = int(input())
D, L = map(int, input().split()); L *= 1000
P = [complex(*map(int, input().split())) for _ in range(N)]
def valid(z, p, q):
    return min(p.real, q.real) <= z.real <= max(p.real, q.real) and min(p.imag, q.imag) <= z.imag <= max(p.imag, q.imag) if z else 0
def f(H):
    l = ((-1e7+H*1j), (1e7+H*1j)); T = []
    for i in range(N):
        z = intersect(P[i], P[i-1], *l)
        if valid(z, P[i], P[i-1]): T += [z]
    Q = [p for p in P if p.imag < H]+T; c = sum(Q)/len(Q); Q.sort(key=lambda x: phase(x-c))
    return area(Q)*D > L
lo, hi = 0, max(p.imag for p in P)
while abs(lo-hi) > 1e-5:
    if f(mi:=(lo+hi)/2): hi = mi
    else: lo = mi
print('%.2f'%mi)