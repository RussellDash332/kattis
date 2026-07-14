from fractions import Fraction
c, f = map(float, input().split())
d = Fraction(c)
lo, hi = 1, 10**7
while abs(lo-hi) > 16:
    mid = (lo+hi)//2
    if abs(d.limit_denominator(mid)-c) <= f: hi = mid-1
    else: lo = mid
s = set()
for i in range(lo-4, hi+4):
    e = d.limit_denominator(max(1, i))
    if abs(e-c) <= f: s.add((e.numerator, e.denominator))
print(*min(s))