import sys; input = sys.stdin.readline
from math import *
def merge(intervals):
    h=lambda a,b:0 if a[1]<b[0]or b[1]<a[0]else[min(a[0],b[0]),max(a[1],b[1])]
    return [r:=[],[[r.pop(),r.append(k)]if r and(k:=h(r[-1],j))else r.append(j)for j in sorted(intervals)]][0]
def f(t):
    c = []
    for x, y, rs, vs in ll:
        ti = ((x**2+y**2)**0.5-r)/rs
        if ti < t:
            ts = t-ti
            if (ss:=ts*vs/r) >= pi: return 1 # covers both sides
            ia = atan2(y, x); cl, cr = ia-ss, ia+ss
            if cl%(2*pi) > cr%(2*pi): c.append((cl%(2*pi), 2*pi)), c.append((0, cr%(2*pi)))
            else: c.append((cl%(2*pi), cr%(2*pi)))
    m = merge(c)
    return len(m)==1 and m[0][1]-m[0][0]==2*pi
for _ in range(int(input())):
    r, k = map(int, input().split())
    ll = [[*map(int, input().split())] for _ in range(k)]
    lo, hi = min(((x**2+y**2)**0.5-r)/rs for x, y, rs, vs in ll), 1e9
    while abs(lo-hi)>1e-7:
        mi = (lo+hi)/2
        if f(mi): hi = mi
        else: lo = mi
    print(mi)