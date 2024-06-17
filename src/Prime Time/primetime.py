LIMIT = INF = 10070; spf = list(range(LIMIT+1)); primes = [2]; p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def pf(n):
    res = []; idx = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp
            res.append(pp)
        idx += 1
    if n != 1: res.append(n)
    return res

dp = [(INF, INF, INF) for _ in range(LIMIT)]
for p in primes: dp[p] = (1, INF, INF)
for i in range(1, len(primes)):
    for j in range(primes[i]-1, primes[i-1], -1):
        a, b, c = dp[j+1]; x = (c, a, b)
        for f in pf(j):
            a, b, c = dp[j//f]
            if min(j//f, c) <= x[0]: x = (min(j//f, c), a, b)
        dp[j] = x
for i in range(LIMIT): dp[i] = [min(a, i) for a in dp[i]]

z = [0, 0, 0]
for _ in range(int(input())):
    s, n = input().split(); n = int(n); t = 'OEI'.index(s)
    for i in range(3): z[(t+i)%3] += dp[n][i]
print(*z)