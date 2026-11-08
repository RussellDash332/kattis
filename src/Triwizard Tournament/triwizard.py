import sys; input = sys.stdin.readline
from collections import *
F = "The Yule Ball can't happen, Draco's father will hear about this"
while 1:
    N, M = map(int, input().split()); N *= 100; M *= 100
    if N+M<1: break
    L = int(input()); K = int(input())
    A = Counter(map(lambda x: int(x)*100, input().split()))
    Z = 10**18
    for _ in range(2):
        N, M = M, N
        if N%L<1:
            t = N//L; m = u = A[M]
            if m >= t: Z = min(Z, t)
            for i in sorted(A)[::-1]:
                if i >= M: continue
                if 2*i < M: break
                if i != M-i: d = min(A[i], A[M-i])
                else: d = A[i]//2
                k = min(d, t-m); m += k; u += 2*k
                if m == t: break
            if m == t: Z = min(Z, u)
    print(Z if Z<1e9 else F)