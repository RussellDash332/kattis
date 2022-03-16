import sys

LIMIT = 432
sieve = [True] * LIMIT
primes = []

p = 2
while p < LIMIT:
    if sieve[p]:
        primes.append(p)
        for i in range(2*p, LIMIT, p):
            sieve[i] = False
    if p == 2:
        p -= 1
    p += 2
    
dp = [[]]
for k in range(1, 432):
    temp = []
    for p in primes:
        if k % p == 0:
            temp.append([p, 0])
        while k % p == 0:
            temp[-1][-1] += 1
            k //= p
    dp.append(temp)

for line in sys.stdin:
    n, k = map(int, line.split())
    pf = {}
    for i in range(k):
        a, b = dp[n - i], dp[i + 1]
        for p, k in a:
            if p not in pf:
                pf[p] = 0
            pf[p] += k
        for p, k in b:
            pf[p] -= k
    ans = 1
    for k in pf.values():
        ans *= k + 1
    print(ans)