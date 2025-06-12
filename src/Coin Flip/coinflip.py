import sys; from cmath import *; from collections import *; from decimal import *
getcontext().prec = 9
def fft(v, inv=False):
    n = len(v); j = 0; k = 2
    for i in range(1, n):
        b = n>>1
        while j&b: j ^= b; b >>= 1
        j ^= b
        if i < j: v[i], v[j] = v[j], v[i]
    wk = exp(1j*(1-2*inv)*pi)
    while k <= n:
        for i in range(0, n, k):
            w = 1
            for j in range(i, i+(k>>1)): y = v[j+(k>>1)]*w; v[j+(k>>1)] = v[j]-y; v[j] += y; w *= wk
        k <<= 1; wk **= .5
    return v
def mult(p1, p2):
    n = 2**(len(bin(m:=len(p1)+len(p2)-1))-2); fft1, fft2 = fft(p1+[0]*(n-len(p1))), fft(p2+[0]*(n-len(p2)))
    return [t.real/n for t in fft([fft1[i]*fft2[i] for i in range(n)], inv=True)][:m]
def ppow(i, n):
    z = []; p = Decimal(i/100); q = p/(1-p); f = (1-p)**n
    for k in range(n+1): z.append(f); f *= Decimal((n-k)/(k+1))*q
    return [*map(float, z)]
def f(a, b):
    m = (a+b)//2
    if a == b: return ppow(a, C[a])
    z = mult(f(a, m), f(m+1, b))
    while z and z[-1] < 1e-8: z.pop()
    return z
N, *P = map(int, sys.stdin.read().split()); C = Counter(P); Z = f(1, 99)
while len(Z) < N+1: Z.append(0)
for i in Z: sys.stdout.write(str(round(i, 7))+' ')