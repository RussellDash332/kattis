import sys; input = sys.stdin.readline
from math import *

def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a%b); return (q, p-q*(a//b))

def crt(a, m, b, n):
    d = gcd(m, n); k = m*n//d
    assert (a-b)%d == 0
    return (a-m*bezout(m, n)[0]*(a-b)//d)%k

n = int(input())
a = [*map(lambda x: int(x)-1, input().split())]
b = [*map(lambda x: int(x)-1, input().split())]
ab = [b[a[i]] for i in range(n)]
v = [0]*n; d = []; t = []
for i in range(n):
    if v[i] == 0:
        v[i] = 1; c = 1; t.append([i]); p = ab[i]
        while p != i: t[-1].append(p); v[p] = 1; p = ab[p]; c += 1
        d.append(c)

x = 1
for y in d:
    x = lcm(x, 2*y)
    if x > 10**12: x = 'huge'; break

u = []
for k in t:
    r = {e:i for i,e in enumerate(k)}
    if a[k[0]] not in r: continue
    m = (r[a[k[0]]]-r[k[0]])%len(k); z = 0
    for i in k:
        if a[i] not in r or (r[a[i]]-r[i])%len(k) != m: z += 1
    if z == 0: u.append((-m, len(k)))
if len(u) != len(t): print(x)
else:
    w, q = 0, 1
    for i, j in u:
        w, q = crt(w, q, i, j), lcm(q, j)
        if 2*w+1 > 10**12: w = 'huge'; break
    if w == 'huge': print(x)
    elif x == 'huge': print(2*w+1)
    else: print(min(2*w+1, x))