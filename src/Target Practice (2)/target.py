import sys; input = sys.stdin.readline; TC = 0

def d2(a, b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def intersect_check(s1, s2):
    (p1, p2), (p3, p4) = s1, s2; (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    c1 = (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1); c2 = (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
    if (c1 < 0 and c2 < 0) or (c1 > 0 and c2 > 0): return 0
    c1 = (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3); c2 = (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
    if (c1 < 0 and c2 < 0) or (c1 > 0 and c2 > 0): return 0
    return 1

def pip(p):
    ray = (p, (p[0]+10**5, p[1]+1)); return sum(intersect_check(ray, (P[i], P[i+1])) for i in range(n))%2

while (n:=int(input())):
    TC += 1; P = [[*map(int, input().split())] for _ in range(n)]; P.append(P[0]); Q = int(input()); print('Case', TC)
    for _ in range(Q):
        x, y = map(int, input().split()); hit = pip(p:=(x, y)); best = 1e18
        for i in range(n):
            x1, y1 = P[i]; x2, y2 = P[i+1]; A = y2-y1; B = x1-x2; r = (y-y1)*A-(x-x1)*B; d = A*A+B*B
            if r < 0: best = min(best, d2(p, P[i]))
            elif r > d: best = min(best, d2(p, P[i+1]))
            else: best = min(best, (A*(x-x1)+B*(y-y1))**2/d)
        if best == 0: print('Winged!')
        elif hit: print('Hit!', best**.5)
        else: print('Miss!', best**.5)