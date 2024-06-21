def miller_rabin(p):
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(randint(3, 6)):
        x = pow(randint(2, p-2), d, p)
        if x == 1 or x == p-1: continue
        ok = 0
        for _ in range(s):
            x = x*x%p
            if x == 1: return 0
            if x == p-1: ok = 1; break
        if not ok: return 0
    return 1

def pollard_rho_brent(n):
    while True:
        y = randint(1, n-1); c = randint(1, n-1); m = randint(1, n-1); g = r = q = 1
        while g == 1:
            x = y; k = 0
            for _ in range(r): y = (y*y+c)%n
            while k < r and g == 1:
                s = y
                for _ in range(min(m, r-k)): y = (y*y+c)%n; q = q*abs(x-y)%n
                g = gcd(q, n); k += m
            r *= 2
        if g == n: g = 1
        while g == 1: s = (s*s+c)%n; g = gcd(abs(x-s), n)
        if g != n: return g

def pf(n, K):
    while n%2 == 0: n //= 2; E[2] += K
    while n != 1:
        if miller_rabin(n): E[n] += K; break
        pf(d:=pollard_rho_brent(n), K); n //= d

import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import gcd; from random import *; from array import *; from collections import *; U = 24000; MOD = 10**9+7; Z = 1; P, N, M = map(int, input().split()); E = Counter(); K = array('i', [pow(d, P, MOD) for d in range(U+1)]); C = array('i', [(K[d+1]-2*K[d]+K[d-1])%MOD for d in range(1, U)])
for i in map(int, input().split()): pf(i, -1)
for i in map(int, input().split()): pf(i, 1)
for i in E:
    if E[i] < 0: print(0), exit(0)
    elif E[i] > 0: Z *= C[E[i]-1]; Z %= MOD
print(Z)