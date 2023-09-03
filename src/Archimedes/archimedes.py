from math import *
bb, tx, ty = map(float, input().split()); h = hypot(tx, ty)
def make(x1, y1, x2, y2): return y2-y1, x1-x2, (x2-x1)*y1-(y2-y1)*x1
def z(t):   return (bb*t*cos(t), bb*t*sin(t))
def zp(t):  return (bb*(cos(t)-t*sin(t)), bb*(sin(t)+t*cos(t)))
t0 = atan2(ty, tx)
while h > bb*t0: t0 += 2*pi
t0 -= 2*pi
lo, hi = t0-pi/2, t0
while abs(lo-hi)>1e-7:
    mi = (lo+hi)/2; xp, yp = z(mi); dxp, dyp = zp(mi)
    a, b, c = make(xp, yp, xp+dxp, yp+dyp)
    if a*tx+b*ty+c > 0: hi = mi
    else: lo = mi
print(*z(mi))