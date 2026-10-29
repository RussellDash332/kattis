from ctypes import *
class mpz(Structure): _fields_ = [('alloc', c_int), ('size', c_int), ('d', c_void_p)]
g = CDLL('libgmp.so.10')
init = g.__gmpz_init; init.argtypes = [c_void_p]
set_ui = g.__gmpz_set_ui; set_ui.argtypes = [c_void_p, c_ulong]
get_ui = g.__gmpz_get_ui; get_ui.argtypes = [c_void_p]; get_ui.restype = c_ulong
is_sq = g.__gmpz_perfect_square_p; is_sq.argtypes = [c_void_p]; is_sq.restype = c_int
gsqrt = g.__gmpz_sqrt; gsqrt.argtypes = [c_void_p, c_void_p]

X = mpz(); R = mpz()
init(byref(X)); init(byref(R))
bX, bR = byref(X), byref(R)

def sq(n):
    set_ui(bX, n)
    if not is_sq(bX): return 0
    gsqrt(bR, bX)
    return get_ui(bR)

import sys; from array import *
from collections import *
input = sys.stdin.readline
T = 10**6+1
F = array('I', [0])*T
S = array('I')
for i in range(2, T):
    if F[i] < 1: F[i] = i; S.append(i)
    for p in S:
        if (j:=i*p) >= T: break
        F[j] = p
        if p == F[i]: break
P = array('H', [p for p in S if p < 10**4])
def gen(k):
    u = [1]
    for v in k: u += [-v*c for c in u]
    return u
Z = 0; M = array('i', [0])*(2*T+3); H = Counter()
for _ in range(int(input())):
    n = int(input()); z = 1
    for s in P:
        if s*s > n: break
        if n%s == 0:
            n //= s
            if n%s == 0:
                z *= s
                while n%s == 0: n //= s
    else:
        if n > 1:
            r = sq(n)
            if r: z *= r
    H[z] += 1; Z -= z==1
for z, v in H.items():
    c = []
    while z > 1: c.append(F[z]); z //= F[z]
    for u in gen(c): M[u] += v
Z += sum(x*x for x in M[:T+1])-sum(x*x for x in M[T+1:])
print(Z//2)