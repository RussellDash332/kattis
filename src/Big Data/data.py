n, arr = int(input()), list(map(int, input().split()))

# find sum for each combi
def e(ss):
    b = bin(ss)
    return sum(arr[i] for i in range(len(b)-2) if int(b[-i-1]))
ee = list(map(e, range(1<<n)))

# generate sieve
LIMIT = max(arr)*n
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

# distinct prime factors
mem = {}
def dpf(n):
    if n < 2: return 0
    if n not in mem:
        res = 0
        for p in primes:
            res += (n % p == 0)
            if n == 1: break
        mem[n] = res
    return mem[n]

# powerset
def p(s):
    s2, x = [0], 1
    if not s: return s2
    while x <= s:
        if x&s: s2 += [i+x for i in s2]
        x *= 2
    return s2

# memoized recursion
mem2 = {}
def f(s):
    if not s: return 0
    if s not in mem2: mem2[s] = max(f(s-ss)+dpf(ee[ss]) for ss in p(s) if ss)
    return mem2[s]

print(f((1<<n)-1))