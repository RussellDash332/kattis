from math import *
n, m = map(int, input().split()); b = m-n; C = [1]*-~b; A = [0]*-~n
for s in range(1, b+1): C[s] = C[s-1]*(n+s)//s
for r in range(1, n+1): A[r] = sum(C[b-q*r] for q in range(b//r+1))
P = [comb(n, r) for r in range(n+1)]; Z = [0]*n; Z[-1] = n*-~m/-~n
for d in  range(2, n+1):
    s = 0
    for r in range(d, n+1): s += (1, -1)[(r+d)&1]*P[r]*comb(r-2, d-2)*A[r]
    Z[n-d] = s/C[b]
print(*Z)