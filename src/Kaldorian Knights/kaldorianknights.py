from array import *
n, k, *a = map(int, open(0).read().split())
M = 10**9+7
F = array('i', [1])
for i in range(1, n+1): F.append(F[-1]*i%M)
P = array('i', [0])
for i in a: P.append(P[-1]+i)
H = array('i', [-1]*(k+1))
def f(n, k):
    if H[k] > -1: return H[k]
    z = F[n]
    for i in range(1, k+1): z = (z-F[n-P[i]]*f(P[i], i-1))%M
    H[k] = z; return z
print(f(n, k))