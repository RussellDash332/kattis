import os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from random import *
N, M, C = map(int, input().split()); P = 10**9+7
H = [randint(1, P-1)*P+randint(1, P-1) for _ in range(C)]
R = []
for i in range(N):
    hx = hy = 0
    for c in map(int, input().split()): kx, ky = divmod(H[c-1], P); hx = (hx+kx)%P; hy = (hy+ky)%P
    R += [hx*P+hy]
nA = N//2; nB = N-N//2; A = [[] for _ in range(nA+1)]; B = [set() for _ in range(nB+1)]
for i in range(1<<nA):
    hx = hy = bc = 0
    while i: bc += 1; u = i&-i; i ^= u; kx, ky = divmod(R[u.bit_length()-1], P); hx = (hx+kx)%P; hy = (hy+ky)%P
    A[bc].append(hx*P+hy)
for i in range(1<<nB):
    hx = hy = bc = 0
    while i: bc += 1; u = i&-i; i ^= u; kx, ky = divmod(R[u.bit_length()-1+nA], P); hx = (hx+kx)%P; hy = (hy+ky)%P
    B[bc].add(hx*P+hy)
hx = hy = 0
for h in H: hx = (hx+h//P)%P; hy = (hy+h)%P
for z in range(N, -1, -1):
    if z*M%C: continue
    u = z*M//C; tx = hx*u%P; ty = hy*u%P
    for r in range(len(A)):
        if z-r >= len(B): continue
        for a in A[r]:
            if (tx-a//P)%P*P+(ty-a)%P in B[z-r]: print(z); exit()