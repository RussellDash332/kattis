from math import *
N = int(input()); P = [(0, 0)]; S = []
for _ in range(N): a, b = P[-1]; L = int(input()); S.append(L); P.append((L-b if L > b else max(a-L, 0), b+L))
x, y = map(int, input().split()); Z = []; a, b = P.pop(); d = (x*x+y*y)**.5
if d == 0: x = a
if x*x+y*y < a*a: x *= a/d; y *= a/d
elif x*x+y*y > b*b: x *= b/d; y *= b/d
while S:
    a, b = P.pop(); l = S.pop(); d = (x*x+y*y)**.5; Z.append((x, y))
    # choose r in [a, b] such that r, l, d are valid triangle sides
    r = min(b, l+d)
    t = acos(max(min((r*r+d*d-l*l)/(2*r*d), 1), -1)) if r*d else 0
    # rotate (x, y) by t and then dilate by r/d
    if d: x, y = (r/d)*(x*cos(t)-y*sin(t)), (r/d)*(y*cos(t)+x*sin(t))
    else: x = l # pick any point within x*x+y*y == l*l
while Z: print(*Z.pop())