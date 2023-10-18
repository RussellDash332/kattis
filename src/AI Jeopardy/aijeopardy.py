from math import comb
x = int(input()); k = 1; best = (1, (0, 0))
while comb(2*k, k) <= x:
    lo, hi = k, 2*k
    while comb(hi, k) < x: lo *= 2; hi *= 2
    while hi-lo>1:
        mi = (lo+hi)//2
        if comb(mi, k) >= x: hi = mi
        else: lo = mi+1
    ans = lo if comb(lo, k) >= x else lo+1
    best = min(best, (comb(ans, k), min((ans, k), (ans, ans-k))), key=lambda t: (abs(t[0]-x), t[1]))
    k += 1
assert best[0] == x; print(*best[1])