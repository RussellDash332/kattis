import sys; input = sys.stdin.readline
N, B, R, W = map(int, input().split()); W *= 2
D = [*map(int, input().split())]
P = [d:=0]+[d:=d+i for i in D]
K = [P[i] for i in map(int, input().split())]
from bisect import *
def f(a):
    b = p = z = 0
    while p < N:
        s = b*R; m = 0; d = []; e = []
        if s+W+K[p] > a: break # can't even take this person
        while p < N:
            m = max(m, k:=K[p]); s += W*(q:=bisect_left(d, k))
            if q == len(d) or d[q] != K[p]: s += W*(len(e)-bisect_left(e, k*N+p)); insort(d, k)
            insort(e, k*N+p); s += W
            if s+m > a: break # can't include this person in the bus
            p += 1
        b += 1; z = max(z, s+m)
    return (p==N, z)
lo, hi = 0, f(10**99)[1]
while lo < hi:
    if f(mi:=(lo+hi)//2)[0]: hi = mi
    else: lo = mi+1
print(lo)