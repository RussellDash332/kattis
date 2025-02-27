from random import *; from array import *
n = int(input()); M = 10**9+7; F = array('i', [1, 1]); L = 10**6; U = 95; H = {}
if n == 0: print('.##\n##.'); exit()
for _ in range(U): F.append((F[-1]+F[-2])%M)
for _ in range(L):
    s = []; t = 0; f = 1
    while t+(x:=randint(1, U//2)) <= U: s.append(x); t += x; f = f*F[x]%M
    H[f] = s
for i in H:
    j = n*pow(i, -1, M)%M
    if j in H: z = '#'.join('.'*k for k in H[i]+H[j]); print(z); print(z); exit()
assert 0