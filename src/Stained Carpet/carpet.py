import sys
from math import acos, pi

def ac(a, b, c): return acos((a**2+b**2-c**2)/(2*a*b))

for l in sys.stdin:
    a, b, c = map(float, l.split())
    # solve x**2 first
    # 3(a^4+b^4+c^4+x^4) = (a^2+b^2+c^2+x^2)^2
    # 2x^4 - 2(a^2+b^2+c^2)x^2 + 3(a^4+b^4+c^4) - (a^2+b^2+c^2)^2
    B = -2*(a**2+b**2+c**2)
    C = -(a**2+b**2+c**2)**2 + 3*(a**4+b**4+c**4)
    D = B**2 - 8*C
    if D < 0 or abs(ac(a, b, X:=((-B + D**0.5)/4)**0.5) + ac(b, c, X) + ac(c, a, X) - 2*pi) > 1e-5: print('-1.000')
    else: print(X**2*3**0.5/4)