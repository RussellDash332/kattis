from fractions import *
a, b, n = map(Fraction, input().split()); x, y = Fraction(-1), Fraction(0)
for _ in range(int(n)+1):
    t1 = (1-x)/b; t1 = t1 if t1 > 0 else 10**9
    t2 = (-1-x)/b; t2 = t2 if t2 > 0 else 10**9
    t3 = (1-y)/a; t3 = t3 if t3 > 0 else 10**9
    t4 = (-1-y)/a; t4 = t4 if t4 > 0 else 10**9
    mt = min(t1, t2, t3, t4); x += b*mt; y += a*mt
    if mt == t1 or mt == t2: b = -b
    else: a = -a
print(*x.as_integer_ratio(), *y.as_integer_ratio())