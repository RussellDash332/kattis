N = int(input())
MOD = 10**9+7
res = 1

def egcd(a, b):
    if a == 0: return (0, 1)
    else: y, x = egcd(b % a, a); return (x - (b // a) * y, y)

def inv_mod(a, m):
    return egcd(a, m)[0] % m

for i in range(N): res *= 2*N-i; res *= inv_mod(i+2, MOD); res %= MOD
print(res)