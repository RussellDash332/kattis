import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from array import *; from collections import *
T = 10**6
spf = array('i', range(T+1)); p = 3
while p <= T:
    if spf[p] == p:
        for i in range(p*p, T+1, 2*p):
            if spf[i] == i: spf[i] = p
    p += 2

def gen(k):
    u = [1]
    for v in k: u += [-v*c for c in u]
    return u

S = array('h', [2]+[p for p in range(3, 10**4, 2) if spf[p] == p])
Z = 0; M = array('i', [0]*(2*T+3)); H = Counter()
for _ in range(int(input())):
    n = int(input()); z = 1
    for s in S:
        if n%(s*s) == 0: z *= s
        while n%s == 0: n //= s
        if n == 1: break
    if n > 10**4 and round(n**0.5)**2 == n: z *= round(n**0.5)
    H[z] += 1; Z -= z==1
for z, v in H.items():
    c = []
    if z%2 == 0: c.append(2); z //= 2
    while z != 1: c.append(spf[z]); z //= spf[z]
    for u in gen(c): M[u] += v
for k in range(len(M)): Z += M[k]**2*(1-2*(k>T))
print(Z//2)