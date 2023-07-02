import sys
from collections import Counter
t = 0
for l in sys.stdin:
    if t: arr = list(map(int, l.split()))
    else: t = 1
LIMIT = max(arr) + 3
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

ans, MOD = 1, 10**9+7
res = [1]*LIMIT
for n, k in Counter(arr).items():
    while n != 1:
        f = spf[n]
        while n % f == 0: n //= f; res[f] += k
for i in res:
    if i > 1: ans = (ans*i)%MOD
print(ans)