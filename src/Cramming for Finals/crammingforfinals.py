import sys; input = sys.stdin.readline; from random import *
R = set(); V = 1001; r, c, d, n = map(int, input().split()); p = [-1]*(d+1); P = [[*map(lambda x: int(x)-1, input().split())] for _ in range(n)]
for i in range(d+1):
    for j in range(d+1):
        if i*i+j*j<=d*d: p[i] = j
while len(R) < r:
    i = randint(0, r-1)
    if i in R: continue
    R.add(i); m = {}
    for x, y in P:
        if abs(x-i) > d: continue
        f = p[abs(x-i)]; s = max(y-f, 0); e = min(y+f+1, c)
        if s < e:
            if s not in m: m[s] = 0
            if e not in m: m[e] = 0
            m[s] += 1; m[e] -= 1
        if x == i:
            if y not in m: m[y] = 0
            if y+1 not in m: m[y+1] = 0
            m[y] -= 1001; m[y+1] += 1001
    g = q = 0; v = 1001
    for x in sorted(m):
        if q != x and g >= 0: v = min(v, g)
        g += m[x]; q = x
        if v == 0: break
    V = min(V, v)
    if V == 0: break
print(V)