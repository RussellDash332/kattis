from math import *
def rot(x, y, xr, yr, a): return (x-xr)*cos(a)-(y-yr)*sin(a)+xr, (y-yr)*cos(a)+(x-xr)*sin(a)+yr
def dist(xr, yr, x1, y1, x2, y2): px = x2-x1; py = y2-y1; u = min(max(((xr-x1)*px+(yr-y1)*py)/(px*px+py*py), 0), 1); dx = x1+u*px-xr; dy = y1+u*py-yr; return (dx*dx+dy*dy)**.5
R, l, w = map(int, input().split())
for _ in range(int(input())): A, B = map(float, input().split()); ap = rot(0, w, l, w, -A); bp = rot(0, 0, l, 0, -B); print(min(2*R, w, l, dist(0, w, *ap, l, w), dist(*bp, *ap, l, w), dist(l, w, *bp, l, 0), dist(*ap, *bp, l, 0), dist(*bp, l, w, 10**9, w))/2)