from math import *
def can(x):
    for s in range(len(e)):
        p = s; z = c = 0
        while True:
            if c+e[p] > x: c = 0; z += 1; p = (p+1)%len(e)
            else: c += e[p]; p = (p+1)%len(e)
            if p == s: break
        if z+(c!=0) <= n: return 1
while True:
    try: n, d, _, *f = map(int, input().split())
    except: break
    a = [i for i in range(d) if any(i%k==0 for k in f)]; e = [2000*sin((a[(i+1)%len(a)]-a[i])%d*pi/d) for i in range(len(a))]; lo, hi = 0, 2000*pi+.3
    while abs(lo-hi)>1e-2:
        if can(mi:=(lo+hi)/2): hi = mi
        else: lo = mi
    print('%.1f'%(mi+2000))