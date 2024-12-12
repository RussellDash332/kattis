from random import randint
def miller_rabin(p):
    if p % 2 == 0: return p < 4
    if p == 3: return 1
    d, s = p-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for _ in range(3):
        x = pow(randint(2, p-2), d, p)
        for _ in range(s):
            y = x**2 % p
            if y == 1 and x != 1 and x != p-1: return 0
            x = y
        if y != 1: return 0
    return 1

LIMIT = 10**4
spf = list(range(LIMIT+1))
primes = []; p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2

n = int(input())
for i in range(len(primes)):
    for j in range(i+1):
        if miller_rabin(n-primes[i]-primes[j]): print(primes[i], primes[j], n-primes[i]-primes[j]), exit(0)