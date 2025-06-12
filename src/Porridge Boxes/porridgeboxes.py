A, B, D, N, *T = map(int, open(0).read().split()); T = set(T)
def f(x):
    f = p = 0
    for t in range(B):
        if t in T:
            f -= 1; p += 1
            if f+D <= x: f += D
        elif f: f -= 1; p += 1
    return p >= A
lo, hi = D-1, 2*(D+B)
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo if lo < 2*(D+B) else 'impossible')