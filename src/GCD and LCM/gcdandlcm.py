x, y = map(int, input().split())
LIMIT = int(max(x, y)**0.5) + 10
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

def pf(n):
    res = {}
    idx = 0
    while n != 1 and idx < len(primes):
        if n % primes[idx] == 0:
            n //= primes[idx]
            if primes[idx] not in res: res[primes[idx]] = 0
            res[primes[idx]] += 1
        else:
            idx += 1
    if n != 1:
        is_prime = True
        for p in range(primes[idx - 1], LIMIT-8):
            if n % p == 0:
                is_prime = False
                res[p] = 1
        if is_prime: res[n] = 1
    return res

pfx, pfy, xy = pf(x), pf(y), x*y
pfs = [*{*([*pfx]+[*pfy])}]
for d in [pfx, pfy]:
    for f in pfs:
        if f not in d: d[f] = 0
if not pfs: print(1, 1)
else:
    r, c = set(), [pfx, pfy]
    for i in range(2**len(pfs)):
        t, a = [], 1
        for _ in range(len(pfs)): t.append(i%2); i//=2
        for u in range(len(pfs)): a *= pfs[u]**(c[t[u]][pfs[u]])
        r.add((a, xy//a))
    for i in sorted(r): print(*i)