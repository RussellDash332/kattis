from math import *
n, d, g = map(int, input().split()); r = d*g; x = y = 0
poly = [[*map(int, input().split())] for _ in range(n)]
for xx, yy in poly: x += xx; y += yy
poly.sort(key=lambda t: atan2(t[1]*n-y, t[0]*n-x)); a = p = 0
for i in range(n): a += poly[i][0]*poly[(i+1)%n][1] - poly[i][1]*poly[(i+1)%n][0]; p += hypot(poly[i][0]-poly[(i+1)%n][0], poly[i][1]-poly[(i+1)%n][1])
print(r*p+abs(a)/2+pi*r*r)