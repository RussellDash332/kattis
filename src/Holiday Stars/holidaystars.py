from math import *

def centroid(p):
    a = cx = cy = 0; n = len(p)
    for i in range(n): d = p[i][0]*p[(i+1)%n][1]-p[(i+1)%n][0]*p[i][1]; a += d; cx += (p[i][0]+p[(i+1)%n][0])*d; cy += (p[i][1]+p[(i+1)%n][1])*d
    return (cx/a/3, cy/a/3)

n, omega, v0, theta, w = map(float, input().split()); n = round(n); theta *= pi/180; poly = []; vx = v0*cos(theta)
for _ in range(n): poly.append([*map(float, input().split())])
cx, cy = centroid(poly)
a = [hypot(p[0]-cx, p[1]-cy) for p in poly]; d = [atan2(p[0]-cx, p[1]-cy) for p in poly]; t = []

def f(i, t):
    return cx+vx*t+a[i]*sin(omega*t+d[i])
def df(i, t):
    return vx+a[i]*omega*cos(omega*t+d[i])
def d2f(i, t):
    return -a[i]*omega*omega*sin(omega*t+d[i])

for i in range(n):
    if vx-a[i]*omega > -1e-9:
        # binary search on monotic increasing fn
        lo, hi = 0, 1e9
        while abs(lo-hi)>1e-6:
            mi = (lo+hi)/2
            if f(i, mi) < w: lo = mi
            else: hi = mi
        t.append(mi)
    else:
        # find points such that df(i, t) == 0
        # cos(omega*t+d[i]) == -vx/(a[i]*omega)
        # -> omega*t+d[i] = +-acos(-vx/a[i]/omega)+2*pi*k
        # -> t = (2*pi*k-d[i]+-acos(-vx/a[i]/omega))/omega
        t1 = (-d[i]+acos(-vx/a[i]/omega))/omega
        while t1 < 0: t1 += 2*pi/omega
        t2 = (-d[i]-acos(-vx/a[i]/omega))/omega
        while t2 < 0: t2 += 2*pi/omega
        if t1 > t2: t1, t2 = t2, t1
        # check if f(i, t) goes downwards as t = t1
        # if so, [0, t1] is uw, then [t1, t2] is dw, then [t2, t1+2*pi/omega] uw, and so on...
        if d2f(i, t1) > 0: lo, hi = t1, t2
        else: lo, hi = t2-2*pi/omega, t1
        k = max(ceil((w-f(i, hi))/vx/2/pi*omega), 0); w2 = w-vx*2*pi/omega*k
        while abs(lo-hi)>1e-6:
            mi = (lo+hi)/2
            if f(i, mi) < w2: lo = mi
            else: hi = mi
        t.append(mi+2*pi/omega*k)
v = min(range(n), key=lambda x: t[x]); print(v+1, t[v])