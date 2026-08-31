R, C = map(int, input().split()); P = {}
for _ in range(int(input())):
    a, r, c = map(int, input().split())
    for _ in range(a): P[1<<len(P)] = [(r, c, [i*C+j for i in range(r) for j in range(c)]), (c, r, [i*C+j for i in range(c) for j in range(r)])]
from array import *
B = array('B', [1]*R*C)
def f(p, k=0):
    while k < R*C and not B[k]: k += 1
    if k == R*C: return 1
    p2 = p; pr = pc = -1
    while p2:
        u = p2&-p2; p2 ^= u
        for rr, cc, t in P[u]:
            if (pr, pc) == (rr, cc): continue
            pr, pc = rr, cc
            if k//C+rr<=R and k%C+cc<=C and all(B[i+k] for i in t):
                for i in t: B[i+k] = 0
                if f(p^u, k): return 1
                for i in t: B[i+k] = 1
    return 0
print('yneos'[1-f(2**len(P)-1)::2])