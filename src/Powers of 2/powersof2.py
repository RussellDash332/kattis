from functools import *
n, e = map(int, input().split()); n = [*map(int, str(n))]; e = [*map(int, str(2**e))]
@cache
def f(p, q, t):
    if q == len(e): return int(''.join(map(str, n[p:])) or 0)+1 if not t else 10**(len(n)-p)
    if p == len(n): return 0
    z = 0
    for i in range((n[p], 9)[t]+1): z += f(p+1, next((k for k in range(q+1, 0, -1) if (e[:q]+[i])[-k:] == e[:k]), 0), t|(i<n[p]))
    return z
print(f(0, 0, 0))