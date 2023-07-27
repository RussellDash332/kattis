def p(x):
    while x > 9:
        f = 1
        while x:
            if x%10: f *= x%10
            x //= 10
        x = f
    return x

primes = [2, 3, 5, 7]
facts = set()
def bt(i=0, x=1):
    if i == 4 or x > 10**15: return
    facts.add(x)
    bt(i, x*primes[i]), bt(i+1, x)
bt()

mem = {}
def dp(f, N):
    if f > N > 0: return 0
    if (f, N) in mem: return mem[(f, N)]
    if N < 10:
        r = 0
        for i in range(N+1): r += (i or 1) == f
        mem[(f, N)] = r; return r
    s = 0; d = len(str(N))-1; l = N//(10**d); k = 10**d-1
    for i in range(l):
        if f % (i or 1) == 0: s += dp(f//(i or 1), k)
    if f % l == 0: s += dp(f//l, N%(k+1))
    mem[(f, N)] = s; return s

a, b = map(int, input().split()); s = [0]*9
for f in facts: s[p(f)-1] += dp(f, b)-dp(f, a-1)
print(*s)