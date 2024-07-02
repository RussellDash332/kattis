from math import *
for tc in range(int(input())):
    f, R, t, r, g = map(float, input().split()); x1 = r+f; R2 = R-t-f; A = 0
    while x1 < R2:
        y1 = r+f
        while y1 < R2:
            x2 = x1+g-2*f; y2 = y1+g-2*f
            if x2 < x1 or y2 < y1 or x1*x1+y1*y1 > R2*R2: y1 += g+2*r; continue
            if x2*x2+y2*y2 <= R2*R2: A += (x2-x1)*(y2-y1)
            elif x1*x1+y2*y2 <= R2*R2 and x2*x2+y1*y1 <= R2*R2: p1 = ((R2*R2-y2*y2)**.5, y2); p2 = (x2, (R2*R2-x2*x2)**.5); th = atan2(p1[1], p1[0])-atan2(p2[1], p2[0]); A += (x2-x1)*(y2-y1)-(x2-p1[0])*(y2-p2[1])/2+R2*R2/2*(th-sin(th))
            elif x1*x1+y2*y2 <= R2*R2 and x2*x2+y1*y1 >= R2*R2: p1 = ((R2*R2-y2*y2)**.5, y2); p2 = ((R2*R2-y1*y1)**.5, y1); th = atan2(p1[1], p1[0])-atan2(p2[1], p2[0]); A += (p1[0]+p2[0]-2*x1)*(y2-y1)/2+R2*R2/2*(th-sin(th))
            elif x1*x1+y2*y2 >= R2*R2 and x2*x2+y1*y1 <= R2*R2: p1 = (x1, (R2*R2-x1*x1)**.5); p2 = (x2, (R2*R2-x2*x2)**.5); th = atan2(p1[1], p1[0])-atan2(p2[1], p2[0]); A += (p1[1]+p2[1]-2*y1)*(x2-x1)/2+R2*R2/2*(th-sin(th))
            else: p1 = (x1, (R2*R2-x1*x1)**.5); p2 = ((R2*R2-y1*y1)**.5, y1); th = atan2(p1[1], p1[0])-atan2(p2[1], p2[0]); A += (p1[1]-y1)*(p2[0]-x1)/2+R2*R2/2*(th-sin(th))
            y1 += g+2*r
        x1 += g+2*r
    print(f'Case #{tc+1}:', 1-4*A/pi/R/R)