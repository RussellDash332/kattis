from functools import lru_cache
from random import randint
from bisect import *

@lru_cache
def miller_rabin(p):
    if p == 2: return 1
    if p == 3: return 1
    if p % 2 == 0: return 0
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(10):
        x = pow(randint(2, p-2), d, p)
        for _ in range(s):
            y = x**2 % p
            if y == 1 and x != 1 and x != p-1: return 0
            x = y
        if y != 1: return 0
    return 1

def gcd(a, b):
    while b: a, b = b, a % b
    return a

@lru_cache
def pollard_rho(n):
    c = 1
    while True:
        x, y, d = 2, 2, 1
        while d == 1: 
            x = (x*x+c)%n
            y = (y*y+c)%n; y = (y*y+c)%n
            d = gcd(abs(x-y), n)
        if d != n: return d
        else: c += 1

@lru_cache
def pf(n):
    if n <= LIMIT:
        f = {}
        while n != 1:
            pp = spf[n]
            if n % pp == 0:
                k = 0
                while n % pp == 0: n //= pp; k += 1
                if k: f[pp] = k
        return f
    elif miller_rabin(n): return {n: 1}
    else:
        f = {}
        p = pollard_rho(n)
        for k, v in pf(p).items():
            if k not in f: f[k] = 0
            f[k] += v
        for k, v in pf(n//p).items():
            if k not in f: f[k] = 0
            f[k] += v
        return f

LIMIT = 10**6
spf = list(range(LIMIT+1))
primes = []
p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
a, b = map(int, input().split())
p = pf(a)
facts = [1]
for k, v in p.items():
    e = [1]
    for _ in range(v): e.append(e[-1]*k)
    facts = [x*y for x in facts for y in e]
print(abs(min(facts, key=lambda x: abs(x-b))-b))