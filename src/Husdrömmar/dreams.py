def cg(A, b):
    n = len(b); x = array('f', [0]*n); r = array('f', b)
    for i in range(n):
        for j in range(n): r[i] -= A[i*n+j]*x[j]
    p = array('f', r); Ap = array('f', [0]*n)
    for _ in range(10 if n > 50 else n):
        rTr = pTAp = new_rTr = 0
        for i in range(n):
            rTr += r[i]*r[i]; Ap[i] = 0
            for j in range(n): Ap[i] += A[i*n+j]*p[j]
            pTAp += p[i]*Ap[i]
        if pTAp < 1e-7: break
        alpha = rTr/pTAp
        for i in range(n): x[i] += alpha*p[i]; r[i] -= alpha*Ap[i]; new_rTr += r[i]*r[i]
        if new_rTr < 1e-7: break
        beta = new_rTr/rTr
        for i in range(n): p[i] *= beta; p[i] += r[i]
    return x

import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline; from array import *
n = int(input())
b = [*map(float, input().split())]
s = [*map(float, input().split())]
A = array('f', [0]*n*n)
F = array('f', [0]*n*n)
for i in range(n):
    for j, v in enumerate(map(float, input().split())): A[i*n+j] = A[j*n+i] = v
for i in range(n):
    for j, v in enumerate(map(float, input().split())): F[i*n+j] = F[j*n+i] = v
x = cg(A, b)
print(sum(x[i]*(sum(F[i*n+j]*x[j] for j in range(n))+s[i]) for i in range(n)))