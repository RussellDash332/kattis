k, n = map(int, input().split())
LIMIT = 10001
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
v = 0
for i in range(n): v += check(5*i+6) and check(k*i+7)
print(v)