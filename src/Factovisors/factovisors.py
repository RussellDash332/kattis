LIMIT = int(2**15.5 + 3)
sieve = [True] * (LIMIT + 1)
primes = []

p = 2
while p <= LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2

rev = dict(map(reversed, enumerate(primes)))

def pf(n):
    if n in memo: return memo[n]
    res = {}
    idx = 0
    while n != 1 and idx < len(primes):
        if n % primes[idx] == 0:
            n //= primes[idx]
            res[primes[idx]] = res.get(primes[idx], 0) + 1
        else:
            idx += 1
    if n != 1:
        is_prime = True
        for p in range(primes[idx - 1], int(n**0.5) + 2):
            if n % p == 0:
                is_prime = False
                res[p] = 1
        if is_prime: res[n] = 1
    memo[n] = res
    return res

def v(n, p):
    if (n, p) in memo: return memo[(n, p)]
    if n == 0: return 0
    memo[(n, p)] = n//p + v(n//p, p)
    return memo[(n, p)]

import sys
memo = {}
for line in sys.stdin:
    n, m = map(int, line.split())
    can = True
    if m == 0: can = False
    elif n == 0: can = m == 1
    elif n < m:
        for p, e in pf(m).items():
            if v(n, p) < e:
                can = False
                break
    if can: print(f'{m} divides {n}!')
    else: print(f'{m} does not divide {n}!')