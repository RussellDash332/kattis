from math import gcd; from random import *; from collections import *

def miller_rabin(p):
    if p % 2 == 0: return 0
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
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

def pf(n):
    if n == 2: return [2]
    if miller_rabin(n): return [n]
    d = pollard_rho_brent(n)
    return pf(n//d) + pf(d)

n = int(input())
if n == 1: print(1), exit(0)
z = 1; c = Counter(pf(n)+pf(n+1)); c[2] -= 1
for k in c.values(): z *= k+1
print(z)