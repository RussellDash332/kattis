N, M, K = map(int, input().split()); ans = 0
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
    if n < m: return (fmp[m][n]*egcd((fmp[m][r]*fmp[m][n-r])%m, m)[0])%m
    else:
        s = 1
        while n: s = (s*binmod(n%m, r%m, m))%m; n //= m; r //= m
        return s
# C(N, q)
def f(r): return crt(binmod(N, r, 29), 29, binmod(N, r, 34483), 34483)
# C(X, N-1)
def g(n): return crt(binmod(n, N-1, 29), 29, binmod(n, N-1, 34483), 34483)
fmp = {i: [1, 1, 2] for i in [29, 34483]}
for i in fmp:
    for j in range(3, i): fmp[i].append((fmp[i][-1])*j%i)
# 10**6+7 = 29*34483, https://math.stackexchange.com/questions/553960/extended-stars-and-bars-problemwhere-the-upper-limit-of-the-variable-is-bounded
for q in range(min(N, K//(M+1))+1): ans += (-1)**q*f(q)*g(K-q*(M+1)+N-1); ans %= 10**6+7
print(ans)