from math import *
from bisect import *
import sys; input = sys.stdin.readline

def rotate(pt, ag, base=(0, 0)):
    x, y = pt; return (cos(ag)*(x-base[0])-sin(ag)*(y-base[1])+base[0], sin(ag)*(x-base[0])+cos(ag)*(y-base[1])+base[1])

def scale(segs, k):
    base = segs[0][0]
    return [[((ep[0]-base[0])*k+base[0], (ep[1]-base[1])*k+base[1]) for ep in seg] for seg in segs]

for _ in range(int(input())):
    pts = [[*map(int, input().split())] for _ in range(int(input()))]
    segs = [(pts[i], pts[i+1]) for i in range(len(pts)-1)]
    parts = [hypot(a[0]-b[0], a[1]-b[1]) for a, b in segs]; sp = sum(parts); cumparts = [0]
    for i in parts: cumparts.append(cumparts[-1]+i/sp)
    d = int(input())
    f = float(input())
    if f == 0: print(*pts[0]); continue # will not work properly with bisect
    b = []
    for _ in range(d-1):
        b.append(bisect_left(cumparts, f)-1)
        lo, hi = cumparts[0], cumparts[-1]; ss, ee = cumparts[b[-1]], cumparts[b[-1]+1]
        cumparts = [(ee-ss)/(hi-lo)*(i-lo)+ss for i in cumparts]
    s1, e1 = pts[0], pts[-1]
    n1 = hypot(e1[1]-s1[1], e1[0]-s1[0])
    a1 = atan2(e1[1]-s1[1], e1[0]-s1[0])
    for nxt in b:
        s2, e2 = segs[nxt]
        n2 = hypot(e2[1]-s2[1], e2[0]-s2[0])
        a2 = atan2(e2[1]-s2[1], e2[0]-s2[0])
        segs = [[rotate((ep[0]-s1[0]+s2[0], ep[1]-s1[1]+s2[1]), a2-a1, s2) for ep in seg] for seg in scale(segs, n2/n1)]
        n1, a1, s1, e1 = n2, a2, s2, e2
    pos = bisect_left(cumparts, f)-1
    ss, ee = cumparts[pos], cumparts[pos+1]
    w = (ee-f)/(ee-ss)
    (xs, ys), (xe, ye) = segs[pos]
    print(xs*w+xe*(1-w), ys*w+ye*(1-w))