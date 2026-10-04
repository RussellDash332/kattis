from bisect import *
from math import *
n = int(input())
p = sorted([*map(float, input().split())] for _ in range(n))
z = 1e38; j = 0; s = []
for x, y in p:
    d = z/2
    while j < n and x-p[j][0] >= d: s.remove((p[j][1], p[j][0])); j += 1
    b = bisect_left(s, (y-d, -1e38))
    for k in range(b, len(s)):
        if s[k][0] > y+d: break
        e = s[k]
        for l in range(k+1, len(s)):
            if s[l][0] > y+d: break
            f = s[l]; w = hypot(x-e[1], y-e[0])+hypot(x-f[1], y-f[0])+hypot(e[1]-f[1], e[0]-f[0])
            if w < z: z = w
    insort(s, (y, x))
print(z)