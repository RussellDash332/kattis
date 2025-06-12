n = 100*int(input()); lo, hi = 0, 10**18
def f(x): return (355+(4+2*x)*(110+x))**2 > n
while lo < hi:
    if f(mi:=(lo+hi)//2): hi = mi
    else: lo = mi+1
print(lo)