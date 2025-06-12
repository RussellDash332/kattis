from array import *
M = 998244353; R = array('I', [1])
def ntt(P):
    n = k = len(P); P = [*P]; Z = [0]*n
    while 2*len(R) < n: u = pow(3, M//(4*len(R)), M); R.extend([r*u%M for r in R]) # 3 is a primitive root of M
    while k > 1:
        for i in range(n//k):
            r = R[i]
            for j in range(i*k, i*k+k//2): z = r*P[j+k//2]; P[j+k//2] = (P[j]-z)%M; P[j] = (P[j]+z)%M
        k >>= 1
    for i in range(1, n): Z[i] = Z[i//2]//2+(i&1)*n//2
    return [P[r] for r in Z]

def mult(p1, p2):
    m = len(p1)+len(p2)-1; n = 1
    while n < m: n *= 2
    p1 += [0]*(n-len(p1)); p2 += [0]*(n-len(p2)); ntt1 = ntt(p1); ntt2 = ntt(p2)
    z = pow(n, -1, M); return ntt([ntt1[-i]*ntt2[-i]%M*z%M for i in range(n)])[:m]

def sq(p):
    m = 2*len(p)-1; n = 1
    while n < m: n *= 2
    p += [0]*(n-len(p)); t = ntt(p)
    z = pow(n, -1, M); return ntt([t[-i]**2%M*z%M for i in range(n)])[:m]

def div(u, v):
    b = 0
    while v[b] == 0: b += 1
    v = v[b:]; vi = [pow(v[0], -1, M)]; n = len(u)-len(v)+1; x = 1; w = []
    while x < n:
        x <<= 1
        while len(w) < min(x, len(v)): w.append(v[len(w)])
        q = mult(sq(vi), w)
        while len(w) > min(x, len(v)) and w[-1] == 0: w.pop()
        while len(vi) < x: vi.append(0)
        for i in range(len(vi)):
            vi[i] <<= 1
            if i < len(q): vi[i] -= q[i]
            vi[i] %= M
    return mult(u, vi)[b:n]

import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from math import gcd
nA, nB, nC = map(int, input().split())
A = [0]*(2*10**5+1)
B = [0]*(2*10**5+1)
C = [0]*(2*10**5+1)
for p in (A, B, C):
    for i in map(int, input().split()): p[i] += 1
    while not p[-1]: p.pop()
gA = gB = gC = gD = 0
for i in A: gA = gcd(gA, i)
for i in B: gB = gcd(gB, i)
for i in C: gC = gcd(gC, i)
for i in range(len(A)): A[i] //= gA
for i in range(len(B)): B[i] //= gB
for i in range(len(C)): C[i] //= gC
D = array('I', div(mult(A, B), C)); S = 0
for i in D: gD = gcd(gD, i); S += i
print(S//gD)
for i in range(len(D)): sys.stdout.write((str(i)+' ')*(D[i]//gD))