n, s, a, *H = map(int, open(0).read().split()); lo, hi = 1, 10**10
while lo < hi:
    mi = (lo+hi)//2
    if sum((max(0, H[i]-a*mi)+s-1)//s for i in range(n)) <= mi: hi = mi
    else: lo = mi+1
print(lo)