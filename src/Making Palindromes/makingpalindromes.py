n = int(input()); s = input(); mem = [[[-1]*(n+1) for _ in range(n)] for _ in range(n)]; MOD = 10**9+7
def f(l, r, k):
    if l > r: return pow(26, k, MOD)
    if k < 1: return 0
    if mem[l][r][k] != -1: return mem[l][r][k]
    elif s[l] == s[r]: ans = f(l+1, r-1, k-1) + 25*f(l, r, k-1)
    else: ans = f(l+1, r, k-1) + f(l, r-1, k-1) + 24*f(l, r, k-1)
    mem[l][r][k] = ans%MOD; return ans%MOD
print(f(0, n-1, n))