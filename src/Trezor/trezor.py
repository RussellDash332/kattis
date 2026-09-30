A, B, L = map(int, open(0).read().split()); S = A+B
from functools import *
def f(s):
    P = []
    for p in range(2, int(s**.5)+1):
        if s<2: break
        if s%p<1:
            P += [p]
            while s%p<1: s //= p
    if s>1: P += [s]
    return tuple(P)
@cache
def g(p):
    n = len(p); z = 0
    for b in range(1<<n):
        f = 1
        while b: u = b&-b; b ^= u; f *= -p[u.bit_length()-1]
        z += L//f if f > 0 else -(L//-f)
    return z
P = [*map(f, range(S+1))]; Y = Z = 0
for k in range(S+1):
    p = P[k]; q = P[S-k]
    x = 1 if k == 0 else g(p)
    y = 1 if k == S else g(q)
    z = 1 if k in (0, S) else g(tuple(sorted({*p, *q})))
    Y += x+y-2*z; Z += z
print(L*-~S-Y-Z, Y, Z)