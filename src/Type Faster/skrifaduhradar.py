n, T, *a = map(int, open(0).read().split()); lo, hi = 1, 10**18; a.sort()
def f(x):
    s = t = 0
    for i in a: t += i; s += t//x
    return s < T
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)