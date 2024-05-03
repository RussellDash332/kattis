def its(s1, s2):
    (p1, p2), (p3, p4) = s1, s2; (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    c1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); c2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    c1 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); c2 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    if (c1 < -1e-9 and c2 < -1e-9) or (c1 > 1e-9 and c2 > 1e-9): return 0
    return 1

def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])

from math import *
x1, y1, x2, y2, h12 = map(int, input().split())
x3, y3, x4, y4, h34 = map(int, input().split())
dx12, dy12, dx34, dy34 = x2-x1, y2-y1, x4-x3, y4-y3
p12 = [(x1, y1), (x2, y2), (x2-dy12, y2+dx12), (x2-dy12-dx12, y2+dx12-dy12)]
p34 = [(x3, y3), (x4, y4), (x4-dy34, y4+dx34), (x4-dy34-dx34, y4+dx34-dy34)]
a12 = []; a34 = [] # folded apex
for i in range(4):
    v12 = ((p12[(i+2)%4][0]-p12[(i+1)%4][0])/2, (p12[(i+2)%4][1]-p12[(i+1)%4][1])/2); k12 = hypot(h12, dx12/2, dy12/2)/hypot(*v12)
    v34 = ((p34[(i+2)%4][0]-p34[(i+1)%4][0])/2, (p34[(i+2)%4][1]-p34[(i+1)%4][1])/2); k34 = hypot(h34, dx34/2, dy34/2)/hypot(*v34)
    a12.append(((p12[i][0]+p12[(i+1)%4][0])/2+v12[0]*k12, (p12[i][1]+p12[(i+1)%4][1])/2+v12[1]*k12))
    a34.append(((p34[i][0]+p34[(i+1)%4][0])/2+v34[0]*k34, (p34[i][1]+p34[(i+1)%4][1])/2+v34[1]*k34))
ans = 10**9
for i in range(4):
    b12 = (p12[i], p12[(i+1)%4])
    for j in range(4):
        b34 = (p34[j], p34[(j+1)%4])
        # try normal line, check if it intersects b12 and b34
        l = (a12[i], a34[j])
        if its(l, b12) and its(l, b34):
            if not its(b12, b34) and (its((a12[i], p12[i]), b34) or its((a12[i], p12[(i+1)%4]), b34) or its((a34[j], p34[j]), b12) or its((a34[j], p34[(j+1)%4]), b12)): pass
            else: ans = min(ans, dist(*l))
        # take the minimum path among (a12[i] -> {any of the four points} -> a34[j]) but must still intersect both bases
        for tp in (p12[i], p12[(i+1)%4], p34[j], p34[(j+1)%4]):
            t12, t34 = (a12[i], tp), (tp, a34[j])
            if its(t12, b12) and its(t34, b34): ans = min(ans, dist(*t12)+dist(*t34))
        # naive 3-segment, definitely works regardless
        for tp in (p12[i], p12[(i+1)%4]):
            for tq in (p34[j], p34[(j+1)%4]):
                tr = (tp, tq); ok = 1
                for u in range(1, 3):
                    if its(tr, (p12[(i+u)%4], p12[(i+u+1)%4])) or its(tr, (p34[(j+u)%4], p34[(j+u+1)%4])): ok = 0; break
                if ok: ans = min(ans, dist(a12[i], tp)+dist(tp, tq)+dist(tq, a34[j]))
print(ans)