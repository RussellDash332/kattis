LIMIT = 33000
spf = [*range(LIMIT+1)]
primes = []; p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
def pf(n):
    res = []; idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            res.append(-pp)
        idx += 1; k = 0
    if n != 1: res.append(-n)
    return res
from math import *; from heapq import *
a, b = map(int, input().split()); m = n = 1; d = gcd(a, b); a //= d; b //= d; P = pf(a*b); heapify(P); p = 0
while P:
    p = -heappop(P); va = vb = 0; ma = a; mb = b
    while ma%p == 0: ma //= p; va += 1
    while mb%p == 0: mb //= p; vb += 1
    if va == vb == 0: continue
    sw = va < vb
    if sw: a, b, m, n, va, vb = b, a, n, m, vb, va
    if va%2:
        m *= p**(va//2+1); b *= p-1
        for i in pf(p-1): heappush(P, i)
    else: m *= p**(va//2+1); n *= p
    a //= p**va; b //= p**vb
    if sw: a, b, m, n, va, vb = b, a, n, m, vb, va
    d = gcd(a, b); a //= d; b //= d
print(m, n)