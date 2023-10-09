import sys; input = sys.stdin.readline
from math import *
def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a % b); return (q, p - q * (a // b))
for _ in range(int(input())):
    r, s, q = map(int, input().split())
    d = gcd(r, s); r //= d; s //= d; q //= d
    a, b = bezout(r, s); a *= q; b *= q
    if a*r+b*s+q == 0: a = -a; b = -b
    a -= 10**8*s; b += 10**8*r; k = min((1-a)//s, (b-1)//r)
    a += k*s; b -= k*r; print(a, b)