from functools import *
N, K, *A = map(int, open(0).read().split())
@cache
def f(l, r, x):
    if l > r: return 0
    if l == r: return K-x-1
    z = f(l, r, x+1)+1 if x < K-1 else f(l+1, r, 0)
    for i in range(l+1, r+1):
        if A[l] == A[i]: z = min(z, f(l+1, i-1, 0)+f(i, r, min(x+1, K-1)))
    return z
print(f(0, N-1, 0))