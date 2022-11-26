def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def bezout(a, b):
    if a == 0:
        return 0, 1
    elif b == 0:
        return 1, 0
    else:
        p, q = bezout(b, a % b)
        return (q, p - q * (a // b))

def crt(a, m, b, n):
    d = gcd(m, n)
    k = m * n // d
    if (a - b) % d != 0:
        print('no solution')
    else:
        u, _ = bezout(m, n)
        return (a - m * u * (a - b) // d) % k, k

a, b, c, d, e, f, g = map(int, input().split())

# (16-2*x)*(21-2*x)*x is maximized when 12x^2 - 4(a+b)x + ab = 0
x = int(((a + b) - (a*a - a*b + b*b)**0.5) / 6)
def v(x):
    return (a-2*x)*(b-2*x)*x
vv = sorted([v(i) for i in range(x-2, x+3)], reverse=True)
v1, v2, v3 = vv[:3]

s, k = crt(*crt(c, v1, d, v2), e, v3)
while s < f:
    s += k
while s > g:
    s -= k
print(s)