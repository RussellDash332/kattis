def binmod(n, r, m):
    if r > n: return 0
    if r == 0 or r == n: return 1
    if n < m:
        # compute nCr as usual
        s = 1
        for i in range(r): s *= (n-i)*pow(i+1, -1, m); s %= m
    else:
        s = 1
        while n: s = s*binmod(n%m, r%m, m)%m; n //= m; r //= m
    return s

M = 10567201
while True:
    n, m, v = map(int, input().split())
    if n+m+v:
        a = binmod(pow(2, n, M), m, M)
        if m%2: print(a*pow(2, -n, M)%M)
        else: b = binmod(pow(2, n-1, M), m//2, M); print(((a-(-1)**(m//2)*b)*pow(2, -n, M)%M+(v<1)*b*(-1)**(m//2))%M)
    else: break