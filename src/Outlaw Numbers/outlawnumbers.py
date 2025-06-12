LIMIT = 10**4
spf = list(range(LIMIT+1))
primes = [2]; p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2
def spd(n):
    res = 1; idx = k = 0; z = n
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            while n % pp == 0: n //= pp; k += 1
            res *= (pp**(k+1)-1)//(pp-1)
        idx += 1; k = 0
    if n != 1: res *= n+1
    return res-z
S = [int(input())]
for _ in range(32): S.append(spd(S[-1]))
print(['safe from harm','looking down a barrel'][S.count(S[0])>1])