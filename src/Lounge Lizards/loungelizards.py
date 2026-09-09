import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from math import *
X, Y = map(int, input().split())
H = {}
for _ in range(N:=int(input())):
    x, y, h = map(int, input().split())
    dx = x-X; dy = y-Y; d = gcd(dx, dy); dx //= d; dy //= d
    if (dx, dy) not in H: H[(dx, dy)] = []
    H[(dx, dy)] += [(x-X or y-Y, h)]
for p in H: H[p].sort(key=lambda x: abs(x[0]))
from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
print(sum(lis([p[1] for p in v]) for v in H.values()))