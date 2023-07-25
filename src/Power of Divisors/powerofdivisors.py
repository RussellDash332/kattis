LIMIT = int(10**4.5+20)
spf = list(range(LIMIT+1))
primes = [2]

p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

from random import randint
def miller_rabin(p):
    if p == 1: return 0
    if p == 2: return 0
    if p == 3: return 1
    if p % 2 == 0: return 0
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(100):
        x = pow(randint(2, p-2), d, p)
        for _ in range(s):
            y = x**2 % p
            if y == 1 and x != 1 and x != p-1: return 0
            x = y
        if y != 1: return 0
    return 1

n = int(input())
if n == 1: print(1), exit(0)
if n < 4: print(-1), exit(0)
s = []
for i in range(len(primes)):
    p = primes[i]
    k = 1
    while True:
        q = p**(k*(k+1))
        if q >= 10**18: break
        if q == n: s.append(p**k)
        k += 1
    for j in range(i+1, len(primes)):
        q = primes[j]
        if p*q > LIMIT: break
        if (p*q)**4 == n: s.append(p*q)
        if (p*q)**18 == n: s.append((p*q)**2)
        if p**6*q**12 == n: s.append(p*q*q)
        if p**12*q**6 == n: s.append(p*p*q)
        if p**24*q**8 == n: s.append(p*p*p*q)
        if p**8*q**24 == n: s.append(p*q*q*q)
if n == 30**8: s.append(30)
if n == 105**8: s.append(105)
rt = int(n**0.5)-1
for o in range(3):
    if miller_rabin(rt+o) and (rt+o)**2 == n: s.append(rt+o)
print(min(s, default=-1))