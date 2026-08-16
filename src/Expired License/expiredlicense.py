from array import *; from math import *
LIMIT = 10**7+67; F = array('I', [0]*LIMIT); P = array('I')
for i in range(2, LIMIT):
    if F[i] < 1: F[i] = i; P.append(i)
    for p in P:
        if (j:=i*p) >= LIMIT: break
        F[j] = p
        if p == F[i]: break
for _ in '.'*int(input()):
    a, b = map(lambda x: round(10**5*float(x)), input().split())
    d = gcd(a,b); a //= d; b //= d
    if a == b: print(2, 2)
    elif F[a] == a and F[b] == b: print(a, b)
    else: print('impossible')