def egcd(a, b):
    if a == 0: return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inv_mod(a, m):
    return egcd(a, m)[1] % m

def powmod(a, b, m):
    if b == 0: return 1
    elif b == 1: return a % m
    elif b % 2: return a * powmod(a * a % m, b // 2, m) % m
    return powmod(a * a % m, b // 2, m)

s, n = input().strip(), int(input())
h, p, f, m = [ord(s[0])-95], 31, 1, 10**18 + 7
for i in range(1, len(s)):
    f *= p; f %= m
    h.append((h[-1] + f*(ord(s[i])-95))%m)
h.append(0)
for _ in range(n):
    i, j = map(int, input().split())
    print(((h[j-1]-h[i-1])*inv_mod(powmod(p, i, m), m)) % m)