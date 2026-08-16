def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a%b); return (q, p-a//b*q)
def crt(a, m, b, n):
    d = gcd(m, n); k = m*n//d
    return (a-m*bezout(m, n)[0]*(a-b)//d)%k
from math import gcd
for _ in range(int(input())):
    m = int(input()); Z = set()
    for z in range(1, int(m**.5)+2):
        if m%z < 1 and gcd(z, m//z) == 1:
            Z.add(crt(crt(0, z, 1, m//z), m, 1, m-1))
            Z.add(crt(crt(0, m//z, 1, z), m, 1, m-1))
    Z.discard(1); print(*sorted(Z))