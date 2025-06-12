def f(n):
    print(n); v = input()
    if v == 'correct': exit()
    return v == 'lower'
B = int(input()); lo, hi = 1, 10**9
while lo < hi:
    if f(mi:=(B*lo+hi)//(B+1)): hi = mi
    else: lo = mi+1
f(lo)