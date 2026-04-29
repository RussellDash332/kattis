LIMIT = 10**6+67
spf = [0]*LIMIT
primes = []

for i in range(2, LIMIT):
    if spf[i] < 1: spf[i] = i; primes.append(i)
    for p in primes:
        if (j:=i*p) >= LIMIT: break
        spf[j] = p
        if p == spf[i]: break

P = [0, 0]
for n in range(2, LIMIT):
    P.append(P[-1])
    while n>1: P[-1] += 1; n //= spf[n]

import sys
for l in sys.stdin: print(P[int(l)])