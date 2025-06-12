n, k, *a = map(int, open(0).read().split()); lo, hi = 1, 10**18
def f(n): return sum((x+n-1)//n for x in a) <= k
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)