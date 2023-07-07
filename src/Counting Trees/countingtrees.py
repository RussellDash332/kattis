import sys; input()

def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a % b); return (q, p - q * (a // b))

def egcd(a, b):
    if a == 0: return (0, 1)
    else: y, x = egcd(b % a, a); return (x - (b // a) * y, y)

def crt(a, m, b, n):
    u, _ = bezout(m, n); return (a - m * u * (a - b)) % (m * n)

def binmod(n, r, m):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if r == 1 or r == n-1: return n%m
    if r == 2 or r == n-2: return n*(n-1)//2%m
    if n < m: return (fmp[m][n]*egcd((fmp[m][r]*fmp[m][n-r])%m, m)[0])%m
    else:
        s = 1
        while n: s = (s*binmod(n%m, r%m, m))%m; n //= m; r //= m
        return s

mods = [11, 101, 3000301]
fmp = {i: [1, 1, 2] for i in [3]+mods}
for i in fmp:
    for j in range(3, i): fmp[i].append((fmp[i][-1])*j%i)
for l in sys.stdin:
    n, k, c = map(int, l.split())
    p, s = binmod(n-1, c-1, 3), 3
    for m in mods: p, s = crt(p, s, binmod(n-1, c-1, m), m), s*m
    print(2*p%s)