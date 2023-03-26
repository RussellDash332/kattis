from math import ceil
m = {}
def t(n):
    if n == 1: return 0
    if n in m: return m[n]
    d = {}
    for k in range(n-1, 0, -1): d[ceil(n/(k+1))] = k
    m[n] = min(v*p + t(k) for k,v in d.items()) + r
    return m[n]
n, r, p = map(int, input().split())
print(t(n))