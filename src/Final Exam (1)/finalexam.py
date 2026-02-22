import os; from array import *
c = r = 0; W = array('I'); F = W.append
for i in os.read(0, 1<<23):
    if i > 45: c = c*10+i-48; r = 1
    elif r: F(c); c = r = 0

nA, nB, nC = W[0], W[1], W[2]
M = 3*10**7+1; S = int(M**.5)+1
A = array('I', [0]*M)
B = array('I', A)
C = array('I', A)
for i in range(3, nA+3): A[W[i]] += 1
for i in range(nA+3, nA+nB+3): B[W[i]] += 1
for i in range(nA+nB+3, nA+nB+nC+3): C[W[i]] += 1

F = array('H', [0]*S)
P = array('H')
for i in range(2, S):
    if F[i] < 1: F[i] = i; P.append(i)
    for p in P:
        if (j:=i*p) >= S: break
        F[j] = p
        if p == F[i]: break

Z = 0
for m in range(2, S):
    pf = []; x = m
    while x > 1:
        p = F[x]
        while x%p < 1: x //= p
        pf.append(p)
    for n in range(m%2+1, m, 2):
        z = 0
        for p in pf:
            if n%p < 1: z = 1; break
        if z: continue
        a = m*m-n*n; b = 2*m*n; c = m*m+n*n; k = 1
        while k*c < M:
            if (cc:=C[k*c]): Z += (A[k*a]*B[k*b]+A[k*b]*B[k*a])*cc
            k += 1
print(Z)