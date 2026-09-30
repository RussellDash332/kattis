N, V = map(int, input().split())
X, Y = zip(*[[*map(int, input().split())] for _ in range(N)])
from functools import *
@cache
def f(n, v, p):
    if n == N: return 0
    z = 10**18
    if v and n < N-1: z = min(z, f(n+1, v-1, p))
    return min(z, f(n+1, v, n)+(X[p]-X[n])**2+(Y[p]-Y[n])**2)
print(f(1, V, 0)%(10**9+7))