import sys; input = sys.stdin.readline
from bisect import *
from math import *
def closest_pair(p, D=None):
    p.sort(); best = (1e21, None, None); j = 0; n = len(p); s = []
    for i in range(n):
        d = ceil(best[0]**.5); x, y = p[i]
        while j < n and x-p[j][0] >= d:
            try: s.remove((p[j][1], p[j][0])); j += 1
            except: break
        b = bisect_left(s, (y-d, x))
        for k in range(b, min(b+5, len(s))):
            e = s[k]; new = (x-e[1])**2+(y-e[0])**2
            if new < best[0] and (u:=(new, (x, y), (e[1], e[0]))) != D: best = u
        insort(s, (y, x))
    return best
from collections import *
N = int(input())
P = [tuple(map(float, input().split())) for _ in range(N)]
C = Counter(P).values()
if max(C) > 2 or sum(c>1 for c in C) > 1: print(0, 0); exit()
d = closest_pair(P)
e = closest_pair(P, d)
print(d[0]**.5, e[0]**.5)