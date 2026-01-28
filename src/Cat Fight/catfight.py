import sys; input = sys.stdin.readline; from math import *; from bisect import *; P = 2*10**9+67
def closest_pair(p, ss):
    p.sort(); best = 1e38; j = 0; n = len(p); s = []
    for i in range(n):
        d = ceil(best**.5); x, y, z = p[i]//2//P, p[i]//2%P, p[i]%2
        while j < n and x-p[j]//2//P >= d: s.remove(p[j]//2%P*P*2+p[j]//2//P*2+p[j]%2); j += 1
        b = bisect_left(s, 2*(y-d)*P+2*x)
        for k in range(b, min(b+6, len(s))):
            e = s[k]
            if (e%2)^z%2 == ss: best = min(best, (x-e//2%P)**2+(y-e//2//P)**2)
        insort(s, 2*y*P+2*x+z)
    return best**.5
def area(r1, r2, d):
    if d >= r1+r2: return 0
    if d <= abs(r1-r2): return pi*min(r1, r2)**2
    return r1*r1*acos((d*d+r1*r1-r2*r2)/2/d/r1)+r2*r2*acos((d*d+r2*r2-r1*r1)/2/d/r2)-.5*((r1+r2+d)*(r1+r2-d)*(r1+d-r2)*(r2+d-r1))**.5
M, F = [], []; N, rF, rM = map(eval, input().split())
for _ in range(N):
    c, x, y = input().split(); x, y = int(x)+10**9, int(y)+10**9
    if c == 'M': M.append(2*P*x+2*y)
    else: F.append(2*P*x+2*y+1)
print(max(area(rM, rM, closest_pair(M, 0)), area(rF, rF, closest_pair(F, 0)), area(rF, rM, closest_pair(M+F, 1))))