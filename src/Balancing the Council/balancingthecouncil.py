LIMIT = 33333
spf = list(range(LIMIT+1))
primes = [2]; p = 3
while p <= LIMIT:
    if spf[p] == p:
        primes.append(p)
        for i in range(p*p, LIMIT+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2
def f(n):
    idx = k = 0
    while n != 1 and idx < len(primes):
        pp = primes[idx]
        if pp*pp > n: break
        if n % pp == 0:
            return pp
            while n % pp == 0: n //= pp; k += 1
        idx += 1; k = 0
    return n
N, M = map(int, input().split()); B = N
if M%2 == 0: print('Yes'); exit()
while B%2 == 0: B >>= 1
F = f(B); print('YNeos'[M<F or M>N-F or F<2::2])