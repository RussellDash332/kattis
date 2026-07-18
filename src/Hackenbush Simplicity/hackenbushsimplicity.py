import sys; sys.set_int_max_str_digits(10067)
p, *q = map(int, input().split('/2^')); q = (q or [0])[0]
r, *s = map(int, input().split('/2^')); s = (s or [0])[0]
m = max(q, s); lo, hi = 0, m+1
def f(x):
    return p<<(x-q) if x>q else ~(~p>>(q-x)), r<<(x-s) if x>s else (~-r>>(s-x))+1
while lo < hi:
    a, b = f(mi:=(lo+hi)//2)
    if b-a > 1: hi = mi
    else: lo = mi+1
a, b = f(lo)
if a*b < 0: print(0)<exit()
n = [b-1, a+1][b>0]
while lo and n%2<1: n //= 2; lo -= 1
print(f'{n}/2^{lo}' if lo else n)