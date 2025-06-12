def closest_pair(px, py, s):
    if len(px) < 40:
        d = 3e9; p1 = p2 = None
        for i in range(len(px)-1):
            for j in range(i+1, len(px)):
                if (d2:=abs(px[i][0]-px[j][0])) < d and px[i][1]^px[j][1] == s: d, p1, p2 = d2, px[i], px[j]
        return d, p1, p2
    mid = len(px)//2; xmid = px[mid][0].real; py1, py2 = [], []
    for i in py:
        if i[0].real < xmid: py1.append(i)
        else: py2.append(i)
    d, p1, p2 = min(closest_pair(px[:mid], py1, s), closest_pair(px[mid:], py2, s), key=lambda z:z[0]); q = [i for i in py if abs(i[0].real-xmid) < d]
    for i in range(len(q)-1):
        for j in range(i+1, min(i+7, len(q))):
            if (d2:=abs(q[i][0]-q[j][0])) < d and q[i][1]^q[j][1] == s: d, p1, p2 = d2, q[i], q[j]
            else: break
    return d, p1, p2

from math import *
def area(r1, r2, d):
    if d >= r1+r2: return 0
    if d <= abs(r1-r2): return pi*min(r1, r2)**2
    return r1*r1*acos((d*d+r1*r1-r2*r2)/2/d/r1)+r2*r2*acos((d*d+r2*r2-r1*r1)/2/d/r2)-.5*((r1+r2+d)*(r1+r2-d)*(r1+d-r2)*(r2+d-r1))**.5

import sys; input = sys.stdin.readline
gr, gi = lambda c: c[0].real, lambda c: c[0].imag
M, F = [], []; N, rF, rM = map(eval, input().split())
for _ in range(N):
    c, x, y = input().split()
    if c == 'M': M.append((complex(int(x), int(y)), 0))
    else: F.append((complex(int(x), int(y)), 1))
dm, _, _ = closest_pair(sorted(M, key=gr), sorted(M, key=gi), 0)
df, _, _ = closest_pair(sorted(F, key=gr), sorted(F, key=gi), 0)
db, _, _ = closest_pair(sorted(M+F, key=gr), sorted(M+F, key=gi), 1)
print(max(area(rM, rM, dm), area(rF, rF, df), area(rF, rM, db)))