from math import *
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n, r = map(float, input().split()); n = round(n)
    bb = []
    for _ in range(n):
        x, y, d, s = map(float, input().split())
        a = (90-d)*pi/180
        bb.append((x, y, s*cos(a), s*sin(a)))
    best = 1e9
    for i in range(n-1):
        x1, y1, dx1, dy1 = bb[i]
        for j in range(i+1, n):
            x2, y2, dx2, dy2 = bb[j]
            a = (dx1-dx2)**2+(dy1-dy2)**2
            b = 2*((x1-x2)*(dx1-dx2)+(y1-y2)*(dy1-dy2))
            c = (x1-x2)**2+(y1-y2)**2-r*r
            d = b*b-4*a*c
            if d < 0: continue
            if c < 0: best = 0; continue
            if abs(a) < 1e-8:
                if abs(b) > 1e-8: t1 = t2 = -c/b
                else: continue
            else: t1, t2 = (-b-d**0.5)/(2*a), (-b+d**0.5)/(2*a)
            if t1 < 0 and t2 >= 0: best = min(best, t2)
            elif t1 >= 0: best = min(best, t1)
    if best == 1e9: print('No collision.')
    else: print(round(best))