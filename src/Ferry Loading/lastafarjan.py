from functools import *
N, L, *W = map(int, open(0).read().split()); W += [10**9]
@cache
def f(i, a, b, c, d):
    if not a<=b<=c<=d: return f(i, *sorted((a, b, c, d)))
    if a < 0 or b < 0 or c < 0 or d < 0: return -1
    if W[i]+1 > max(a, b, c, d): return i
    return max(f(i+1, a-W[i]-1, b, c, d), f(i+1, a, b-W[i]-1, c, d), f(i+1, a, b, c-W[i]-1, d), f(i+1, a, b, c, d-W[i]-1))
print(f(0, *[L+1]*4))