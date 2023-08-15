from math import *
for _ in range(int(input())):
    r, n, d, m, s = map(int, input().split())
    a = d+m/60+s/3600
    v = set(); c = 0
    for _ in range(n):
        v.add(c)
        c = (c+a)%360
        if c in v: break
    v = sorted(v)
    if n > 1: v.append(v[0]), print(pi*r*r*max((b-a)%360 for a,b in zip(v, v[1:]))/360)
    else: print(pi*r*r)