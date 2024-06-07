from math import *; N = int(input())
if N == 1: print(0), exit(0)
L = int((N/2)**.5); M = 10**20
for h in range(L, 2*L+3):
    w = (N+h-1)//h
    if h <= 2*w <= 4*h: M = min(M, h*w)
print(M-N)