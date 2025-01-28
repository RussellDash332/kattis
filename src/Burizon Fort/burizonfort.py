LIMIT = 10**6+1
spf = list(range(LIMIT+1))
primes = []; p = 2
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, p):
            if spf[i] == i: spf[i] = p
    if p == 2: p -= 1
    p += 2
for _ in range(int(input())):
    m = int(input()); y = 1; p = 1
    for k in primes:
        if m == 1: break
        if m%k == 0:
            if k > 2 and k > p+1: y = 0; break
            e = 0
            while m%k == 0: m //= k; e += 1
            p *= (k**(e+1)-1)//(k-1)
    if m > p+1: y = 0
    print('YNeos'[1-y::2])