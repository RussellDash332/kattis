n = int(input())
LIMIT = int(n**0.5)+3
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

ans = 1
for p, v in res.items():
    m = 1
    for i in range(v): m = p*m + 2*i + 3
    ans *= m
print(ans)