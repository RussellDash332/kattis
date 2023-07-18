LIMIT = 10**7
spf = list(range(LIMIT+1))
primes = [2]
p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def tot(n):
    res = n
    for p, _ in pf(n): res //= p; res *= p-1
    return res

def pf(n):
    res = []
    idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            if k: res.append((pp, k))
        idx += 1; k = 0
    if n != 1: res.append((n, 1))
    return res

def solve(n):
    divs = [1]
    for p, k in pf(n):
        l = len(divs)
        for _ in range(k*l): divs.append(divs[len(divs)-l]*p)
    print(sum(tot(i+1) for i in divs))

import sys; input = sys.stdin.readline
for _ in range(int(input())): solve(int(input()))