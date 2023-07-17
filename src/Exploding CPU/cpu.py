from collections import defaultdict
from bisect import *
MAXN = 2*10**9
LIMIT = int((MAXN)**0.5+3)
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

def check(n):
    if n <= LIMIT: return spf[n] == n
    for p in primes:
        if p*p > n: break
        if n % p == 0: return n == p
    return 1
exp = defaultdict(list)
for i in range(len(primes)):
    for a in range(1, primes[i]+1000):
        b = primes[i]-a
        c = a*primes[i]+b
        if c < 0 or (prod:=primes[i]*c) > MAXN: break
        while True:
            if check(c): exp[(a, b)].append(c)
            else: break
            c = a*c + b; prod *= c
            if c < 0 or prod > MAXN: break
s = set()
for (a, b), v in exp.items():
    if len(v) > 1:
        p = (a+b)*v[0]*v[1]; s.add(p)
        for i in range(2, len(v)): p *= v[i]; s.add(p)
s = sorted(s)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bisect_right(s, b) - bisect_left(s, a))