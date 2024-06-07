from math import *
def f(x): return x/2/sin(x/2)
while True:
    L, n, C = map(float, input().split()); lo, hi = 0, 2*pi
    if L == -1: break
    while abs(lo-hi)>1e-14:
        mi = (lo+hi)/2
        if f(mi) < 1+n*C: lo = mi
        else: hi = mi
    print(L*(1-cos(mi/2))/2/sin(mi/2))