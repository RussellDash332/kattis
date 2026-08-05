T, a, b, c, d = map(eval, open(0).read().split())
def f(t): return (t-a)**6+(t-b)**4+(t-c)**2+d-T+t
gr = (5**0.5-1)/2
def g(a, b):
    while b-a>1e-9:
        if f(μ:=(1-gr)*a+gr*b) > f(λ:=gr*a+(1-gr)*b): b = μ
        else: a = λ
    return (a+b)/2
lo, hi = 0, (k:=g(0, T))
while abs(lo-hi)>1e-13:
    if f(mi:=(lo+hi)/2)<0: hi = mi
    else: lo = mi
lo2, hi2 = k, T
while abs(lo2-hi2)>1e-13:
    if f(mi:=(lo2+hi2)/2)>0: hi2 = mi
    else: lo2 = mi
if abs(f(lo))<1e-5: print(lo)
elif abs(f(lo2))<1e-5: print(lo2)
else: print('O nei!')