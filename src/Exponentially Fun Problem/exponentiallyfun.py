M = 10**9+7; n = int(input()); r = 1
spf = list(range(n+1)); primes = []; p = 2
while p <= n:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, n+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
dp = [float('inf')]*(n+1)
for p in primes:
    if p <= n: dp[p] = p
for i in range(4, n+1):
    for p in primes:
        if p > i: break
        dp[i] = min(dp[i], dp[i-p]*p)
while n%3: n -= 2; r *= 2; r %= M
r *= pow(3, n//3, M); r %= M
print(dp[-1], r)